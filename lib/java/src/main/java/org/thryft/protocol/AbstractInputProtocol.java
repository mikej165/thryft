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

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.math.BigDecimal;

import com.google.common.annotations.GwtIncompatible;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class AbstractInputProtocol implements InputProtocol {
    @Override
    public BigDecimal readDecimal() throws InputProtocolException {
        try {
            return new BigDecimal(readString());
        } catch (final IllegalArgumentException e) {
            throw new InputProtocolException(e);
        }
    }

    @GwtIncompatible("")
    @Override
    @SuppressWarnings("unchecked")
    public <E extends Enum<E>> E readEnum(final Class<E> enumClass) throws InputProtocolException {
        final String enumStringValue = readString().trim().toUpperCase();
        if (enumStringValue.isEmpty()) {
            throw new InputProtocolException("empty string");
        }

        try {
            return Enum.valueOf(enumClass, enumStringValue);
        } catch (final IllegalArgumentException e) {
            Integer enumIntValue;
            try {
                enumIntValue = Integer.parseInt(enumStringValue);
            } catch (final NumberFormatException e1) {
                throw e;
            }

            final Method valueOfMethod;
            try {
                valueOfMethod = enumClass.getMethod("valueOf", Integer.class);
            } catch (final NoSuchMethodException | SecurityException e1) {
                throw e;
            }

            try {
                return (E) valueOfMethod.invoke(null, enumIntValue);
            } catch (final IllegalAccessException | IllegalArgumentException | InvocationTargetException e1) {
                throw e;
            }
        }
    }

    @Override
    public FieldBegin readFieldBegin() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readFieldEnd() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readListEnd() throws InputProtocolException {
    }

    @Override
    public void readMapEnd() throws InputProtocolException {
    }

    @Override
    public MessageBegin readMessageBegin() throws InputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readMessageEnd() {
    }

    @Override
    public SetBegin readSetBegin() throws InputProtocolException {
        final ListBegin list = readListBegin();
        return new SetBegin(list.getElementType(), list.getSize());
    }

    @Override
    public void readSetEnd() throws InputProtocolException {
        readListEnd();
    }

    @Override
    public void readStructEnd() throws InputProtocolException {
    }

    @Override
    public UnsignedInteger readU32() throws InputProtocolException {
        return UnsignedInteger.valueOf(readI32());
    }

    @Override
    public UnsignedLong readU64() throws InputProtocolException {
        return UnsignedLong.valueOf(readI64());
    }
}
