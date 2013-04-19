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

import org.apache.thrift.TBase;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public class PrimaryBackupStore<ModelT extends TBase<?, ?>> extends
        Store<ModelT> {
    public PrimaryBackupStore(final Store<ModelT> primaryStore,
            final Store<ModelT> backupStore) {
        super(primaryStore._getModelClass());
        this.backupStore = checkNotNull(backupStore);
        this.primaryStore = checkNotNull(primaryStore);
    }

    @Override
    protected boolean _deleteModelById(final String modelId,
            final String username) {
        if (primaryStore._deleteModelById(modelId, username)) {
            backupStore._deleteModelById(modelId, username);
            return true;
        } else {
            return false;
        }
    }

    @Override
    protected void _deleteModels(final String username) {
        primaryStore._deleteModels(username);
        backupStore._deleteModels(username);
    }

    @Override
    protected ModelT _getModelById(final String modelId, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        return primaryStore._getModelById(modelId, username);
    }

    @Override
    protected int _getModelCount(final String username) {
        return primaryStore._getModelCount(username);
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String username) {
        return primaryStore._getModelIds(username);
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModels(final String username) {
        return primaryStore._getModels(username);
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        return primaryStore._getModelsByIds(modelIds, username);
    }

    @Override
    protected ImmutableSet<String> _getUsernames() {
        return primaryStore._getUsernames();
    }

    @Override
    protected boolean _headModelById(final String modelId, final String username) {
        return primaryStore._headModelById(modelId, username);
    }

    @Override
    protected void _putModel(final ModelT model, final String modelId,
            final String username) throws ModelIoException {
        primaryStore.putModel(model, modelId, username);
        backupStore.putModel(model, modelId, username);
    }

    @Override
    protected void _putModels(final ImmutableMap<String, ModelT> models,
            final String username) throws ModelIoException {
        primaryStore.putModels(models, username);
        backupStore.putModels(models, username);
    }

    private final Store<ModelT> backupStore;

    private final Store<ModelT> primaryStore;
}
