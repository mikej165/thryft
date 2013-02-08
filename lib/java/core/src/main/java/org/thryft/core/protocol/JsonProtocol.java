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

package org.thryft.core.protocol;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.StringReader;
import java.io.Writer;
import java.util.Iterator;
import java.util.Stack;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TStruct;
import org.apache.thrift.protocol.TType;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.TextNode;

public class JsonProtocol extends StackedProtocol {
    protected class ArrayReaderProtocol extends ReaderProtocol {
        public ArrayReaderProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode().get(nextValueIndex++);
        }

        private int nextValueIndex = 0;
    }

    protected class ArrayWriterProtocol extends WriterProtocol {
    }

    protected class MapObjectReaderProtocol extends ReaderProtocol {
        public MapObjectReaderProtocol(final JsonNode node) {
            super(node);
            for (final Iterator<String> fieldName = node.fieldNames(); fieldName
                    .hasNext();) {
                fieldNameStack.add(fieldName.next());
            }
        }

        @Override
        protected JsonNode _readChildNode() {
            if (nextReadIsKey) {
                nextReadIsKey = false;
                return new TextNode(fieldNameStack.peek());
            } else {
                nextReadIsKey = true;
                return _getMyNode().get(fieldNameStack.pop());
            }
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
        private boolean nextReadIsKey = true;
    }

    protected class MapObjectWriterProtocol extends WriterProtocol {
        @Override
        public void writeBool(final boolean b) throws TException {
            if (nextWriteIsKey) {
                writeString(Boolean.toString(b));
            } else {
                nextWriteIsKey = true;
                super.writeBool(b);
            }
        }

        @Override
        public void writeByte(final byte b) throws TException {
            if (nextWriteIsKey) {
                writeString(Byte.toString(b));
            } else {
                nextWriteIsKey = true;
                super.writeByte(b);
            }
        }

        @Override
        public void writeDouble(final double dub) throws TException {
            if (nextWriteIsKey) {
                writeString(Double.toString(dub));
            } else {
                nextWriteIsKey = true;
                super.writeDouble(dub);
            }
        }

        @Override
        public void writeI16(final short i16) throws TException {
            if (nextWriteIsKey) {
                writeString(Short.toString(i16));
            } else {
                nextWriteIsKey = true;
                super.writeI16(i16);
            }
        }

        @Override
        public void writeI32(final int i32) throws TException {
            if (nextWriteIsKey) {
                writeString(Integer.toString(i32));
            } else {
                nextWriteIsKey = true;
                super.writeI32(i32);
            }
        }

        @Override
        public void writeI64(final long i64) throws TException {
            if (nextWriteIsKey) {
                writeString(Long.toString(i64));
            } else {
                nextWriteIsKey = true;
                super.writeI64(i64);
            }
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeListBegin(list);
            }
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeMapBegin(map);
            }
        }

        @Override
        public void writeNull() throws TException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeNull();
            }
        }

        @Override
        public void writeString(final String str) throws TException {
            if (nextWriteIsKey) {
                nextWriteIsKey = false;
                try {
                    generator.writeFieldName(str);
                } catch (final IOException e) {
                    throw new TException(e);
                }
            } else {
                nextWriteIsKey = true;
                super.writeString(str);
            }
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            if (nextWriteIsKey) {
                throw new UnsupportedOperationException();
            } else {
                nextWriteIsKey = true;
                super.writeStructBegin(struct);
            }
        }

        private boolean nextWriteIsKey = true;
    }

    protected abstract class ReaderProtocol extends Protocol {
        protected ReaderProtocol(final JsonNode node) {
            myNode = node;
        }

        @Override
        public boolean readBool() throws TException {
            return _readChildNode().asBoolean();
        }

        @Override
        public byte readByte() throws TException {
            return (byte) _readChildNode().asInt();
        }

        @Override
        public double readDouble() throws TException {
            return _readChildNode().asDouble();
        }

        @Override
        public short readI16() throws TException {
            return (short) _readChildNode().asInt();
        }

        @Override
        public int readI32() throws TException {
            return _readChildNode().asInt();
        }

        @Override
        public long readI64() throws TException {
            return _readChildNode().asLong();
        }

        @Override
        public TList readListBegin() throws TException {
            final JsonNode node = _readChildNode();
            if (!node.isArray()) {
                throw new TException("expected JSON array");
            }
            _getProtocolStack().push(_createArrayReaderProtocol(node));
            return new TList(TType.VOID, node.size());
        }

        @Override
        public TMap readMapBegin() throws TException {
            final JsonNode node = _readChildNode();
            if (!node.isObject()) {
                throw new TException("expected JSON object");
            }
            _getProtocolStack().push(_createMapObjectReaderProtocol(node));
            return new TMap(TType.VOID, TType.VOID, node.size());
        }

        @Override
        public String readString() throws TException {
            return _readChildNode().asText();
        }

        @Override
        public TStruct readStructBegin() throws TException {
            final JsonNode node = _readChildNode();
            if (!node.isObject()) {
                throw new TException("expected JSON object");
            }
            _getProtocolStack().push(_createStructObjectReaderProtocol(node));
            return new TStruct();
        }

        protected JsonNode _getMyNode() {
            return myNode;
        }

        protected abstract JsonNode _readChildNode();

        private final JsonNode myNode;
    }

    protected class RootReaderProtocol extends ReaderProtocol {
        protected RootReaderProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode();
        }
    }

    protected class RootWriterProtocol extends WriterProtocol {
        @Override
        public void writeFieldEnd() throws TException {
        }

        @Override
        public void writeFieldStop() throws TException {
        }
    }

    protected class StructObjectReaderProtocol extends ReaderProtocol {
        public StructObjectReaderProtocol(final JsonNode node) {
            super(node);
            for (final Iterator<String> fieldName = node.fieldNames(); fieldName
                    .hasNext();) {
                fieldNameStack.add(fieldName.next());
            }
        }

        @Override
        public TField readFieldBegin() throws TException {
            if (!fieldNameStack.isEmpty()) {
                return new TField(fieldNameStack.peek(), TType.VOID, (short) -1);
            } else {
                return new TField();
            }
        }

        @Override
        public void readFieldEnd() throws TException {
            fieldNameStack.pop();
        }

        protected final Stack<String> _getFieldNameStack() {
            return fieldNameStack;
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode().get(fieldNameStack.peek());
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
    }

    protected class StructObjectWriterProtocol extends WriterProtocol {
        @Override
        public void writeFieldBegin(final TField field) throws TException {
            try {
                generator.writeFieldName(field.name);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeFieldEnd() throws TException {
        }

        @Override
        public void writeFieldStop() throws TException {
        }
    }

    protected abstract class WriterProtocol extends Protocol {
        @Override
        public void writeBool(final boolean b) throws TException {
            try {
                generator.writeBoolean(b);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeByte(final byte b) throws TException {
            try {
                generator.writeNumber(b);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeDouble(final double dub) throws TException {
            try {
                generator.writeNumber(dub);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeI16(final short i16) throws TException {
            try {
                generator.writeNumber(i16);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeI32(final int i32) throws TException {
            try {
                generator.writeNumber(i32);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeI64(final long i64) throws TException {
            try {
                generator.writeNumber(i64);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            try {
                generator.writeStartArray();
                _getProtocolStack().push(_createArrayWriterProtocol());
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeListEnd() throws TException {
            try {
                generator.writeEndArray();
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            try {
                generator.writeStartObject();
                _getProtocolStack().push(_createMapObjectWriterProtocol());
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeMapEnd() throws TException {
            try {
                generator.writeEndObject();
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeNull() throws TException {
            try {
                generator.writeNull();
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeString(final String str) throws TException {
            try {
                generator.writeString(str);
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            try {
                generator.writeStartObject();
                _getProtocolStack().push(_createStructObjectWriterProtocol());
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeStructEnd() throws TException {
            try {
                generator.writeEndObject();
            } catch (final IOException e) {
                throw new TException(e);
            }
        }
    }

    public JsonProtocol(final InputStream inputStream) throws IOException {
        this(new InputStreamReader(inputStream));
    }

    public JsonProtocol(final JsonGenerator generator) {
        this.generator = generator;
        _getProtocolStack().push(_createRootWriterProtocol());
    }

    public JsonProtocol(final JsonNode parsedTree) {
        generator = null;
        _getProtocolStack().push(_createRootReaderProtocol(parsedTree));
    }

    public JsonProtocol(final OutputStream outputStream) throws IOException {
        this(new OutputStreamWriter(outputStream));
    }

    public JsonProtocol(final Reader reader) throws IOException,
            JsonParseException {
        this(new ObjectMapper().readTree(reader));
    }

    public JsonProtocol(final String json) throws IOException {
        this(new StringReader(json));
    }

    public JsonProtocol(final Writer writer) throws IOException {
        this(new JsonFactory().createJsonGenerator(writer));
    }

    @Override
    public void flush() throws IOException {
        generator.flush();
    }

    protected Protocol _createArrayReaderProtocol(final JsonNode node) {
        return new ArrayReaderProtocol(node);
    }

    protected Protocol _createArrayWriterProtocol() {
        return new ArrayWriterProtocol();
    }

    protected Protocol _createMapObjectReaderProtocol(final JsonNode node) {
        return new MapObjectReaderProtocol(node);
    }

    protected Protocol _createMapObjectWriterProtocol() {
        return new MapObjectWriterProtocol();
    }

    protected Protocol _createRootReaderProtocol(final JsonNode parsedTree) {
        return new RootReaderProtocol(parsedTree);
    }

    protected Protocol _createRootWriterProtocol() {
        return new RootWriterProtocol();
    }

    protected Protocol _createStructObjectReaderProtocol(final JsonNode node) {
        return new StructObjectReaderProtocol(node);
    }

    protected Protocol _createStructObjectWriterProtocol() {
        return new StructObjectWriterProtocol();
    }

    private final JsonGenerator generator;
}
