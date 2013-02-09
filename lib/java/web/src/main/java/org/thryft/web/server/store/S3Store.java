package org.thryft.web.server.store;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;
import java.io.StringWriter;
import java.util.Map;
import java.util.Properties;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.IOUtils;
import org.apache.thrift.TBase;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TType;
import org.thryft.core.protocol.JsonProtocol;

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
import com.google.common.collect.Sets;

public final class S3Store<ModelT extends TBase<?, ?>> extends
        AwsKeyValueStore<ModelT> {
    public final static class Configuration extends
            AwsKeyValueStore.Configuration {
        public Configuration(final AWSCredentials credentials) {
            this(BUCKET_NAME_PREFIX_DEFAULT, credentials);
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
            } else {
                this.bucketNamePrefix = BUCKET_NAME_PREFIX_DEFAULT;
            }
        }

        public Configuration(final String bucketNamePrefix,
                final AWSCredentials credentials) {
            super(credentials);
            checkNotNull(bucketNamePrefix);
            checkArgument(!bucketNamePrefix.isEmpty());
            this.bucketNamePrefix = bucketNamePrefix;
        }

        public String getBucketNamePrefix() {
            return bucketNamePrefix;
        }

        public final static String BUCKET_NAME_PREFIX_DEFAULT = "yogento-dev-";

        private String bucketNamePrefix;
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
    }

    @Override
    protected boolean _deleteModelById(final Key modelKey) {
        final ImmutableMap<String, ModelT> models = __getModels(modelKey
                .getUsername());
        if (models.get(modelKey.getModelId()) == null) {
            return false;
        }
        final Map<String, ModelT> updatedModels = Maps.newLinkedHashMap(models);
        updatedModels.remove(modelKey.getModelId());
        __putModels(ImmutableMap.copyOf(updatedModels), modelKey.getUsername());
        return true;
    }

    @Override
    protected void _deleteModels(final String username) {
        final String objectKey = __getObjectKey(username);
        objectCache.invalidate(objectKey);
        try {
            client.deleteObject(bucketName, objectKey);
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on deleteModels: ", e);
        }
    }

    @Override
    protected ModelT _getModelById(final Key modelKey)
            throws NoSuchModelException {
        final ImmutableMap<String, ModelT> models;
        try {
            models = __getModels(modelKey.getUsername());
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelById: ", e);
            throw new NoSuchModelException(modelKey.getModelId());
        }
        final ModelT model = models.get(modelKey.getModelId());
        if (model != null) {
            return model;
        } else {
            throw new NoSuchModelException(modelKey.getModelId());
        }
    }

    @Override
    protected int _getModelCount(final String username) {
        try {
            return __getModels(username).size();
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelCount: ", e);
            return 0;
        }
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String username) {
        try {
            return __getModels(username).keySet();
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelIds: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected ImmutableSet<ModelT> _getModels(final String username) {
        try {
            return ImmutableSet.copyOf(__getModels(username).values());
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModels: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected ImmutableSet<ModelT> _getModelsByIds(
            final ImmutableSet<Key> modelKeys) throws NoSuchModelException {
        final ImmutableMap<String, ModelT> allModels;
        try {
            allModels = __getModels(modelKeys.iterator().next().getUsername());
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on getModelsByIds: ", e);
            return ImmutableSet.of();
        }
        final Set<ModelT> outModels = Sets.newLinkedHashSet();
        for (final Key modelKey : modelKeys) {
            final ModelT outModel = allModels.get(modelKey.getModelId());
            if (outModel != null) {
                outModels.add(outModel);
            } else {
                throw new NoSuchModelException(modelKey.getModelId());
            }
        }
        return ImmutableSet.copyOf(outModels);
    }

    @Override
    protected void _putModel(final ModelT model, final Key modelKey) {
        _putModels(ImmutableMap.of(modelKey, model));
    }

    @Override
    protected void _putModels(final ImmutableMap<Key, ModelT> models) {
        try {
            final String username = models.keySet().iterator().next()
                    .getUsername();
            final ImmutableMap<String, ModelT> existingModels = __getModels(username);
            final Map<String, ModelT> updatedModels = Maps
                    .newLinkedHashMap(existingModels);
            for (final ImmutableMap.Entry<Key, ModelT> model : models
                    .entrySet()) {
                updatedModels
                        .put(model.getKey().getModelId(), model.getValue());
            }
            __putModels(ImmutableMap.copyOf(updatedModels), username);
        } catch (final AmazonServiceException e) {
            logger.error("AWS service exception on putModels: ", e);
            return;
        }
    }

    private ImmutableMap<String, ModelT> __getModels(final String username) {
        final String objectKey = __getObjectKey(username);

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
                final JsonProtocol iprot = new JsonProtocol(istringReader);
                final TMap map = iprot.readMapBegin();
                final Map<String, ModelT> modelsMutable = Maps
                        .newLinkedHashMap();
                for (int i = 0; i < map.size; i++) {
                    final String modelId = iprot.readString();
                    final ModelT model = _getModel(iprot);
                    if (model != null) {
                        modelsMutable.put(modelId, model);
                    }
                }
                iprot.readMapEnd();
                final ImmutableMap<String, ModelT> models = ImmutableMap
                        .copyOf(modelsMutable);
                objectCache.put(objectKey, new ObjectCacheEntry(models, object
                        .getObjectMetadata().getETag()));
                return models;
            } finally {
                istringReader.close();
            }
        } catch (final IOException e) {
            logger.error("IOException on __getModels: ", e);
            return ImmutableMap.of();
        } catch (final TException e) {
            logger.error("TException on __getModels: ", e);
            return ImmutableMap.of();
        }
    }

    private String __getObjectKey(final String username) {
        return Key.prefix(username);
    }

    private void __putModels(final ImmutableMap<String, ModelT> models,
            final String username) {
        if (models.isEmpty()) {
            _deleteModels(username);
            return;
        }

        final String ostring;
        try {
            final StringWriter ostringWriter = new StringWriter();
            final JsonProtocol oprot = new JsonProtocol(ostringWriter);
            oprot.writeMapBegin(new TMap(TType.STRING, TType.STRUCT, models
                    .size()));
            for (final ImmutableMap.Entry<String, ModelT> model : models
                    .entrySet()) {
                oprot.writeString(model.getKey());
                model.getValue().write(oprot);
            }
            oprot.writeMapEnd();
            oprot.flush();
            ostring = ostringWriter.toString();
        } catch (final IOException e) {
            logger.error("error serializing models: ", e);
            return;
        } catch (final TException e) {
            logger.error("error serializing models: ", e);
            return;
        }

        final byte[] obytes = ostring.getBytes();

        final ObjectMetadata objectMetadata = new ObjectMetadata();
        objectMetadata.setContentLength(obytes.length);
        objectMetadata.setContentType("application/json");

        final String objectKey = __getObjectKey(username);
        final PutObjectResult putObjectResult = client.putObject(bucketName,
                objectKey, new ByteArrayInputStream(obytes), objectMetadata);
        objectCache.put(objectKey,
                new ObjectCacheEntry(models, putObjectResult.getETag()));
    }

    private final String bucketName;
    private final AmazonS3 client;
    private final Cache<String, ObjectCacheEntry> objectCache = CacheBuilder
            .newBuilder().expireAfterAccess(1, TimeUnit.HOURS).build();

}