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

package org.thryft.store;

import java.util.BitSet;

import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.net.QuotedPrintableCodec;

public final class FileNameCodec {
    public static String decodeFileName(final byte[] fileName) {
        try {
            return new String(
                    QuotedPrintableCodec.decodeQuotedPrintable(fileName));
        } catch (final DecoderException e) {
            return new String(fileName);
        }
        // return new String(base32.decode(fileName.getBytes()));
    }

    public static String decodeFileName(final String fileName) {
        return decodeFileName(fileName.getBytes());
    }

    public static String encodeFileName(final byte[] fileName) {
        return new String(QuotedPrintableCodec.encodeQuotedPrintable(
                fileNameSafeChars, fileName));
        // return base32.encodeAsString(fileName.getBytes());
    }

    public static String encodeFileName(final String fileName) {
        return encodeFileName(fileName.getBytes());
    }

    private static final BitSet fileNameSafeChars = new BitSet(256);
    static {
        // Digits
        for (int i = 48; i <= 57; i++) {
            fileNameSafeChars.set(i);
        }
        // =
        fileNameSafeChars.set(61);
        // Uppercase alphas
        for (int i = 65; i <= 90; i++) {
            fileNameSafeChars.set(i);
        }
        // Lowercase alphas
        for (int i = 97; i <= 122; i++) {
            fileNameSafeChars.set(i);
        }
    }

    // private final static Base32 base32 = new Base32();
}
