package org.thryft.web.server.util;

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