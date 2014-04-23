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

import org.apache.commons.codec.binary.Base64;
import org.thryft.Base;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class AbstractOutputProtocol implements OutputProtocol {
    @Override
    public void flush() throws OutputProtocolException {
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
        writeString(Base64.encodeBase64String(value));
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
        writeI64(value.getTime());
    }

    @Override
    public void writeDecimal(final BigDecimal value)
            throws OutputProtocolException {
        writeString(value.toString());
    }

    @Override
    public void writeEmailAddress(final EmailAddress value)
            throws OutputProtocolException {
        writeString(value.toString());
    }

    @Override
    public void writeEnum(final Enum<?> value) throws OutputProtocolException {
        writeString(value.toString().toUpperCase());
    }

    @Override
    public void writeFieldBegin(final String name, final Type type,
            final short id) throws OutputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMessageBegin(final String name, final MessageType type,
            final int sequenceId) throws OutputProtocolException {
        writeStructBegin(name);
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        writeStructEnd();
    }

    @Override
    public void writeMixed(final Object value) throws OutputProtocolException {
        if (value == null) {
            writeNull();
        } else if (value instanceof Boolean) {
            writeBool((Boolean) value);
        } else if (value instanceof Byte) {
            writeByte((Byte) value);
        } else if (value instanceof Date) {
            writeDateTime((Date) value);
        } else if (value instanceof BigDecimal) {
            writeDecimal((BigDecimal) value);
        } else if (value instanceof Double) {
            writeDouble((Double) value);
        } else if (value instanceof ImmutableList) {
            @SuppressWarnings("unchecked")
            final ImmutableList<Object> set = (ImmutableList<Object>) value;
            writeListBegin(Type.VOID, set.size());
            for (final Object element : set) {
                writeMixed(element);
            }
            writeListEnd();
        } else if (value instanceof ImmutableMap) {
            @SuppressWarnings("unchecked")
            final ImmutableMap<Object, Object> map = (ImmutableMap<Object, Object>) value;
            writeMapBegin(Type.VOID, Type.VOID, map.size());
            for (final ImmutableMap.Entry<Object, Object> entry : map
                    .entrySet()) {
                writeMixed(entry.getKey());
                writeMixed(entry.getValue());
            }
            writeMapEnd();
        } else if (value instanceof ImmutableSet) {
            @SuppressWarnings("unchecked")
            final ImmutableSet<Object> set = (ImmutableSet<Object>) value;
            writeSetBegin(Type.VOID, set.size());
            for (final Object element : set) {
                writeMixed(element);
            }
            writeSetEnd();
        } else if (value instanceof EmailAddress) {
            writeEmailAddress((EmailAddress) value);
        } else if (value instanceof Short) {
            writeI16((Short) value);
        } else if (value instanceof Integer) {
            writeI32((Integer) value);
        } else if (value instanceof Long) {
            writeI64((Long) value);
        } else if (value instanceof String) {
            writeString((String) value);
        } else if (value instanceof Url) {
            writeUrl((Url) value);
        } else if (value instanceof Base<?>) {
            ((Base<?>) value).write(this);
        } else {
            throw new UnsupportedOperationException(value.getClass()
                    .getCanonicalName());
        }
    }

    @Override
    public void writeSetBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        writeListBegin(elementType, size);
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        writeListEnd();
    }

    @Override
    public void writeU32(final UnsignedInteger value)
            throws OutputProtocolException {
        writeI32(value.intValue());
    }

    @Override
    public void writeU64(final UnsignedLong value)
            throws OutputProtocolException {
        writeI64(value.longValue());
    }

    @Override
    public void writeUri(final Uri value) throws OutputProtocolException {
        writeString(value.toString());
    }

    @Override
    public void writeUrl(final Url value) throws OutputProtocolException {
        writeString(value.toString());
    }
}
