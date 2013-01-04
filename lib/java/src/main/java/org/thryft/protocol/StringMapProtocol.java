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

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static com.google.common.base.Preconditions.checkState;

import java.util.Map;
import java.util.Set;
import java.util.Stack;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TStruct;
import org.apache.thrift.protocol.TType;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Maps;
import com.google.common.collect.Sets;

public class StringMapProtocol extends StackedProtocol {
    protected abstract class ReaderProtocol extends Protocol {
        protected ReaderProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
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
        public final boolean readBool() throws TException {
            return Boolean.parseBoolean(readString());
        }

        @Override
        public final byte readByte() throws TException {
            return Byte.parseByte(readString());
        }

        @Override
        public final double readDouble() throws TException {
            return Double.parseDouble(readString());
        }

        @Override
        public final short readI16() throws TException {
            return Short.parseShort(readString());
        }

        @Override
        public final int readI32() throws TException {
            return Integer.parseInt(readString());
        }

        @Override
        public final long readI64() throws TException {
            return Long.parseLong(readString());
        }

        protected final Stack<String> _getChildKeyStack() {
            return childKeyStack;
        }

        protected ImmutableMap<String, String> _getInput() {
            return input;
        }

        protected TList _readListBegin(final String childKey) throws TException {
            final ListReaderProtocol listReaderProtocol = new ListReaderProtocol(
                    input, __joinKeys(myKey, childKey));
            _getProtocolStack().push(listReaderProtocol);
            return new TList(TType.VOID, listReaderProtocol._getChildKeyStack()
                    .size());
        }

        protected TMap _readMapBegin(final String childKey) throws TException {
            final MapReaderProtocol mapReaderProtocol = new MapReaderProtocol(
                    input, __joinKeys(myKey, childKey));
            _getProtocolStack().push(mapReaderProtocol);
            return new TMap(TType.VOID, TType.VOID, mapReaderProtocol
                    ._getChildKeyStack().size());
        }

        protected String _readString(final String childKey) {
            return input.get(__joinKeys(myKey, childKey));
        }

        protected TStruct _readStructBegin(final String childKey)
                throws TException {
            final StructReaderProtocol structReaderProtocol = new StructReaderProtocol(
                    input, __joinKeys(myKey, childKey));
            _getProtocolStack().push(structReaderProtocol);
            return new TStruct();
        }

        private final String myKey;

        private final ImmutableMap<String, String> input;

        private final Stack<String> childKeyStack = new Stack<String>();
    }

    protected abstract class WriterProtocol extends Protocol {
        protected WriterProtocol(final String myKey) {
            this.myKey = myKey;
        }

        @Override
        public final void writeBool(final boolean b) throws TException {
            writeString(Boolean.toString(b));
        }

        @Override
        public final void writeByte(final byte b) throws TException {
            writeString(Byte.toString(b));
        }

        @Override
        public final void writeDouble(final double dub) throws TException {
            writeString(Double.toString(dub));
        }

        @Override
        public final void writeI16(final short i16) throws TException {
            writeString(Short.toString(i16));
        }

        @Override
        public final void writeI32(final int i32) throws TException {
            writeString(Integer.toString(i32));
        }

        @Override
        public final void writeI64(final long i64) throws TException {
            writeString(Long.toString(i64));
        }

        @Override
        public void writeListEnd() throws TException {
        }

        @Override
        public void writeMapEnd() throws TException {
        }

        @Override
        public void writeStructEnd() throws TException {
        }

        protected void _writeListBegin(final String childKey) throws TException {
            output.put(__joinKeys(myKey, childKey), "");
            _getProtocolStack().push(
                    new ListWriterProtocol(__joinKeys(myKey, childKey)));
        }

        protected void _writeMapBegin(final String childKey) throws TException {
            output.put(__joinKeys(myKey, childKey), "");
            _getProtocolStack().push(
                    new MapWriterProtocol(__joinKeys(myKey, childKey)));
        }

        protected void _writeString(final String childKey, final String value) {
            checkNotNull(childKey);
            checkNotNull(value);
            output.put(__joinKeys(myKey, childKey), value);
        }

        protected void _writeStructBegin(final String childKey)
                throws TException {
            output.put(__joinKeys(myKey, childKey), "");
            _getProtocolStack().push(
                    new StructWriterProtocol(__joinKeys(myKey, childKey)));
        }

        private final String myKey;
    }

    private final class ListReaderProtocol extends ReaderProtocol {
        public ListReaderProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
            super(input, myKey);
        }

        @Override
        public TList readListBegin() throws TException {
            return _readListBegin(_getChildKeyStack().pop());
        }

        @Override
        public TMap readMapBegin() throws TException {
            return _readMapBegin(_getChildKeyStack().pop());
        }

        @Override
        public String readString() throws TException {
            return _readString(_getChildKeyStack().pop());
        }

        @Override
        public TStruct readStructBegin() throws TException {
            return _readStructBegin(_getChildKeyStack().pop());
        }
    }

    private final class ListWriterProtocol extends WriterProtocol {
        public ListWriterProtocol(final String myKey) {
            super(myKey);
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            _writeListBegin(Integer.toString(nextChildKey++));
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            _writeMapBegin(Integer.toString(nextChildKey++));
        }

        @Override
        public void writeString(final String value) throws TException {
            _writeString(Integer.toString(nextChildKey++), value);
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            _writeStructBegin(Integer.toString(nextChildKey++));
        }

        private int nextChildKey;
    }

    private final class MapReaderProtocol extends ReaderProtocol {
        public MapReaderProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
            super(input, myKey);
        }

        @Override
        public TList readListBegin() throws TException {
            checkState(!nextReadIsKey);
            nextReadIsKey = true;
            return _readListBegin(_getChildKeyStack().pop());
        }

        @Override
        public TMap readMapBegin() throws TException {
            checkState(!nextReadIsKey);
            nextReadIsKey = true;
            return _readMapBegin(_getChildKeyStack().pop());
        }

        @Override
        public String readString() throws TException {
            if (nextReadIsKey) {
                nextReadIsKey = false;
                return _getChildKeyStack().peek();
            } else {
                nextReadIsKey = true;
                return _readString(_getChildKeyStack().pop());
            }
        }

        @Override
        public TStruct readStructBegin() throws TException {
            checkState(!nextReadIsKey);
            nextReadIsKey = true;
            return _readStructBegin(_getChildKeyStack().pop());
        }

        private boolean nextReadIsKey = true;
    }

    private final class MapWriterProtocol extends WriterProtocol {
        public MapWriterProtocol(final String myKey) {
            super(myKey);
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            checkState(nextChildKey != null);
            _writeListBegin(nextChildKey);
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            checkState(nextChildKey != null);
            _writeMapBegin(nextChildKey);
        }

        @Override
        public void writeString(final String value) throws TException {
            if (nextChildKey == null) {
                nextChildKey = value;
            } else {
                _writeString(nextChildKey, value);
                nextChildKey = null;
            }
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            checkState(nextChildKey != null);
            _writeStructBegin(nextChildKey);
        }

        private String nextChildKey = null;
    }

    private final class RootReaderProtocol extends ReaderProtocol {
        public RootReaderProtocol(final ImmutableMap<String, String> input) {
            super(input, "");
        }

        @Override
        public TList readListBegin() throws TException {
            final ListReaderProtocol listReaderProtocol = new ListReaderProtocol(
                    _getInput(), "");
            _getProtocolStack().push(listReaderProtocol);
            return new TList(TType.VOID, listReaderProtocol._getChildKeyStack()
                    .size());
        }

        @Override
        public TMap readMapBegin() throws TException {
            final MapReaderProtocol mapReaderProtocol = new MapReaderProtocol(
                    _getInput(), "");
            _getProtocolStack().push(mapReaderProtocol);
            return new TMap(TType.VOID, TType.VOID, mapReaderProtocol
                    ._getChildKeyStack().size());
        }

        @Override
        public String readString() throws TException {
            throw new IllegalStateException();
        }

        @Override
        public TStruct readStructBegin() throws TException {
            _getProtocolStack().push(new StructReaderProtocol(_getInput(), ""));
            return new TStruct();
        }
    }

    private final class RootWriterProtocol extends WriterProtocol {
        public RootWriterProtocol() {
            super("");
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            _getProtocolStack().push(new ListWriterProtocol(""));
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            _getProtocolStack().push(new MapWriterProtocol(""));
        }

        @Override
        public void writeString(final String value) throws TException {
            throw new IllegalStateException();
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            _getProtocolStack().push(new StructWriterProtocol(""));
        }
    }

    private final class StructReaderProtocol extends ReaderProtocol {
        public StructReaderProtocol(final ImmutableMap<String, String> input,
                final String myKey) {
            super(input, myKey);
        }

        @Override
        public TField readFieldBegin() throws TException {
            if (!_getChildKeyStack().empty()) {
                return new TField(_getChildKeyStack().peek(), TType.VOID,
                        (short) -1);
            } else {
                return new TField();
            }
        }

        @Override
        public void readFieldEnd() throws TException {
            _getChildKeyStack().pop();
        }

        @Override
        public TList readListBegin() throws TException {
            return _readListBegin(_getChildKeyStack().peek());
        }

        @Override
        public TMap readMapBegin() throws TException {
            return _readMapBegin(_getChildKeyStack().peek());
        }

        @Override
        public String readString() throws TException {
            return _readString(_getChildKeyStack().peek());
        }

        @Override
        public TStruct readStructBegin() throws TException {
            return _readStructBegin(_getChildKeyStack().peek());
        }
    }

    private final class StructWriterProtocol extends WriterProtocol {
        public StructWriterProtocol(final String myKey) {
            super(myKey);
        }

        @Override
        public void writeFieldBegin(final TField field) throws TException {
            nextChildKey = field.name;
        }

        @Override
        public void writeFieldEnd() throws TException {
        }

        @Override
        public void writeFieldStop() throws TException {
        }

        @Override
        public void writeListBegin(final TList list) throws TException {
            checkState(nextChildKey != null);
            _writeListBegin(nextChildKey);
        }

        @Override
        public void writeMapBegin(final TMap map) throws TException {
            checkState(nextChildKey != null);
            _writeMapBegin(nextChildKey);
        }

        @Override
        public void writeString(final String value) throws TException {
            checkState(nextChildKey != null);
            _writeString(nextChildKey, value);
        }

        @Override
        public void writeStructBegin(final TStruct struct) throws TException {
            checkState(nextChildKey != null);
            _writeStructBegin(nextChildKey);
        }

        private String nextChildKey = null;
    }

    private final static String __joinKeys(final String parentKey,
            final String childKey) {
        checkArgument(!childKey.isEmpty());
        if (parentKey.isEmpty()) {
            return childKey;
        } else {
            return parentKey + "." + childKey;
        }
    }

    public StringMapProtocol() {
        _getProtocolStack().push(new RootWriterProtocol());
    }

    public StringMapProtocol(final ImmutableMap<String, String> input) {
        _getProtocolStack().push(new RootReaderProtocol(input));
    }

    public StringMapProtocol(final Map<String, String> input) {
        this(ImmutableMap.copyOf(input));
    }

    public final ImmutableMap<String, String> toStringMap() {
        return ImmutableMap.copyOf(output);
    }

    private final Map<String, String> output = Maps.newHashMap();
}
