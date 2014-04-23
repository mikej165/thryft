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

public abstract class StackedOutputProtocol extends ForwardingOutputProtocol {
    @Override
    public void flush() throws OutputProtocolException {
        if (!protocolStack.isEmpty()) {
            protocolStack.peek().flush();
        }
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
    public void writeMessageBegin(final String name, final MessageType type,
            final int sequenceId) throws OutputProtocolException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeMessageBegin(name, type, sequenceId);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new OutputProtocolException(
                    "writeMessageBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        protocolStack.pop();
        protocolStack.peek().writeMessageEnd();
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
    protected OutputProtocol _delegate() {
        return protocolStack.peek();
    }

    protected final Stack<OutputProtocol> _getProtocolStack() {
        return protocolStack;
    }

    private final Stack<OutputProtocol> protocolStack = new Stack<OutputProtocol>();
}
