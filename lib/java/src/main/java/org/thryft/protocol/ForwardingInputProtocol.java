package org.thryft.protocol;

import java.util.Date;

import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class ForwardingInputProtocol implements InputProtocol {
    @Override
    public byte[] readBinary() throws InputProtocolException {
        return _delegate().readBinary();
    }

    @Override
    public boolean readBool() throws InputProtocolException {
        return _delegate().readBool();
    }

    @Override
    public byte readByte() throws InputProtocolException {
        return _delegate().readByte();
    }

    @Override
    public Date readDateTime() throws InputProtocolException {
        return _delegate().readDateTime();
    }

    @Override
    public java.math.BigDecimal readDecimal() throws InputProtocolException {
        return _delegate().readDecimal();
    }

    @Override
    public double readDouble() throws InputProtocolException {
        return _delegate().readDouble();
    }

    @Override
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws InputProtocolException {
        return _delegate().readEnum(enumClass);
    }

    @Override
    public FieldBegin readFieldBegin() throws InputProtocolException {
        return _delegate().readFieldBegin();
    }

    @Override
    public void readFieldEnd() throws InputProtocolException {
        _delegate().readFieldEnd();
    }

    @Override
    public short readI16() throws InputProtocolException {
        return _delegate().readI16();
    }

    @Override
    public int readI32() throws InputProtocolException {
        return _delegate().readI32();
    }

    @Override
    public long readI64() throws InputProtocolException {
        return _delegate().readI64();
    }

    @Override
    public ListBegin readListBegin() throws InputProtocolException {
        return _delegate().readListBegin();
    }

    @Override
    public void readListEnd() throws InputProtocolException {
        _delegate().readListEnd();
    }

    @Override
    public MapBegin readMapBegin() throws InputProtocolException {
        return _delegate().readMapBegin();
    }

    @Override
    public void readMapEnd() throws InputProtocolException {
        _delegate().readMapEnd();
    }

    @Override
    public MessageBegin readMessageBegin() throws InputProtocolException {
        return _delegate().readMessageBegin();
    }

    @Override
    public void readMessageEnd() throws InputProtocolException {
        _delegate().readMessageEnd();
    }

    @Override
    public SetBegin readSetBegin() throws InputProtocolException {
        return _delegate().readSetBegin();
    }

    @Override
    public void readSetEnd() throws InputProtocolException {
        _delegate().readSetEnd();
    }

    @Override
    public String readString() throws InputProtocolException {
        return _delegate().readString();
    }

    @Override
    public String readStructBegin() throws InputProtocolException {
        return _delegate().readStructBegin();
    }

    @Override
    public void readStructEnd() throws InputProtocolException {
        _delegate().readStructEnd();
    }

    @Override
    public UnsignedInteger readU32() throws InputProtocolException {
        return _delegate().readU32();
    }

    @Override
    public UnsignedLong readU64() throws InputProtocolException {
        return _delegate().readU64();
    }

    @Override
    public Object readVariant() throws InputProtocolException {
        return _delegate().readVariant();
    }

    protected abstract InputProtocol _delegate();
}
