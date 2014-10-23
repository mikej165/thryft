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
public class LoggingOutputProtocol implements OutputProtocol {
    public LoggingOutputProtocol(final OutputProtocol wrappedProtocol) {
        logger = LoggerFactory.getLogger(wrappedProtocol.getClass());
        wrappedOutputProtocol = wrappedProtocol;
    }

    @Override
    public void flush() throws OutputProtocolException {
        wrappedOutputProtocol.flush();
    }

    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this).add("logger", logger)
                .add("wrappedOutputProtocol", wrappedOutputProtocol).toString();
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeBinary(value);
            logger.info(WRITE_BINARY_MESSAGE, value.length);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_BINARY_MESSAGE, value.length, e);
            throw e;
        }
    }

    @Override
    public void writeBool(final boolean value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeBool(value);
            logger.info(WRITE_BOOL_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_BOOL_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeByte(final byte value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeByte(value);
            logger.info(WRITE_BYTE_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_BYTE_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeDateTime(value);
            logger.info(WRITE_DATE_TIME_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_DATE_TIME_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeDecimal(final BigDecimal value)
            throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeDecimal(value);
            logger.info(WRITE_DECIMAL_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_DECIMAL_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeDouble(final double value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeDouble(value);
            logger.info(WRITE_DOUBLE_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_DOUBLE_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeEnum(final Enum<?> value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeEnum(value);
            logger.info(WRITE_ENUM_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_ENUM_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeFieldBegin(final String name, final Type type,
            final short id) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeFieldBegin(name, type, id);
            logger.info(WRITE_FIELD_BEGIN_MESSAGE, name, type, id);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_FIELD_BEGIN_MESSAGE, name, type, id, e);
            throw e;
        }
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeFieldEnd();
            logger.info(WRITE_FIELD_END_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_FIELD_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeFieldStop();
            logger.info(WRITE_FIELD_STOP_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_FIELD_STOP_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeI16(final short value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeI16(value);
            logger.info(WRITE_I16_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_I16_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeI32(final int value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeI32(value);
            logger.info(WRITE_I32_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_I32_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeI64(final long value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeI64(value);
            logger.info(WRITE_I64_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_I64_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeListBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeListBegin(elementType, size);
            logger.info(WRITE_LIST_BEGIN_MESSAGE, elementType, size);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_I16_MESSAGE, elementType, size, e);
            throw e;
        }
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeListEnd();
            logger.info(WRITE_LIST_END_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_LIST_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType,
            final int size) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeMapBegin(keyType, valueType, size);
            logger.info(WRITE_MAP_BEGIN_MESSAGE, keyType, valueType, size);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_MAP_BEGIN_MESSAGE, keyType, valueType, size, e);
            throw e;
        }
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeMapEnd();
            logger.info(WRITE_MAP_END_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_MAP_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeMessageBegin(final String name, final MessageType type,
            final Object id) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeMessageBegin(name, type, id);
            logger.info(WRITE_MESSAGE_BEGIN_MESSAGE, name, type, id);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_MESSAGE_BEGIN_MESSAGE, name, type, id, e);
            throw e;
        }
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeMessageEnd();
            logger.info(WRITE_MESSAGE_END_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_MESSAGE_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeNull() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeNull();
            logger.info(WRITE_NULL_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_NULL_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeSetBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeSetBegin(elementType, size);
            logger.info(WRITE_SET_BEGIN_MESSAGE, elementType, size);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_SET_BEGIN_MESSAGE, elementType, size, e);
            throw e;
        }
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeSetEnd();
            logger.info(WRITE_SET_END_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_SET_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeString(final String value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeString(value);
            logger.info(WRITE_STRING_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_STRING_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeStructBegin(final String name)
            throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeStructBegin(name);
            logger.info(WRITE_STRUCT_BEGIN_MESSAGE, name);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_STRUCT_BEGIN_MESSAGE, name, e);
            throw e;
        }
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeStructEnd();
            logger.info(WRITE_STRUCT_END_MESSAGE);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_STRUCT_END_MESSAGE, e);
            throw e;
        }
    }

    @Override
    public void writeU32(final UnsignedInteger value)
            throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeU32(value);
            logger.info(WRITE_U32_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_U32_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeU64(final UnsignedLong value)
            throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeU64(value);
            logger.info(WRITE_U64_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_U64_MESSAGE, value, e);
            throw e;
        }
    }

    @Override
    public void writeVariant(final Object value) throws OutputProtocolException {
        try {
            wrappedOutputProtocol.writeVariant(value);
            logger.info(WRITE_VARIANT_MESSAGE, value);
        } catch (final OutputProtocolException e) {
            logger.info(WRITE_VARIANT_MESSAGE, value, e);
            throw e;
        }
    }

    private final static String WRITE_BOOL_MESSAGE = "writeBool({})";
    private final static String WRITE_BINARY_MESSAGE = "writeBinary({} bytes)";
    private final static String WRITE_BYTE_MESSAGE = "writeByte({})";
    private final static String WRITE_DATE_TIME_MESSAGE = "writeDateTime({})";
    private final static String WRITE_DECIMAL_MESSAGE = "writeDecimal({})";
    private final static String WRITE_DOUBLE_MESSAGE = "writeDouble({})";
    private final static String WRITE_ENUM_MESSAGE = "writeEnum({})";
    private final static String WRITE_FIELD_BEGIN_MESSAGE = "writeFieldBegin({}, {}, {})";
    private final static String WRITE_FIELD_END_MESSAGE = "writeFieldEnd()";
    private final static String WRITE_FIELD_STOP_MESSAGE = "writeFieldStop()";
    private final static String WRITE_I16_MESSAGE = "writeI16({})";
    private final static String WRITE_I32_MESSAGE = "writeI32({})";
    private final static String WRITE_I64_MESSAGE = "writeI64({})";
    private final static String WRITE_LIST_BEGIN_MESSAGE = "writeListBegin({}, {})";
    private final static String WRITE_LIST_END_MESSAGE = "writeListEnd()";
    private final static String WRITE_MAP_BEGIN_MESSAGE = "writeMapBegin({}, {}, {})";
    private final static String WRITE_MAP_END_MESSAGE = "writeMapEnd()";
    private final static String WRITE_MESSAGE_BEGIN_MESSAGE = "writeMessageBegin({}, {}, {})";
    private final static String WRITE_MESSAGE_END_MESSAGE = "writeMessageEnd()";
    private final static String WRITE_NULL_MESSAGE = "writeNull()";
    private final static String WRITE_SET_BEGIN_MESSAGE = "writeSetBegin({}, {})";
    private final static String WRITE_SET_END_MESSAGE = "writeSetEnd()";
    private final static String WRITE_STRING_MESSAGE = "writeString({})";
    private final static String WRITE_STRUCT_BEGIN_MESSAGE = "writeStructBegin({})";
    private final static String WRITE_STRUCT_END_MESSAGE = "writeStructEnd()";
    private final static String WRITE_U32_MESSAGE = "writeU32({})";
    private final static String WRITE_U64_MESSAGE = "writeU64({})";
    private final static String WRITE_VARIANT_MESSAGE = "writeVariant({})";

    private final Logger logger;

    private final OutputProtocol wrappedOutputProtocol;
}
