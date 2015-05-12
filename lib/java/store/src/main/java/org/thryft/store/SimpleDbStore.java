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

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Properties;

import org.thryft.Base;
import org.thryft.protocol.OutputProtocolException;
import org.thryft.protocol.StringMapInputProtocol;
import org.thryft.protocol.StringMapOutputProtocol;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.services.simpledb.AmazonSimpleDBClient;
import com.amazonaws.services.simpledb.model.Attribute;
import com.amazonaws.services.simpledb.model.BatchDeleteAttributesRequest;
import com.amazonaws.services.simpledb.model.BatchPutAttributesRequest;
import com.amazonaws.services.simpledb.model.CreateDomainRequest;
import com.amazonaws.services.simpledb.model.DeletableItem;
import com.amazonaws.services.simpledb.model.DeleteAttributesRequest;
import com.amazonaws.services.simpledb.model.GetAttributesRequest;
import com.amazonaws.services.simpledb.model.GetAttributesResult;
import com.amazonaws.services.simpledb.model.Item;
import com.amazonaws.services.simpledb.model.PutAttributesRequest;
import com.amazonaws.services.simpledb.model.ReplaceableAttribute;
import com.amazonaws.services.simpledb.model.ReplaceableItem;
import com.amazonaws.services.simpledb.model.SelectRequest;
import com.amazonaws.services.simpledb.model.SelectResult;
import com.google.common.base.CaseFormat;
import com.google.common.base.Charsets;
import com.google.common.base.Joiner;
import com.google.common.base.Splitter;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.LinkedHashMultimap;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.google.common.collect.Multimap;
import com.google.common.hash.Hashing;

public final class SimpleDbStore<ModelT extends Base<?>> extends
AwsKeyValueStore<ModelT> {
    public final static class Configuration extends
    AwsKeyValueStore.Configuration {
        public Configuration(final AWSCredentials credentials) {
            this(credentials, DOMAIN_NAME_PREFIX_DEFAULT);
        }

        public Configuration(final AWSCredentials credentials,
                final String domainNamePrefix) {
            super(credentials);
            this.domainNamePrefix = checkNotNull(domainNamePrefix);
        }

        public Configuration(final Properties properties) {
            super(properties);
            final String domainNamePrefix = properties.getProperty(this
                    .getClass().getCanonicalName() + ".domainNamePrefix");
            if (domainNamePrefix != null) {
                this.domainNamePrefix = domainNamePrefix;
            } else {
                this.domainNamePrefix = DOMAIN_NAME_PREFIX_DEFAULT;
            }
        }

        public String getDomainNamePrefix() {
            return domainNamePrefix;
        }

        private final String domainNamePrefix;

        public final static String DOMAIN_NAME_PREFIX_DEFAULT = "yogento-dev-";
    }

    public SimpleDbStore(final Configuration configuration,
            final Class<ModelT> modelClass) {
        super(modelClass);
        checkNotNull(configuration);
        client = new AmazonSimpleDBClient(configuration.getCredentials());
        domainName = configuration.getDomainNamePrefix()
                + CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE,
                        modelClass.getSimpleName());
        logger.info("creating domain " + domainName);
        client.createDomain(new CreateDomainRequest(domainName));
    }

    @Override
    protected boolean _deleteModelById(final Key modelKey)
            throws ModelIoException {
        final String itemName = modelKey.toString();
        final GetAttributesRequest getAttributesRequest = new GetAttributesRequest(
                domainName, itemName);
        getAttributesRequest.setConsistentRead(true);
        final GetAttributesResult attributes = client
                .getAttributes(getAttributesRequest);
        if (attributes.getAttributes().isEmpty()) {
            return false;
        }
        client.deleteAttributes(new DeleteAttributesRequest(domainName,
                itemName));
        return true;
    }

    @Override
    protected void _deleteModels(final String userId) throws ModelIoException {
        final ImmutableSet<String> modelIds = getModelIds(userId);
        final List<List<String>> modelIdBatches = Lists.partition(
                ImmutableList.copyOf(modelIds), ITEM_BATCH_SIZE);
        for (final List<String> modelIdBatch : modelIdBatches) {
            final List<DeletableItem> deleteItems = Lists.newArrayList();
            for (final String modelId : modelIdBatch) {
                deleteItems.add(new DeletableItem(new Key(modelId, userId)
                .toString(), ImmutableList.<Attribute> of()));
            }
            client.batchDeleteAttributes(new BatchDeleteAttributesRequest(
                    domainName, deleteItems));
        }
    }

    @Override
    protected ModelT _getModelById(final Key modelKey) throws ModelIoException,
    ModelIoException, NoSuchModelException {
        final GetAttributesRequest request = new GetAttributesRequest(
                domainName, modelKey.toString());
        request.setConsistentRead(true);
        final GetAttributesResult attributes = client.getAttributes(request);
        return __getModelFromAttributes(attributes.getAttributes(),
                modelKey.getModelId());
    }

    @Override
    protected int _getModelCount(final String userId) {
        final ImmutableList<Item> items = __selectItems("SELECT count(*) FROM `"
                + domainName
                + "` WHERE itemName() LIKE '"
                + Key.prefix(userId)
                + "%'");
        for (final Item item : items) {
            if (item.getName().equalsIgnoreCase("Domain")) {
                for (final Attribute attribute : item.getAttributes()) {
                    if (attribute.getName().equalsIgnoreCase("Count")) {
                        return Integer.parseInt(attribute.getValue());
                    }
                }
            }
        }
        return 0;
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String userId) {
        final ImmutableList<Item> items = __selectItems("SELECT itemName() FROM `"
                + domainName
                + "` WHERE itemName() LIKE '"
                + Key.prefix(userId)
                + "%'");
        final ImmutableSet.Builder<String> modelIds = ImmutableSet.builder();
        for (final Item item : items) {
            modelIds.add(Key.parse(item.getName()).getModelId());
        }
        return modelIds.build();
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModels(final String userId)
            throws ModelIoException {
        final ImmutableList<Item> items = __selectItems("SELECT * FROM `"
                + domainName + "` WHERE itemName() LIKE '" + Key.prefix(userId)
                + "%'");
        final ImmutableMap.Builder<String, ModelT> models = ImmutableMap
                .builder();
        for (final Item item : items) {
            final Key modelKey = Key.parse(item.getName());
            try {
                final ModelT model = __getModelFromAttributes(
                        item.getAttributes(), modelKey.getModelId());
                models.put(modelKey.getModelId(), model);
            } catch (final NoSuchModelException e) {
                throw new IllegalStateException(e);
            }
        }
        return models.build();
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<Key> modelKeys) throws ModelIoException,
            NoSuchModelException {
        final ImmutableMap.Builder<String, ModelT> modelsBuilder = ImmutableMap
                .builder();
        ;
        // SimpleDB can only handle batches of 20 IN (...) values at a time
        for (final List<Key> modelKeyBatch : Lists.partition(
                ImmutableList.copyOf(modelKeys), 20)) {
            final List<String> itemNames = Lists.newArrayList();
            for (final Key modelKey : modelKeyBatch) {
                final String itemName = modelKey.toString();
                itemNames.add("'" + itemName.replace("'", "''") + "'");
            }

            final ImmutableList<Item> items = __selectItems("select * FROM `"
                    + domainName + "` WHERE itemName() IN ("
                    + Joiner.on(',').join(itemNames) + ")");

            for (final Item item : items) {
                final Key modelKey = Key.parse(item.getName());
                final ModelT model = __getModelFromAttributes(
                        item.getAttributes(), modelKey.getModelId());
                modelsBuilder.put(modelKey.getModelId(), model);
            }
        }
        final ImmutableMap<String, ModelT> models = modelsBuilder.build();

        if (models.size() == modelKeys.size()) {
            return models;
        } else {
            for (final Key modelKey : modelKeys) {
                if (models.get(modelKey.getModelId()) == null) {
                    throw new NoSuchModelException(modelKey.getModelId());
                }
            }
            throw new IllegalStateException();
        }
    }

    @Override
    protected void _putModel(final ModelT model, final Key modelKey) {
        final String itemName = modelKey.toString();
        client.deleteAttributes(new DeleteAttributesRequest(domainName,
                itemName));
        final ImmutableList<ReplaceableAttribute> modelAttributes = __getModelAttributes(model);
        if (!modelAttributes.isEmpty()) {
            client.putAttributes(new PutAttributesRequest(domainName, itemName,
                    modelAttributes));
        }
    }

    @Override
    protected void _putModels(final ImmutableMap<Key, ModelT> models) {
        final List<List<ImmutableMap.Entry<Key, ModelT>>> modelBatches = Lists
                .partition(Lists.newArrayList(models.entrySet()),
                        ITEM_BATCH_SIZE);
        for (final List<ImmutableMap.Entry<Key, ModelT>> modelBatch : modelBatches) {
            final List<DeletableItem> deleteItems = Lists.newArrayList();
            final List<ReplaceableItem> putItems = Lists.newArrayList();
            for (final ImmutableMap.Entry<Key, ModelT> model : modelBatch) {
                final String itemName = model.getKey().toString();
                deleteItems.add(new DeletableItem(itemName, ImmutableList
                        .<Attribute> of()));
                final ImmutableList<ReplaceableAttribute> modelAttributes = __getModelAttributes(model
                        .getValue());
                if (!modelAttributes.isEmpty()) {
                    putItems.add(new ReplaceableItem(itemName, modelAttributes));
                }
            }
            client.batchDeleteAttributes(new BatchDeleteAttributesRequest(
                    domainName, deleteItems));
            client.batchPutAttributes(new BatchPutAttributesRequest(domainName,
                    putItems));
        }
    }

    private ImmutableList<ReplaceableAttribute> __getModelAttributes(
            final ModelT model) {
        final StringMapOutputProtocol oprot = new StringMapOutputProtocol();
        try {
            model.writeAsStruct(oprot);
        } catch (final OutputProtocolException e) {
            return ImmutableList.of();
        }
        final ImmutableMap<String, String> stringMap = oprot.toStringMap();

        final ImmutableList.Builder<ReplaceableAttribute> attributesBuilder = ImmutableList
                .builder();
        for (final ImmutableMap.Entry<String, String> entry : stringMap
                .entrySet()) {
            final String attributeName = entry.getKey();
            final String attributeValue = entry.getValue();
            final String urlEncodedAttributeValue;
            try {
                urlEncodedAttributeValue = URLEncoder.encode(attributeValue,
                        "UTF-8");
            } catch (final UnsupportedEncodingException e) {
                throw new IllegalStateException(e);
            }
            if (urlEncodedAttributeValue.getBytes().length < 1024) {
                attributesBuilder.add(new ReplaceableAttribute(attributeName,
                        attributeValue, false));
            } else {
                final String attributeValueHash = Hashing.md5()
                        .hashString(attributeValue, Charsets.UTF_8).toString();
                // 32 character hash
                // 5 characters for the 0-padded order marker (store a uint16)
                // Worst-case string encoding: URL-encoded UTF-8, max 3 bytes
                // per character
                int attributeValueChunkI = 0;
                for (String attributeValueChunk : Splitter.fixedLength(
                        1024 / 3 - 32 - 5).split(attributeValue)) {
                    attributeValueChunk = attributeValueHash
                            + String.format("%05d", attributeValueChunkI)
                            + attributeValueChunk;
                    try {
                        if (URLEncoder.encode(attributeValueChunk, "UTF-8")
                                .getBytes().length > 1024) {
                            logger.warn("attribute value chunk for "
                                    + attributeName
                                    + " still contains more than 1024 bytes");
                        }
                    } catch (final UnsupportedEncodingException e) {
                    }
                    attributesBuilder.add(new ReplaceableAttribute(
                            attributeName, attributeValueChunk, false));
                    attributeValueChunkI++;
                }
            }
        }
        final ImmutableList<ReplaceableAttribute> attributes = attributesBuilder
                .build();
        if (attributes.size() > 256) { // Limit imposed by the API
            logger.warn("model has " + Integer.toString(attributes.size())
                    + " attributes, more than the limit of 256.");
        }
        return attributes;
    }

    private ModelT __getModelFromAttributes(final List<Attribute> attributes,
            final String modelId) throws ModelIoException, NoSuchModelException {
        if (attributes.isEmpty()) {
            throw new NoSuchModelException(modelId);
        }

        final Multimap<String, String> attributeMultimap = LinkedHashMultimap
                .create();
        for (final Attribute attribute : attributes) {
            attributeMultimap.put(attribute.getName(), attribute.getValue());
        }

        final Map<String, String> attributeMap = Maps.newLinkedHashMap();
        for (final Map.Entry<String, Collection<String>> entry : attributeMultimap
                .asMap().entrySet()) {
            final String attributeName = entry.getKey();
            if (entry.getValue().size() == 1) {
                final String attributeValue = entry.getValue().iterator()
                        .next();
                attributeMap.put(attributeName, attributeValue);
            } else {
                String referenceAttributeValueChunkHash = null;
                // Use a map indexed by attributeValueChunkI rather than a list,
                // in case attributeValueChunkI is corrupted.
                // A sparse array would be nice here.
                final Map<Integer, String> attributeValueChunkMap = Maps
                        .newTreeMap();
                for (String attributeValueChunk : entry.getValue()) {
                    if (attributeValueChunk.length() < 38) {
                        logger.error(attributeName
                                + " has attribute value chunk with less than minimum length");
                        attributeValueChunkMap.clear();
                        break;
                    }

                    final String attributeValueChunkHash = attributeValueChunk
                            .substring(0, 32);
                    if (referenceAttributeValueChunkHash == null) {
                        referenceAttributeValueChunkHash = attributeValueChunkHash;
                    } else if (!attributeValueChunkHash
                            .equals(referenceAttributeValueChunkHash)) {
                        // Have conflicting hashes
                        logger.error("conflicting attribute value chunk hashes for "
                                + attributeName
                                + ", discarding attribute value");
                        attributeValueChunkMap.clear();
                        break;
                    }

                    final String attributeValueChunkIString = attributeValueChunk
                            .substring(32, 37);
                    final int attributeValueChunkI;
                    try {
                        attributeValueChunkI = Integer
                                .parseInt(attributeValueChunkIString);
                    } catch (final NumberFormatException e) {
                        logger.error("invalid attribute value chunk number "
                                + attributeValueChunkIString + " for "
                                + attributeName);
                        attributeValueChunkMap.clear();
                        break;
                    }

                    attributeValueChunk = attributeValueChunk.substring(37);

                    attributeValueChunkMap.put(attributeValueChunkI,
                            attributeValueChunk);
                }

                if (!attributeValueChunkMap.isEmpty()) {
                    final StringBuilder attributeValueBuilder = new StringBuilder();
                    boolean haveCompleteAttributeValue = true;
                    int attributeValueChunkI = 0;
                    for (final Map.Entry<Integer, String> attributeValueChunkEntry : attributeValueChunkMap
                            .entrySet()) {
                        if (attributeValueChunkEntry.getKey() == attributeValueChunkI) {
                            attributeValueBuilder
                            .append(attributeValueChunkEntry.getValue());
                            attributeValueChunkI++;
                        } else {
                            logger.error("missing attribute value chunk "
                                    + attributeValueChunkI + " for "
                                    + attributeName);
                            haveCompleteAttributeValue = false;
                            break;
                        }
                    }
                    if (haveCompleteAttributeValue) {
                        final String attributeValue = attributeValueBuilder
                                .toString();
                        attributeMap.put(attributeName, attributeValue);
                    }
                }
            }
        }

        return _getModel(new StringMapInputProtocol(attributeMap));
    }

    private ImmutableList<Item> __selectItems(final String selectExpression) {
        final ImmutableList.Builder<Item> items = ImmutableList.builder();
        SelectRequest selectRequest = new SelectRequest(selectExpression);
        selectRequest.setConsistentRead(true);
        SelectResult selectResult = client.select(selectRequest);
        items.addAll(selectResult.getItems());
        while (selectResult.getNextToken() != null) {
            final String nextToken = selectResult.getNextToken();
            selectRequest = new SelectRequest(selectExpression);
            selectRequest.setConsistentRead(true);
            selectRequest.setNextToken(nextToken);

            selectResult = client.select(selectRequest);
            items.addAll(selectResult.getItems());
        }
        return items.build();
    }

    private final AmazonSimpleDBClient client;
    private final String domainName;
    private final static int ITEM_BATCH_SIZE = 25;
}
