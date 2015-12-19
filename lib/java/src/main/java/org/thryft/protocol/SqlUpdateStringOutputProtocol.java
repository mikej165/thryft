package org.thryft.protocol;

import static org.thryft.Preconditions.checkNotEmpty;

import java.util.Collection;
import java.util.Date;
import java.util.List;

import com.google.common.annotations.GwtIncompatible;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.Lists;

@GwtIncompatible("")
public final class SqlUpdateStringOutputProtocol extends AbstractOutputProtocol {
    public SqlUpdateStringOutputProtocol(final String tableName) {
        this(tableName, ImmutableList.<String> of());
    }

    public SqlUpdateStringOutputProtocol(final String tableName, final Collection<String> extraColumnNames) {
        columnNames.addAll(extraColumnNames);
        this.tableName = checkNotEmpty(tableName);
    }

    public String getSqlUpdateString() {
        if (columnNames.isEmpty()) {
            return "";
        }

        final StringBuilder builder = new StringBuilder();
        builder.append("UPDATE ");
        builder.append(tableName);
        builder.append(" SET ");
        for (int columnI = 0; columnI < columnNames.size(); columnI++) {
            if (columnI > 0) {
                builder.append(", ");
            }
            builder.append(columnNames.get(columnI));
            builder.append(" = ?");
        }
        return builder.toString();
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
    }

    @Override
    public void writeBool(final boolean value) throws OutputProtocolException {
    }

    @Override
    public void writeByte(final byte value) throws OutputProtocolException {
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
    }

    @Override
    public void writeDouble(final double value) throws OutputProtocolException {
    }

    @Override
    public void writeFieldBegin(final String name, final Type type, final short id) throws OutputProtocolException {
        if (depth == 1) {
            switch (type) {
            case LIST:
            case MAP:
            case SET:
            case STRUCT:
                break;
            default:
                columnNames.add(name);
            }
        }
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
    }

    @Override
    public void writeI16(final short value) throws OutputProtocolException {
    }

    @Override
    public void writeI32(final int value) throws OutputProtocolException {
    }

    @Override
    public void writeI64(final long value) throws OutputProtocolException {
    }

    @Override
    public void writeListBegin(final Type elementType, final int size) throws OutputProtocolException {
        depth++;
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        depth--;
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType, final int size) throws OutputProtocolException {
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
    }

    @Override
    public void writeStructBegin(final String name) throws OutputProtocolException {
        depth++;
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        depth--;
    }

    private final List<String> columnNames = Lists.newArrayList();
    int depth = 0;
    private final String tableName;
}
