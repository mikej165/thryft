package org.thryft.protocol;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
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
        protected JsonNode _readNode() {
            return node.get(nextValueIndex++);
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
        protected JsonNode _readNode() {
            if (nextReadIsKey) {
                nextReadIsKey = false;
                return new TextNode(fieldNameStack.peek());
            } else {
                nextReadIsKey = true;
                return node.get(fieldNameStack.pop());
            }
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
        private boolean nextReadIsKey = true;
    }

    protected class MapObjectWriterProtocol extends WriterProtocol {
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

        private boolean nextWriteIsKey = true;
    }

    protected abstract class ReaderProtocol extends Protocol {
        protected ReaderProtocol(final JsonNode node) {
            this.node = node;
        }

        @Override
        public boolean readBool() throws TException {
            return _readNode().asBoolean();
        }

        @Override
        public byte readByte() throws TException {
            return (byte) _readNode().asInt();
        }

        @Override
        public double readDouble() throws TException {
            return _readNode().asDouble();
        }

        @Override
        public short readI16() throws TException {
            return (short) _readNode().asInt();
        }

        @Override
        public int readI32() throws TException {
            return _readNode().asInt();
        }

        @Override
        public long readI64() throws TException {
            return _readNode().asLong();
        }

        @Override
        public TList readListBegin() throws TException {
            final JsonNode node = _readNode();
            if (!node.isArray()) {
                throw new TException("expected JSON array");
            }
            _getProtocolStack().push(_createArrayReaderProtocol(node));
            return new TList(TType.VOID, node.size());
        }

        @Override
        public TMap readMapBegin() throws TException {
            final JsonNode node = _readNode();
            if (!node.isObject()) {
                throw new TException("expected JSON object");
            }
            _getProtocolStack().push(_createMapObjectReaderProtocol(node));
            return new TMap(TType.VOID, TType.VOID, node.size());
        }

        @Override
        public String readString() throws TException {
            return _readNode().asText();
        }

        @Override
        public TStruct readStructBegin() throws TException {
            final JsonNode node = _readNode();
            if (!node.isObject()) {
                throw new TException("expected JSON object");
            }
            _getProtocolStack().push(_createStructObjectReaderProtocol(node));
            return new TStruct();
        }

        protected Protocol _createArrayReaderProtocol(final JsonNode node) {
            return new ArrayReaderProtocol(node);
        }

        protected Protocol _createMapObjectReaderProtocol(final JsonNode node) {
            return new MapObjectReaderProtocol(node);
        }

        protected Protocol _createStructObjectReaderProtocol(final JsonNode node) {
            return new StructObjectReaderProtocol(node);
        }

        protected abstract JsonNode _readNode();

        protected final JsonNode node;

    }

    protected class RootReaderProtocol extends ReaderProtocol {
        protected RootReaderProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        protected JsonNode _readNode() {
            return node;
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

        @Override
        protected JsonNode _readNode() {
            return node.get(fieldNameStack.peek());
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
                _getProtocolStack().pop();
                generator.writeEndObject();
            } catch (final IOException e) {
                throw new TException(e);
            }
        }

        @Override
        public void writeMixed(final Object value) throws TException {
            if (value == null) {
                try {
                    generator.writeNull();
                } catch (final IOException e) {
                    throw new TException(e);
                }
            } else {
                super.writeMixed(value);
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

        protected Protocol _createArrayWriterProtocol() {
            return new ArrayWriterProtocol();
        }

        protected Protocol _createMapObjectWriterProtocol() {
            return new MapObjectWriterProtocol();
        }

        protected Protocol _createStructObjectWriterProtocol() {
            return new StructObjectWriterProtocol();
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

    public JsonProtocol(final Writer writer) throws IOException {
        this(new JsonFactory().createJsonGenerator(writer));
    }

    @Override
    public void flush() throws IOException {
        generator.flush();
    }

    protected Protocol _createRootReaderProtocol(final JsonNode parsedTree) {
        return new RootReaderProtocol(parsedTree);
    }

    protected Protocol _createRootWriterProtocol() {
        return new RootWriterProtocol();
    }

    private final JsonGenerator generator;
}