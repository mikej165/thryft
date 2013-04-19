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

package org.thryft.web.server.store.test;

import static org.hamcrest.Matchers.contains;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.math.BigDecimal;
import java.util.Map;

import org.apache.commons.lang.StringUtils;
import org.joda.time.DateTime;
import org.junit.After;
import org.junit.Test;
import org.thryft.web.server.store.Store;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Maps;

public abstract class StoreTest {
    protected StoreTest() {
        final ImmutableMap.Builder<String, StoreTestStruct> models = ImmutableMap
                .builder();
        // models.size() should be > SimpleDBStore batch size of 25
        for (int modelI = 0; modelI < 32; modelI++) {
            // Use a long string to overflow SimpleDBStore's attribute
            // value limit of 1024
            final StoreTestStruct model = new StoreTestStruct.Builder()
                    .setBoolField(true)
                    .setByteField((byte) modelI)
                    .setDateField(DateTime.now())
                    .setDateTimeField(DateTime.now())
                    .setDecimalField(new BigDecimal(modelI))
                    .setEnumField(StoreTestEnum.ENUMERATOR1)
                    .setI16Field((short) modelI)
                    .setI32Field(modelI)
                    .setI64Field((long) modelI)
                    .setListStringField(
                            ImmutableList.of("Test model "
                                    + StringUtils.repeat("0", 1024)
                                    + Integer.toString(modelI)))
                    .setMapStringStringField(
                            ImmutableMap.of("key", "Test model " + modelI))
                    .setSetStringField(ImmutableSet.of("Test model " + modelI))
                    .setStringField("testmodel" + modelI)
                    .setStructField(new StoreTestStruct()).build();
            models.put(model.getStringField(), model);
        }
        this.models = models.build();
    }

    @After
    public void tearDown() throws Exception {
        store.deleteModels(USERNAME);
        // assertEquals(0, store.getModelCount(USERNAME));
    }

    @Test
    public void testDeleteModelById() throws Store.ModelIoException {
        __putModels();

        final String deleteModelId = models.keySet().iterator().next();

        boolean ret = store.deleteModelById(deleteModelId, USERNAME);
        assertTrue(ret);

        final ImmutableMap<String, StoreTestStruct> models = store
                .getModels(USERNAME);

        final Map<String, StoreTestStruct> expectedModels = Maps
                .newLinkedHashMap(this.models);
        expectedModels.remove(deleteModelId);
        assertEquals(expectedModels, models);

        ret = store.deleteModelById("nonextantmodel", USERNAME);
        assertFalse(ret);
    }

    @Test
    public void testDeleteModels() throws Store.ModelIoException {
        ImmutableMap<String, StoreTestStruct> models = store
                .getModels(USERNAME);
        assertEquals(0, models.size());

        __putModels();

        models = store.getModels(USERNAME);
        assertEquals(this.models.size(), models.size());

        store.deleteModels(USERNAME);

        models = store.getModels(USERNAME);
        assertEquals(0, models.size());
    }

    @Test
    public void testGetModelById() throws Store.ModelIoException,
            Store.NoSuchModelException {
        __putModels();

        for (final ImmutableMap.Entry<String, StoreTestStruct> modelEntry : models
                .entrySet()) {
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USERNAME));
        }
    }

    @Test
    public void testGetModelByIdCached() throws Store.ModelIoException,
            Store.NoSuchModelException {
        __putModels();

        for (final ImmutableMap.Entry<String, StoreTestStruct> modelEntry : models
                .entrySet()) {
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USERNAME));
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USERNAME));
            break;
        }
    }

    @Test
    public void testGetModelByIdMissing() throws Store.ModelIoException {
        __putModels();

        try {
            store.getModelById("nonextantmodel", USERNAME);
            fail();
        } catch (final Store.NoSuchModelException e) {
        }
    }

    @Test
    public void testGetModelCount() throws Store.ModelIoException {
        __putModels();

        final int modelCount = store.getModelCount(USERNAME);
        assertEquals(models.size(), modelCount);
    }

    @Test
    public void testGetModelIds() throws Store.ModelIoException {
        __putModels();

        final ImmutableSet<String> modelIds = store.getModelIds(USERNAME);
        assertEquals(models.keySet(), modelIds);
    }

    @Test
    public void testGetModels() throws Store.ModelIoException {
        __putModels();

        final ImmutableMap<String, StoreTestStruct> models = store
                .getModels(USERNAME);
        assertEquals(this.models, models);
    }

    @Test
    public void testGetModelsByIds() throws Store.ModelIoException,
            Store.NoSuchModelException {
        __putModels();

        final ImmutableMap<String, StoreTestStruct> models = store
                .getModelsByIds(this.models.keySet(), USERNAME);
        assertEquals(this.models, models);

        for (final ImmutableMap.Entry<String, StoreTestStruct> modelEntry : models
                .entrySet()) {
            assertEquals(modelEntry.getValue(),
                    store.getModelById(modelEntry.getKey(), USERNAME));
        }

        for (final String modelId : models.keySet()) {
            try {
                store.getModelsByIds(
                        ImmutableSet.of(modelId, "nonextantmodel"), USERNAME);
                fail();
            } catch (final Store.NoSuchModelException e) {
                assertEquals("nonextantmodel", e.getId());
            }
            break;
        }
    }

    @Test
    public void testGetUsernames() throws Store.ModelIoException {
        __putModels();

        ImmutableSet<String> usernames;
        try {
            usernames = store.getUsernames();
        } catch (final UnsupportedOperationException e) {
            return;
        }

        assertThat(usernames, contains(USERNAME));
    }

    @Test
    public void testHeadModelById() throws Store.ModelIoException,
            Store.NoSuchModelException {
        __putModels();

        for (final String modelId : models.keySet()) {
            assertTrue(store.headModelById(modelId, USERNAME));
        }

        assertFalse(store.headModelById("nonextantsku", USERNAME));
    }

    @Test
    public void testPutModel() throws Store.ModelIoException,
            Store.NoSuchModelException {
        for (final ImmutableMap.Entry<String, StoreTestStruct> modelEntry : models
                .entrySet()) {
            final StoreTestStruct expectedModel = modelEntry.getValue();
            store.putModel(expectedModel, modelEntry.getKey(), USERNAME);
            final StoreTestStruct actualModel = store.getModelById(
                    modelEntry.getKey(), USERNAME);
            assertEquals(expectedModel, actualModel);
            break;
        }
    }

    @Test
    public void testPutModels() throws Store.ModelIoException {
        assertEquals(0, store.getModels(USERNAME).size());
        store.putModels(ImmutableMap.<String, StoreTestStruct> of(), USERNAME);
        assertEquals(0, store.getModels(USERNAME).size());

        __putModels();
        assertEquals(models, store.getModels(USERNAME));

        __putModels(); // Should overwrite
        assertEquals(models, store.getModels(USERNAME));
    }

    protected void _setUp(final Store<StoreTestStruct> store) {
        this.store = store;
    }

    private void __putModels() throws Store.ModelIoException {
        store.putModels(models, USERNAME);
    }

    private final ImmutableMap<String, StoreTestStruct> models;

    private Store<StoreTestStruct> store;

    private final static String USERNAME = StoreTest.class.getSimpleName()
            + "_user";
}
