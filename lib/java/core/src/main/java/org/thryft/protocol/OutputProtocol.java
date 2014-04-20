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

import java.math.BigDecimal;
import java.util.Date;

import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public interface OutputProtocol extends Protocol {
    public void flush() throws OutputProtocolException;

    public void writeBinary(final byte[] buf) throws OutputProtocolException;

    public void writeBool(final boolean b) throws OutputProtocolException;

    public void writeByte(final byte b) throws OutputProtocolException;

    public void writeDateTime(final Date dateTime)
            throws OutputProtocolException;

    public void writeDecimal(final BigDecimal decimal)
            throws OutputProtocolException;

    public void writeDouble(final double dub) throws OutputProtocolException;

    public void writeEmailAddress(final EmailAddress emailAddress)
            throws OutputProtocolException;

    public void writeEnum(final Enum<?> enum_) throws OutputProtocolException;

    public void writeFieldBegin(final FieldBegin field)
            throws OutputProtocolException;

    public void writeFieldEnd() throws OutputProtocolException;

    public void writeFieldStop() throws OutputProtocolException;

    public void writeI16(final short i16) throws OutputProtocolException;

    public void writeI32(final int i32) throws OutputProtocolException;

    public void writeI64(final long i64) throws OutputProtocolException;

    public void writeListBegin(final ListBegin list)
            throws OutputProtocolException;

    public void writeListEnd() throws OutputProtocolException;

    public void writeMapBegin(final MapBegin map)
            throws OutputProtocolException;

    public void writeMapEnd() throws OutputProtocolException;

    public void writeMixed(final Object value) throws OutputProtocolException;

    public void writeNull() throws OutputProtocolException;

    public void writeSetBegin(final SetBegin set)
            throws OutputProtocolException;

    public void writeSetEnd() throws OutputProtocolException;

    public void writeString(final String str) throws OutputProtocolException;

    public void writeStructBegin(final StructBegin struct)
            throws OutputProtocolException;

    public void writeStructEnd() throws OutputProtocolException;

    public void writeU32(final UnsignedInteger u32)
            throws OutputProtocolException;

    public void writeU64(final UnsignedLong u64) throws OutputProtocolException;

    public void writeUri(final Uri uri) throws OutputProtocolException;

    public void writeUrl(final Url url) throws OutputProtocolException;
}
