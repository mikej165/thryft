/*******************************************************************************
 * Copyright (c) 2015, Minor Gordon
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

import javax.annotation.Nullable;

import org.thryft.CompoundType;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class AbstractOutputProtocol implements OutputProtocol {
    public static void writeVariant(final OutputProtocol oprot,
            final Object value) throws OutputProtocolException {
        if (value == null) {
            oprot.writeNull();
        } else if (value instanceof Boolean) {
            oprot.writeBool((Boolean) value);
        } else if (value instanceof Byte) {
            oprot.writeByte((Byte) value);
        } else if (value instanceof Date) {
            oprot.writeDateTime((Date) value);
        } else if (value instanceof BigDecimal) {
            oprot.writeDecimal((BigDecimal) value);
        } else if (value instanceof Double) {
            oprot.writeDouble((Double) value);
        } else if (value instanceof ImmutableList) {
            @SuppressWarnings("unchecked")
            final ImmutableList<Object> set = (ImmutableList<Object>) value;
            oprot.writeListBegin(Type.VOID_, set.size());
            for (final Object element : set) {
                oprot.writeVariant(element);
            }
            oprot.writeListEnd();
        } else if (value instanceof ImmutableMap) {
            @SuppressWarnings("unchecked")
            final ImmutableMap<Object, Object> map = (ImmutableMap<Object, Object>) value;
            oprot.writeMapBegin(Type.VOID_, Type.VOID_, map.size());
            for (final ImmutableMap.Entry<Object, Object> entry : map
                    .entrySet()) {
                oprot.writeVariant(entry.getKey());
                oprot.writeVariant(entry.getValue());
            }
            oprot.writeMapEnd();
        } else if (value instanceof ImmutableSet) {
            @SuppressWarnings("unchecked")
            final ImmutableSet<Object> set = (ImmutableSet<Object>) value;
            oprot.writeSetBegin(Type.VOID_, set.size());
            for (final Object element : set) {
                oprot.writeVariant(element);
            }
            oprot.writeSetEnd();
        } else if (value instanceof EmailAddress) {
            oprot.writeString(((EmailAddress) value).toString());
        } else if (value instanceof Short) {
            oprot.writeI16((Short) value);
        } else if (value instanceof Integer) {
            oprot.writeI32((Integer) value);
        } else if (value instanceof Long) {
            oprot.writeI64((Long) value);
        } else if (value instanceof String) {
            oprot.writeString((String) value);
        } else if (value instanceof Uri) {
            oprot.writeString(((Uri) value).toString());
        } else if (value instanceof CompoundType) {
            ((CompoundType) value).writeAsStruct(oprot);
        } else {
            throw new UnsupportedOperationException(value.toString());
        }
    }

    @Override
    public void flush() throws OutputProtocolException {
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
    public void writeEnum(final Enum<?> value) throws OutputProtocolException {
        writeString(value.toString().toUpperCase());
    }

    @Override
    public final void writeFieldBegin(final String name, final Type type)
            throws OutputProtocolException {
        writeFieldBegin(name, type, FieldBegin.ABSENT_ID);
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
            @Nullable final Object id) throws OutputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        throw new UnsupportedOperationException();
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
    public void writeVariant(final Object value) throws OutputProtocolException {
    }
}
