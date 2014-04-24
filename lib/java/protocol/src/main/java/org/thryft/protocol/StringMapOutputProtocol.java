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

package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;
import static com.google.common.base.Preconditions.checkState;
import static org.thryft.Preconditions.checkNotEmpty;

import java.util.Map;

import org.thryft.protocol.StringMapOutputProtocol.NestedOutputProtocol;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Maps;

public class StringMapOutputProtocol extends
        StackedOutputProtocol<NestedOutputProtocol> {
    protected abstract class NestedOutputProtocol extends
            AbstractOutputProtocol {
        protected NestedOutputProtocol(final String myKey) {
            this.myKey = myKey;
        }

        @Override
        public final void writeBool(final boolean value)
                throws OutputProtocolException {
            writeString(Boolean.toString(value));
        }

        @Override
        public final void writeByte(final byte value)
                throws OutputProtocolException {
            writeString(Byte.toString(value));
        }

        @Override
        public final void writeDouble(final double value)
                throws OutputProtocolException {
            writeString(Double.toString(value));
        }

        @Override
        public final void writeI16(final short value)
                throws OutputProtocolException {
            writeString(Short.toString(value));
        }

        @Override
        public final void writeI32(final int value)
                throws OutputProtocolException {
            writeString(Integer.toString(value));
        }

        @Override
        public final void writeI64(final long value)
                throws OutputProtocolException {
            writeString(Long.toString(value));
        }

        @Override
        public void writeListEnd() throws OutputProtocolException {
        }

        @Override
        public void writeMapEnd() throws OutputProtocolException {
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            throw new UnsupportedOperationException();
        }

        @Override
        public void writeStructEnd() throws OutputProtocolException {
        }

        protected void _writeListBegin(final String childKey)
                throws OutputProtocolException {
            output.put(__joinKeys(myKey, childKey), "");
            _getOutputProtocolStack().push(
                    new ListOutputProtocol(__joinKeys(myKey, childKey)));
        }

        protected void _writeMapBegin(final String childKey)
                throws OutputProtocolException {
            output.put(__joinKeys(myKey, childKey), "");
            _getOutputProtocolStack().push(
                    new MapOutputProtocol(__joinKeys(myKey, childKey)));
        }

        protected void _writeString(final String childKey, final String value) {
            checkNotNull(childKey);
            checkNotNull(value);
            output.put(__joinKeys(myKey, childKey), value);
        }

        protected void _writeStructBegin(final String childKey)
                throws OutputProtocolException {
            output.put(__joinKeys(myKey, childKey), "");
            _getOutputProtocolStack().push(
                    new StructOutputProtocol(__joinKeys(myKey, childKey)));
        }

        private final String myKey;
    }

    private final class ListOutputProtocol extends NestedOutputProtocol {
        public ListOutputProtocol(final String myKey) {
            super(myKey);
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            _writeListBegin(Integer.toString(nextChildKey++));
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            _writeMapBegin(Integer.toString(nextChildKey++));
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            _writeString(Integer.toString(nextChildKey++), value);
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            _writeStructBegin(Integer.toString(nextChildKey++));
        }

        private int nextChildKey;
    }

    private final class MapOutputProtocol extends NestedOutputProtocol {
        public MapOutputProtocol(final String myKey) {
            super(myKey);
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeListBegin(nextChildKey);
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeMapBegin(nextChildKey);
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            if (nextChildKey == null) {
                nextChildKey = value;
            } else {
                _writeString(nextChildKey, value);
                nextChildKey = null;
            }
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeStructBegin(nextChildKey);
        }

        private String nextChildKey = null;
    }

    private final class RootOutputProtocol extends NestedOutputProtocol {
        public RootOutputProtocol() {
            super("");
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            _getOutputProtocolStack().push(new ListOutputProtocol(""));
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            _getOutputProtocolStack().push(new MapOutputProtocol(""));
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            throw new IllegalStateException();
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            _getOutputProtocolStack().push(new StructOutputProtocol(""));
        }
    }

    private final class StructOutputProtocol extends NestedOutputProtocol {
        public StructOutputProtocol(final String myKey) {
            super(myKey);
        }

        @Override
        public void writeFieldBegin(final String name, final Type type,
                final short id) throws OutputProtocolException {
            nextChildKey = name;
        }

        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeListBegin(nextChildKey);
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeMapBegin(nextChildKey);
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeString(nextChildKey, value);
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            checkState(nextChildKey != null);
            _writeStructBegin(nextChildKey);
        }

        private String nextChildKey = null;
    }

    private final static String __joinKeys(final String parentKey,
            final String childKey) {
        checkNotEmpty(childKey);
        if (parentKey.isEmpty()) {
            return childKey;
        } else {
            return parentKey + "." + childKey;
        }
    }

    public StringMapOutputProtocol() {
        _getOutputProtocolStack().push(new RootOutputProtocol());
    }

    public final ImmutableMap<String, String> toStringMap() {
        return ImmutableMap.copyOf(output);
    }

    private final Map<String, String> output = Maps.newHashMap();
}
