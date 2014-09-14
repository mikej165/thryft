package org.thryft.protocol;

import java.util.Date;

import javax.annotation.Nullable;

import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class ForwardingOutputProtocol implements OutputProtocol {
    @Override
    public void flush() throws OutputProtocolException {
        _delegate().flush();
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
        _delegate().writeBinary(value);
    }

    @Override
    public void writeBool(final boolean value) throws OutputProtocolException {
        _delegate().writeBool(value);
    }

    @Override
    public void writeByte(final byte value) throws OutputProtocolException {
        _delegate().writeByte(value);
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
        _delegate().writeDateTime(value);
    }

    @Override
    public void writeDecimal(final java.math.BigDecimal value)
            throws OutputProtocolException {
        _delegate().writeDecimal(value);
    }

    @Override
    public void writeDouble(final double value) throws OutputProtocolException {
        _delegate().writeDouble(value);
    }

    @Override
    public void writeEmailAddress(final EmailAddress value)
            throws OutputProtocolException {
        _delegate().writeEmailAddress(value);
    }

    @Override
    public void writeEnum(final Enum<?> value) throws OutputProtocolException {
        _delegate().writeEnum(value);
    }

    @Override
    public void writeFieldBegin(final String name, final Type type,
            final short id) throws OutputProtocolException {
        _delegate().writeFieldBegin(name, type, id);
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        _delegate().writeFieldEnd();
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
        _delegate().writeFieldStop();
    }

    @Override
    public void writeI16(final short value) throws OutputProtocolException {
        _delegate().writeI16(value);
    }

    @Override
    public void writeI32(final int value) throws OutputProtocolException {
        _delegate().writeI32(value);
    }

    @Override
    public void writeI64(final long value) throws OutputProtocolException {
        _delegate().writeI64(value);
    }

    @Override
    public void writeListBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        _delegate().writeListBegin(elementType, size);
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        _delegate().writeListEnd();
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType,
            final int size) throws OutputProtocolException {
        _delegate().writeMapBegin(keyType, valueType, size);
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        _delegate().writeMapEnd();
    }

    @Override
    public void writeMessageBegin(final String name, final MessageType type,
            @Nullable final Object id) throws OutputProtocolException {
        _delegate().writeMessageBegin(name, type, id);
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        _delegate().writeMessageEnd();
    }

    @Override
    public void writeVariant(final Object value) throws OutputProtocolException {
        _delegate().writeVariant(value);
    }

    @Override
    public void writeNull() throws OutputProtocolException {
        _delegate().writeNull();
    }

    @Override
    public void writeSetBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        _delegate().writeSetBegin(elementType, size);
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        _delegate().writeSetEnd();
    }

    @Override
    public void writeString(final String value) throws OutputProtocolException {
        _delegate().writeString(value);
    }

    @Override
    public void writeStructBegin(final String name)
            throws OutputProtocolException {
        _delegate().writeStructBegin(name);
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        _delegate().writeStructEnd();
    }

    @Override
    public void writeU32(final UnsignedInteger value)
            throws OutputProtocolException {
        _delegate().writeU32(value);
    }

    @Override
    public void writeU64(final UnsignedLong value)
            throws OutputProtocolException {
        _delegate().writeU64(value);
    }

    @Override
    public void writeUri(final Uri value) throws OutputProtocolException {
        _delegate().writeUri(value);
    }

    @Override
    public void writeUrl(final Url value) throws OutputProtocolException {
        _delegate().writeUrl(value);
    }

    protected abstract OutputProtocol _delegate();
}
