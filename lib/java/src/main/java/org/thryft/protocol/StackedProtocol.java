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

public class StackedProtocol extends Protocol {
    @Override
    public boolean readBool() throws IOException {
        return protocolStack.peek().readBool();
    }

    @Override
    public byte readByte() throws IOException {
        return protocolStack.peek().readByte();
    }

    @Override
    public org.joda.time.DateTime readDate() throws IOException {
        return protocolStack.peek().readDate();
    }

    @Override
    public org.joda.time.DateTime readDateTime() throws IOException {
        return protocolStack.peek().readDateTime();
    }

    @Override
    public java.math.BigDecimal readDecimal() throws IOException {
        return protocolStack.peek().readDecimal();
    }

    @Override
    public double readDouble() throws IOException {
        return protocolStack.peek().readDouble();
    }

    @Override
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws IOException {
        return protocolStack.peek().readEnum(enumClass);
    }

    @Override
    public TField readFieldBegin() throws IOException {
        return protocolStack.peek().readFieldBegin();
    }

    @Override
    public void readFieldEnd() throws IOException {
        protocolStack.peek().readFieldEnd();
    }

    @Override
    public short readI16() throws IOException {
        return protocolStack.peek().readI16();
    }

    @Override
    public int readI32() throws IOException {
        return protocolStack.peek().readI32();
    }

    @Override
    public long readI64() throws IOException {
        return protocolStack.peek().readI64();
    }

    @Override
    public TList readListBegin() throws IOException {
        return protocolStack.peek().readListBegin();
    }

    @Override
    public void readListEnd() throws IOException {
        protocolStack.pop();
    }

    @Override
    public TMap readMapBegin() throws IOException {
        return protocolStack.peek().readMapBegin();
    }

    @Override
    public void readMapEnd() throws IOException {
        protocolStack.pop();
    }

    @Override
    public Object readMixed() throws IOException {
        return protocolStack.peek().readMixed();
    }

    @Override
    public TSet readSetBegin() throws IOException {
        return protocolStack.peek().readSetBegin();
    }

    @Override
    public void readSetEnd() throws IOException {
        protocolStack.pop();
    }

    @Override
    public String readString() throws IOException {
        return protocolStack.peek().readString();
    }

    @Override
    public TStruct readStructBegin() throws IOException {
        return protocolStack.peek().readStructBegin();
    }

    @Override
    public void readStructEnd() throws IOException {
        protocolStack.pop();
    }

    @Override
    public void writeBinary(final java.nio.ByteBuffer buf) throws IOException {
        protocolStack.peek().writeBinary(buf);
    }

    @Override
    public void writeBool(final boolean b) throws IOException {
        protocolStack.peek().writeBool(b);
    }

    @Override
    public void writeByte(final byte b) throws IOException {
        protocolStack.peek().writeByte(b);
    }

    @Override
    public void writeDateTime(final org.joda.time.DateTime dateTime)
            throws IOException {
        protocolStack.peek().writeDateTime(dateTime);
    }

    @Override
    public void writeDecimal(final java.math.BigDecimal decimal)
            throws IOException {
        protocolStack.peek().writeDecimal(decimal);
    }

    @Override
    public void writeDouble(final double dub) throws IOException {
        protocolStack.peek().writeDouble(dub);
    }

    @Override
    public void writeEnum(final Enum<?> enum_) throws IOException {
        protocolStack.peek().writeEnum(enum_);
    }

    @Override
    public void writeFieldBegin(final TField field) throws IOException {
        protocolStack.peek().writeFieldBegin(field);
    }

    @Override
    public void writeFieldEnd() throws IOException {
        protocolStack.peek().writeFieldEnd();
    }

    @Override
    public void writeFieldStop() throws IOException {
        protocolStack.peek().writeFieldStop();
    }

    @Override
    public void writeI16(final short i16) throws IOException {
        protocolStack.peek().writeI16(i16);
    }

    @Override
    public void writeI32(final int i32) throws IOException {
        protocolStack.peek().writeI32(i32);
    }

    @Override
    public void writeI64(final long i64) throws IOException {
        protocolStack.peek().writeI64(i64);
    }

    @Override
    public void writeListBegin(final TList list) throws IOException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeListBegin(list);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new IOException(
                    "writeListBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeListEnd() throws IOException {
        protocolStack.pop();
        protocolStack.peek().writeListEnd();
    }

    @Override
    public void writeMapBegin(final TMap map) throws IOException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeMapBegin(map);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new IOException(
                    "writeMapBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeMapEnd() throws IOException {
        protocolStack.pop();
        protocolStack.peek().writeMapEnd();
    }

    @Override
    public void writeMixed(final Object value) throws IOException {
        super.writeMixed(value);
    }

    @Override
    public void writeNull() throws IOException {
        protocolStack.peek().writeNull();
    }

    @Override
    public void writeSetBegin(final TSet set) throws IOException {
        protocolStack.peek().writeSetBegin(set);
    }

    @Override
    public void writeSetEnd() throws IOException {
        protocolStack.pop();
        protocolStack.peek().writeSetEnd();
    }

    @Override
    public void writeString(final String str) throws IOException {
        protocolStack.peek().writeString(str);
    }

    @Override
    public void writeStructBegin(final TStruct struct) throws IOException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeStructBegin(struct);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new IOException(
                    "writeStructBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeStructEnd() throws IOException {
        protocolStack.pop();
        protocolStack.peek().writeStructEnd();
    }

    protected final Stack<Protocol> _getProtocolStack() {
        return protocolStack;
    }

    private final Stack<Protocol> protocolStack = new Stack<Protocol>();
}
