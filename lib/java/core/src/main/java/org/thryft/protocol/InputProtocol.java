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
import java.math.BigDecimal;

import org.joda.time.DateTime;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public interface InputProtocol {
    public byte[] readBinary() throws IOException;

    public boolean readBool() throws IOException;

    public byte readByte() throws IOException;

    public DateTime readDate() throws IOException;

    public DateTime readDateTime() throws IOException;

    public BigDecimal readDecimal() throws IOException;

    public double readDouble() throws IOException;

    public EmailAddress readEmailAddress() throws IOException;

    public <E extends Enum<E>> E readEnum(final Class<E> enumClass)
            throws IOException;

    public FieldBegin readFieldBegin() throws IOException;

    public void readFieldEnd() throws IOException;

    public short readI16() throws IOException;

    public int readI32() throws IOException;

    public long readI64() throws IOException;

    public ListBegin readListBegin() throws IOException;

    public void readListEnd() throws IOException;

    public MapBegin readMapBegin() throws IOException;

    public void readMapEnd() throws IOException;

    public Object readMixed() throws IOException;

    public SetBegin readSetBegin() throws IOException;

    public void readSetEnd() throws IOException;

    public String readString() throws IOException;

    public StructBegin readStructBegin() throws IOException;

    public void readStructEnd() throws IOException;

    public UnsignedInteger readU32() throws IOException;

    public UnsignedLong readU64() throws IOException;

    public Uri readUri() throws IOException;

    public Url readUrl() throws IOException;
}
