/*******************************************************************************
 * Copyright (c) 2015, Minor Gordon
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in
 *       the documentation and/or other materials provided with the
 *       distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
 * CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGE.
 ******************************************************************************/

package org.thryft.store;

import static com.google.common.base.Preconditions.checkNotNull;
import static org.thryft.Preconditions.checkNotEmpty;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;
import java.io.StringWriter;
import java.util.Map;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.IOUtils;
import org.thryft.Struct;
import org.thryft.protocol.InputProtocolException;
import org.thryft.protocol.JacksonJsonInputProtocol;
import org.thryft.protocol.JacksonJsonOutputProtocol;
import org.thryft.protocol.MapBegin;
import org.thryft.protocol.OutputProtocolException;
import org.thryft.protocol.Type;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.model.PutObjectResult;
import com.amazonaws.services.s3.model.S3Object;
import com.google.common.base.CaseFormat;
import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Maps;

public final class S3Store<ModelT extends Struct> extends
        AwsKeyValueStore<ModelT> {
    public final static class Configuration extends
            AwsKeyValueStore.Configuration {
        public Configuration(final AWSCredentials credentials) {
            super(credentials);
        }

        public Configuration(final Properties properties) {
            super(properties);
            String bucketNamePrefix = properties.getProperty(this.getClass()
                    .getCanonicalName() + ".bucketNamePrefix");
            if (bucketNamePrefix == null) {
                bucketNamePrefix = properties.getProperty("s3BucketNamePrefix");
            }
            if (bucketNamePrefix != null) {
                this.bucketNamePrefix = bucketNamePrefix;
            }
            try {
                this.objectCacheExpireAfterAccessDuration = Long
                        .parseLong(properties.getProperty(this.getClass()
                                .getCanonicalName()
                                + ".objectCacheExpireAfterAccessDuration"));
                this.objectCacheExpireAfterAccessTimeUnit = TimeUnit
                        .valueOf(properties.getProperty(this.getClass()
                                .getCanonicalName()
                                + ".objectCacheExpireAfterAccessTimeUnit"));
            } catch (final IllegalArgumentException e) {
            }
        }

        public Configuration(final String bucketNamePrefix,
                final AWSCredentials credentials) {
            super(credentials);
            this.bucketNamePrefix = checkNotEmpty(bucketNamePrefix);
        }

        public Configuration(final String bucketNamePrefix,
                final AWSCredentials credentials,
                final long objectCacheExpireAfterAccessDuration,
                final TimeUnit objectCacheExpireAfterAccessTimeUnit) {
            super(credentials);
            this.bucketNamePrefix = checkNotEmpty(bucketNamePrefix);
            this.objectCacheExpireAfterAccessDuration = objectCacheExpireAfterAccessDuration;
            this.objectCacheExpireAfterAccessTimeUnit = checkNotNull(objectCacheExpireAfterAccessTimeUnit);
        }

        public String getBucketNamePrefix() {
            return bucketNamePrefix;
        }

        public long getObjectCacheExpireAfterAccessDuration() {
            return objectCacheExpireAfterAccessDuration;
        }

        public TimeUnit getObjectCacheExpireAfterAccessTimeUnit() {
            return objectCacheExpireAfterAccessTimeUnit;
        }

        private String bucketNamePrefix = BUCKET_NAME_PREFIX_DEFAULT;

        private long objectCacheExpireAfterAccessDuration = OBJECT_CACHE_EXPIRE_AFTER_ACCESS_DURATION_DEFAULT;

        private TimeUnit objectCacheExpireAfterAccessTimeUnit = OBJECT_CACHE_EXPIRE_AFTER_ACCESS_TIME_UNIT_DEFAULT;

        public final static String BUCKET_NAME_PREFIX_DEFAULT = "yogento-dev-";
        public final static long OBJECT_CACHE_EXPIRE_AFTER_ACCESS_DURATION_DEFAULT = 1;
        public final static TimeUnit OBJECT_CACHE_EXPIRE_AFTER_ACCESS_TIME_UNIT_DEFAULT = TimeUnit.HOURS;
    }

    private final class ObjectCacheEntry {
        public ObjectCacheEntry(final ImmutableMap<String, ModelT> data,
                final String etag) {
            this.data = data;
            this.etag = etag;
        };

        public ImmutableMap<String, ModelT> getData() {
            return data;
        }

        public String getEtag() {
            return etag;
        }

        private final ImmutableMap<String, ModelT> data;
        private final String etag;
    }

    public S3Store(final Configuration configuration,
            final Class<ModelT> modelClass) {
        super(modelClass);
        checkNotNull(configuration);
        bucketName = configuration.getBucketNamePrefix()
                + CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_HYPHEN,
                        modelClass.getSimpleName());
        client = new AmazonS3Client(configuration.getCredentials());
        try {
            logger.info("creating bucket " + bucketName);
            client.createBucket(bucketName);
        } catch (final AmazonServiceException e) {
            if (!e.getErrorCode().equals("BucketAlreadyExists")) {
                logger.error("error creating bucket " + bucketName + ": ", e);
                throw e;
            }
        }
        objectCache = CacheBuilder
                .newBuilder()
                .expireAfterAccess(
                        configuration.getObjectCacheExpireAfterAccessDuration(),
                        configuration.getObjectCacheExpireAfterAccessTimeUnit())
                .build();
    }

    @Override
    protected boolean _deleteModelById(final Key modelKey)
            throws ModelIoException {
        final ImmutableMap<String, ModelT> models = __getModels(modelKey
                .getUserId());
        if (models.get(modelKey.getModelId()) == null) {
            return false;
        }
        final Map<String, ModelT> updatedModels = Maps.newLinkedHashMap(models);
        updatedModels.remove(modelKey.getModelId());
        __putModels(ImmutableMap.copyOf(updatedModels), modelKey.getUserId());
        return true;
    }

    @Override
    protected void _deleteModels(final String userId) throws ModelIoException {
        final String objectKey = __getObjectKey(userId);
        objectCache.invalidate(objectKey);
        try {
            client.deleteObject(bucketName, objectKey);
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on deleteModels: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    @Override
    protected ModelT _getModelById(final Key modelKey) throws ModelIoException,
            NoSuchModelException {
        final ImmutableMap<String, ModelT> models;
        try {
            models = __getModels(modelKey.getUserId());
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelById: ", e);
            throw new ModelIoException(modelKey.getModelId());
        }
        final ModelT model = models.get(modelKey.getModelId());
        if (model != null) {
            return model;
        } else {
            throw new NoSuchModelException(modelKey.getModelId());
        }
    }

    @Override
    protected int _getModelCount(final String userId) throws ModelIoException {
        try {
            return __getModels(userId).size();
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelCount: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String userId)
            throws ModelIoException {
        try {
            return __getModels(userId).keySet();
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelIds: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModels(final String userId)
            throws ModelIoException {
        try {
            return __getModels(userId);
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModels: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<Key> modelKeys) throws ModelIoException,
            NoSuchModelException {
        final ImmutableMap<String, ModelT> allModels;
        try {
            allModels = __getModels(modelKeys.iterator().next().getUserId());
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelsByIds: ", e);
            throw new ModelIoException(e.getMessage());
        }
        final ImmutableMap.Builder<String, ModelT> outModels = ImmutableMap
                .builder();
        for (final Key modelKey : modelKeys) {
            final ModelT outModel = allModels.get(modelKey.getModelId());
            if (outModel != null) {
                outModels.put(modelKey.getModelId(), outModel);
            } else {
                throw new NoSuchModelException(modelKey.getModelId());
            }
        }
        return outModels.build();
    }

    @Override
    protected void _putModel(final ModelT model, final Key modelKey)
            throws ModelIoException {
        _putModels(ImmutableMap.of(modelKey, model));
    }

    @Override
    protected void _putModels(final ImmutableMap<Key, ModelT> models)
            throws ModelIoException {
        try {
            final String userId = models.keySet().iterator().next().getUserId();
            final ImmutableMap<String, ModelT> existingModels = __getModels(userId);
            final Map<String, ModelT> updatedModels = Maps
                    .newLinkedHashMap(existingModels);
            for (final ImmutableMap.Entry<Key, ModelT> model : models
                    .entrySet()) {
                updatedModels
                        .put(model.getKey().getModelId(), model.getValue());
            }
            __putModels(ImmutableMap.copyOf(updatedModels), userId);
        } catch (final AmazonServiceException e) {
            throw new ModelIoException(e);
        }
    }

    private ImmutableMap<String, ModelT> __getModels(final String userId)
            throws ModelIoException {
        final String objectKey = __getObjectKey(userId);

        final GetObjectRequest getObjectRequest = new GetObjectRequest(
                bucketName, objectKey);
        final ObjectCacheEntry objectCacheEntry = objectCache
                .getIfPresent(objectKey);
        if (objectCacheEntry != null) {
            // Do a conditional GET with an ETag
            getObjectRequest.setNonmatchingETagConstraints(ImmutableList
                    .of(objectCacheEntry.getEtag()));
        }

        final S3Object object;
        try {
            object = client.getObject(getObjectRequest);
        } catch (final AmazonServiceException e) {
            if (objectCacheEntry != null) {
                objectCache.invalidate(objectKey);
            }
            if (e.getErrorCode().equals("NoSuchKey")) {
                return ImmutableMap.of();
            } else {
                logger.error("AWS service exception on __getModels: ", e);
                throw e;
            }
        }

        if (object == null) { // Our cached ETag matched the one on the server
            return objectCacheEntry.getData();
        }

        final InputStream istream = object.getObjectContent();
        try {
            String istring;
            try {
                istring = IOUtils.toString(istream);
            } finally {
                istream.close();
            }

            final StringReader istringReader = new StringReader(istring);
            try {
                final JacksonJsonInputProtocol iprot = new JacksonJsonInputProtocol(
                        istringReader);
                final MapBegin map = iprot.readMapBegin();
                final ImmutableMap.Builder<String, ModelT> modelsBuilder = ImmutableMap
                        .builder();
                for (int i = 0; i < map.getSize(); i++) {
                    final String modelId = iprot.readString();
                    modelsBuilder.put(modelId, _getModel(iprot));
                }
                iprot.readMapEnd();
                final ImmutableMap<String, ModelT> models = modelsBuilder
                        .build();
                objectCache.put(objectKey, new ObjectCacheEntry(models, object
                        .getObjectMetadata().getETag()));
                return models;
            } finally {
                istringReader.close();
            }
        } catch (final IOException | InputProtocolException e) {
            logger.error("IOException on __getModels: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    private String __getObjectKey(final String userId) {
        return Key.prefix(userId);
    }

    private void __putModels(final ImmutableMap<String, ModelT> models,
            final String userId) throws ModelIoException {
        if (models.isEmpty()) {
            _deleteModels(userId);
            return;
        }

        final String ostring;
        try {
            final StringWriter ostringWriter = new StringWriter();
            final JacksonJsonOutputProtocol oprot = new JacksonJsonOutputProtocol(
                    ostringWriter);
            oprot.writeMapBegin(Type.STRING, Type.STRUCT, models.size());
            for (final ImmutableMap.Entry<String, ModelT> model : models
                    .entrySet()) {
                oprot.writeString(model.getKey());
                model.getValue().writeAsStruct(oprot);
            }
            oprot.writeMapEnd();
            oprot.flush();
            ostring = ostringWriter.toString();
        } catch (final OutputProtocolException e) {
            throw new ModelIoException(e);
        }

        final byte[] obytes = ostring.getBytes();

        final ObjectMetadata objectMetadata = new ObjectMetadata();
        objectMetadata.setContentLength(obytes.length);
        objectMetadata.setContentType("application/json");

        final String objectKey = __getObjectKey(userId);
        final PutObjectResult putObjectResult = client.putObject(bucketName,
                objectKey, new ByteArrayInputStream(obytes), objectMetadata);
        objectCache.put(objectKey,
                new ObjectCacheEntry(models, putObjectResult.getETag()));
    }

    private final String bucketName;
    private final AmazonS3 client;
    private final Cache<String, ObjectCacheEntry> objectCache;
}
