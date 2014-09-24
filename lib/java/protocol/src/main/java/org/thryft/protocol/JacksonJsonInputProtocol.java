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

import static com.google.common.base.Preconditions.checkNotNull;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.StringReader;
import java.util.Iterator;
import java.util.Stack;

import org.apache.commons.codec.binary.Base64;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.TextNode;
import com.google.common.annotations.GwtIncompatible;

@GwtIncompatible("")
public final class JacksonJsonInputProtocol extends
        JsonInputProtocol<JacksonJsonInputProtocol.NestedInputProtocol> {
    public abstract class NestedInputProtocol extends AbstractInputProtocol {
        private NestedInputProtocol(final JsonNode node) {
            myNode = node;
        }

        public abstract Type getType();

        @Override
        public byte[] readBinary() throws InputProtocolException {
            return Base64.decodeBase64(readString());
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
            _getInputProtocolStack().push(__createArrayInputProtocol(node));
            return new ListBegin(Type.VOID_, node.size());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            final JsonNode node = _readChildNode();
            if (!node.isObject()) {
                throw new InputProtocolException("expected JSON object");
            }
            _getInputProtocolStack().push(__createMapObjectInputProtocol(node));
            return new MapBegin(Type.VOID_, Type.VOID_, node.size());
        }

        @Override
        public Object readVariant() throws InputProtocolException {
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
            _getInputProtocolStack().push(
                    __createStructObjectInputProtocol(node));
            return "";
        }

        protected JsonNode _getMyNode() {
            return myNode;
        }

        protected abstract JsonNode _readChildNode();

        private final JsonNode myNode;
    }

    private final class ArrayInputProtocol extends NestedInputProtocol {
        public ArrayInputProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        public Type getType() {
            return Type.LIST;
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode().get(nextValueIndex++);
        }

        private int nextValueIndex = 0;
    }

    private final class MapObjectInputProtocol extends NestedInputProtocol {
        public MapObjectInputProtocol(final JsonNode node) {
            super(node);
            for (final Iterator<String> fieldName = node.fieldNames(); fieldName
                    .hasNext();) {
                fieldNameStack.add(fieldName.next());
            }
        }

        @Override
        public Type getType() {
            return Type.MAP;
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

    private final class RootInputProtocol extends NestedInputProtocol {
        private RootInputProtocol(final JsonNode node) {
            super(node);
        }

        @Override
        public Type getType() {
            throw new UnsupportedOperationException();
        }

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode();
        }
    }

    private final class StructObjectInputProtocol extends NestedInputProtocol {
        public StructObjectInputProtocol(final JsonNode node) {
            super(node);
            for (final Iterator<String> fieldName = node.fieldNames(); fieldName
                    .hasNext();) {
                fieldNameStack.add(fieldName.next());
            }
        }

        @Override
        public Type getType() {
            return Type.STRUCT;
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
                    type = Type.VOID_;
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

        @Override
        protected JsonNode _readChildNode() {
            return _getMyNode().get(fieldNameStack.peek());
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
    }

    private static JsonNode __readTree(final Reader reader)
            throws InputProtocolException {
        try {
            return new ObjectMapper().readTree(reader);
        } catch (final IOException e) {
            throw new InputProtocolException(e);
        }
    }

    public JacksonJsonInputProtocol(final InputStream inputStream)
            throws InputProtocolException {
        this(new InputStreamReader(inputStream));
    }

    public JacksonJsonInputProtocol(final JsonNode rootNode) {
        this.rootNode = checkNotNull(rootNode);
        _getInputProtocolStack().push(__createRootInputProtocol(rootNode));
    }

    public JacksonJsonInputProtocol(final Reader reader)
            throws InputProtocolException {
        this(__readTree(reader));
    }

    public JacksonJsonInputProtocol(final String json)
            throws InputProtocolException {
        this(new StringReader(json));
    }

    @Override
    public Type getCurrentFieldType() {
        return _getInputProtocolStack().peek().getType();
    }

    @Override
    public void reset() {
        _getInputProtocolStack().clear();
        _getInputProtocolStack().push(__createRootInputProtocol(rootNode));
    }

    private ArrayInputProtocol __createArrayInputProtocol(final JsonNode node) {
        return new ArrayInputProtocol(node);
    }

    private MapObjectInputProtocol __createMapObjectInputProtocol(
            final JsonNode node) {
        return new MapObjectInputProtocol(node);
    }

    private RootInputProtocol __createRootInputProtocol(final JsonNode rootNode) {
        return new RootInputProtocol(rootNode);
    }

    private StructObjectInputProtocol __createStructObjectInputProtocol(
            final JsonNode node) {
        return new StructObjectInputProtocol(node);
    }

    private final JsonNode rootNode;
}
