package org.thryft.protocol;

import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.protocol.TStruct;
import org.apache.thrift.protocol.TType;
import org.joda.time.format.DateTimeFormat;
import org.joda.time.format.DateTimeFormatter;

import au.com.bytecode.opencsv.CSVReader;

import com.google.common.collect.Lists;

public class CsvProtocol extends Protocol {
    protected class File extends Protocol {
        protected class Row extends Protocol {
            protected class SequenceColumn extends Protocol {
                public SequenceColumn(final String[] elements) {
                    this.elements = elements;
                    currentElementI = 0;
                }

                @Override
                public TList readListBegin() throws TException {
                    throw new IllegalStateException();
                }

                @Override
                public String readString() throws TException {
                    return elements[currentElementI++];
                }

                private int currentElementI;
                private final String[] elements;
            }

            public Row(final String[] columnNames, final String[] columnValues) {
                this.columnNames = columnNames;
                this.columnValues = columnValues;
                currentColumnI = 0;
            }

            @Override
            public TField readFieldBegin() throws TException {
                if (currentColumnI < columnValues.length) {
                    return _readFieldBegin();
                } else {
                    return new TField();
                }
            }

            @Override
            public void readFieldEnd() {
                currentColumnI++;
            }

            @Override
            public TList readListBegin() throws TException {
                return _readListBegin(readString());
            }

            @Override
            public String readString() {
                return _getCurrentColumnValue();
            }

            @Override
            public TStruct readStructBegin() {
                // Assume a struct will read inline
                scopeStack.push(this);
                return new TStruct();
            }

            protected TProtocol _createSequenceColumn(final String[] elements) {
                return new SequenceColumn(elements);
            }

            protected String _getCurrentColumnName() {
                return columnNames[currentColumnI];
            }

            protected String _getCurrentColumnValue() {
                return columnValues[currentColumnI];
            }

            protected TField _readFieldBegin() throws TException {
                return new TField(_getCurrentColumnName(), TType.STRING,
                        (short) 0);
            }

            protected TList _readListBegin(final String list) throws TException {
                final CSVReader listReader = new CSVReader(new StringReader(
                        list));
                String[] listElements;
                try {
                    listElements = listReader.readNext();
                    if (listElements == null) {
                        listElements = new String[0];
                    }
                } catch (final IOException e) {
                    listElements = new String[0];
                } finally {
                    try {
                        listReader.close();
                    } catch (final IOException e) {
                        throw new TException(e);
                    }
                }
                scopeStack.push(_createSequenceColumn(new String[0]));
                return new TList(TType.STRING, 0);
            }

            protected String _readString(final String columnName) {
                for (int columnI = 0; columnI < columnNames.length; columnI++) {
                    if (columnNames[columnI].equals(columnName)) {
                        return columnValues[columnI];
                    }
                }

                return null;
            }

            private int currentColumnI;
            private final String[] columnNames;
            private final String[] columnValues;
        }

        public File(final List<String[]> rows) {
            this.rows = new Stack<TProtocol>();
            Collections.reverse(rows);
            final String[] columnNames = rows.remove(rows.size() - 1);
            for (final String[] row : rows) {
                this.rows.push(_createRow(columnNames, row));
            }
        }

        @Override
        public TList readListBegin() throws TException {
            return new TList(TType.STRUCT, rows.size());
        }

        @Override
        public String readString() throws TException {
            throw new IllegalStateException();
        }

        @Override
        public TStruct readStructBegin() throws TException {
            scopeStack.push(rows.pop());
            return new TStruct();
        }

        protected TProtocol _createRow(final String[] columnNames,
                final String[] columnValues) {
            return new Row(columnNames, columnValues);
        }

        private final Stack<TProtocol> rows;
    }

    public CsvProtocol(final Reader reader) {
        final CSVReader csvReader = new CSVReader(reader);
        List<String[]> rows;
        try {
            try {
                rows = csvReader.readAll();
            } catch (final IOException e) {
                rows = Lists.newArrayList();
            }
        } finally {
            try {
                csvReader.close();
            } catch (final IOException e) {
            }
        }

        scopeStack.push(_createFile(rows));
    }

    @Override
    public boolean readBool() throws TException {
        return readString().equals("1");
    }

    @Override
    public byte readByte() throws TException {
        return Byte.parseByte(readString());
    }

    @Override
    public double readDouble() throws TException {
        return Double.parseDouble(readString());
    }

    @Override
    public TField readFieldBegin() throws TException {
        return scopeStack.peek().readFieldBegin();
    }

    @Override
    public void readFieldEnd() throws TException {
        scopeStack.peek().readFieldEnd();
    }

    @Override
    public short readI16() throws TException {
        return Short.parseShort(readString());
    }

    @Override
    public int readI32() throws TException {
        return Integer.parseInt(readString());
    }

    @Override
    public long readI64() throws TException {
        final String value = readString();
        try {
            return Long.parseLong(value);
        } catch (final NumberFormatException e) {
            return dateTimeFormatter.parseMillis(value);
        }
    }

    @Override
    public TList readListBegin() throws TException {
        return scopeStack.peek().readListBegin();
    }

    @Override
    public void readListEnd() throws TException {
        scopeStack.pop();
    }

    @Override
    public String readString() throws TException {
        return scopeStack.peek().readString();
    }

    @Override
    public TStruct readStructBegin() throws TException {
        return scopeStack.peek().readStructBegin();
    }

    @Override
    public void readStructEnd() throws TException {
        scopeStack.pop();
    }

    protected TProtocol _createFile(final List<String[]> rows) {
        return new File(rows);
    }

    private final static DateTimeFormatter dateTimeFormatter = DateTimeFormat
            .forPattern("yyyy-MM-dd HH:mm:ss");
    protected final Stack<TProtocol> scopeStack = new Stack<TProtocol>();
}