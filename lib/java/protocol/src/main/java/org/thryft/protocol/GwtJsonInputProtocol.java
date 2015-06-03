/*******************************************************************************
 * Copyright (c) 2015, Minor Gordon
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
import java.util.Stack;

import org.thryft.protocol.GwtJsonInputProtocol.NestedInputProtocol;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.json.client.JSONBoolean;
import com.google.gwt.json.client.JSONNumber;
import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONParser;
import com.google.gwt.json.client.JSONString;
import com.google.gwt.json.client.JSONValue;
import com.googlecode.gwt.crypto.bouncycastle.util.encoders.Base64;

public class GwtJsonInputProtocol extends
        JsonInputProtocol<NestedInputProtocol<?>> {
    abstract class NestedInputProtocol<JSONValueT extends JSONValue>
            extends
            JsonInputProtocol<NestedInputProtocol<JSONValueT>>.NestedInputProtocol {
        protected NestedInputProtocol(final JSONValueT node) {
            myNode = node;
        }

        @Override
        public boolean readBool() throws InputProtocolException {
            return _readChildNode().isBoolean().booleanValue();
        }

        @Override
        public double readDouble() throws InputProtocolException {
            return _readChildNode().isNumber().doubleValue();
        }

        @Override
        public int readI32() throws InputProtocolException {
            return (int) _readChildNode().isNumber().doubleValue();
        }

        @Override
        public long readI64() throws InputProtocolException {
            return (long) _readChildNode().isNumber().doubleValue();
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            final JSONArray node = _readChildNode().isArray();
            if (node == null) {
                throw new InputProtocolException("expected JSON array");
            }
            _getInputProtocolStack().push(new ArrayInputProtocol(node));
            return new ListBegin(Type.VOID_, node.size());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            final JSONObject node = _readChildNode().isObject();
            if (node == null) {
                throw new InputProtocolException("expected JSON object");
            }
            _getInputProtocolStack().push(new MapObjectInputProtocol(node));
            return new MapBegin(Type.VOID_, Type.VOID_, node.size());
        }

        @Override
        public String readString() throws InputProtocolException {
            return _readChildNode().isString().stringValue();
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            final JSONObject node = _readChildNode().isObject();
            if (node == null) {
                throw new InputProtocolException("expected JSON object");
            }
            _getInputProtocolStack().push(new StructObjectInputProtocol(node));
            return "";
        }

        @Override
        public Object readVariant() throws InputProtocolException {
            final JSONValue node = _readChildNode();
            if (node.isBoolean() != null) {
                return ((JSONBoolean) node).booleanValue();
            } else if (node.isNumber() != null) {
                return ((JSONNumber) node).doubleValue();
            } else if (node.isString() != null) {
                return ((JSONString) node).stringValue();
            } else {
                throw new UnsupportedOperationException();
            }
        }

        @Override
        protected byte[] _decodeBase64(final String base64String) {
            return Base64.decode(base64String);
        }

        protected final JSONValueT _getMyNode() {
            return myNode;
        }

        protected abstract JSONValue _readChildNode();

        private final JSONValueT myNode;
    }

    private final class ArrayInputProtocol extends
            NestedInputProtocol<JSONArray> {
        public ArrayInputProtocol(final JSONArray node) {
            super(node);
        }

        @Override
        public Type getType() {
            return Type.LIST;
        }

        @Override
        protected JSONValue _readChildNode() {
            return _getMyNode().get(nextValueIndex++);
        }

        private int nextValueIndex = 0;
    }

    private final class MapObjectInputProtocol extends
            NestedInputProtocol<JSONObject> {
        public MapObjectInputProtocol(final JSONObject node) {
            super(node);
            fieldNameStack.addAll(node.keySet());
        }

        @Override
        public Type getType() {
            return Type.MAP;
        }

        @Override
        protected JSONValue _readChildNode() {
            if (nextReadIsKey) {
                nextReadIsKey = false;
                return new JSONString(fieldNameStack.peek());
            } else {
                nextReadIsKey = true;
                return _getMyNode().get(fieldNameStack.pop());
            }
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
        private boolean nextReadIsKey = true;
    }

    private final class RootInputProtocol extends
            NestedInputProtocol<JSONValue> {
        protected RootInputProtocol(final JSONValue node) {
            super(node);
        }

        @Override
        public Type getType() {
            throw new UnsupportedOperationException();
        }

        @Override
        protected JSONValue _readChildNode() {
            return _getMyNode();
        }
    }

    private final class StructObjectInputProtocol extends
            NestedInputProtocol<JSONObject> {
        public StructObjectInputProtocol(final JSONObject node) {
            super(node);
            fieldNameStack.addAll(node.keySet());
        }

        @Override
        public Type getType() {
            return Type.STRUCT;
        }

        @Override
        public FieldBegin readFieldBegin() throws InputProtocolException {
            if (!fieldNameStack.isEmpty()) {
                return new FieldBegin(fieldNameStack.peek(), Type.VOID_,
                        (short) -1);
            } else {
                return FieldBegin.STOP;
            }
        }

        @Override
        public void readFieldEnd() throws InputProtocolException {
            fieldNameStack.pop();
        }

        @Override
        protected JSONValue _readChildNode() {
            return _getMyNode().get(fieldNameStack.peek());
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
    }

    public GwtJsonInputProtocol(final JSONValue rootNode) {
        this.rootNode = checkNotNull(rootNode);
        _getInputProtocolStack().push(new RootInputProtocol(rootNode));
    }

    public GwtJsonInputProtocol(final String json) throws IOException {
        this(JSONParser.parseStrict(json));
    }

    @Override
    public void reset() {
        _getInputProtocolStack().clear();
        _getInputProtocolStack().push(new RootInputProtocol(rootNode));
    }

    private final JSONValue rootNode;
}
