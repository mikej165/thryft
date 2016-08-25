/*******************************************************************************
 * Copyright (c) 2016, Minor Gordon
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

public abstract class StackedOutputProtocol<OutputProtocolT extends OutputProtocol>
extends ForwardingOutputProtocol {
    @Override
    public void flush() throws OutputProtocolException {
        if (!outputProtocolStack.isEmpty()) {
            outputProtocolStack.peek().flush();
        }
    }

    @Override
    public void writeListBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        final int protocolStackSize = outputProtocolStack.size();
        outputProtocolStack.peek().writeListBegin(elementType, size);
        if (outputProtocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeListBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        outputProtocolStack.pop();
        outputProtocolStack.peek().writeListEnd();
    }

    @Override
    public void writeMapBegin(final Type keyType, final Type valueType,
            final int size) throws OutputProtocolException {
        final int protocolStackSize = outputProtocolStack.size();
        outputProtocolStack.peek().writeMapBegin(keyType, valueType, size);
        if (outputProtocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeMapBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        outputProtocolStack.pop();
        outputProtocolStack.peek().writeMapEnd();
    }

    @Override
    public void writeMessageBegin(final String name, final MessageType type,
            final Object id) throws OutputProtocolException {
        final int protocolStackSize = outputProtocolStack.size();
        outputProtocolStack.peek().writeMessageBegin(name, type, id);
        if (outputProtocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeMessageBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        outputProtocolStack.pop();
        outputProtocolStack.peek().writeMessageEnd();
    }

    @Override
    public void writeSetBegin(final Type elementType, final int size)
            throws OutputProtocolException {
        outputProtocolStack.peek().writeSetBegin(elementType, size);
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        outputProtocolStack.pop();
        outputProtocolStack.peek().writeSetEnd();
    }

    @Override
    public void writeStructBegin(final String name)
            throws OutputProtocolException {
        final int protocolStackSize = outputProtocolStack.size();
        outputProtocolStack.peek().writeStructBegin(name);
        if (outputProtocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeStructBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        outputProtocolStack.pop();
        outputProtocolStack.peek().writeStructEnd();
    }

    @Override
    public void writeVariant(final Object value) throws OutputProtocolException {
        AbstractOutputProtocol.writeVariant(this, value);
    }

    @Override
    protected OutputProtocol _delegate() {
        return outputProtocolStack.peek();
    }

    protected final Stack<OutputProtocolT> _getOutputProtocolStack() {
        return outputProtocolStack;
    }

    private final Stack<OutputProtocolT> outputProtocolStack = new Stack<OutputProtocolT>();
}
