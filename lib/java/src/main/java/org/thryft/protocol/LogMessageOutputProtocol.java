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

import java.io.Writer;
import java.math.BigDecimal;
import java.util.Date;
import java.util.Stack;

import com.google.common.annotations.GwtIncompatible;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

@GwtIncompatible("")
public final class LogMessageOutputProtocol implements OutputProtocol {
    public LogMessageOutputProtocol(final Writer writer) throws OutputProtocolException {
        delegate = new JacksonJsonOutputProtocol(writer);
    }

    @Override
    public void flush() throws OutputProtocolException {
        delegate.flush();
    }

    @Override
    public void writeBinary(final byte[] value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeBinary(value);
        }
    }

    @Override
    public void writeBool(final boolean value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeBool(value);
        }
    }

    @Override
    public void writeByte(final byte value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeByte(value);
        }
    }

    @Override
    public void writeDateTime(final Date value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeDateTime(value);
        }
    }

    @Override
    public void writeDecimal(final BigDecimal value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeDecimal(value);
        }
    }

    @Override
    public void writeDouble(final double value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeDouble(value);
        }
    }

    @Override
    public void writeEnum(final Enum<?> value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeEnum(value);
        }
    }

    @Override
    public void writeFieldBegin(final String name, final Type type) throws OutputProtocolException {
        delegate.writeFieldBegin(name, type);
    }

    @Override
    public void writeFieldBegin(final String name, final Type type, final short id) throws OutputProtocolException {
        delegate.writeFieldBegin(name, type, id);
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        delegate.writeFieldEnd();
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
        delegate.writeFieldStop();
    }

    @Override
    public void writeI16(final short value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeI16(value);
        }
    }

    @Override
    public void writeI32(final int value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeI32(value);
        }
    }

    @Override
    public void writeI64(final long value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeI64(value);
        }
    }

    @Override
    public void writeListBegin(final Type elementType, final int size) throws OutputProtocolException {
        sizeStack.push(0);
        delegate.writeListBegin(elementType, size);
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        delegate.writeListEnd();
        sizeStack.pop();
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType, final int size) throws OutputProtocolException {
        sizeStack.push(0);
        delegate.writeMapBegin(keyType, valueType, size);
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        delegate.writeMapEnd();
        sizeStack.pop();
    }

    @Override
    public void writeMessageBegin(final String name, final MessageType type, final Object id)
            throws OutputProtocolException {
        delegate.writeMessageBegin(name, type, id);
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        delegate.writeMessageEnd();
    }

    @Override
    public void writeNull() throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeNull();
        }
    }

    @Override
    public void writeSetBegin(final Type elementType, final int size) throws OutputProtocolException {
        sizeStack.push(0);
        delegate.writeSetBegin(elementType, size);
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        delegate.writeSetEnd();
        sizeStack.push(0);
    }

    @Override
    public void writeString(final String value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            if (value.length() > STRING_LENGTH_MAX) {
                delegate.writeString(value.substring(0, STRING_LENGTH_MAX));
            } else {
                delegate.writeString(value);
            }
        }
    }

    @Override
    public void writeStructBegin(final String name) throws OutputProtocolException {
        sizeStack.push(null);
        delegate.writeStructBegin(name);
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        delegate.writeStructEnd();
        sizeStack.pop();
    }

    @Override
    public void writeU32(final UnsignedInteger value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeU32(value);
        }
    }

    @Override
    public void writeU64(final UnsignedLong value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeU64(value);
        }
    }

    @Override
    public void writeVariant(final Object value) throws OutputProtocolException {
        if (__writeValueBegin()) {
            delegate.writeVariant(value);
        }
    }

    private boolean __writeValueBegin() {
        return true;
        // if (sizeStack.isEmpty()) {
        // return true;
        // } else if (sizeStack.peek() == null) {
        // // Struct
        // return true;
        // } else if (sizeStack.peek() < CONTAINER_SIZE_MAX) {
        // sizeStack.push(sizeStack.pop() + 1);
        // return true;
        // } else {
        // return false;
        // }
    }

    private final JacksonJsonOutputProtocol delegate;

    private final Stack<Integer> sizeStack = new Stack<Integer>();

    private final static int CONTAINER_SIZE_MAX = 16;

    private final static int STRING_LENGTH_MAX = 256;
}
