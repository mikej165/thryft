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

import static com.google.common.base.Preconditions.checkState;
import static org.thryft.Preconditions.checkNotEmpty;

import java.util.Map;
import java.util.Set;
import java.util.Stack;

import org.thryft.protocol.StringMapInputProtocol.NestedInputProtocol;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Sets;

public class StringMapInputProtocol extends
        StackedInputProtocol<NestedInputProtocol> {
    protected abstract class NestedInputProtocol extends
            AbstractInputProtocol {
        protected NestedInputProtocol(
                final ImmutableMap<String, String> input, final String myKey) {
            this.input = input;
            this.myKey = myKey;

            final Set<String> childKeyStack = Sets.newLinkedHashSet();
            if (myKey.isEmpty()) {
                for (final String childKey : input.keySet()) {
                    childKeyStack.add(childKey.split("\\.", 2)[0]);
                }
            } else {
                final String childKeyPrefix = myKey + ".";
                for (final String childKey : input.keySet()) {
                    if (childKey.startsWith(childKeyPrefix)
                            && childKey.length() > childKeyPrefix.length()) {
                        childKeyStack.add(childKey.substring(
                                childKeyPrefix.length()).split("\\.", 2)[0]);
                    }
                }
            }
            this.childKeyStack.addAll(childKeyStack);
        }

        @Override
        public final boolean readBool() throws InputProtocolException {
            return Boolean.parseBoolean(readString());
        }

        @Override
        public final byte readByte() throws InputProtocolException {
            return Byte.parseByte(readString());
        }

        @Override
        public final double readDouble() throws InputProtocolException {
            return Double.parseDouble(readString());
        }

        @Override
        public final short readI16() throws InputProtocolException {
            return Short.parseShort(readString());
        }

        @Override
        public final int readI32() throws InputProtocolException {
            return Integer.parseInt(readString());
        }

        @Override
        public final long readI64() throws InputProtocolException {
            return Long.parseLong(readString());
        }

        @Override
        public Object readMixed() throws InputProtocolException {
            throw new UnsupportedOperationException();
        }

        protected final Stack<String> _getChildKeyStack() {
            return childKeyStack;
        }

        protected ImmutableMap<String, String> _getInput() {
            return input;
        }

        protected ListBegin _readListBegin(final String childKey)
                throws InputProtocolException {
            final ListInputProtocol listInputProtocol = new ListInputProtocol(
                    input, __joinKeys(myKey, childKey));
            _getInputProtocolStack().push(listInputProtocol);
            return new ListBegin(Type.VOID, listInputProtocol
                    ._getChildKeyStack().size());
        }

        protected MapBegin _readMapBegin(final String childKey)
                throws InputProtocolException {
            final MapInputProtocol mapInputProtocol = new MapInputProtocol(
                    input, __joinKeys(myKey, childKey));
            _getInputProtocolStack().push(mapInputProtocol);
            return new MapBegin(Type.VOID, Type.VOID, mapInputProtocol
                    ._getChildKeyStack().size());
        }

        protected String _readString(final String childKey) {
            return input.get(__joinKeys(myKey, childKey));
        }

        protected String _readStructBegin(final String childKey)
                throws InputProtocolException {
            final StructInputProtocol structInputProtocol = new StructInputProtocol(
                    input, __joinKeys(myKey, childKey));
            _getInputProtocolStack().push(structInputProtocol);
            return "";
        }

        private final String myKey;

        private final ImmutableMap<String, String> input;

        private final Stack<String> childKeyStack = new Stack<String>();
    }

    private final class ListInputProtocol extends NestedInputProtocol {
        public ListInputProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
            super(input, myKey);
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            return _readListBegin(_getChildKeyStack().pop());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            return _readMapBegin(_getChildKeyStack().pop());
        }

        @Override
        public String readString() throws InputProtocolException {
            return _readString(_getChildKeyStack().pop());
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            return _readStructBegin(_getChildKeyStack().pop());
        }
    }

    private final class MapInputProtocol extends NestedInputProtocol {
        public MapInputProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
            super(input, myKey);
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            checkState(!nextReadIsKey);
            nextReadIsKey = true;
            return _readListBegin(_getChildKeyStack().pop());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            checkState(!nextReadIsKey);
            nextReadIsKey = true;
            return _readMapBegin(_getChildKeyStack().pop());
        }

        @Override
        public String readString() throws InputProtocolException {
            if (nextReadIsKey) {
                nextReadIsKey = false;
                return _getChildKeyStack().peek();
            } else {
                nextReadIsKey = true;
                return _readString(_getChildKeyStack().pop());
            }
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            checkState(!nextReadIsKey);
            nextReadIsKey = true;
            return _readStructBegin(_getChildKeyStack().pop());
        }

        private boolean nextReadIsKey = true;
    }

    private final class RootInputProtocol extends NestedInputProtocol {
        public RootInputProtocol(final ImmutableMap<String, String> input) {
            super(input, "");
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            final ListInputProtocol listInputProtocol = new ListInputProtocol(
                    _getInput(), "");
            _getInputProtocolStack().push(listInputProtocol);
            return new ListBegin(Type.VOID, listInputProtocol
                    ._getChildKeyStack().size());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            final MapInputProtocol mapInputProtocol = new MapInputProtocol(
                    _getInput(), "");
            _getInputProtocolStack().push(mapInputProtocol);
            return new MapBegin(Type.VOID, Type.VOID, mapInputProtocol
                    ._getChildKeyStack().size());
        }

        @Override
        public String readString() throws InputProtocolException {
            throw new IllegalStateException();
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            _getInputProtocolStack().push(
                    new StructInputProtocol(_getInput(), ""));
            return "";
        }
    }

    private final class StructInputProtocol extends
            NestedInputProtocol {
        public StructInputProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
            super(input, myKey);
        }

        @Override
        public FieldBegin readFieldBegin() throws InputProtocolException {
            if (!_getChildKeyStack().empty()) {
                return new FieldBegin(_getChildKeyStack().peek(), Type.VOID,
                        (short) -1);
            } else {
                return new FieldBegin();
            }
        }

        @Override
        public void readFieldEnd() throws InputProtocolException {
            _getChildKeyStack().pop();
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            return _readListBegin(_getChildKeyStack().peek());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            return _readMapBegin(_getChildKeyStack().peek());
        }

        @Override
        public String readString() throws InputProtocolException {
            return _readString(_getChildKeyStack().peek());
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            return _readStructBegin(_getChildKeyStack().peek());
        }
    }

    private final static String __joinKeys(final String parentKey,
            final String childKey) {
        checkNotEmpty(childKey);
        if (parentKey.isEmpty()) {
            return childKey;
        } else {
            return parentKey + "." + childKey;
        }
    }

    public StringMapInputProtocol(final ImmutableMap<String, String> input) {
        _getInputProtocolStack().push(new RootInputProtocol(input));
    }

    public StringMapInputProtocol(final Map<String, String> input) {
        this(ImmutableMap.copyOf(input));
    }
}
