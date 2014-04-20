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

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LoggingInputProtocol extends AbstractInputProtocol {
    public LoggingInputProtocol(final InputProtocol wrappedProtocol) {
        logger = LoggerFactory.getLogger(wrappedProtocol.getClass());
        this.wrappedProtocol = wrappedProtocol;
    }

    @Override
    public byte[] readBinary() throws InputProtocolException {
        final String message = "readBinary() -> ";
        try {
            final byte[] binary = wrappedProtocol.readBinary();
            logger.info(message + __toString(binary));
            return binary;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public boolean readBool() throws InputProtocolException {
        final String message = "readBool() -> ";
        try {
            final boolean bool = wrappedProtocol.readBool();
            logger.info(message + Boolean.toString(bool));
            return bool;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public byte readByte() throws InputProtocolException {
        final String message = "readByte() -> ";
        try {
            final byte byte_ = wrappedProtocol.readByte();
            logger.info(message + Byte.toString(byte_));
            return byte_;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public double readDouble() throws InputProtocolException {
        final String message = "readDouble() -> ";
        try {
            final double double_ = wrappedProtocol.readDouble();
            logger.info(message + Double.toString(double_));
            return double_;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public FieldBegin readFieldBegin() throws InputProtocolException {
        final String message = "readFieldBegin() -> ";
        try {
            final FieldBegin field = wrappedProtocol.readFieldBegin();
            logger.info(message + field.toString());
            return field;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readFieldEnd() throws InputProtocolException {
        final String message = "readFieldEnd()";
        try {
            wrappedProtocol.readFieldEnd();
            logger.info(message);
        } catch (final InputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public short readI16() throws InputProtocolException {
        final String message = "readI16() -> ";
        try {
            final short i16 = wrappedProtocol.readI16();
            logger.info(message + Short.toString(i16));
            return i16;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public int readI32() throws InputProtocolException {
        final String message = "readI32() -> ";
        try {
            final int i32 = wrappedProtocol.readI32();
            logger.info(message + Integer.toString(i32));
            return i32;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public long readI64() throws InputProtocolException {
        final String message = "readI64() -> ";
        try {
            final long i64 = wrappedProtocol.readI64();
            logger.info(message + Long.toString(i64));
            return i64;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public ListBegin readListBegin() throws InputProtocolException {
        final String message = "readListBegin() ->";
        try {
            final ListBegin list = wrappedProtocol.readListBegin();
            logger.info(message + __toString(list));
            return list;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readListEnd() throws InputProtocolException {
        final String message = "readListEnd()";
        try {
            wrappedProtocol.readListEnd();
            logger.info(message);
        } catch (final InputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public MapBegin readMapBegin() throws InputProtocolException {
        final String message = "readMapBegin() -> ";
        try {
            final MapBegin map = wrappedProtocol.readMapBegin();
            logger.info(message + __toString(map));
            return map;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readMapEnd() throws InputProtocolException {
        final String message = "readMapEnd()";
        try {
            wrappedProtocol.readMapEnd();
            logger.info(message);
        } catch (final InputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public SetBegin readSetBegin() throws InputProtocolException {
        final String message = "readSetBegin() -> ";
        try {
            final SetBegin set = wrappedProtocol.readSetBegin();
            logger.info(message + "(" + __toString(set) + ")");
            return set;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readSetEnd() throws InputProtocolException {
        final String message = "readSetEnd()";
        try {
            wrappedProtocol.readSetEnd();
            logger.info(message);
        } catch (final InputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public String readString() throws InputProtocolException {
        final String message = "readString() -> ";
        try {
            final String string = wrappedProtocol.readString();
            logger.info(message + string);
            return string;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public StructBegin readStructBegin() throws InputProtocolException {
        final String message = "readStructBegin() -> ";
        try {
            final StructBegin struct = wrappedProtocol.readStructBegin();
            logger.info(message + "TStruct(" + __toString(struct) + ")");
            return struct;
        } catch (final InputProtocolException e) {
            logger.info(message + __toString(e));
            throw e;
        }
    }

    @Override
    public void readStructEnd() throws InputProtocolException {
        final String message = "readStructEnd()";
        try {
            wrappedProtocol.readStructEnd();
            logger.info(message);
        } catch (final InputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    private final String __toString(final byte[] bytes) {
        return "bytes[length=" + Integer.toString(bytes.length) + "]";
    }

    private final String __toString(final Exception e) {
        return "exception: " + e.getMessage();
    }

    private final String __toString(final ListBegin list) {
        return "TList(" + Byte.toString(list.elemType) + ", "
                + Integer.toString(list.size) + ")";
    }

    private final String __toString(final MapBegin map) {
        return "TMap(" + Byte.toString(map.keyType) + ", "
                + Byte.toString(map.valueType) + ", "
                + Integer.toString(map.size) + ")";
    }

    private final String __toString(final SetBegin set) {
        return "TSet(" + Byte.toString(set.elemType) + ", "
                + Integer.toString(set.size) + ")";
    }

    private final String __toString(final StructBegin struct) {
        return "TStruct(" + struct.name + ")";
    }

    private final Logger logger;
    private final InputProtocol wrappedProtocol;
}
