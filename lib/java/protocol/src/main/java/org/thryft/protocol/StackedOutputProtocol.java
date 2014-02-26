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

public class StackedOutputProtocol extends AbstractOutputProtocol {
    @Override
    public void writeBinary(final byte[] buf) throws IOException {
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
    public void writeFieldBegin(final FieldBegin field) throws IOException {
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
    public void writeListBegin(final ListBegin list) throws IOException {
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
    public void writeMapBegin(final MapBegin map) throws IOException {
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
    public void writeSetBegin(final SetBegin set) throws IOException {
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
    public void writeStructBegin(final StructBegin struct) throws IOException {
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

    protected final Stack<OutputProtocol> _getProtocolStack() {
        return protocolStack;
    }

    private final Stack<OutputProtocol> protocolStack = new Stack<OutputProtocol>();
}