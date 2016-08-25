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

import java.math.BigDecimal;
import java.util.Date;

import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public interface InputProtocol extends Protocol {
    public byte[] readBinary() throws InputProtocolException;

    public boolean readBool() throws InputProtocolException;

    public byte readByte() throws InputProtocolException;

    public Date readDateTime() throws InputProtocolException;

    public BigDecimal readDecimal() throws InputProtocolException;

    public double readDouble() throws InputProtocolException;

    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws InputProtocolException;

    public FieldBegin readFieldBegin() throws InputProtocolException;

    public void readFieldEnd() throws InputProtocolException;

    public short readI16() throws InputProtocolException;

    public int readI32() throws InputProtocolException;

    public long readI64() throws InputProtocolException;

    public ListBegin readListBegin() throws InputProtocolException;

    public void readListEnd() throws InputProtocolException;

    public MapBegin readMapBegin() throws InputProtocolException;

    public void readMapEnd() throws InputProtocolException;

    public MessageBegin readMessageBegin() throws InputProtocolException;

    public void readMessageEnd() throws InputProtocolException;

    public SetBegin readSetBegin() throws InputProtocolException;

    public void readSetEnd() throws InputProtocolException;

    public String readString() throws InputProtocolException;

    public String readStructBegin() throws InputProtocolException;

    public void readStructEnd() throws InputProtocolException;

    public UnsignedInteger readU32() throws InputProtocolException;

    public UnsignedLong readU64() throws InputProtocolException;

    public Object readVariant() throws InputProtocolException;
}
