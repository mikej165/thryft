/*******************************************************************************
 * Copyright (c) 2013, Minor Gordon
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

package org.thryft.web.server.store;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.Set;

import org.apache.thrift.TBase;
import org.apache.thrift.TException;
import org.thryft.core.protocol.StringMapProtocol;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.services.dynamodb.AmazonDynamoDBClient;
import com.amazonaws.services.dynamodb.model.AttributeValue;
import com.amazonaws.services.dynamodb.model.BatchGetItemRequest;
import com.amazonaws.services.dynamodb.model.BatchGetItemResult;
import com.amazonaws.services.dynamodb.model.BatchResponse;
import com.amazonaws.services.dynamodb.model.BatchWriteItemRequest;
import com.amazonaws.services.dynamodb.model.BatchWriteItemResult;
import com.amazonaws.services.dynamodb.model.CreateTableRequest;
import com.amazonaws.services.dynamodb.model.DeleteItemRequest;
import com.amazonaws.services.dynamodb.model.DeleteRequest;
import com.amazonaws.services.dynamodb.model.DescribeTableRequest;
import com.amazonaws.services.dynamodb.model.GetItemRequest;
import com.amazonaws.services.dynamodb.model.GetItemResult;
import com.amazonaws.services.dynamodb.model.KeySchema;
import com.amazonaws.services.dynamodb.model.KeySchemaElement;
import com.amazonaws.services.dynamodb.model.KeysAndAttributes;
import com.amazonaws.services.dynamodb.model.ProvisionedThroughput;
import com.amazonaws.services.dynamodb.model.PutItemRequest;
import com.amazonaws.services.dynamodb.model.PutRequest;
import com.amazonaws.services.dynamodb.model.QueryRequest;
import com.amazonaws.services.dynamodb.model.QueryResult;
import com.amazonaws.services.dynamodb.model.ScalarAttributeType;
import com.amazonaws.services.dynamodb.model.TableDescription;
import com.amazonaws.services.dynamodb.model.TableStatus;
import com.amazonaws.services.dynamodb.model.UpdateTableRequest;
import com.amazonaws.services.dynamodb.model.WriteRequest;
import com.google.common.base.CaseFormat;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.google.common.collect.Sets;
import com.google.common.collect.Sets.SetView;

public final class DynamoDbStore<ModelT extends TBase<?, ?>> extends
        AwsKeyValueStore<ModelT> {
    public final static class Configuration extends AwsKeyValueStore.Configuration {
        public Configuration(final AWSCredentials credentials) {
            this(credentials, TABLE_READ_CAPACITY_UNITS_DEFAULT,
                    TABLE_WRITE_CAPACITY_UNITS_DEFAULT);
        }

        public Configuration(final AWSCredentials credentials,
                final long tableReadCapacityUnits,
                final long tableWriteCapacityUnits) {
            super(credentials);
            this.tableReadCapacityUnits = tableReadCapacityUnits;
            this.tableWriteCapacityUnits = tableWriteCapacityUnits;
        }

        public Configuration(final Properties properties) {
            super(properties);

            this.tableReadCapacityUnits = TABLE_READ_CAPACITY_UNITS_DEFAULT;
            this.tableWriteCapacityUnits = TABLE_WRITE_CAPACITY_UNITS_DEFAULT;

            final String tableReadCapacityUnitsString = properties
                    .getProperty(this.getClass().getCanonicalName()
                            + ".tableReadCapacityUnits");
            final String tableWriteCapacityUnitsString = properties
                    .getProperty(this.getClass().getCanonicalName()
                            + ".tableWriteCapacityUnits");
            if (tableReadCapacityUnitsString != null
                    && tableWriteCapacityUnitsString != null) {
                try {
                    final long tableReadCapacityUnits = Long
                            .parseLong(tableReadCapacityUnitsString);
                    final long tableWriteCapacityUnits = Long
                            .parseLong(tableWriteCapacityUnitsString);
                    if (tableReadCapacityUnits > 0
                            && tableWriteCapacityUnits > 0) {
                        this.tableReadCapacityUnits = tableReadCapacityUnits;
                        this.tableWriteCapacityUnits = tableWriteCapacityUnits;
                    }
                } catch (final NumberFormatException e) {
                }
            }
        }

        public long getTableReadCapacityUnits() {
            return tableReadCapacityUnits;
        }

        public long getTableWriteCapacityUnits() {
            return tableWriteCapacityUnits;
        }

        private long tableReadCapacityUnits;
        private long tableWriteCapacityUnits;

        // "A unit of Write Capacity enables you to perform one write per second
        // for items of up to 1KB in size. Similarly, a unit of Read Capacity
        // enables you to perform one strongly consistent read per second (or
        // two eventually consistent reads per second) of items of up to 1KB in
        // size. Larger items will require more capacity. You can calculate the
        // number of units of read and write capacity you need by estimating the
        // number of reads or writes you need to do per second and multiplying
        // by the size of your items (rounded up to the nearest KB)."
        public final static long TABLE_READ_CAPACITY_UNITS_DEFAULT = 200l;

        public final static long TABLE_WRITE_CAPACITY_UNITS_DEFAULT = 200l;
    }

    public DynamoDbStore(final Configuration configuration,
            final Class<ModelT> modelClass) {
        super(modelClass);
        checkNotNull(configuration);

        client = new AmazonDynamoDBClient(configuration.getCredentials());
        tableName = CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE,
                modelClass.getSimpleName());

        for (final String tableName : client.listTables().getTableNames()) {
            if (tableName.equals(this.tableName)) {
                final TableDescription tableDescription = __waitForTableToBecomeAvailable();
                if (tableDescription.getProvisionedThroughput()
                        .getReadCapacityUnits() < configuration
                        .getTableReadCapacityUnits()
                        || tableDescription.getProvisionedThroughput()
                                .getWriteCapacityUnits() < configuration
                                .getTableWriteCapacityUnits()) {
                    logger.info("re-provisioning table "
                            + this.tableName
                            + " from "
                            + tableDescription.getProvisionedThroughput()
                                    .getReadCapacityUnits()
                            + " to "
                            + configuration.getTableReadCapacityUnits()
                            + " read capacity units and "
                            + tableDescription.getProvisionedThroughput()
                                    .getWriteCapacityUnits() + " to "
                            + configuration.getTableWriteCapacityUnits()
                            + " write capacity units.");
                    client.updateTable(new UpdateTableRequest()
                            .withProvisionedThroughput(
                                    new ProvisionedThroughput()
                                            .withReadCapacityUnits(
                                                    tableDescription
                                                            .getProvisionedThroughput()
                                                            .getReadCapacityUnits() < configuration
                                                            .getTableReadCapacityUnits() ? configuration
                                                            .getTableReadCapacityUnits()
                                                            : tableDescription
                                                                    .getProvisionedThroughput()
                                                                    .getReadCapacityUnits())
                                            .withWriteCapacityUnits(
                                                    tableDescription
                                                            .getProvisionedThroughput()
                                                            .getWriteCapacityUnits() < configuration
                                                            .getTableWriteCapacityUnits() ? configuration
                                                            .getTableWriteCapacityUnits()
                                                            : tableDescription
                                                                    .getProvisionedThroughput()
                                                                    .getWriteCapacityUnits()))
                            .withTableName(this.tableName));
                    __waitForTableToBecomeAvailable();
                }
                return;
            }
        }

        logger.info("provisioning table " + this.tableName + " with "
                + configuration.getTableReadCapacityUnits()
                + " read capacity units and "
                + configuration.getTableWriteCapacityUnits()
                + " write capacity units.");
        client.createTable(new CreateTableRequest()
                .withKeySchema(
                        new KeySchema(new KeySchemaElement().withAttributeName(
                                HASH_KEY_ATTRIBUTE_NAME).withAttributeType(
                                ScalarAttributeType.S))
                                .withRangeKeyElement(new KeySchemaElement()
                                        .withAttributeName(
                                                RANGE_KEY_ATTRIBUTE_NAME)
                                        .withAttributeType(
                                                ScalarAttributeType.S)))
                .withProvisionedThroughput(
                        new ProvisionedThroughput().withReadCapacityUnits(
                                configuration.getTableReadCapacityUnits())
                                .withWriteCapacityUnits(
                                        configuration
                                                .getTableWriteCapacityUnits()))
                .withTableName(tableName));
        __waitForTableToBecomeAvailable();
    }

    @Override
    protected boolean _deleteModelById(final Key modelKey) {
        final boolean modelExisted = _headModelById(modelKey);
        client.deleteItem(new DeleteItemRequest(tableName,
                __toDynamoDbKey(modelKey)));
        return modelExisted;
    }

    @Override
    protected void _deleteModels(final String username) {
        final ImmutableSet<String> modelIds = _getModelIds(username);
        final List<WriteRequest> writeRequests = Lists.newArrayList();
        for (final String modelId : modelIds) {
            final Key modelKey = new Key(modelId, username);
            writeRequests.add(new WriteRequest()
                    .withDeleteRequest(new DeleteRequest()
                            .withKey(__toDynamoDbKey(modelKey))));
        }
        __batchWriteItem(writeRequests);
    }

    @Override
    protected ModelT _getModelById(final Key modelKey)
            throws NoSuchModelException {
        final GetItemResult getItemResult = client.getItem(new GetItemRequest(
                tableName, __toDynamoDbKey(modelKey)).withConsistentRead(true));
        final ModelT model = __getModelFromAttributes(getItemResult.getItem());
        if (model != null) {
            return model;
        } else {
            throw new NoSuchModelException(modelKey.getModelId());
        }
    }

    @Override
    protected int _getModelCount(final String username) {
        return _getModelIds(username).size();
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String username) {
        final Set<String> modelIds = Sets.newLinkedHashSet();
        for (final Map<String, AttributeValue> item : __query(new QueryRequest()
                .withAttributesToGet(RANGE_KEY_ATTRIBUTE_NAME)
                .withHashKeyValue(new AttributeValue(username)))) {
            final AttributeValue modelId = item.get(RANGE_KEY_ATTRIBUTE_NAME);
            checkNotNull(modelId);
            modelIds.add(modelId.getS());
        }
        return ImmutableSet.copyOf(modelIds);
    }

    @Override
    protected ImmutableSet<ModelT> _getModels(final String username) {
        final Set<ModelT> models = Sets.newLinkedHashSet();
        for (final Map<String, AttributeValue> item : __query(new QueryRequest()
                .withHashKeyValue(new AttributeValue(username)))) {
            final ModelT model = __getModelFromAttributes(item);
            if (model != null) {
                models.add(model);
            }
        }
        return ImmutableSet.copyOf(models);
    }

    @Override
    protected ImmutableSet<ModelT> _getModelsByIds(
            final ImmutableSet<Key> modelKeys) throws NoSuchModelException {
        if (modelKeys.isEmpty()) {
            return ImmutableSet.of();
        }

        final List<com.amazonaws.services.dynamodb.model.Key> keys = Lists
                .newArrayList();
        for (final Key modelKey : modelKeys) {
            keys.add(__toDynamoDbKey(modelKey));
        }
        BatchGetItemResult batchGetItemResult = client
                .batchGetItem(new BatchGetItemRequest()
                        .withRequestItems(ImmutableMap.of(tableName,
                                new KeysAndAttributes().withKeys(keys))));
        BatchResponse batchResponse = batchGetItemResult.getResponses().get(
                tableName);
        if (batchResponse == null) {
            return ImmutableSet.of();
        }
        final Map<Key, ModelT> models = Maps.newLinkedHashMap();
        models.putAll(__getModelsFromAttributes(batchResponse.getItems()));
        while (batchGetItemResult.getUnprocessedKeys() != null
                && !batchGetItemResult.getUnprocessedKeys().isEmpty()) {
            logger.info("_getModelsByIds: rereading "
                    + batchGetItemResult.getUnprocessedKeys().size()
                    + " unprocessed keys");
            batchGetItemResult = client.batchGetItem(new BatchGetItemRequest()
                    .withRequestItems(batchGetItemResult.getUnprocessedKeys()));
            batchResponse = batchGetItemResult.getResponses().get(tableName);
            if (batchResponse == null) {
                break;
            }
            models.putAll(__getModelsFromAttributes(batchResponse.getItems()));
        }

        final SetView<Key> notFoundKeys = Sets.difference(modelKeys,
                models.keySet());
        if (notFoundKeys.isEmpty()) {
            return ImmutableSet.copyOf(models.values());
        } else {
            throw new NoSuchModelException(notFoundKeys.iterator().next()
                    .getModelId());
        }
    }

    @Override
    protected void _putModel(final ModelT model, final Key modelKey) {
        client.putItem(new PutItemRequest(tableName, __getModelAttributes(
                model, modelKey)));
    }

    @Override
    protected void _putModels(final ImmutableMap<Key, ModelT> models) {
        final List<WriteRequest> writeRequests = Lists.newArrayList();
        for (final ImmutableMap.Entry<Key, ModelT> model : models.entrySet()) {
            writeRequests.add(new WriteRequest()
                    .withPutRequest(new PutRequest()
                            .withItem(__getModelAttributes(model.getValue(),
                                    model.getKey()))));
        }
        __batchWriteItem(writeRequests);
    }

    private void __batchWriteItem(final List<WriteRequest> writeRequests) {
        for (final List<WriteRequest> writeRequestBatch : Lists.partition(
                writeRequests, WRITE_REQUEST_BATCH_SIZE)) {
            BatchWriteItemResult batchWriteItemResult = client
                    .batchWriteItem(new BatchWriteItemRequest()
                            .withRequestItems(ImmutableMap.of(tableName,
                                    writeRequestBatch)));
            while (batchWriteItemResult.getUnprocessedItems() != null
                    && !batchWriteItemResult.getUnprocessedItems().isEmpty()) {
                logger.info("__batchWriteItem: rewriting "
                        + batchWriteItemResult.getUnprocessedItems().size()
                        + " unprocessed items from batch of "
                        + writeRequestBatch.size());
                batchWriteItemResult = client
                        .batchWriteItem(new BatchWriteItemRequest()
                                .withRequestItems(batchWriteItemResult
                                        .getUnprocessedItems()));
            }
        }
    }

    private Map<String, AttributeValue> __getModelAttributes(
            final ModelT model, final Key modelKey) {
        final StringMapProtocol oprot = new StringMapProtocol();
        try {
            model.write(oprot);
        } catch (final TException e) {
        }
        final ImmutableMap<String, String> stringMap = oprot.toStringMap();

        final Map<String, AttributeValue> attributes = Maps.newLinkedHashMap();
        for (final ImmutableMap.Entry<String, String> entry : stringMap
                .entrySet()) {
            if (!entry.getValue().isEmpty()) {
                attributes.put(entry.getKey(),
                        new AttributeValue(entry.getValue()));
            } else {
                attributes.put(entry.getKey(), new AttributeValue("."));
            }
        }
        attributes.put(RANGE_KEY_ATTRIBUTE_NAME,
                new AttributeValue(modelKey.getModelId()));
        attributes.put(HASH_KEY_ATTRIBUTE_NAME,
                new AttributeValue(modelKey.getUsername()));

        return attributes;
    }

    private ModelT __getModelFromAttributes(
            final Map<String, AttributeValue> item) {
        if (item == null) {
            // logger.error("__getModelFromAttributes: null item attribute-value map");
            return null;
        } else if (item.isEmpty()) {
            logger.error("__getModelFromAttributes: empty item attribute-value map");
            return null;
        }

        final Map<String, String> itemStringMap = Maps.newLinkedHashMap();
        for (final Map.Entry<String, AttributeValue> entry : item.entrySet()) {
            itemStringMap.put(entry.getKey(), entry.getValue().getS());
        }
        final ModelT model = _getModel(new StringMapProtocol(itemStringMap));
        if (model != null) {
            return model;
        } else {
            return null;
        }
    }

    private Key __getModelKeyFromAttributes(
            final Map<String, AttributeValue> item) {
        final AttributeValue modelId = item.get(RANGE_KEY_ATTRIBUTE_NAME);
        final AttributeValue username = item.get(HASH_KEY_ATTRIBUTE_NAME);
        if (modelId != null && username != null) {
            return new Key(modelId.getS(), username.getS());
        } else {
            return null;
        }
    }

    private ImmutableMap<Key, ModelT> __getModelsFromAttributes(
            final List<Map<String, AttributeValue>> items) {
        if (items == null || items.isEmpty()) {
            return ImmutableMap.of();
        }
        final Map<Key, ModelT> models = Maps.newLinkedHashMap();
        for (final Map<String, AttributeValue> item : items) {
            final ModelT model = __getModelFromAttributes(item);
            final Key modelKey = __getModelKeyFromAttributes(item);
            if (model != null && modelKey != null) {
                models.put(modelKey, model);
            }
        }
        return ImmutableMap.copyOf(models);
    }

    private ImmutableList<Map<String, AttributeValue>> __query(
            final QueryRequest queryRequest) {
        queryRequest.setConsistentRead(true);
        queryRequest.setTableName(tableName);

        try {
            QueryResult queryResult = client.query(queryRequest);
            // logger.info("__query: read " + queryResult.getItems().size() +
            // " items");
            final List<Map<String, AttributeValue>> items = Lists
                    .newArrayList(queryResult.getItems());
            while (queryResult.getLastEvaluatedKey() != null) {
                // logger.info("__query: requerying from "
                // + queryResult.getLastEvaluatedKey().getRangeKeyElement()
                // .getS());
                queryRequest.setExclusiveStartKey(queryResult
                        .getLastEvaluatedKey());
                queryResult = client.query(queryRequest);
                // logger.info("__query: read " + queryResult.getItems().size()
                // + " items");
                items.addAll(queryResult.getItems());
            }
            return ImmutableList.copyOf(items);
        } catch (final AmazonClientException e) {
            logger.error("error in __query: ", e);
            return ImmutableList.of();
        }
    }

    private com.amazonaws.services.dynamodb.model.Key __toDynamoDbKey(
            final Key modelKey) {
        return new com.amazonaws.services.dynamodb.model.Key()
                .withHashKeyElement(new AttributeValue(modelKey.getUsername()))
                .withRangeKeyElement(new AttributeValue(modelKey.getModelId()));
    }

    private TableDescription __waitForTableToBecomeAvailable() {
        final long startTime = System.currentTimeMillis();
        final long endTime = startTime + (10 * 60 * 1000);
        do {
            try {
                final DescribeTableRequest request = new DescribeTableRequest()
                        .withTableName(tableName);
                final TableDescription tableDescription = client.describeTable(
                        request).getTable();
                final String tableStatus = tableDescription.getTableStatus();
                if (tableStatus.equals(TableStatus.ACTIVE.toString())) {
                    return tableDescription;
                }
                if (System.currentTimeMillis() < endTime) {
                    logger.info("waiting for " + tableName
                            + " to become available");
                    try {
                        Thread.sleep(1000 * 1);
                    } catch (final Exception e) {
                    }
                } else {
                    break;
                }
            } catch (final AmazonServiceException e) {
                if (!e.getErrorCode().equalsIgnoreCase(
                        "ResourceNotFoundException")) {
                    throw e;
                }
            }
        } while (System.currentTimeMillis() < endTime);

        throw new RuntimeException("could not create table: never went active");
    }

    private final AmazonDynamoDBClient client;

    private final String HASH_KEY_ATTRIBUTE_NAME = "__username";

    private final String RANGE_KEY_ATTRIBUTE_NAME = "__modelId";

    private final String tableName;

    private final static int WRITE_REQUEST_BATCH_SIZE = 25;
}
