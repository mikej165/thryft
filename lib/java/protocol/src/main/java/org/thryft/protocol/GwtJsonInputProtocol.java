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
import java.util.Stack;

import com.google.gwt.json.client.JSONArray;
import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONParser;
import com.google.gwt.json.client.JSONString;
import com.google.gwt.json.client.JSONValue;

public class GwtJsonInputProtocol extends StackedInputProtocol {
    protected abstract class AbstractInputProtocol extends
            org.thryft.protocol.AbstractInputProtocol {
        protected AbstractInputProtocol(final JSONValue node) {
            myNode = node;
        }

        @Override
        public boolean readBool() throws InputProtocolException {
            return _readChildNode().isBoolean().booleanValue();
        }

        @Override
        public byte readByte() throws InputProtocolException {
            return (byte) _readChildNode().isNumber().doubleValue();
        }

        @Override
        public double readDouble() throws InputProtocolException {
            return _readChildNode().isNumber().doubleValue();
        }

        @Override
        public short readI16() throws InputProtocolException {
            return (short) _readChildNode().isNumber().doubleValue();
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
            _getProtocolStack().push(_createArrayInputProtocol(node));
            return new ListBegin(Type.VOID, node.size());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            final JSONObject node = _readChildNode().isObject();
            if (node == null) {
                throw new InputProtocolException("expected JSON object");
            }
            _getProtocolStack().push(_createMapObjectInputProtocol(node));
            return new MapBegin(Type.VOID, Type.VOID, node.size());
        }

        @Override
        public Object readMixed() throws InputProtocolException {
            throw new UnsupportedOperationException();
        }

        @Override
        public String readString() throws InputProtocolException {
            return _readChildNode().isString().stringValue();
        }

        @Override
        public StructBegin readStructBegin() throws InputProtocolException {
            final JSONObject node = _readChildNode().isObject();
            if (node == null) {
                throw new InputProtocolException("expected JSON object");
            }
            _getProtocolStack().push(_createStructObjectInputProtocol(node));
            return new StructBegin();
        }

        protected JSONValue _getMyNode() {
            return myNode;
        }

        protected abstract JSONValue _readChildNode();

        private final JSONValue myNode;
    }

    protected class ArrayInputProtocol extends AbstractInputProtocol {
        public ArrayInputProtocol(final JSONArray node) {
            super(node);
        }

        @Override
        protected JSONArray _getMyNode() {
            return (JSONArray) super._getMyNode();
        }

        @Override
        protected JSONValue _readChildNode() {
            return _getMyNode().get(nextValueIndex++);
        }

        private int nextValueIndex = 0;
    }

    protected class MapObjectInputProtocol extends AbstractInputProtocol {
        public MapObjectInputProtocol(final JSONObject node) {
            super(node);
            fieldNameStack.addAll(node.keySet());
        }

        @Override
        protected JSONObject _getMyNode() {
            return (JSONObject) super._getMyNode();
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

    protected class RootInputProtocol extends AbstractInputProtocol {
        protected RootInputProtocol(final JSONValue node) {
            super(node);
        }

        @Override
        protected JSONValue _readChildNode() {
            return _getMyNode();
        }
    }

    protected class StructObjectInputProtocol extends AbstractInputProtocol {
        public StructObjectInputProtocol(final JSONObject node) {
            super(node);
            fieldNameStack.addAll(node.keySet());
        }

        @Override
        public FieldBegin readFieldBegin() throws InputProtocolException {
            if (!fieldNameStack.isEmpty()) {
                return new FieldBegin(fieldNameStack.peek(), Type.VOID,
                        (short) -1);
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
        protected JSONObject _getMyNode() {
            return (JSONObject) super._getMyNode();
        }

        @Override
        protected JSONValue _readChildNode() {
            return _getMyNode().get(fieldNameStack.peek());
        }

        private final Stack<String> fieldNameStack = new Stack<String>();
    }

    public GwtJsonInputProtocol(final JSONValue node) {
        _getProtocolStack().push(_createRootInputProtocol(node));
    }

    public GwtJsonInputProtocol(final String json) throws IOException {
        this(JSONParser.parseStrict(json));
    }

    protected InputProtocol _createArrayInputProtocol(final JSONArray node) {
        return new ArrayInputProtocol(node);
    }

    protected InputProtocol _createMapObjectInputProtocol(final JSONObject node) {
        return new MapObjectInputProtocol(node);
    }

    protected InputProtocol _createRootInputProtocol(final JSONValue parsedTree) {
        return new RootInputProtocol(parsedTree);
    }

    protected InputProtocol _createStructObjectInputProtocol(
            final JSONObject node) {
        return new StructObjectInputProtocol(node);
    }
}
