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
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.StringReader;
import java.util.Iterator;
import java.util.Stack;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.TextNode;
import com.google.common.annotations.GwtIncompatible;

@GwtIncompatible("")
public class JsonInputProtocol extends StackedInputProtocol {
    protected abstract class AbstractInputProtocol extends
            org.thryft.protocol.AbstractInputProtocol {
        protected AbstractInputProtocol(final JsonNode node) {
            myNode = node;
        }

        @Override
        public boolean readBool() throws InputProtocolException {
            return _readChildNode().asBoolean();
        }

        @Override
        public byte readByte() throws InputProtocolException {
            return (byte) _readChildNode().asInt();
        }

        @Override
        public double readDouble() throws InputProtocolException {
            return _readChildNode().asDouble();
        }

        @Override
        public short readI16() throws InputProtocolException {
            return (short) _readChildNode().asInt();
        }

        @Override
        public int readI32() throws InputProtocolException {
            return _readChildNode().asInt();
        }

        @Override
        public long readI64() throws InputProtocolException {
            return _readChildNode().asLong();
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            final JsonNode node = _readChildNode();
            if (!node.isArray()) {
                throw new InputProtocolException("expected JSON array");
            }
            _getProtocolStack().push(_createArrayInputProtocol(node));
            return new ListBegin(Type.VOID, node.size());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            final JsonNode node = _readChildNode();
            if (!node.isObject()) {
                throw new InputProtocolException("expected JSON object");
            }
            _getProtocolStack().push(_createMapObjectInputProtocol(node));
            return new MapBegin(Type.VOID, Type.VOID, node.size());
        }

        @Override
        public Object readMixed() throws InputProtocolException {
            final JsonNode value = _readChildNode();
            if (value.isBoolean()) {
                return value.asBoolean();
            } else if (value.isDouble()) {
                return value.asDouble();
            } else if (value.isInt()) {
                return value.asInt();
            } else if (value.isLong()) {
                return value.asLong();
            } else if (value.isTextual()) {
                return value.asText();
            } else {
                throw new UnsupportedOperationException();
            }
        }

        @Override
        public String readString() throws InputProtocolException {
            return _readChildNode().asText();
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            final JsonNode node = _readChildNode();
            if (!node.isObject()) {
                throw new InputProtocolException("expected JSON object");
            }
            _getProtocolStack().push(_createStructObjectInputProtocol(node));
            return "";
        }

        protected JsonNode _getMyNode() {
            return myNode;
        }

        protected abstract JsonNode _readChildNode();

        private final JsonNode myNode;
    }

    protected class ArrayInputProtocol extends AbstractInputProtocol {
        public ArrayInputProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode().get(nextValueIndex++);
        }

        private int nextValueIndex = 0;
    }

    protected class MapObjectInputProtocol extends AbstractInputProtocol {
        public MapObjectInputProtocol(final JsonNode node) {
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

    protected class RootInputProtocol extends AbstractInputProtocol {
        protected RootInputProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode();
        }
    }

    protected class StructObjectInputProtocol extends AbstractInputProtocol {
        public StructObjectInputProtocol(final JsonNode node) {
            super(node);
            for (final Iterator<String> fieldName = node.fieldNames(); fieldName
                    .hasNext();) {
                fieldNameStack.add(fieldName.next());
            }
        }

        @Override
        public FieldBegin readFieldBegin() throws InputProtocolException {
            if (!fieldNameStack.isEmpty()) {
                final JsonNode value = _getMyNode().get(fieldNameStack.peek());
                Type type;
                if (value.isArray()) {
                    type = Type.LIST;
                } else if (value.isBoolean()) {
                    type = Type.BOOL;
                } else if (value.isDouble()) {
                    type = Type.DOUBLE;
                } else if (value.isInt()) {
                    type = Type.I32;
                } else if (value.isLong()) {
                    type = Type.I64;
                } else if (value.isObject()) {
                    type = Type.STRUCT;
                } else if (value.isTextual()) {
                    type = Type.STRING;
                } else {
                    type = Type.VOID;
                }
                return new FieldBegin(fieldNameStack.peek(), type, (short) -1);
            } else {
                return new FieldBegin();
            }
        }

        @Override
        public void readFieldEnd() throws InputProtocolException {
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

    public JsonInputProtocol(final InputStream inputStream) throws IOException {
        this(new InputStreamReader(inputStream));
    }

    public JsonInputProtocol(final JsonNode parsedTree) {
        _getProtocolStack().push(_createRootInputProtocol(parsedTree));
    }

    public JsonInputProtocol(final Reader reader) throws IOException,
            JsonParseException {
        this(new ObjectMapper().readTree(reader));
    }

    public JsonInputProtocol(final String json) throws IOException {
        this(new StringReader(json));
    }

    protected InputProtocol _createArrayInputProtocol(final JsonNode node) {
        return new ArrayInputProtocol(node);
    }

    protected InputProtocol _createMapObjectInputProtocol(final JsonNode node) {
        return new MapObjectInputProtocol(node);
    }

    protected InputProtocol _createRootInputProtocol(final JsonNode parsedTree) {
        return new RootInputProtocol(parsedTree);
    }

    protected InputProtocol _createStructObjectInputProtocol(final JsonNode node) {
        return new StructObjectInputProtocol(node);
    }
}
