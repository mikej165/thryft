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

package org.thryft.store;

import static com.google.common.base.Preconditions.checkNotNull;

import org.thryft.TBase;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public class PrimaryBackupStore<ModelT extends TBase<?>> extends
        AbstractStore<ModelT> {
    public PrimaryBackupStore(final AbstractStore<ModelT> primaryStore,
            final AbstractStore<ModelT> backupStore) {
        super(primaryStore.getModelClass());
        this.backupStore = checkNotNull(backupStore);
        this.primaryStore = checkNotNull(primaryStore);
    }

    @Override
    protected boolean _deleteModelById(final String modelId, final String userId)
            throws ModelIoException {
        if (primaryStore._deleteModelById(modelId, userId)) {
            backupStore._deleteModelById(modelId, userId);
            return true;
        } else {
            return false;
        }
    }

    @Override
    protected void _deleteModels(final String userId) throws ModelIoException {
        primaryStore._deleteModels(userId);
        backupStore._deleteModels(userId);
    }

    @Override
    protected ModelT _getModelById(final String modelId, final String userId)
            throws ModelIoException, NoSuchModelException {
        return primaryStore._getModelById(modelId, userId);
    }

    @Override
    protected int _getModelCount(final String userId) throws ModelIoException {
        return primaryStore._getModelCount(userId);
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String userId)
            throws ModelIoException {
        return primaryStore._getModelIds(userId);
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModels(final String userId)
            throws ModelIoException {
        return primaryStore._getModels(userId);
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws ModelIoException, NoSuchModelException {
        return primaryStore._getModelsByIds(modelIds, userId);
    }

    @Override
    protected ImmutableSet<String> _getUserIds() throws ModelIoException {
        return primaryStore._getUserIds();
    }

    @Override
    protected boolean _headModelById(final String modelId, final String userId)
            throws ModelIoException {
        return primaryStore._headModelById(modelId, userId);
    }

    @Override
    protected void _putModel(final ModelT model, final String modelId,
            final String userId) throws ModelIoException {
        primaryStore.putModel(model, modelId, userId);
        backupStore.putModel(model, modelId, userId);
    }

    @Override
    protected void _putModels(final ImmutableMap<String, ModelT> models,
            final String userId) throws ModelIoException {
        primaryStore.putModels(models, userId);
        backupStore.putModels(models, userId);
    }

    private final AbstractStore<ModelT> backupStore;

    private final AbstractStore<ModelT> primaryStore;
}
