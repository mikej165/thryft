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

public class JsonOutputProtocol extends StackedOutputProtocol {
    protected abstract class AbstractOutputProtocol extends
            org.thryft.protocol.AbstractOutputProtocol {
        @Override
        public void writeBool(final boolean b) throws OutputProtocolException {
            try {
                generator.writeBoolean(b);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeByte(final byte b) throws OutputProtocolException {
            try {
                generator.writeNumber(b);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeDouble(final double dub)
                throws OutputProtocolException {
            try {
                generator.writeNumber(dub);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeI16(final short i16) throws OutputProtocolException {
            try {
                generator.writeNumber(i16);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeI32(final int i32) throws OutputProtocolException {
            try {
                generator.writeNumber(i32);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeI64(final long i64) throws OutputProtocolException {
            try {
                generator.writeNumber(i64);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeListBegin(final ListBegin list)
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
        public void writeMapBegin(final MapBegin map)
                throws OutputProtocolException {
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
        public void writeString(final String str)
                throws OutputProtocolException {
            try {
                generator.writeString(str);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeStructBegin(final StructBegin struct)
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
        public void writeBool(final boolean b) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Boolean.toString(b));
            } else {
                nextWriteIsKey = true;
                super.writeBool(b);
            }
        }

        @Override
        public void writeByte(final byte b) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Byte.toString(b));
            } else {
                nextWriteIsKey = true;
                super.writeByte(b);
            }
        }

        @Override
        public void writeDouble(final double dub)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Double.toString(dub));
            } else {
                nextWriteIsKey = true;
                super.writeDouble(dub);
            }
        }

        @Override
        public void writeI16(final short i16) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Short.toString(i16));
            } else {
                nextWriteIsKey = true;
                super.writeI16(i16);
            }
        }

        @Override
        public void writeI32(final int i32) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Integer.toString(i32));
            } else {
                nextWriteIsKey = true;
                super.writeI32(i32);
            }
        }

        @Override
        public void writeI64(final long i64) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Long.toString(i64));
            } else {
                nextWriteIsKey = true;
                super.writeI64(i64);
            }
        }

        @Override
        public void writeListBegin(final ListBegin list)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeListBegin(list);
            }
        }

        @Override
        public void writeMapBegin(final MapBegin map)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeMapBegin(map);
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
        public void writeString(final String str)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                nextWriteIsKey = false;
                try {
                    generator.writeFieldName(str);
                } catch (final IOException e) {
                    throw new OutputProtocolException(e);
                }
            } else {
                nextWriteIsKey = true;
                super.writeString(str);
            }
        }

        @Override
        public void writeStructBegin(final StructBegin struct)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeStructBegin(struct);
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
        public void writeFieldBegin(final FieldBegin field)
                throws OutputProtocolException {
            try {
                generator.writeFieldName(field.name);
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
