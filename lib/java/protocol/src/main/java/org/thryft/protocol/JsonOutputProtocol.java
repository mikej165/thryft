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

import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.google.common.annotations.GwtIncompatible;

@GwtIncompatible("")
public class JsonOutputProtocol extends StackedOutputProtocol {
    protected abstract class AbstractOutputProtocol extends
            org.thryft.protocol.AbstractOutputProtocol {
        @Override
        public void writeBool(final boolean value)
                throws OutputProtocolException {
            try {
                generator.writeBoolean(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeByte(final byte value) throws OutputProtocolException {
            try {
                generator.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeDouble(final double value)
                throws OutputProtocolException {
            try {
                generator.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeI16(final short value) throws OutputProtocolException {
            try {
                generator.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeI32(final int value) throws OutputProtocolException {
            try {
                generator.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeI64(final long value) throws OutputProtocolException {
            try {
                generator.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            try {
                generator.writeStartArray();
                _getProtocolStack().push(_createArrayOutputProtocol());
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeListEnd() throws OutputProtocolException {
            try {
                generator.writeEndArray();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            try {
                generator.writeStartObject();
                _getProtocolStack().push(_createMapObjectOutputProtocol());
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeMapEnd() throws OutputProtocolException {
            try {
                generator.writeEndObject();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            try {
                generator.writeNull();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            try {
                generator.writeString(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            try {
                generator.writeStartObject();
                _getProtocolStack().push(_createStructObjectOutputProtocol());
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeStructEnd() throws OutputProtocolException {
            try {
                generator.writeEndObject();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }
    }

    protected class ArrayOutputProtocol extends AbstractOutputProtocol {
    }

    protected class MapObjectOutputProtocol extends AbstractOutputProtocol {
        @Override
        public void writeBool(final boolean value)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Boolean.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeBool(value);
            }
        }

        @Override
        public void writeByte(final byte value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Byte.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeByte(value);
            }
        }

        @Override
        public void writeDouble(final double value)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Double.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeDouble(value);
            }
        }

        @Override
        public void writeI16(final short value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Short.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeI16(value);
            }
        }

        @Override
        public void writeI32(final int value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Integer.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeI32(value);
            }
        }

        @Override
        public void writeI64(final long value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Long.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeI64(value);
            }
        }

        @Override
        public void writeListBegin(final Type elementType, final int size)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeListBegin(elementType, size);
            }
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType,
                final int size) throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeMapBegin(keyType, valueType, size);
            }
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeNull();
            }
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                nextWriteIsKey = false;
                try {
                    generator.writeFieldName(value);
                } catch (final IOException e) {
                    throw new OutputProtocolException(e);
                }
            } else {
                nextWriteIsKey = true;
                super.writeString(value);
            }
        }

        @Override
        public void writeStructBegin(final String name)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeStructBegin(name);
            }
        }

        private boolean nextWriteIsKey = true;
    }

    protected class RootOutputProtocol extends AbstractOutputProtocol {
        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }
    }

    protected class StructObjectOutputProtocol extends AbstractOutputProtocol {
        @Override
        public void writeFieldBegin(final String name, final Type type,
                final short id) throws OutputProtocolException {
            try {
                generator.writeFieldName(name);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }
    }

    public JsonOutputProtocol(final JsonGenerator generator) {
        this.generator = generator;
        _getProtocolStack().push(_createRootOutputProtocol());
    }

    public JsonOutputProtocol(final OutputStream outputStream)
            throws IOException {
        this(new OutputStreamWriter(outputStream));
    }

    public JsonOutputProtocol(final Writer writer) throws IOException {
        this(new JsonFactory().createJsonGenerator(writer));
    }

    @Override
    public void flush() throws OutputProtocolException {
        try {
            generator.flush();
        } catch (final IOException e) {
            throw new OutputProtocolException(e);
        }
    }

    protected OutputProtocol _createArrayOutputProtocol() {
        return new ArrayOutputProtocol();
    }

    protected OutputProtocol _createMapObjectOutputProtocol() {
        return new MapObjectOutputProtocol();
    }

    protected OutputProtocol _createRootOutputProtocol() {
        return new RootOutputProtocol();
    }

    protected OutputProtocol _createStructObjectOutputProtocol() {
        return new StructObjectOutputProtocol();
    }

    private final JsonGenerator generator;
}
