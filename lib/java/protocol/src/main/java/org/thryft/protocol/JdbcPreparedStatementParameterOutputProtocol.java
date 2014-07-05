package org.thryft.protocol;

import java.sql.Timestamp;
import java.util.Date;

import com.google.common.annotations.GwtIncompatible;
import com.google.common.collect.ImmutableMap;

@GwtIncompatible("")
public final class JdbcPreparedStatementParameterOutputProtocol extends
        AbstractOutputProtocol {
    public JdbcPreparedStatementParameterOutputProtocol() {
        this(ImmutableMap.<String, Object> of());
    }

    public JdbcPreparedStatementParameterOutputProtocol(
            final ImmutableMap<String, Object> extraParameters) {
        builder.putAll(extraParameters);
    }

    public ImmutableMap<String, Object> getJdbcPreparedStatementParameters() {
        return builder.build();
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeBool(final boolean value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, Boolean.valueOf(value));
        }
    }

    @Override
    public void writeByte(final byte value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, Byte.valueOf(value));
        }
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, new Timestamp(value.getTime()));
        }
    }

    @Override
    public void writeDouble(final double value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, Double.valueOf(value));
        }
    }

    @Override
    public void writeFieldBegin(final String name, final Type type,
            final short id) throws OutputProtocolException {
        if (depth == 1) {
            nextFieldName = name;
        }
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        if (depth == 1) {
            nextFieldName = null;
        }
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
    }

    @Override
    public void writeI16(final short value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, Short.valueOf(value));
        }
    }

    @Override
    public void writeI32(final int value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, Integer.valueOf(value));
        }
    }

    @Override
    public void writeI64(final long value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, Long.valueOf(value));
        }
    }

    @Override
    public void writeListBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        depth++;
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        depth--;
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType,
            final int size) throws OutputProtocolException {
        depth++;
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        depth--;
    }

    @Override
    public void writeNull() throws OutputProtocolException {
    }

    @Override
    public void writeString(final String value) throws OutputProtocolException {
        if (depth == 1) {
            builder.put(nextFieldName, value);
        }
    }

    @Override
    public void writeStructBegin(final String name)
            throws OutputProtocolException {
        depth++;
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        depth--;
    }

    private final ImmutableMap.Builder<String, Object> builder = ImmutableMap
            .builder();
    private String nextFieldName = null;
    int depth = 0;
}
