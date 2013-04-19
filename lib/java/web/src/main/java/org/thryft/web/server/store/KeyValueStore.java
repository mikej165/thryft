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
import static org.thryft.core.Preconditions.checkNotEmpty;

import java.util.Map;

import org.apache.thrift.TBase;
import org.thryft.web.server.util.FileNameCodec;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class KeyValueStore<ModelT extends TBase<?, ?>> extends
        Store<ModelT> {
    protected final static class Key {
        public static Key parse(final String key) {
            final String[] components = key.split(SEPARATOR, 2);
            return new Key(FileNameCodec.decodeFileName(components[1]),
                    FileNameCodec.decodeFileName(components[0]));
        }

        public static String prefix(final String username) {
            return FileNameCodec.encodeFileName(username) + SEPARATOR;
        }

        public Key(final String modelId, final String username) {
            this.modelId = checkNotEmpty(modelId);
            this.username = checkNotEmpty(username);
        }

        @Override
        public boolean equals(final Object other) {
            if (!(other instanceof Key)) {
                return false;
            }
            final Key keyOther = (Key) other;
            return getModelId().equals(keyOther.getModelId())
                    && getUsername().equals(keyOther.getUsername());
        }

        public String getEncodedModelId() {
            return FileNameCodec.encodeFileName(modelId);
        }

        public String getEncodedUsername() {
            return FileNameCodec.encodeFileName(username);
        }

        public String getModelId() {
            return modelId;
        }

        public String getUsername() {
            return username;
        }

        @Override
        public int hashCode() {
            return toString().hashCode();
        }

        @Override
        public String toString() {
            return getEncodedUsername() + SEPARATOR + getEncodedModelId();
        }

        private final String modelId;

        private final String username;

        private final static String SEPARATOR = "_";
    }

    protected KeyValueStore(final Class<ModelT> modelClass) {
        super(modelClass);
    }

    protected abstract boolean _deleteModelById(Key modelKey);

    @Override
    protected boolean _deleteModelById(final String modelId,
            final String username) {
        return _deleteModelById(new Key(modelId, username));
    }

    protected String _getKeyPrefix(final String username) {
        return FileNameCodec.encodeFileName(username);
    }

    protected abstract ModelT _getModelById(Key modelKey)
            throws org.thryft.web.server.store.Store.NoSuchModelException;

    @Override
    protected ModelT _getModelById(final String modelId, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        return _getModelById(new Key(modelId, username));
    }

    protected abstract ImmutableMap<String, ModelT> _getModelsByIds(
            ImmutableSet<Key> modelKeys)
            throws org.thryft.web.server.store.Store.NoSuchModelException;

    @Override
    protected ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        final ImmutableSet.Builder<Key> modelKeys = ImmutableSet.builder();
        for (final String modelId : modelIds) {
            modelKeys.add(new Key(modelId, username));
        }
        return _getModelsByIds(modelKeys.build());
    }

    @Override
    protected ImmutableSet<String> _getUsernames() {
        throw new UnsupportedOperationException();
    }

    protected boolean _headModelById(final Key modelKey) {
        try {
            _getModelById(modelKey);
            return true;
        } catch (final NoSuchModelException e) {
            return false;
        }
    }

    @Override
    protected boolean _headModelById(final String modelId, final String username) {
        checkNotNull(modelId);
        checkNotNull(username);
        return _headModelById(new Key(modelId, username));
    }

    protected abstract void _putModel(ModelT model, Key modelKey)
            throws ModelIoException;

    @Override
    protected void _putModel(final ModelT model, final String modelId,
            final String username) throws ModelIoException {
        _putModel(model, new Key(modelId, username));
    }

    protected abstract void _putModels(ImmutableMap<Key, ModelT> models)
            throws ModelIoException;

    @Override
    protected void _putModels(final ImmutableMap<String, ModelT> models,
            final String username) throws ModelIoException {
        final ImmutableMap.Builder<Key, ModelT> modelMap = ImmutableMap
                .builder();
        for (final Map.Entry<String, ModelT> model : models.entrySet()) {
            modelMap.put(new Key(model.getKey(), username), model.getValue());
        }
        _putModels(modelMap.build());
    }
}
