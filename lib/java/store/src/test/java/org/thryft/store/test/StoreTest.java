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

package org.thryft.store.test;

import static org.hamcrest.Matchers.contains;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.math.BigDecimal;
import java.util.Date;
import java.util.Map;

import org.apache.commons.lang.StringUtils;
import org.junit.After;
import org.junit.Test;
import org.thryft.protocol.test.NestedProtocolTestStruct;
import org.thryft.protocol.test.ProtocolTestEnum;
import org.thryft.protocol.test.ProtocolTestStruct;
import org.thryft.store.AbstractStore;
import org.thryft.store.Store.ModelIoException;
import org.thryft.store.Store.NoSuchModelException;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Maps;

public abstract class StoreTest {
    protected StoreTest() {
        final ImmutableMap.Builder<String, ProtocolTestStruct> models = ImmutableMap
                .builder();
        // models.size() should be > SimpleDBStore batch size of 25
        for (int modelI = 0; modelI < 32; modelI++) {
            // Use a long string to overflow SimpleDBStore's attribute
            // value limit of 1024
            final ProtocolTestStruct model = new ProtocolTestStruct.Builder()
                    .setBoolField(true)
                    .setDateTimeField(new Date())
                    .setDecimalField(new BigDecimal(modelI))
                    .setEnumField(ProtocolTestEnum.ENUMERATOR1)
                    .setI8Field((byte) modelI)
                    .setI16Field((short) modelI)
                    .setI32Field(modelI)
                    .setI64Field(modelI)
                    .setListStringField(
                            ImmutableList.of("Test model "
                                    + StringUtils.repeat("0", 1024)
                                    + Integer.toString(modelI)))
                    .setMapStringStringField(
                            ImmutableMap.of("key", "Test model " + modelI))
                    .setRequiredI32Field(1).setRequiredStringField("test")
                    .setSetStringField(ImmutableSet.of("Test model " + modelI))
                    .setStringField("testmodel" + modelI)
                    .setStructField(new NestedProtocolTestStruct(1, "test"))
                    .build();
            models.put(model.getStringField().get(), model);
        }
        this.models = models.build();
    }

    @After
    public void tearDown() throws Exception {
        store.deleteModels(USER_ID);
        // assertEquals(0, store.getModelCount(USER_ID));
    }

    @Test
    public void testDeleteModelById() throws ModelIoException {
        __putModels();

        final String deleteModelId = models.keySet().iterator().next();

        boolean ret = store.deleteModelById(deleteModelId, USER_ID);
        assertTrue(ret);

        final ImmutableMap<String, ProtocolTestStruct> models = store
                .getModels(USER_ID);

        final Map<String, ProtocolTestStruct> expectedModels = Maps
                .newLinkedHashMap(this.models);
        expectedModels.remove(deleteModelId);
        assertEquals(expectedModels, models);

        ret = store.deleteModelById("nonextantmodel", USER_ID);
        assertFalse(ret);
    }

    @Test
    public void testDeleteModels() throws ModelIoException {
        ImmutableMap<String, ProtocolTestStruct> models = store
                .getModels(USER_ID);
        assertEquals(0, models.size());

        __putModels();

        models = store.getModels(USER_ID);
        assertEquals(this.models.size(), models.size());

        store.deleteModels(USER_ID);

        models = store.getModels(USER_ID);
        assertEquals(0, models.size());
    }

    @Test
    public void testGetModelById() throws ModelIoException,
            NoSuchModelException {
        __putModels();

        for (final ImmutableMap.Entry<String, ProtocolTestStruct> modelEntry : models
                .entrySet()) {
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USER_ID));
        }
    }

    @Test
    public void testGetModelByIdCached() throws ModelIoException,
            NoSuchModelException {
        __putModels();

        for (final ImmutableMap.Entry<String, ProtocolTestStruct> modelEntry : models
                .entrySet()) {
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USER_ID));
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USER_ID));
            break;
        }
    }

    @Test
    public void testGetModelByIdMissing() throws ModelIoException {
        __putModels();

        try {
            store.getModelById("nonextantmodel", USER_ID);
            fail();
        } catch (final NoSuchModelException e) {
        }
    }

    @Test
    public void testGetModelCount() throws ModelIoException {
        __putModels();

        final int modelCount = store.getModelCount(USER_ID);
        assertEquals(models.size(), modelCount);
    }

    @Test
    public void testGetModelIds() throws ModelIoException {
        __putModels();

        final ImmutableSet<String> modelIds = store.getModelIds(USER_ID);
        assertEquals(models.keySet(), modelIds);
    }

    @Test
    public void testGetModels() throws ModelIoException {
        __putModels();

        final ImmutableMap<String, ProtocolTestStruct> models = store
                .getModels(USER_ID);
        assertEquals(this.models, models);
    }

    @Test
    public void testGetModelsByIds() throws ModelIoException,
            NoSuchModelException {
        __putModels();

        final ImmutableMap<String, ProtocolTestStruct> models = store
                .getModelsByIds(this.models.keySet(), USER_ID);
        assertEquals(this.models, models);

        for (final ImmutableMap.Entry<String, ProtocolTestStruct> modelEntry : models
                .entrySet()) {
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USER_ID));
        }

        for (final String modelId : models.keySet()) {
            try {
                store.getModelsByIds(
                        ImmutableSet.of(modelId, "nonextantmodel"), USER_ID);
                fail();
            } catch (final NoSuchModelException e) {
                assertEquals("nonextantmodel", e.getId());
            }
            break;
        }
    }

    @Test
    public void testGetUserIds() throws ModelIoException {
        __putModels();

        ImmutableSet<String> userIds;
        try {
            userIds = store.getUserIds();
        } catch (final UnsupportedOperationException e) {
            return;
        }

        assertThat(userIds, contains(USER_ID));
    }

    @Test
    public void testHeadModelById() throws ModelIoException,
            NoSuchModelException {
        __putModels();

        for (final String modelId : models.keySet()) {
            assertTrue(store.headModelById(modelId, USER_ID));
        }

        assertFalse(store.headModelById("nonextantsku", USER_ID));
    }

    @Test
    public void testPutModel() throws ModelIoException, NoSuchModelException {
        for (final ImmutableMap.Entry<String, ProtocolTestStruct> modelEntry : models
                .entrySet()) {
            final ProtocolTestStruct expectedModel = modelEntry.getValue();
            store.putModel(expectedModel, modelEntry.getKey(), USER_ID);
            final ProtocolTestStruct actualModel = store.getModelById(
                    modelEntry.getKey(), USER_ID);
            assertEquals(expectedModel, actualModel);
            break;
        }
    }

    @Test
    public void testPutModels() throws ModelIoException {
        assertEquals(0, store.getModels(USER_ID).size());
        store.putModels(ImmutableMap.<String, ProtocolTestStruct> of(), USER_ID);
        assertEquals(0, store.getModels(USER_ID).size());

        __putModels();
        assertEquals(models, store.getModels(USER_ID));

        __putModels(); // Should overwrite
        assertEquals(models, store.getModels(USER_ID));
    }

    protected void _setUp(final AbstractStore<ProtocolTestStruct> store) {
        this.store = store;
    }

    private void __putModels() throws ModelIoException {
        store.putModels(models, USER_ID);
    }

    private final ImmutableMap<String, ProtocolTestStruct> models;

    private AbstractStore<ProtocolTestStruct> store;

    private final static String USER_ID = StoreTest.class.getSimpleName()
            + "_user";
}
