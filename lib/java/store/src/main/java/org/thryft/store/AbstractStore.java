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

import java.lang.reflect.InvocationTargetException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.thryft.Base;
import org.thryft.protocol.InputProtocol;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class AbstractStore<ModelT extends Base<?>> implements
        Store<ModelT> {
    protected AbstractStore(final Class<ModelT> modelClass) {
        logger = LoggerFactory.getLogger(getClass());
        this.modelClass = checkNotNull(modelClass);
    }

    @Override
    public final boolean deleteModelById(final String modelId,
            final String userId) throws ModelIoException {
        checkNotNull(modelId);
        checkNotNull(userId);
        return _deleteModelById(modelId, userId);
    }

    @Override
    public void deleteModels() throws ModelIoException {
        for (final String userId : getUserIds()) {
            deleteModels(userId);
        }
    }

    @Override
    public final void deleteModels(final String userId) throws ModelIoException {
        checkNotNull(userId);
        _deleteModels(userId);
    }

    @Override
    public final ModelT getModelById(final String modelId, final String userId)
            throws ModelIoException, NoSuchModelException {
        checkNotNull(modelId);
        checkNotNull(userId);
        return checkNotNull(_getModelById(modelId, userId));
    }

    public final Class<ModelT> getModelClass() {
        return modelClass;
    }

    @Override
    public final int getModelCount(final String userId) throws ModelIoException {
        checkNotNull(userId);
        return _getModelCount(userId);
    }

    @Override
    public final ImmutableSet<String> getModelIds(final String userId)
            throws ModelIoException {
        checkNotNull(userId);
        return checkNotNull(_getModelIds(userId));
    }

    @Override
    public final ImmutableMap<String, ModelT> getModels(final String userId)
            throws ModelIoException {
        checkNotNull(userId);
        return checkNotNull(_getModels(userId));
    }

    @Override
    public final ImmutableMap<String, ModelT> getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws ModelIoException, NoSuchModelException {
        checkNotNull(modelIds);
        if (modelIds.isEmpty()) {
            return ImmutableMap.of();
        }
        checkNotNull(userId);
        return checkNotNull(_getModelsByIds(modelIds, userId));
    }

    @Override
    public final ImmutableSet<String> getUserIds() throws ModelIoException {
        return checkNotNull(_getUserIds());
    }

    @Override
    public final boolean headModelById(final String modelId, final String userId)
            throws ModelIoException {
        checkNotNull(modelId);
        checkNotNull(userId);
        return _headModelById(modelId, userId);
    }

    @Override
    public final void putModel(final ModelT model, final String modelId,
            final String userId) throws ModelIoException {
        checkNotNull(model);
        checkNotNull(modelId);
        checkNotNull(userId);
        _putModel(model, modelId, userId);
    }

    @Override
    public final void putModels(final ImmutableMap<String, ModelT> models,
            final String userId) throws ModelIoException {
        checkNotNull(models);
        if (models.isEmpty()) {
            return;
        }
        checkNotNull(userId);
        _putModels(models, userId);
    }

    protected abstract boolean _deleteModelById(final String modelId,
            final String userId) throws ModelIoException;

    protected abstract void _deleteModels(final String userId)
            throws ModelIoException;

    protected ModelT _getModel(final InputProtocol iprot) throws ModelIoException {
        try {
            return modelClass.getConstructor(InputProtocol.class)
                    .newInstance(iprot);
        } catch (InstantiationException | IllegalAccessException
                | IllegalArgumentException | InvocationTargetException
                | NoSuchMethodException | SecurityException e) {
            logger.error("error creating model from protocol: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    protected abstract ModelT _getModelById(final String modelId,
            final String userId) throws ModelIoException, NoSuchModelException;

    protected abstract int _getModelCount(final String userId)
            throws ModelIoException;

    protected abstract ImmutableSet<String> _getModelIds(final String userId)
            throws ModelIoException;

    protected abstract ImmutableMap<String, ModelT> _getModels(
            final String userId) throws ModelIoException;

    protected abstract ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws ModelIoException, NoSuchModelException;

    protected abstract ImmutableSet<String> _getUserIds()
            throws ModelIoException;

    protected abstract boolean _headModelById(final String modelId,
            final String userId) throws ModelIoException;

    protected abstract void _putModel(final ModelT model, final String modelId,
            final String userId) throws ModelIoException;

    protected abstract void _putModels(
            final ImmutableMap<String, ModelT> models, final String userId)
            throws ModelIoException;

    protected final Logger logger;

    private final Class<ModelT> modelClass;
}
