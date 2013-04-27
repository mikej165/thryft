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
import java.nio.ByteBuffer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LoggingProtocol extends Protocol {
    public LoggingProtocol(final Protocol wrappedProtocol) {
        logger = LoggerFactory.getLogger(wrappedProtocol.getClass());
        this.wrappedProtocol = wrappedProtocol;
    }

    @Override
    public boolean readBool() throws IOException {
        final String message = "readBool() -> ";
        try {
            final boolean bool = wrappedProtocol.readBool();
            logger.info(message + Boolean.toString(bool));
            return bool;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public byte readByte() throws IOException {
        final String message = "readByte() -> ";
        try {
            final byte byte_ = wrappedProtocol.readByte();
            logger.info(message + Byte.toString(byte_));
            return byte_;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public double readDouble() throws IOException {
        final String message = "readDouble() -> ";
        try {
            final double double_ = wrappedProtocol.readDouble();
            logger.info(message + Double.toString(double_));
            return double_;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public TField readFieldBegin() throws IOException {
        final String message = "readFieldBegin() -> ";
        try {
            final TField field = wrappedProtocol.readFieldBegin();
            logger.info(message + field.toString());
            return field;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readFieldEnd() throws IOException {
        final String message = "readFieldEnd()";
        try {
            wrappedProtocol.readFieldEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public short readI16() throws IOException {
        final String message = "readI16() -> ";
        try {
            final short i16 = wrappedProtocol.readI16();
            logger.info(message + Short.toString(i16));
            return i16;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public int readI32() throws IOException {
        final String message = "readI32() -> ";
        try {
            final int i32 = wrappedProtocol.readI32();
            logger.info(message + Integer.toString(i32));
            return i32;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public long readI64() throws IOException {
        final String message = "readI64() -> ";
        try {
            final long i64 = wrappedProtocol.readI64();
            logger.info(message + Long.toString(i64));
            return i64;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public TList readListBegin() throws IOException {
        final String message = "readListBegin() ->";
        try {
            final TList list = wrappedProtocol.readListBegin();
            logger.info(message + __toString(list));
            return list;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readListEnd() throws IOException {
        final String message = "readListEnd()";
        try {
            wrappedProtocol.readListEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public TMap readMapBegin() throws IOException {
        final String message = "readMapBegin() -> ";
        try {
            final TMap map = wrappedProtocol.readMapBegin();
            logger.info(message + __toString(map));
            return map;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readMapEnd() throws IOException {
        final String message = "readMapEnd()";
        try {
            wrappedProtocol.readMapEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public TSet readSetBegin() throws IOException {
        final String message = "readSetBegin() -> ";
        try {
            final TSet set = wrappedProtocol.readSetBegin();
            logger.info(message + "(" + __toString(set) + ")");
            return set;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readSetEnd() throws IOException {
        final String message = "readSetEnd()";
        try {
            wrappedProtocol.readSetEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public String readString() throws IOException {
        final String message = "readString() -> ";
        try {
            final String string = wrappedProtocol.readString();
            logger.info(message + string);
            return string;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public TStruct readStructBegin() throws IOException {
        final String message = "readStructBegin() -> ";
        try {
            final TStruct struct = wrappedProtocol.readStructBegin();
            logger.info(message + "TStruct(" + __toString(struct) + ")");
            return struct;
        } catch (final IOException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readStructEnd() throws IOException {
        final String message = "readStructEnd()";
        try {
            wrappedProtocol.readStructEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeBinary(final ByteBuffer buf) throws IOException {
        final String message = "writeBinary(" + __toString(buf) + " bytes)";
        try {
            wrappedProtocol.writeBinary(buf);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeBool(final boolean b) throws IOException {
        final String message = "writeBool(" + b + ")";
        try {
            wrappedProtocol.writeBool(b);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeByte(final byte b) throws IOException {
        final String message = "writeByte(" + b + ")";
        try {
            wrappedProtocol.writeByte(b);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeDouble(final double dub) throws IOException {
        final String message = "writeDouble(" + dub + ")";
        try {
            wrappedProtocol.writeDouble(dub);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeFieldBegin(final TField field) throws IOException {
        final String message = "writeFieldBegin(" + field.toString() + ")";
        try {
            wrappedProtocol.writeFieldBegin(field);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeFieldEnd() throws IOException {
        final String message = "writeFieldEnd()";
        try {
            wrappedProtocol.writeFieldEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeFieldStop() throws IOException {
        final String message = "writeFieldStop()";
        try {
            wrappedProtocol.writeFieldStop();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeI16(final short i16) throws IOException {
        final String message = "writeI16(" + i16 + ")";
        try {
            wrappedProtocol.writeI16(i16);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeI32(final int i32) throws IOException {
        final String message = "writeI32(" + i32 + ")";
        try {
            wrappedProtocol.writeI32(i32);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeI64(final long i64) throws IOException {
        final String message = "writeI64(" + i64 + ")";
        try {
            wrappedProtocol.writeI64(i64);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeListBegin(final TList list) throws IOException {
        final String message = "writeListBegin(" + __toString(list) + ")";
        try {
            wrappedProtocol.writeListBegin(list);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeListEnd() throws IOException {
        final String message = "writeListEnd()";
        try {
            wrappedProtocol.writeListEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeMapBegin(final TMap map) throws IOException {
        final String message = "writeMapBegin(" + __toString(map) + ")";
        try {
            wrappedProtocol.writeMapBegin(map);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeMapEnd() throws IOException {
        final String message = "writeMapEnd()";
        try {
            wrappedProtocol.writeMapEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeSetBegin(final TSet set) throws IOException {
        final String message = "writeSetBegin(" + __toString(set) + ")";
        try {
            wrappedProtocol.writeSetBegin(set);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeSetEnd() throws IOException {
        final String message = "writeSetEnd()";
        try {
            wrappedProtocol.writeSetEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeString(final String str) throws IOException {
        final String message = "writeString(" + str + ")";
        try {
            wrappedProtocol.writeString(str);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeStructBegin(final TStruct struct) throws IOException {
        final String message = "writeStructBegin(" + __toString(struct) + ")";
        try {
            wrappedProtocol.writeStructBegin(struct);
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeStructEnd() throws IOException {
        final String message = "writeStructEnd()";
        try {
            wrappedProtocol.writeStructEnd();
            logger.info(message);
        } catch (final IOException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    private final String __toString(final ByteBuffer byteBuffer) {
        return "ByteBuffer(capacity=" + Integer.toString(byteBuffer.capacity())
                + ")";
    }

    private final String __toString(final Exception e) {
        return "exception: " + e.getMessage();
    }

    private final String __toString(final TList list) {
        return "TList(" + Byte.toString(list.elemType) + ", "
                + Integer.toString(list.size) + ")";
    }

    private final String __toString(final TMap map) {
        return "TMap(" + Byte.toString(map.keyType) + ", "
                + Byte.toString(map.valueType) + ", "
                + Integer.toString(map.size) + ")";
    }

    private final String __toString(final TSet set) {
        return "TSet(" + Byte.toString(set.elemType) + ", "
                + Integer.toString(set.size) + ")";
    }

    private final String __toString(final TStruct struct) {
        return "TStruct(" + struct.name + ")";
    }

    private final Logger logger;
    private final Protocol wrappedProtocol;
}
