package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;
import static com.google.common.base.Preconditions.checkState;

import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Types;
import java.util.Stack;

import com.google.common.annotations.GwtIncompatible;

@GwtIncompatible("")
public class JdbcResultSetInputProtocol extends AbstractInputProtocol {
    public JdbcResultSetInputProtocol(final ResultSet resultSet)
            throws SQLException {
        this.resultSet = checkNotNull(resultSet);
        resultSetMetaData = resultSet.getMetaData();
    }

    public boolean next() throws SQLException {
        if (!resultSet.next()) {
            return false;
        }
        checkState(fieldStack.isEmpty());
        final int columnCount = resultSetMetaData.getColumnCount();
        for (int columnI = 0; columnI < columnCount; columnI++) {
            final String fieldName = resultSetMetaData
                    .getColumnName(columnI + 1);
            Type fieldType;
            switch (resultSetMetaData.getColumnType(columnI + 1)) {
            case Types.BIGINT:
                fieldType = Type.I64;
                break;
            case Types.BOOLEAN:
                fieldType = Type.BOOL;
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
            case Types.TINYINT:
                fieldType = Type.BYTE;
                break;
            case Types.VARCHAR:
                fieldType = Type.STRING;
                break;
            default:
                throw new UnsupportedOperationException();
            }
            fieldStack.push(new FieldBegin(fieldName, fieldType, (short) -1));
        }
        return true;
    }

    @Override
    public byte[] readBinary() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean readBool() throws InputProtocolException {
        try {
            return resultSet.getBoolean(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public byte readByte() throws InputProtocolException {
        try {
            return resultSet.getByte(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public double readDouble() throws InputProtocolException {
        try {
            return resultSet.getDouble(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public FieldBegin readFieldBegin() throws InputProtocolException {
        return fieldStack.peek();
    }

    @Override
    public void readFieldEnd() throws InputProtocolException {
        fieldStack.pop();
    }

    @Override
    public short readI16() throws InputProtocolException {
        try {
            return resultSet.getShort(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public int readI32() throws InputProtocolException {
        try {
            return resultSet.getInt(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public long readI64() throws InputProtocolException {
        try {
            return resultSet.getLong(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public ListBegin readListBegin() throws InputProtocolException {
        return new ListBegin(Type.VOID, 0);
    }

    @Override
    public MapBegin readMapBegin() throws InputProtocolException {
        return new MapBegin(Type.VOID, Type.VOID, 0);
    }

    @Override
    public Object readMixed() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public String readString() throws InputProtocolException {
        try {
            return resultSet.getString(fieldStack.peek().getName());
        } catch (final SQLException e) {
            throw new InputProtocolException(e);
        }
    }

    @Override
    public String readStructBegin() throws InputProtocolException {
        return "";
    }

    private final Stack<FieldBegin> fieldStack = new Stack<FieldBegin>();
    private final ResultSet resultSet;
    private final ResultSetMetaData resultSetMetaData;
}
