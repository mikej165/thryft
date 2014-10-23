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

import java.math.BigDecimal;
import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.common.annotations.GwtIncompatible;
import com.google.common.base.MoreObjects;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

@GwtIncompatible("")
public class LoggingInputProtocol implements InputProtocol {
    public LoggingInputProtocol(final InputProtocol wrappedProtocol) {
        logger = LoggerFactory.getLogger(wrappedProtocol.getClass());
        wrappedInputProtocol = wrappedProtocol;
    }

    @Override
    public byte[] readBinary() throws InputProtocolException {
        try {
            final byte[] value = wrappedInputProtocol.readBinary();
            logger.info(READ_BINARY_MESSAGE, value.length);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_BINARY_MESSAGE, 0, e);
            throw e;
        }
    }

    @Override
    public boolean readBool() throws InputProtocolException {
        try {
            final boolean value = wrappedInputProtocol.readBool();
            logger.info(READ_BOOL_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_BOOL_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public byte readByte() throws InputProtocolException {
        try {
            final byte value = wrappedInputProtocol.readByte();
            logger.info(READ_BYTE_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_BYTE_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public Date readDateTime() throws InputProtocolException {
        try {
            final Date value = wrappedInputProtocol.readDateTime();
            logger.info(READ_DATE_TIME_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_DATE_TIME_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public BigDecimal readDecimal() throws InputProtocolException {
        try {
            final BigDecimal value = wrappedInputProtocol.readDecimal();
            logger.info(READ_DECIMAL_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_DECIMAL_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public double readDouble() throws InputProtocolException {
        try {
            final double value = wrappedInputProtocol.readDouble();
            logger.info(READ_DOUBLE_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_DOUBLE_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws InputProtocolException {
        try {
            final E value = wrappedInputProtocol.readEnum(enumClass);
            logger.info(READ_ENUM_MESSAGE, enumClass, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_ENUM_MESSAGE, enumClass, "", e);
            throw e;
        }
    }

    @Override
    public FieldBegin readFieldBegin() throws InputProtocolException {
        try {
            final FieldBegin value = wrappedInputProtocol.readFieldBegin();
            logger.info(READ_FIELD_BEGIN_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_FIELD_BEGIN_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public void readFieldEnd() throws InputProtocolException {
        try {
            wrappedInputProtocol.readFieldEnd();
            logger.info(READ_FIELD_END_MESSAGE);
        } catch (final InputProtocolException e) {
            logger.info(READ_FIELD_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public short readI16() throws InputProtocolException {
        try {
            final short value = wrappedInputProtocol.readI16();
            logger.info(READ_I16_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_I16_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public int readI32() throws InputProtocolException {
        try {
            final int value = wrappedInputProtocol.readI32();
            logger.info(READ_I32_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_I32_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public long readI64() throws InputProtocolException {
        try {
            final long value = wrappedInputProtocol.readI64();
            logger.info(READ_I64_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_I64_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public ListBegin readListBegin() throws InputProtocolException {
        try {
            final ListBegin value = wrappedInputProtocol.readListBegin();
            logger.info(READ_LIST_BEGIN_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_LIST_BEGIN_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public void readListEnd() throws InputProtocolException {
        try {
            wrappedInputProtocol.readListEnd();
            logger.info(READ_LIST_END_MESSAGE);
        } catch (final InputProtocolException e) {
            logger.info(READ_LIST_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public MapBegin readMapBegin() throws InputProtocolException {
        try {
            final MapBegin value = wrappedInputProtocol.readMapBegin();
            logger.info(READ_MAP_BEGIN_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_MAP_BEGIN_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public void readMapEnd() throws InputProtocolException {
        try {
            wrappedInputProtocol.readMapEnd();
            logger.info(READ_MAP_END_MESSAGE);
        } catch (final InputProtocolException e) {
            logger.info(READ_MAP_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public MessageBegin readMessageBegin() throws InputProtocolException {
        try {
            final MessageBegin value = wrappedInputProtocol.readMessageBegin();
            logger.info(READ_MESSAGE_BEGIN_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_MESSAGE_BEGIN_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public void readMessageEnd() throws InputProtocolException {
        try {
            wrappedInputProtocol.readMessageEnd();
            logger.info(READ_MESSAGE_END_MESSAGE);
        } catch (final InputProtocolException e) {
            logger.info(READ_MESSAGE_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public SetBegin readSetBegin() throws InputProtocolException {
        try {
            final SetBegin value = wrappedInputProtocol.readSetBegin();
            logger.info(READ_SET_BEGIN_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_SET_BEGIN_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public void readSetEnd() throws InputProtocolException {
        try {
            wrappedInputProtocol.readSetEnd();
            logger.info(READ_SET_END_MESSAGE);
        } catch (final InputProtocolException e) {
            logger.info(READ_SET_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public String readString() throws InputProtocolException {
        try {
            final String value = wrappedInputProtocol.readString();
            logger.info(READ_STRING_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_STRING_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public String readStructBegin() throws InputProtocolException {
        try {
            final String value = wrappedInputProtocol.readStructBegin();
            logger.info(READ_STRUCT_BEGIN_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_STRUCT_BEGIN_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public void readStructEnd() throws InputProtocolException {
        try {
            wrappedInputProtocol.readStructEnd();
            logger.info(READ_STRUCT_END_MESSAGE);
        } catch (final InputProtocolException e) {
            logger.info(READ_STRUCT_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public UnsignedInteger readU32() throws InputProtocolException {
        try {
            final UnsignedInteger value = wrappedInputProtocol.readU32();
            logger.info(READ_U32_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_U32_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public UnsignedLong readU64() throws InputProtocolException {
        try {
            final UnsignedLong value = wrappedInputProtocol.readU64();
            logger.info(READ_U64_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_U64_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public Object readVariant() throws InputProtocolException {
        try {
            final Object value = wrappedInputProtocol.readVariant();
            logger.info(READ_VARIANT_MESSAGE, value);
            return value;
        } catch (final InputProtocolException e) {
            logger.info(READ_VARIANT_MESSAGE, "", e);
            throw e;
        }
    }

    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this).add("logger", logger)
                .add("wrappedInputProtocol", wrappedInputProtocol).toString();
    }

    private final static String READ_BOOL_MESSAGE = "readBool() -> {}";
    private final static String READ_BINARY_MESSAGE = "readBinary({} bytes)";
    private final static String READ_BYTE_MESSAGE = "readByte() -> {}";
    private final static String READ_DATE_TIME_MESSAGE = "readDateTime() -> {}";
    private final static String READ_DECIMAL_MESSAGE = "readDecimal() -> {}";
    private final static String READ_DOUBLE_MESSAGE = "readDouble() -> {}";
    private final static String READ_EMAIL_ADDRESS_MESSAGE = "readEmailAddress() -> {}";
    private final static String READ_ENUM_MESSAGE = "readEnum({}) -> {}";
    private final static String READ_FIELD_BEGIN_MESSAGE = "readFieldBegin() -> {}";
    private final static String READ_FIELD_END_MESSAGE = "readFieldEnd()";
    private final static String READ_I16_MESSAGE = "readI16() -> {}";
    private final static String READ_I32_MESSAGE = "readI32() -> {}";
    private final static String READ_I64_MESSAGE = "readI64() -> {}";
    private final static String READ_LIST_BEGIN_MESSAGE = "readListBegin() -> {}";
    private final static String READ_LIST_END_MESSAGE = "readListEnd()";
    private final static String READ_MAP_BEGIN_MESSAGE = "readMapBegin() -> {}";
    private final static String READ_MAP_END_MESSAGE = "readMapEnd()";
    private final static String READ_MESSAGE_BEGIN_MESSAGE = "readMessageBegin() -> {}";
    private final static String READ_MESSAGE_END_MESSAGE = "readMessageEnd()";
    private final static String READ_SET_BEGIN_MESSAGE = "readSetBegin() -> {}";
    private final static String READ_SET_END_MESSAGE = "readSetEnd()";
    private final static String READ_STRING_MESSAGE = "readString() -> {}";
    private final static String READ_STRUCT_BEGIN_MESSAGE = "readStructBegin() -> {}";
    private final static String READ_STRUCT_END_MESSAGE = "readStructEnd()";
    private final static String READ_U32_MESSAGE = "readU32() -> {}";
    private final static String READ_U64_MESSAGE = "readU64() -> {}";
    private final static String READ_URI_MESSAGE = "readUri() -> {}";
    private final static String READ_URL_MESSAGE = "readUrl() -> {}";
    private final static String READ_VARIANT_MESSAGE = "readVariant() -> {}";

    private final Logger logger;

    private final InputProtocol wrappedInputProtocol;
}
