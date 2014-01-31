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

public interface OutputProtocol {
    public void flush() throws IOException;

    public void writeBinary(final byte[] buf) throws IOException;

    public void writeBool(final boolean b) throws IOException;

    public void writeByte(final byte b) throws IOException;

    public void writeDateTime(final DateTime dateTime) throws IOException;

    public void writeDecimal(final BigDecimal decimal) throws IOException;

    public void writeDouble(final double dub) throws IOException;

    public void writeEmailAddress(final EmailAddress emailAddress)
            throws IOException;

    public void writeEnum(final Enum<?> enum_) throws IOException;

    public void writeFieldBegin(final FieldBegin field) throws IOException;

    public void writeFieldEnd() throws IOException;

    public void writeFieldStop() throws IOException;

    public void writeI16(final short i16) throws IOException;

    public void writeI32(final int i32) throws IOException;

    public void writeI64(final long i64) throws IOException;

    public void writeListBegin(final ListBegin list) throws IOException;

    public void writeListEnd() throws IOException;

    public void writeMapBegin(final MapBegin map) throws IOException;

    public void writeMapEnd() throws IOException;

    public void writeMixed(final Object value) throws IOException;

    public void writeNull() throws IOException;

    public void writeSetBegin(final SetBegin set) throws IOException;

    public void writeSetEnd() throws IOException;

    public void writeString(final String str) throws IOException;

    public void writeStructBegin(final StructBegin struct) throws IOException;

    public void writeStructEnd() throws IOException;

    public void writeU32(final UnsignedInteger u32) throws IOException;

    public void writeU64(final UnsignedLong u64) throws IOException;

    public void writeUri(final Uri uri) throws IOException;

    public void writeUrl(final Url url) throws IOException;
}
