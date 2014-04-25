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

import org.thryft.protocol.GwtJsonOutputProtocol.NestedOutputProtocol;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.json.client.JSONBoolean;
import com.google.gwt.json.client.JSONNull;
import com.google.gwt.json.client.JSONNumber;
import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONString;
import com.google.gwt.json.client.JSONValue;
import com.googlecode.gwt.crypto.bouncycastle.util.encoders.Base64;

public class GwtJsonOutputProtocol extends
        JsonOutputProtocol<NestedOutputProtocol> {
    protected abstract class NestedOutputProtocol extends
            AbstractOutputProtocol {
        public abstract JSONValue getJsonValue();

        @Override
        public void writeBinary(final byte[] value)
                throws OutputProtocolException {
            writeString(new String(Base64.encode(value)));
        }

        @Override
        public void writeBool(final boolean value)
                throws OutputProtocolException {
            _write(JSONBoolean.getInstance(value));
        }

        @Override
        public void writeByte(final byte value) throws OutputProtocolException {
            _write(new JSONNumber(value));
        }

        @Override
        public void writeDouble(final double value)
                throws OutputProtocolException {
            _write(new JSONNumber(value));
        }

        @Override
        public void writeI16(final short value) throws OutputProtocolException {
            _write(new JSONNumber(value));
        }

        @Override
        public void writeI32(final int value) throws OutputProtocolException {
            _write(new JSONNumber(value));
        }

        @Override
        public void writeI64(final long value) throws OutputProtocolException {
            _write(new JSONNumber(value));
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            final JSONArray array = new JSONArray();
            _write(array);
            _getOutputProtocolStack().push(__createArrayOutputProtocol(array));
        }

        @Override
        public void writeListEnd() throws OutputProtocolException {
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            final JSONObject object = new JSONObject();
            _write(object);
            _getOutputProtocolStack().push(
                    __createMapObjectOutputProtocol(object));
        }

        @Override
        public void writeMapEnd() throws OutputProtocolException {
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            _write(JSONNull.getInstance());
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            _write(new JSONString(value));
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            final JSONObject object = new JSONObject();
            _write(object);
            _getOutputProtocolStack().push(
                    __createStructObjectOutputProtocol(object));
        }

        @Override
        public void writeStructEnd() throws OutputProtocolException {
        }

        protected abstract void _write(final JSONValue value);
    }

    private class ArrayOutputProtocol extends NestedOutputProtocol {
        public ArrayOutputProtocol(final JSONArray array) {
            this.array = checkNotNull(array);
        }

        @Override
        public JSONValue getJsonValue() {
            return array;
        }

        @Override
        protected void _write(final JSONValue value) {
            array.set(array.size(), value);
        }

        private final JSONArray array;
    }

    private class MapObjectOutputProtocol extends NestedOutputProtocol {
        public MapObjectOutputProtocol(final JSONObject object) {
            this.object = checkNotNull(object);
        }

        @Override
        public JSONValue getJsonValue() {
            return object;
        }

        @Override
        public void writeBool(final boolean value)
                throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Boolean.toString(value));
            } else {
                super.writeBool(value);
            }
        }

        @Override
        public void writeByte(final byte value) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Byte.toString(value));
            } else {
                super.writeByte(value);
            }
        }

        @Override
        public void writeDouble(final double value)
                throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Double.toString(value));
            } else {
                super.writeDouble(value);
            }
        }

        @Override
        public void writeI16(final short value) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Short.toString(value));
            } else {
                super.writeI16(value);
            }
        }

        @Override
        public void writeI32(final int value) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Integer.toString(value));
            } else {
                super.writeI32(value);
            }
        }

        @Override
        public void writeI64(final long value) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Long.toString(value));
            } else {
                super.writeI64(value);
            }
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeListBegin(elementType, size);
            }
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeMapBegin(keyType, valueType, size);
            }
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeNull();
            }
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            if (nextKey == null) {
                nextKey = value;
            } else {
                super.writeString(value);
            }
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeStructBegin(name);
            }
        }

        @Override
        protected void _write(final JSONValue value) {
            checkState(nextKey != null);
            object.put(nextKey, value);
        }

        private final JSONObject object;

        private String nextKey = null;
    }

    private class RootOutputProtocol extends NestedOutputProtocol {
        @Override
        public JSONValue getJsonValue() {
            return value != null ? value : JSONNull.getInstance();
        }

        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }

        @Override
        protected void _write(final JSONValue value) {
            checkState(value instanceof JSONArray
                    || value instanceof JSONObject);
            this.value = value;
        }

        private JSONValue value = null;
    }

    private class StructObjectOutputProtocol extends NestedOutputProtocol {
        public StructObjectOutputProtocol(final JSONObject object) {
            this.object = checkNotNull(object);
        }

        @Override
        public JSONValue getJsonValue() {
            return object;
        }

        @Override
        public void writeFieldBegin(final String name, final Type type,
                final short id) throws OutputProtocolException {
            nextFieldName = name;
        }

        @Override
        public void writeFieldEnd() throws OutputProtocolException {
            nextFieldName = null;
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }

        @Override
        protected void _write(final JSONValue value) {
            checkState(nextFieldName != null);
            object.put(nextFieldName, value);
        }

        private String nextFieldName = null;
        private final JSONObject object;
    }

    public GwtJsonOutputProtocol() {
        _getOutputProtocolStack().push(__createRootOutputProtocol());
    }

    @Override
    public void flush() throws OutputProtocolException {
    }

    public JSONValue toJsonValue() {
        if (!_getOutputProtocolStack().isEmpty()) {
            return _getOutputProtocolStack().get(0).getJsonValue();
        } else {
            return JSONNull.getInstance();
        }
    }

    private ArrayOutputProtocol __createArrayOutputProtocol(
            final JSONArray array) {
        return new ArrayOutputProtocol(array);
    }

    private MapObjectOutputProtocol __createMapObjectOutputProtocol(
            final JSONObject object) {
        return new MapObjectOutputProtocol(object);
    }

    private RootOutputProtocol __createRootOutputProtocol() {
        return new RootOutputProtocol();
    }

    private StructObjectOutputProtocol __createStructObjectOutputProtocol(
            final JSONObject object) {
        return new StructObjectOutputProtocol(object);
    }
}
