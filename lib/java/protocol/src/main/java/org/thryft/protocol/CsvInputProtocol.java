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
import java.io.Reader;
import java.io.StringReader;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

import au.com.bytecode.opencsv.CSVReader;

import com.google.common.base.Optional;
import com.google.common.collect.Lists;

public class CsvInputProtocol extends StackedInputProtocol {
    protected abstract class AbstractInputProtocol extends
            org.thryft.protocol.AbstractInputProtocol {
        @Override
        public boolean readBool() throws InputProtocolException {
            return readString().equals("1");
        }

        @Override
        public byte readByte() throws InputProtocolException {
            return Byte.parseByte(readString());
        }

        @Override
        public double readDouble() throws InputProtocolException {
            return Double.parseDouble(readString());
        }

        @Override
        public short readI16() throws InputProtocolException {
            return Short.parseShort(readString());
        }

        @Override
        public int readI32() throws InputProtocolException {
            return Integer.parseInt(readString());
        }

        @Override
        public long readI64() throws InputProtocolException {
            final String value = readString();
            try {
                return Long.parseLong(value);
            } catch (final NumberFormatException e) {
                try {
                    return dateTimeFormat.parse(value).getTime();
                } catch (final ParseException e1) {
                    throw new InputProtocolException(e1);
                }
            }
        }
    }

    protected class FileInputProtocol extends AbstractInputProtocol {
        protected class RowInputProtocol extends AbstractInputProtocol {
            protected class SequenceColumnInputProtocol extends
                    AbstractInputProtocol {
                public SequenceColumnInputProtocol(final String[] elements) {
                    this.elements = elements;
                    currentElementI = 0;
                }

                @Override
                public ListBegin readListBegin() throws InputProtocolException {
                    throw new IllegalStateException();
                }

                @Override
                public String readString() throws InputProtocolException {
                    return elements[currentElementI++];
                }

                private int currentElementI;
                private final String[] elements;
            }

            public RowInputProtocol(final String[] columnNames,
                    final String[] columnValues) {
                this.columnNames = columnNames;
                this.columnValues = columnValues;
                currentColumnI = 0;
            }

            @Override
            public FieldBegin readFieldBegin() throws InputProtocolException {
                if (currentColumnI < columnValues.length) {
                    return _readFieldBegin();
                } else {
                    return new FieldBegin();
                }
            }

            @Override
            public void readFieldEnd() {
                currentColumnI++;
            }

            @Override
            public ListBegin readListBegin() throws InputProtocolException {
                return _readListBegin(readString());
            }

            @Override
            public String readString() {
                return _getCurrentColumnValue();
            }

            @Override
            public StructBegin readStructBegin() {
                // Assume a struct will read inline
                _getProtocolStack().push(this);
                return new StructBegin();
            }

            protected InputProtocol _createSequenceColumn(
                    final String[] elements) {
                return new SequenceColumnInputProtocol(elements);
            }

            protected String _getCurrentColumnName() {
                return columnNames[currentColumnI];
            }

            protected String _getCurrentColumnValue() {
                return columnValues[currentColumnI];
            }

            protected FieldBegin _readFieldBegin()
                    throws InputProtocolException {
                return new FieldBegin(_getCurrentColumnName(), Type.STRING,
                        (short) 0);
            }

            protected ListBegin _readListBegin(final String list)
                    throws InputProtocolException {
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
                    }
                }
                _getProtocolStack().push(_createSequenceColumn(listElements));
                return new ListBegin(Type.STRING, 0);
            }

            protected Optional<String> _readString(final String columnName) {
                for (int columnI = 0; columnI < columnNames.length; columnI++) {
                    if (columnNames[columnI].equals(columnName)) {
                        return Optional.of(columnValues[columnI]);
                    }
                }

                return Optional.absent();
            }

            private int currentColumnI;
            private final String[] columnNames;
            private final String[] columnValues;
        }

        public FileInputProtocol(final List<String[]> rows) {
            this.rows = new Stack<InputProtocol>();
            Collections.reverse(rows);
            final String[] columnNames = rows.remove(rows.size() - 1);
            for (final String[] row : rows) {
                this.rows.push(_createRowInputProtocol(columnNames, row));
            }
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            return new ListBegin(Type.STRUCT, rows.size());
        }

        @Override
        public String readString() throws InputProtocolException {
            throw new IllegalStateException();
        }

        @Override
        public StructBegin readStructBegin() throws InputProtocolException {
            _getProtocolStack().push(rows.pop());
            return new StructBegin();
        }

        protected InputProtocol _createRowInputProtocol(
                final String[] columnNames, final String[] columnValues) {
            return new RowInputProtocol(columnNames, columnValues);
        }

        private final Stack<InputProtocol> rows;
    }

    public CsvInputProtocol(final Reader reader) {
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

        _getProtocolStack().add(_createFileInputProtocol(rows));
    }

    protected InputProtocol _createFileInputProtocol(final List<String[]> rows) {
        return new FileInputProtocol(rows);
    }

    private final static DateFormat dateTimeFormat = new SimpleDateFormat(
            "yyyy-MM-dd HH:mm:ss");
}
