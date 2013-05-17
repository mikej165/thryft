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
import static org.thryft.Preconditions.checkNotEmpty;

import java.lang.reflect.InvocationTargetException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.thryft.TBase;
import org.thryft.protocol.TProtocol;

import com.google.common.base.Optional;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class Store<ModelT extends TBase<?>> {
    @SuppressWarnings("serial")
    public final static class ModelIoException extends Exception {
        public ModelIoException(final String message) {
            super(message);
            this.id = "";
        }

        public ModelIoException(final Throwable cause) {
            super(cause);
            this.id = "";
        }

        public ModelIoException(final Throwable cause, final String id) {
            super(cause);
            this.id = checkNotEmpty(id);
        }

        public String getId() {
            return id;
        }

        private final String id;
    }

    @SuppressWarnings("serial")
    public final static class NoSuchModelException extends Exception {
        public NoSuchModelException(final String id) {
            super(id);
            this.id = id;
        }

        public String getId() {
            return id;
        }

        private final String id;
    }

    protected Store(final Class<ModelT> modelClass) {
        logger = LoggerFactory.getLogger(getClass());
        this.modelClass = checkNotNull(modelClass);
    }

    public final boolean deleteModelById(final String modelId,
            final String userId) {
        checkNotNull(modelId);
        checkNotNull(userId);
        return _deleteModelById(modelId, userId);
    }

    public final void deleteModels(final String userId) {
        checkNotNull(userId);
        _deleteModels(userId);
    }

    public final ModelT getModelById(final String modelId, final String userId)
            throws NoSuchModelException {
        checkNotNull(modelId);
        checkNotNull(userId);
        return checkNotNull(_getModelById(modelId, userId));
    }

    public final int getModelCount(final String userId) {
        checkNotNull(userId);
        return _getModelCount(userId);
    }

    public final ImmutableSet<String> getModelIds(final String userId) {
        checkNotNull(userId);
        return checkNotNull(_getModelIds(userId));
    }

    public final ImmutableMap<String, ModelT> getModels(final String userId) {
        checkNotNull(userId);
        return checkNotNull(_getModels(userId));
    }

    public final ImmutableMap<String, ModelT> getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws NoSuchModelException {
        checkNotNull(modelIds);
        if (modelIds.isEmpty()) {
            return ImmutableMap.of();
        }
        checkNotNull(userId);
        return checkNotNull(_getModelsByIds(modelIds, userId));
    }

    public final ImmutableSet<String> getUserIds() {
        return checkNotNull(_getUserIds());
    }

    public final boolean headModelById(final String modelId,
            final String userId) {
        checkNotNull(modelId);
        checkNotNull(userId);
        return _headModelById(modelId, userId);
    }

    public final void putModel(final ModelT model, final String modelId,
            final String userId) throws ModelIoException {
        checkNotNull(model);
        checkNotNull(modelId);
        checkNotNull(userId);
        _putModel(model, modelId, userId);
    }

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
            final String userId);

    protected abstract void _deleteModels(final String userId);

    protected Optional<ModelT> _getModel(final TProtocol iprot) {
        try {
            return Optional.of(modelClass.getConstructor(TProtocol.class)
                    .newInstance(iprot));
        } catch (final IllegalArgumentException e) {
            logger.error("exception reading:", e);
        } catch (final SecurityException e) {
            logger.error("exception reading model:", e);
        } catch (final InstantiationException e) {
            logger.error("exception reading model:", e);
        } catch (final IllegalAccessException e) {
            logger.error("exception reading model:", e);
        } catch (final InvocationTargetException e) {
            logger.error("exception reading model:", e);
        } catch (final NoSuchMethodException e) {
            logger.error("exception reading model:", e);
        }

        return Optional.<ModelT> absent();
    }

    protected abstract ModelT _getModelById(final String modelId,
            final String userId) throws NoSuchModelException;

    protected final Class<ModelT> _getModelClass() {
        return modelClass;
    }

    protected abstract int _getModelCount(final String userId);

    protected abstract ImmutableSet<String> _getModelIds(final String userId);

    protected abstract ImmutableMap<String, ModelT> _getModels(
            final String userId);

    protected abstract ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws NoSuchModelException;

    protected abstract ImmutableSet<String> _getUserIds();

    protected abstract boolean _headModelById(final String modelId,
            final String userId);

    protected abstract void _putModel(final ModelT model, final String modelId,
            final String userId) throws ModelIoException;

    protected abstract void _putModels(
            final ImmutableMap<String, ModelT> models, final String userId)
            throws ModelIoException;

    protected final Logger logger;

    private final Class<ModelT> modelClass;
}
