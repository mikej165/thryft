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
import java.net.MalformedURLException;
import java.nio.ByteBuffer;

import org.apache.commons.codec.binary.Base64;
import org.joda.time.DateTime;
import org.thryft.TBase;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Url;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class Protocol {
    public void flush() throws IOException {
    }

    public boolean readBool() throws IOException {
        throw new UnsupportedOperationException();
    }

    public byte readByte() throws IOException {
        throw new UnsupportedOperationException();
    }

    public DateTime readDate() throws IOException {
        return new DateTime(readI64());
    }

    public DateTime readDateTime() throws IOException {
        return new DateTime(readI64());
    }

    public BigDecimal readDecimal() throws IOException {
        return new BigDecimal(readString());
    }

    public double readDouble() throws IOException {
        throw new UnsupportedOperationException();
    }

    public EmailAddress readEmailAddress() throws IOException {
        return new EmailAddress(readString());
    }

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

    public TField readFieldBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void readFieldEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public short readI16() throws IOException {
        throw new UnsupportedOperationException();
    }

    public int readI32() throws IOException {
        throw new UnsupportedOperationException();
    }

    public long readI64() throws IOException {
        throw new UnsupportedOperationException();
    }

    public TList readListBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void readListEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public TMap readMapBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void readMapEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public Object readMixed() throws IOException {
        throw new UnsupportedOperationException();
    }

    public TSet readSetBegin() throws IOException {
        final TList list = readListBegin();
        return new TSet(list.elemType, list.size);
    }

    public void readSetEnd() throws IOException {
        readListEnd();
    }

    public String readString() throws IOException {
        throw new UnsupportedOperationException();
    }

    public TStruct readStructBegin() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void readStructEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public Url readUrl() throws IOException, MalformedURLException {
        return Url.parse(readString());
    }

    public void writeBinary(final ByteBuffer buf) throws IOException {
        writeString(Base64.encodeBase64String(buf.array()));
    }

    public void writeBool(final boolean b) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeByte(final byte b) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeDateTime(final DateTime dateTime) throws IOException {
        writeI64(dateTime.getMillis());
    }

    public void writeDecimal(final BigDecimal decimal) throws IOException {
        writeString(decimal.toString());
    }

    public void writeDouble(final double dub) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeEmailAddress(final EmailAddress emailAddress)
            throws IOException {
        writeString(emailAddress.toString());
    }

    public void writeEnum(final Enum<?> enum_) throws IOException {
        writeString(enum_.toString().toUpperCase());
    }

    public void writeFieldBegin(final TField field) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeFieldEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeFieldStop() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeI16(final short i16) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeI32(final int i32) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeI64(final long i64) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeListBegin(final TList list) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeListEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeMapBegin(final TMap map) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeMapEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

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
            writeListBegin(new TList(TType.VOID, set.size()));
            for (final Object element : set) {
                writeMixed(element);
            }
            writeListEnd();
        } else if (value instanceof ImmutableMap) {
            @SuppressWarnings("unchecked")
            final ImmutableMap<Object, Object> map = (ImmutableMap<Object, Object>) value;
            writeMapBegin(new TMap(TType.VOID, TType.VOID, map.size()));
            for (final ImmutableMap.Entry<Object, Object> entry : map
                    .entrySet()) {
                writeMixed(entry.getKey());
                writeMixed(entry.getValue());
            }
            writeMapEnd();
        } else if (value instanceof ImmutableSet) {
            @SuppressWarnings("unchecked")
            final ImmutableSet<Object> set = (ImmutableSet<Object>) value;
            writeSetBegin(new TSet(TType.VOID, set.size()));
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
        } else if (value instanceof TBase<?>) {
            ((TBase<?>) value).write(this);
        } else {
            throw new UnsupportedOperationException(value.getClass()
                    .getCanonicalName());
        }
    }

    public void writeNull() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeSetBegin(final TSet set) throws IOException {
        writeListBegin(new TList(set.elemType, set.size));
    }

    public void writeSetEnd() throws IOException {
        writeListEnd();
    }

    public void writeString(final String str) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeStructBegin(final TStruct struct) throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeStructEnd() throws IOException {
        throw new UnsupportedOperationException();
    }

    public void writeUrl(final Url url) throws IOException {
        writeString(url.toString());
    }
}
