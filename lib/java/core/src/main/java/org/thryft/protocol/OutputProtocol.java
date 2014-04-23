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

    public void writeBinary(final byte[] value) throws OutputProtocolException;

    public void writeBool(final boolean value) throws OutputProtocolException;

    public void writeByte(final byte value) throws OutputProtocolException;

    public void writeDateTime(final Date value)
            throws OutputProtocolException;

    public void writeDecimal(final BigDecimal value)
            throws OutputProtocolException;

    public void writeDouble(final double value) throws OutputProtocolException;

    public void writeEmailAddress(final EmailAddress value)
            throws OutputProtocolException;

    public void writeEnum(final Enum<?> value) throws OutputProtocolException;

    public void writeFieldBegin(final String name, final Type type,
            final short id) throws OutputProtocolException;

    public void writeFieldEnd() throws OutputProtocolException;

    public void writeFieldStop() throws OutputProtocolException;

    public void writeI16(final short value) throws OutputProtocolException;

    public void writeI32(final int value) throws OutputProtocolException;

    public void writeI64(final long value) throws OutputProtocolException;

    public void writeListBegin(final Type elementType, final int size)
            throws OutputProtocolException;

    public void writeListEnd() throws OutputProtocolException;

    public void writeMapBegin(final Type keyType, final Type valueType,
            final int size) throws OutputProtocolException;

    public void writeMapEnd() throws OutputProtocolException;

    public void writeMixed(final Object value) throws OutputProtocolException;

    public void writeNull() throws OutputProtocolException;

    public void writeSetBegin(final Type elementType, final int size)
            throws OutputProtocolException;

    public void writeSetEnd() throws OutputProtocolException;

    public void writeString(final String value) throws OutputProtocolException;

    public void writeStructBegin(final String name)
            throws OutputProtocolException;

    public void writeStructEnd() throws OutputProtocolException;

    public void writeU32(final UnsignedInteger value)
            throws OutputProtocolException;

    public void writeU64(final UnsignedLong value) throws OutputProtocolException;

    public void writeUri(final Uri value) throws OutputProtocolException;

    public void writeUrl(final Url value) throws OutputProtocolException;
}
