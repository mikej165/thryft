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
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.math.BigDecimal;

import org.apache.commons.codec.binary.Base64;
import org.joda.time.DateTime;
import org.thryft.Base;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class AbstractProtocol implements Protocol {
    public void flush() throws IOException {
    }

    @Override
    public byte[] readBinary() throws IOException {
        final String base64String = readString();
        return Base64.decodeBase64(base64String);
    }

    @Override
    public boolean readBool() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public byte readByte() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public DateTime readDate() throws IOException {
        return new DateTime(readI64());
    }

    @Override
    public DateTime readDateTime() throws IOException {
        return new DateTime(readI64());
    }

    @Override
    public BigDecimal readDecimal() throws IOException {
        return new BigDecimal(readString());
    }

    @Override
    public double readDouble() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public EmailAddress readEmailAddress() throws IOException {
        return new EmailAddress(readString());
    }

    @Override
    @SuppressWarnings("unchecked")
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws IOException {
        final String enumStringValue = readString().trim().toUpperCase();
        if (enumStringValue.isEmpty()) {
            throw new IllegalArgumentException("empty string");
        }

        try {
            return Enum.valueOf(enumClass, enumStringValue);
        } catch (final IllegalArgumentException e) {
            Integer enumIntValue;
            try {
                enumIntValue = Integer.parseInt(enumStringValue);
            } catch (final NumberFormatException e1) {
                throw e;
            }

            final Method valueOfMethod;
            try {
                valueOfMethod = enumClass.getMethod("valueOf", Integer.class);
            } catch (final SecurityException e1) {
                throw e;
            } catch (final NoSuchMethodException e1) {
                throw e;
            }

            try {
                return (E) valueOfMethod.invoke(null, enumIntValue);
            } catch (final IllegalArgumentException e1) {
                throw e;
            } catch (final IllegalAccessException e1) {
                throw e;
            } catch (final InvocationTargetException e1) {
                throw e;
            }
        }
    }

    @Override
    public FieldBegin readFieldBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readFieldEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public short readI16() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public int readI32() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public long readI64() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public ListBegin readListBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readListEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public MapBegin readMapBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readMapEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public Object readMixed() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public SetBegin readSetBegin() throws IOException {
        final ListBegin list = readListBegin();
        return new SetBegin(list.elemType, list.size);
    }

    @Override
    public void readSetEnd() throws IOException {
        readListEnd();
    }

    @Override
    public String readString() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public StructBegin readStructBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readStructEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public UnsignedInteger readU32() throws IOException {
        return UnsignedInteger.valueOf(readI32());
    }

    @Override
    public UnsignedLong readU64() throws IOException {
        return UnsignedLong.valueOf(readI64());
    }

    @Override
    public Uri readUri() throws IOException {
        return Uri.parse(readString());
    }

    @Override
    public Url readUrl() throws IOException {
        return Url.parse(readString());
    }

    @Override
    public void writeBinary(final byte[] buf) throws IOException {
        writeString(Base64.encodeBase64String(buf));
    }

    @Override
    public void writeBool(final boolean b) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeByte(final byte b) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeDateTime(final DateTime dateTime) throws IOException {
        writeI64(dateTime.getMillis());
    }

    @Override
    public void writeDecimal(final BigDecimal decimal) throws IOException {
        writeString(decimal.toString());
    }

    @Override
    public void writeDouble(final double dub) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeEmailAddress(final EmailAddress emailAddress)
            throws IOException {
        writeString(emailAddress.toString());
    }

    @Override
    public void writeEnum(final Enum<?> enum_) throws IOException {
        writeString(enum_.toString().toUpperCase());
    }

    @Override
    public void writeFieldBegin(final FieldBegin field) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldStop() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI16(final short i16) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI32(final int i32) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI64(final long i64) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeListBegin(final ListBegin list) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeListEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMapBegin(final MapBegin map) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMapEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMixed(final Object value) throws IOException {
        if (value == null) {
            writeNull();
        } else if (value instanceof Boolean) {
            writeBool((Boolean) value);
        } else if (value instanceof Byte) {
            writeByte((Byte) value);
        } else if (value instanceof DateTime) {
            writeDateTime((DateTime) value);
        } else if (value instanceof BigDecimal) {
            writeDecimal((BigDecimal) value);
        } else if (value instanceof Double) {
            writeDouble((Double) value);
        } else if (value instanceof ImmutableList) {
            @SuppressWarnings("unchecked")
            final ImmutableList<Object> set = (ImmutableList<Object>) value;
            writeListBegin(new ListBegin(Type.VOID, set.size()));
            for (final Object element : set) {
                writeMixed(element);
            }
            writeListEnd();
        } else if (value instanceof ImmutableMap) {
            @SuppressWarnings("unchecked")
            final ImmutableMap<Object, Object> map = (ImmutableMap<Object, Object>) value;
            writeMapBegin(new MapBegin(Type.VOID, Type.VOID, map.size()));
            for (final ImmutableMap.Entry<Object, Object> entry : map
                    .entrySet()) {
                writeMixed(entry.getKey());
                writeMixed(entry.getValue());
            }
            writeMapEnd();
        } else if (value instanceof ImmutableSet) {
            @SuppressWarnings("unchecked")
            final ImmutableSet<Object> set = (ImmutableSet<Object>) value;
            writeSetBegin(new SetBegin(Type.VOID, set.size()));
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
    public void writeNull() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeSetBegin(final SetBegin set) throws IOException {
        writeListBegin(new ListBegin(set.elemType, set.size));
    }

    @Override
    public void writeSetEnd() throws IOException {
        writeListEnd();
    }

    @Override
    public void writeString(final String str) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeStructBegin(final StructBegin struct) throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeStructEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeU32(final UnsignedInteger u32) throws IOException {
        writeI32(u32.intValue());
    }

    @Override
    public void writeU64(final UnsignedLong u64) throws IOException {
        writeI64(u64.longValue());
    }

    @Override
    public void writeUri(final Uri uri) throws IOException {
        writeString(uri.toString());
    }

    @Override
    public void writeUrl(final Url url) throws IOException {
        writeString(url.toString());
    }
}
