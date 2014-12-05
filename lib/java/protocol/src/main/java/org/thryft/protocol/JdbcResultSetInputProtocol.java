package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;
import static com.google.common.base.Preconditions.checkState;

import java.math.BigDecimal;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Types;
import java.util.Date;
import java.util.Stack;

import com.google.common.annotations.GwtIncompatible;
import com.google.common.base.Optional;

@GwtIncompatible("")
public class JdbcResultSetInputProtocol extends AbstractInputProtocol {
    public JdbcResultSetInputProtocol(final ResultSet resultSet) {
        this(resultSet, Optional.<String> absent());
    }

    public JdbcResultSetInputProtocol(final ResultSet resultSet,
            final Optional<String> tableName) {
        this.resultSet = checkNotNull(resultSet);
        this.tableName = checkNotNull(tableName);
    }

    public JdbcResultSetInputProtocol(final ResultSet resultSet,
            final String tableName) {
        this(resultSet, Optional.of(tableName));
    }

    @Override
    public byte[] readBinary() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean readBool() throws InputProtocolException {
        try {
            return resultSet.getBoolean(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public byte readByte() throws InputProtocolException {
        try {
            return resultSet.getByte(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public Date readDateTime() throws InputProtocolException {
        try {
            return resultSet.getTimestamp(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public BigDecimal readDecimal() throws InputProtocolException {
        try {
            return resultSet.getBigDecimal(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public double readDouble() throws InputProtocolException {
        try {
            return resultSet.getDouble(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public FieldBegin readFieldBegin() throws InputProtocolException {
        while (!fieldBeginStack.isEmpty()) {
            return fieldBeginStack.peek();
        }
        return new FieldBegin();
    }

    @Override
    public void readFieldEnd() throws InputProtocolException {
        fieldBeginStack.pop();
    }

    @Override
    public short readI16() throws InputProtocolException {
        try {
            return resultSet.getShort(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public int readI32() throws InputProtocolException {
        try {
            return resultSet.getInt(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public long readI64() throws InputProtocolException {
        try {
            return resultSet.getLong(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public ListBegin readListBegin() throws InputProtocolException {
        return new ListBegin(Type.VOID_, 0);
    }

    @Override
    public MapBegin readMapBegin() throws InputProtocolException {
        return new MapBegin(Type.VOID_, Type.VOID_, 0);
    }

    @Override
    public String readString() throws InputProtocolException {
        try {
            return resultSet.getString(fieldBeginStack.peek().getId());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public String readStructBegin() throws InputProtocolException {
        checkState(fieldBeginStack.isEmpty());
        try {
            final ResultSetMetaData resultSetMetaData = resultSet.getMetaData();
            final int columnCount = resultSetMetaData.getColumnCount();
            for (int columnI = 0; columnI < columnCount; columnI++) {
                if (tableName.isPresent()) {
                    if (!resultSetMetaData.getTableName(columnI + 1)
                            .equalsIgnoreCase(tableName.get())) {
                        continue;
                    }
                }

                resultSet.getObject(columnI + 1);
                if (resultSet.wasNull()) {
                    continue;
                }

                final String fieldName = resultSetMetaData.getColumnName(
                        columnI + 1).toLowerCase(); // Some databases change
                // case
                Type fieldType;
                final int columnType = resultSetMetaData
                        .getColumnType(columnI + 1);
                switch (columnType) {
                case Types.BIGINT:
                    fieldType = Type.I64;
                    break;
                case Types.BOOLEAN:
                    fieldType = Type.BOOL;
                    break;
                case Types.DECIMAL:
                    fieldType = Type.STRING;
                    break;
                case Types.DOUBLE:
                    fieldType = Type.DOUBLE;
                    break;
                case Types.INTEGER:
                    fieldType = Type.I32;
                    break;
                case Types.SMALLINT:
                    fieldType = Type.I16;
                    break;
                case Types.TIMESTAMP:
                    fieldType = Type.I64;
                    break;
                case Types.TINYINT:
                    fieldType = Type.BYTE;
                    break;
                case Types.VARCHAR:
                    fieldType = Type.STRING;
                    break;
                default:
                    throw new UnsupportedOperationException(String.format(
                            "%s: %d", fieldName, columnType));
                }

                fieldBeginStack.push(new FieldBegin(fieldName, fieldType,
                        (short) (columnI + 1)));
            }
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
        return "";
    }

    @Override
    public Object readVariant() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    private final Stack<FieldBegin> fieldBeginStack = new Stack<FieldBegin>();
    private final ResultSet resultSet;
    private final Optional<String> tableName;
}
