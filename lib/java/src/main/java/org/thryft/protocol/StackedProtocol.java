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

import java.util.Stack;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TMessage;
import org.apache.thrift.protocol.TSet;
import org.apache.thrift.protocol.TStruct;

public class StackedProtocol extends Protocol {
    @Override
    public java.nio.ByteBuffer readBinary() throws TException {
        return protocolStack.peek().readBinary();
    }

    @Override
    public boolean readBool() throws TException {
        return protocolStack.peek().readBool();
    }

    @Override
    public byte readByte() throws TException {
        return protocolStack.peek().readByte();
    }

    @Override
    public org.joda.time.DateTime readDate() throws TException {
        return protocolStack.peek().readDate();
    }

    @Override
    public org.joda.time.DateTime readDateTime() throws TException {
        return protocolStack.peek().readDateTime();
    }

    @Override
    public java.math.BigDecimal readDecimal() throws TException {
        return protocolStack.peek().readDecimal();
    }

    @Override
    public double readDouble() throws TException {
        return protocolStack.peek().readDouble();
    }

    @Override
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws TException {
        return protocolStack.peek().readEnum(enumClass);
    }

    @Override
    public TField readFieldBegin() throws TException {
        return protocolStack.peek().readFieldBegin();
    }

    @Override
    public void readFieldEnd() throws TException {
        protocolStack.peek().readFieldEnd();
    }

    @Override
    public short readI16() throws TException {
        return protocolStack.peek().readI16();
    }

    @Override
    public int readI32() throws TException {
        return protocolStack.peek().readI32();
    }

    @Override
    public long readI64() throws TException {
        return protocolStack.peek().readI64();
    }

    @Override
    public TList readListBegin() throws TException {
        return protocolStack.peek().readListBegin();
    }

    @Override
    public void readListEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public TMap readMapBegin() throws TException {
        return protocolStack.peek().readMapBegin();
    }

    @Override
    public void readMapEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public TMessage readMessageBegin() throws TException {
        return protocolStack.peek().readMessageBegin();
    }

    @Override
    public void readMessageEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public Object readMixed() throws TException {
        return protocolStack.peek().readMixed();
    }

    @Override
    public TSet readSetBegin() throws TException {
        return protocolStack.peek().readSetBegin();
    }

    @Override
    public void readSetEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public String readString() throws TException {
        return protocolStack.peek().readString();
    }

    @Override
    public TStruct readStructBegin() throws TException {
        return protocolStack.peek().readStructBegin();
    }

    @Override
    public void readStructEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public void writeBinary(final java.nio.ByteBuffer buf) throws TException {
        protocolStack.peek().writeBinary(buf);
    }

    @Override
    public void writeBool(final boolean b) throws TException {
        protocolStack.peek().writeBool(b);
    }

    @Override
    public void writeByte(final byte b) throws TException {
        protocolStack.peek().writeByte(b);
    }

    @Override
    public void writeDate(final org.joda.time.DateTime date) throws TException {
        protocolStack.peek().writeDate(date);
    }

    @Override
    public void writeDateTime(final org.joda.time.DateTime dateTime)
            throws TException {
        protocolStack.peek().writeDateTime(dateTime);
    }

    @Override
    public void writeDecimal(final java.math.BigDecimal decimal)
            throws TException {
        protocolStack.peek().writeDecimal(decimal);
    }

    @Override
    public void writeDouble(final double dub) throws TException {
        protocolStack.peek().writeDouble(dub);
    }

    @Override
    public void writeEnum(final Enum<?> enum_) throws TException {
        protocolStack.peek().writeEnum(enum_);
    }

    @Override
    public void writeFieldBegin(final TField field) throws TException {
        protocolStack.peek().writeFieldBegin(field);
    }

    @Override
    public void writeFieldEnd() throws TException {
        protocolStack.peek().writeFieldEnd();
    }

    @Override
    public void writeFieldStop() throws TException {
        protocolStack.peek().writeFieldStop();
    }

    @Override
    public void writeI16(final short i16) throws TException {
        protocolStack.peek().writeI16(i16);
    }

    @Override
    public void writeI32(final int i32) throws TException {
        protocolStack.peek().writeI32(i32);
    }

    @Override
    public void writeI64(final long i64) throws TException {
        protocolStack.peek().writeI64(i64);
    }

    @Override
    public void writeListBegin(final TList list) throws TException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeListBegin(list);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new TException(
                    "writeListBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeListEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeListEnd();
    }

    @Override
    public void writeMapBegin(final TMap map) throws TException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeMapBegin(map);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new TException(
                    "writeMapBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeMapEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeMapEnd();
    }

    @Override
    public void writeMessageBegin(final TMessage message) throws TException {
        protocolStack.peek().writeMessageBegin(message);
    }

    @Override
    public void writeMessageEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeMessageEnd();
    }

    @Override
    public void writeMixed(final Object value) throws TException {
        super.writeMixed(value);
    }

    @Override
    public void writeNull() throws TException {
        protocolStack.peek().writeNull();
    }

    @Override
    public void writeSetBegin(final TSet set) throws TException {
        protocolStack.peek().writeSetBegin(set);
    }

    @Override
    public void writeSetEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeSetEnd();
    }

    @Override
    public void writeString(final String str) throws TException {
        protocolStack.peek().writeString(str);
    }

    @Override
    public void writeStructBegin(final TStruct struct) throws TException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeStructBegin(struct);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new TException(
                    "writeStructBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeStructEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeStructEnd();
    }

    protected final Stack<Protocol> _getProtocolStack() {
        return protocolStack;
    }

    private final Stack<Protocol> protocolStack = new Stack<Protocol>();
}
