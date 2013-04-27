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
import java.io.Writer;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TStruct;

import com.fasterxml.jackson.core.JsonGenerator;

public class LogMessageProtocol extends JsonProtocol {
    private final class ArrayWriterProtocol extends
            JsonProtocol.ArrayWriterProtocol {
        @Override
        public void writeBool(final boolean b) throws TException {
            if (size < SIZE_MAX) {
                super.writeBool(b);
                size++;
            }
        }

        @Override
        public void writeByte(final byte b) throws TException {
            if (size < SIZE_MAX) {
                super.writeByte(b);
                size++;
            }
        }

        @Override
        public void writeDouble(final double dub) throws TException {
            if (size < SIZE_MAX) {
                super.writeDouble(dub);
                size++;
            }
        }

        @Override
        public void writeFieldBegin(final TField field) throws TException {
            if (size < SIZE_MAX) {
                super.writeFieldBegin(field);
            }
        }

        @Override
        public void writeI16(final short i16) throws TException {
            if (size < SIZE_MAX) {
                super.writeI16(i16);
                size++;
            }
        }

        @Override
        public void writeI32(final int i32) throws TException {
            if (size < SIZE_MAX) {
                super.writeI32(i32);
                size++;
            }
        }

        @Override
        public void writeI64(final long i64) throws TException {
            if (size < SIZE_MAX) {
                super.writeI64(i64);
                size++;
            }
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            if (size < SIZE_MAX) {
                super.writeListBegin(list);
            } else {
                _getProtocolStack().push(new NopWriterProtocol());
            }
        }

        @Override
        public void writeListEnd() throws TException {
            if (size < SIZE_MAX) {
                super.writeListEnd();
                size++;
            }
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            if (size < SIZE_MAX) {
                super.writeMapBegin(map);
            } else {
                _getProtocolStack().push(new NopWriterProtocol());
            }
        }

        @Override
        public void writeMapEnd() throws TException {
            if (size < SIZE_MAX) {
                super.writeMapEnd();
                size++;
            }
        }

        @Override
        public void writeString(final String str) throws TException {
            if (size < SIZE_MAX) {
                super.writeString(__cropString(str));
                size++;
            }
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            if (size < SIZE_MAX) {
                super.writeStructBegin(struct);
            } else {
                _getProtocolStack().push(new NopWriterProtocol());
            }
        }

        @Override
        public void writeStructEnd() throws TException {
            if (size < SIZE_MAX) {
                super.writeStructEnd();
                size++;
            }
        }

        public final static int SIZE_MAX = 4;

        private int size = 0;
    }

    private final class MapObjectWriterProtocol extends
            JsonProtocol.MapObjectWriterProtocol {
        @Override
        public void writeBool(final boolean b) throws TException {
            if (size < SIZE_MAX) {
                super.writeBool(b);
                size++;
            }
        }

        @Override
        public void writeByte(final byte b) throws TException {
            if (size < SIZE_MAX) {
                super.writeByte(b);
                size++;
            }
        }

        @Override
        public void writeDouble(final double dub) throws TException {
            if (size < SIZE_MAX) {
                super.writeDouble(dub);
                size++;
            }
        }

        @Override
        public void writeFieldBegin(final TField field) throws TException {
            if (size < SIZE_MAX) {
                super.writeFieldBegin(field);
            }
        }

        @Override
        public void writeI16(final short i16) throws TException {
            if (size < SIZE_MAX) {
                super.writeI16(i16);
                size++;
            }
        }

        @Override
        public void writeI32(final int i32) throws TException {
            if (size < SIZE_MAX) {
                super.writeI32(i32);
                size++;
            }
        }

        @Override
        public void writeI64(final long i64) throws TException {
            if (size < SIZE_MAX) {
                super.writeI64(i64);
                size++;
            }
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            if (size < SIZE_MAX) {
                super.writeListBegin(list);
            } else {
                _getProtocolStack().push(new NopWriterProtocol());
            }
        }

        @Override
        public void writeListEnd() throws TException {
            if (size < SIZE_MAX) {
                super.writeListEnd();
                size++;
            }
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            if (size < SIZE_MAX) {
                super.writeMapBegin(map);
            } else {
                _getProtocolStack().push(new NopWriterProtocol());
            }
        }

        @Override
        public void writeMapEnd() throws TException {
            if (size < SIZE_MAX) {
                super.writeMapEnd();
                size++;
            }
        }

        @Override
        public void writeString(final String str) throws TException {
            if (size < SIZE_MAX) {
                super.writeString(__cropString(str));
                size++;
            }
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            if (size < SIZE_MAX) {
                super.writeStructBegin(struct);
            } else {
                _getProtocolStack().push(new NopWriterProtocol());
            }
        }

        @Override
        public void writeStructEnd() throws TException {
            if (size < SIZE_MAX) {
                super.writeStructEnd();
                size++;
            }
        }

        public final static int SIZE_MAX = 8;

        private int size = 0;
    }

    private final class NopWriterProtocol extends Protocol {
        @Override
        public void writeBool(final boolean b) throws TException {
        }

        @Override
        public void writeByte(final byte b) throws TException {
        }

        @Override
        public void writeDouble(final double dub) throws TException {
        }

        @Override
        public void writeFieldBegin(final TField field) throws TException {
        }

        @Override
        public void writeFieldEnd() throws TException {
        }

        @Override
        public void writeFieldStop() throws TException {
        }

        @Override
        public void writeI16(final short i16) throws TException {
        }

        @Override
        public void writeI32(final int i32) throws TException {
        }

        @Override
        public void writeI64(final long i64) throws TException {
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            _getProtocolStack().push(new NopWriterProtocol());
        }

        @Override
        public void writeListEnd() throws TException {
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            _getProtocolStack().push(new NopWriterProtocol());
        }

        @Override
        public void writeMapEnd() throws TException {
        }

        @Override
        public void writeString(final String str) throws TException {
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            _getProtocolStack().push(new NopWriterProtocol());
        }

        @Override
        public void writeStructEnd() throws TException {
        }
    }

    private final class StructObjectWriterProtocol extends
            JsonProtocol.StructObjectWriterProtocol {
        @Override
        public void writeString(final String str) throws TException {
            super.writeString(__cropString(str));
        }
    }

    private final static String __cropString(final String str) {
        if (str.length() <= STRING_LENGTH_MAX) {
            return str;
        } else {
            return str.substring(0, STRING_LENGTH_MAX - 6) + "..."
                    + str.substring(str.length() - 3);
        }
    }

    public LogMessageProtocol(final JsonGenerator generator) {
        super(generator);
    }

    public LogMessageProtocol(final OutputStream outputStream)
            throws IOException {
        super(outputStream);
    }

    public LogMessageProtocol(final Writer writer) throws IOException {
        super(writer);
    }

    @Override
    protected Protocol _createArrayWriterProtocol() {
        return new ArrayWriterProtocol();
    }

    @Override
    protected Protocol _createMapObjectWriterProtocol() {
        return new MapObjectWriterProtocol();
    }

    @Override
    protected Protocol _createStructObjectWriterProtocol() {
        return new StructObjectWriterProtocol();
    }

    public final static int STRING_LENGTH_MAX = 16;
}
