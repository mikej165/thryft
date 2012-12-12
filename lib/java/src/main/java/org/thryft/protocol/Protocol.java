package org.thryft.protocol;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.ByteBuffer;

import org.apache.commons.codec.binary.Base64;
import org.apache.thrift.TBase;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TMessage;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.protocol.TSet;
import org.apache.thrift.protocol.TStruct;
import org.apache.thrift.protocol.TType;
import org.apache.thrift.transport.TTransport;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableSet;

public abstract class Protocol extends TProtocol {
    protected Protocol() {
        super(null);
    }

    protected Protocol(final TTransport trans) {
        super(trans);
    }

    public void flush() throws IOException {
    }

    @Override
    public java.nio.ByteBuffer readBinary() throws TException {
        final String base64String = readString();
        final byte[] binaryBytes = Base64.decodeBase64(base64String);
        return ByteBuffer.wrap(binaryBytes);
    }

    @Override
    public boolean readBool() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public byte readByte() throws TException {
        throw new UnsupportedOperationException();
    }

    public org.joda.time.DateTime readDate() throws TException {
        return new org.joda.time.DateTime(readI64());
    }

    public org.joda.time.DateTime readDateTime() throws TException {
        return new org.joda.time.DateTime(readI64());
    }

    public java.math.BigDecimal readDecimal() throws TException {
        return new java.math.BigDecimal(readString());
    }

    @Override
    public double readDouble() throws TException {
        throw new UnsupportedOperationException();
    }

    @SuppressWarnings("unchecked")
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws TException {
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
    public TField readFieldBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readFieldEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public short readI16() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public int readI32() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public long readI64() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TList readListBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readListEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TMap readMapBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readMapEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TMessage readMessageBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readMessageEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    public Object readMixed() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TSet readSetBegin() throws TException {
        final TList list = readListBegin();
        return new TSet(list.elemType, list.size);
    }

    @Override
    public void readSetEnd() throws TException {
        readListEnd();
    }

    @Override
    public String readString() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TStruct readStructBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readStructEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeBinary(final java.nio.ByteBuffer buf) throws TException {
        writeString(Base64.encodeBase64String(buf.array()));
    }

    @Override
    public void writeBool(final boolean b) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeByte(final byte b) throws TException {
        throw new UnsupportedOperationException();
    }

    public void writeDate(final org.joda.time.DateTime date) throws TException {
        writeI64(date.getMillis());
    }

    public void writeDateTime(final org.joda.time.DateTime dateTime)
            throws TException {
        writeI64(dateTime.getMillis());
    }

    public void writeDecimal(final java.math.BigDecimal decimal)
            throws TException {
        writeString(decimal.toString());
    }

    @Override
    public void writeDouble(final double dub) throws TException {
        throw new UnsupportedOperationException();
    }

    public void writeEnum(final Enum<?> enum_) throws TException {
        writeString(enum_.toString().toUpperCase());
    }

    @Override
    public void writeFieldBegin(final TField field) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldStop() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI16(final short i16) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI32(final int i32) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI64(final long i64) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeListBegin(final TList list) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeListEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMapBegin(final TMap map) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMapEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMessageBegin(final TMessage message) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMessageEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    public void writeMixed(final Object value) throws TException {
        if (value == null) {
            writeNull();
        } else if (value instanceof Boolean) {
            writeBool((Boolean) value);
        } else if (value instanceof Byte) {
            writeByte((Byte) value);
        } else if (value instanceof org.joda.time.DateTime) {
            writeDateTime((org.joda.time.DateTime) value);
        } else if (value instanceof java.math.BigDecimal) {
            writeDecimal((java.math.BigDecimal) value);
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
        } else if (value instanceof ImmutableSet) {
            @SuppressWarnings("unchecked")
            final ImmutableSet<Object> set = (ImmutableSet<Object>) value;
            writeSetBegin(new TSet(TType.VOID, set.size()));
            for (final Object element : set) {
                writeMixed(element);
            }
            writeSetEnd();
        } else if (value instanceof Short) {
            writeI16((Short) value);
        } else if (value instanceof Integer) {
            writeI32((Integer) value);
        } else if (value instanceof Long) {
            writeI64((Long) value);
        } else if (value instanceof String) {
            writeString((String) value);
        } else if (value instanceof TBase<?, ?>) {
            ((TBase<?, ?>) value).write(this);
        } else {
            throw new UnsupportedOperationException();
        }
    }

    public void writeNull() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeSetBegin(final TSet set) throws TException {
        writeListBegin(new TList(set.elemType, set.size));
    }

    @Override
    public void writeSetEnd() throws TException {
        writeListEnd();
    }

    @Override
    public void writeString(final String str) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeStructBegin(final TStruct struct) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeStructEnd() throws TException {
        throw new UnsupportedOperationException();
    }
}