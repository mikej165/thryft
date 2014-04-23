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

import java.util.Date;
import java.util.Stack;

import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public class StackedOutputProtocol implements OutputProtocol {
    @Override
    public void flush() throws OutputProtocolException {
        if (!protocolStack.isEmpty()) {
            protocolStack.peek().flush();
        }
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
        protocolStack.peek().writeBinary(value);
    }

    @Override
    public void writeBool(final boolean value) throws OutputProtocolException {
        protocolStack.peek().writeBool(value);
    }

    @Override
    public void writeByte(final byte value) throws OutputProtocolException {
        protocolStack.peek().writeByte(value);
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
        protocolStack.peek().writeDateTime(value);
    }

    @Override
    public void writeDecimal(final java.math.BigDecimal value)
            throws OutputProtocolException {
        protocolStack.peek().writeDecimal(value);
    }

    @Override
    public void writeDouble(final double value) throws OutputProtocolException {
        protocolStack.peek().writeDouble(value);
    }

    @Override
    public void writeEmailAddress(final EmailAddress value)
            throws OutputProtocolException {
        protocolStack.peek().writeEmailAddress(value);
    }

    @Override
    public void writeEnum(final Enum<?> value) throws OutputProtocolException {
        protocolStack.peek().writeEnum(value);
    }

    @Override
    public void writeFieldBegin(final String name, final Type type,
            final short id) throws OutputProtocolException {
        protocolStack.peek().writeFieldBegin(name, type, id);
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        protocolStack.peek().writeFieldEnd();
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
        protocolStack.peek().writeFieldStop();
    }

    @Override
    public void writeI16(final short value) throws OutputProtocolException {
        protocolStack.peek().writeI16(value);
    }

    @Override
    public void writeI32(final int value) throws OutputProtocolException {
        protocolStack.peek().writeI32(value);
    }

    @Override
    public void writeI64(final long value) throws OutputProtocolException {
        protocolStack.peek().writeI64(value);
    }

    @Override
    public void writeListBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeListBegin(elementType, size);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeListBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        protocolStack.pop();
        protocolStack.peek().writeListEnd();
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType,
            final int size) throws OutputProtocolException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeMapBegin(keyType, valueType, size);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeMapBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        protocolStack.pop();
        protocolStack.peek().writeMapEnd();
    }

    @Override
    public void writeMixed(final Object value) throws OutputProtocolException {
        protocolStack.peek().writeMixed(value);
    }

    @Override
    public void writeNull() throws OutputProtocolException {
        protocolStack.peek().writeNull();
    }

    @Override
    public void writeSetBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        protocolStack.peek().writeSetBegin(elementType, size);
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        protocolStack.pop();
        protocolStack.peek().writeSetEnd();
    }

    @Override
    public void writeString(final String value) throws OutputProtocolException {
        protocolStack.peek().writeString(value);
    }

    @Override
    public void writeStructBegin(final String name)
            throws OutputProtocolException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeStructBegin(name);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeStructBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        protocolStack.pop();
        protocolStack.peek().writeStructEnd();
    }

    @Override
    public void writeU32(final UnsignedInteger value)
            throws OutputProtocolException {
        protocolStack.peek().writeU32(value);
    }

    @Override
    public void writeU64(final UnsignedLong value)
            throws OutputProtocolException {
        protocolStack.peek().writeU64(value);
    }

    @Override
    public void writeUri(final Uri value) throws OutputProtocolException {
        protocolStack.peek().writeUri(value);
    }

    @Override
    public void writeUrl(final Url value) throws OutputProtocolException {
        protocolStack.peek().writeUrl(value);
    }

    protected final Stack<OutputProtocol> _getProtocolStack() {
        return protocolStack;
    }

    private final Stack<OutputProtocol> protocolStack = new Stack<OutputProtocol>();
}
