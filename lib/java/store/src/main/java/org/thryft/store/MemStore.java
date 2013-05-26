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

import org.thryft.TBase;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Table;
import com.google.common.collect.TreeBasedTable;

public final class MemStore<ModelT extends TBase<?>> extends AbstractStore<ModelT> {
    public MemStore(final Class<ModelT> modelClass) {
        super(modelClass);
    }

    @Override
    protected synchronized boolean _deleteModelById(final String modelId,
            final String userId) {
        return models.remove(userId, modelId) != null;
    }

    @Override
    protected synchronized void _deleteModels(final String userId) {
        final ImmutableSet<String> columnKeys = ImmutableSet.copyOf(models.row(
                userId).keySet());
        for (final String columnKey : columnKeys) {
            models.remove(userId, columnKey);
        }
    }

    @Override
    protected synchronized ModelT _getModelById(final String modelId,
            final String userId) throws NoSuchModelException {
        final ModelT model = models.get(userId, modelId);
        if (model != null) {
            return model;
        } else {
            throw new NoSuchModelException(modelId);
        }
    }

    @Override
    protected synchronized int _getModelCount(final String userId) {
        return models.row(userId).size();
    }

    @Override
    protected synchronized ImmutableSet<String> _getModelIds(final String userId) {
        return ImmutableSet.copyOf(models.row(userId).keySet());
    }

    @Override
    protected synchronized ImmutableMap<String, ModelT> _getModels(
            final String userId) {
        return ImmutableMap.copyOf(models.row(userId));
    }

    @Override
    protected synchronized ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws NoSuchModelException {
        final ImmutableMap.Builder<String, ModelT> models = ImmutableMap
                .builder();
        for (final String modelId : modelIds) {
            models.put(modelId, getModelById(modelId, userId));
        }
        return models.build();
    }

    @Override
    protected ImmutableSet<String> _getUserIds() {
        return ImmutableSet.copyOf(models.rowKeySet());
    }

    @Override
    protected synchronized boolean _headModelById(final String modelId,
            final String userId) {
        return models.get(userId, modelId) != null;
    }

    @Override
    protected synchronized void _putModel(final ModelT model,
            final String modelId, final String userId) {
        models.put(userId, modelId, model);
    }

    @Override
    protected synchronized void _putModels(
            final ImmutableMap<String, ModelT> models, final String userId) {
        for (final ImmutableMap.Entry<String, ModelT> model : models.entrySet()) {
            this.models.put(userId, model.getKey(), model.getValue());
        }
    }

    private final Table<String, String, ModelT> models = TreeBasedTable
            .create(); // user ID, model ID, model
}
