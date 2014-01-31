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

import static org.thryft.Preconditions.checkNotEmpty;

import org.thryft.Base;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public interface Store<ModelT extends Base<?>> {
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

    public boolean deleteModelById(String modelId, String userId)
            throws ModelIoException;

    public void deleteModels() throws ModelIoException;

    public void deleteModels(String userId) throws ModelIoException;

    public ModelT getModelById(String modelId, String userId)
            throws ModelIoException, NoSuchModelException;

    public int getModelCount(String userId) throws ModelIoException;

    public ImmutableSet<String> getModelIds(String userId)
            throws ModelIoException;

    public ImmutableMap<String, ModelT> getModels(String userId)
            throws ModelIoException;

    public ImmutableMap<String, ModelT> getModelsByIds(
            ImmutableSet<String> modelIds, String userId)
            throws ModelIoException, NoSuchModelException;

    public ImmutableSet<String> getUserIds() throws ModelIoException;

    public boolean headModelById(String modelId, String userId)
            throws ModelIoException;

    public void putModel(ModelT model, String modelId, String userId)
            throws ModelIoException;

    public void putModels(ImmutableMap<String, ModelT> models, String userId)
            throws ModelIoException;
}
