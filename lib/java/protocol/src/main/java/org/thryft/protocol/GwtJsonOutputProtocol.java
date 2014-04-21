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

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.json.client.JSONBoolean;
import com.google.gwt.json.client.JSONNull;
import com.google.gwt.json.client.JSONNumber;
import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONString;
import com.google.gwt.json.client.JSONValue;

public class GwtJsonOutputProtocol extends StackedOutputProtocol {
    protected abstract class AbstractOutputProtocol extends
            org.thryft.protocol.AbstractOutputProtocol {
        @Override
        public void writeBool(final boolean b) throws OutputProtocolException {
            _write(JSONBoolean.getInstance(b));
        }

        @Override
        public void writeByte(final byte b) throws OutputProtocolException {
            _write(new JSONNumber(b));
        }

        @Override
        public void writeDouble(final double dub)
                throws OutputProtocolException {
            _write(new JSONNumber(dub));
        }

        @Override
        public void writeI16(final short i16) throws OutputProtocolException {
            _write(new JSONNumber(i16));
        }

        @Override
        public void writeI32(final int i32) throws OutputProtocolException {
            _write(new JSONNumber(i32));
        }

        @Override
        public void writeI64(final long i64) throws OutputProtocolException {
            _write(new JSONNumber(i64));
        }

        @Override
        public void writeListBegin(final ListBegin list)
                throws OutputProtocolException {
            final JSONArray array = new JSONArray();
            _write(array);
            _getProtocolStack().push(_createArrayOutputProtocol(array));
        }

        @Override
        public void writeListEnd() throws OutputProtocolException {
        }

        @Override
        public void writeMapBegin(final MapBegin map)
                throws OutputProtocolException {
            final JSONObject object = new JSONObject();
            _write(object);
            _getProtocolStack().push(_createMapObjectOutputProtocol(object));
        }

        @Override
        public void writeMapEnd() throws OutputProtocolException {
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            _write(JSONNull.getInstance());
        }

        @Override
        public void writeString(final String str)
                throws OutputProtocolException {
            _write(new JSONString(str));
        }

        @Override
        public void writeStructBegin(final StructBegin struct)
                throws OutputProtocolException {
            final JSONObject object = new JSONObject();
            _write(object);
            _getProtocolStack().push(_createStructObjectOutputProtocol(object));
        }

        @Override
        public void writeStructEnd() throws OutputProtocolException {
        }

        protected abstract void _write(final JSONValue value);
    }

    protected class ArrayOutputProtocol extends AbstractOutputProtocol {
        public ArrayOutputProtocol(final JSONArray array) {
            this.array = checkNotNull(array);
        }

        @Override
        protected void _write(final JSONValue value) {
            array.set(array.size(), value);
        }

        private final JSONArray array;
    }

    protected class MapObjectOutputProtocol extends AbstractOutputProtocol {
        public MapObjectOutputProtocol(final JSONObject object) {
            this.object = checkNotNull(object);
        }

        @Override
        public void writeBool(final boolean b) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Boolean.toString(b));
            } else {
                super.writeBool(b);
            }
        }

        @Override
        public void writeByte(final byte b) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Byte.toString(b));
            } else {
                super.writeByte(b);
            }
        }

        @Override
        public void writeDouble(final double dub)
                throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Double.toString(dub));
            } else {
                super.writeDouble(dub);
            }
        }

        @Override
        public void writeI16(final short i16) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Short.toString(i16));
            } else {
                super.writeI16(i16);
            }
        }

        @Override
        public void writeI32(final int i32) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Integer.toString(i32));
            } else {
                super.writeI32(i32);
            }
        }

        @Override
        public void writeI64(final long i64) throws OutputProtocolException {
            if (nextKey == null) {
                writeString(Long.toString(i64));
            } else {
                super.writeI64(i64);
            }
        }

        @Override
        public void writeListBegin(final ListBegin list)
                throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeListBegin(list);
            }
        }

        @Override
        public void writeMapBegin(final MapBegin map)
                throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeMapBegin(map);
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
        public void writeString(final String str)
                throws OutputProtocolException {
            if (nextKey == null) {
                nextKey = str;
            } else {
                super.writeString(str);
            }
        }

        @Override
        public void writeStructBegin(final StructBegin struct)
                throws OutputProtocolException {
            if (nextKey == null) {
                throw new UnsupportedOperationException();
            } else {
                super.writeStructBegin(struct);
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

    protected class RootOutputProtocol extends AbstractOutputProtocol {
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

        }
    }

    protected class StructObjectOutputProtocol extends AbstractOutputProtocol {
        public StructObjectOutputProtocol(final JSONObject object) {
            this.object = checkNotNull(object);
        }

        @Override
        public void writeFieldBegin(final FieldBegin field)
                throws OutputProtocolException {
            nextFieldName = field.name;
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
        _getProtocolStack().push(_createRootOutputProtocol());
    }

    @Override
    public void flush() throws OutputProtocolException {
    }

    protected OutputProtocol _createArrayOutputProtocol(final JSONArray array) {
        return new ArrayOutputProtocol(array);
    }

    protected OutputProtocol _createMapObjectOutputProtocol(
            final JSONObject object) {
        return new MapObjectOutputProtocol(object);
    }

    protected OutputProtocol _createRootOutputProtocol() {
        return new RootOutputProtocol();
    }

    protected OutputProtocol _createStructObjectOutputProtocol(
            final JSONObject object) {
        return new StructObjectOutputProtocol(object);
    }
}
