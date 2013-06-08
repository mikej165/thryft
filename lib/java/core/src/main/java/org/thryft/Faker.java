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

package org.thryft;

import static com.google.common.base.Preconditions.checkArgument;

import java.math.BigDecimal;
import java.util.Random;

import org.thryft.native_.EmailAddress;
import org.thryft.native_.Url;
import org.thryft.native_.UrlParser;

import com.google.common.collect.ImmutableList;

public final class Faker {
    public final static class Address {
        public static String secondaryAddress() {
            return "Apt. 1";
        }

        public static String streetAddress() {
            return "Main St.";
        }

        public static String ukCountry() {
            return "USA";
        }

        public static String usState() {
            return "OK";
        }

        public static String zipCode() {
            return "74017";
        }
    }

    public final static class Internet {
        public static EmailAddress email() {
            return new EmailAddress("fake@example.com");
        }

        public static Url url() {
            return UrlParser.parseUrl("http://example.com");
        }

        private Internet() {
        }
    }

    public final static class Lorem {
        public static String paragraph() {
            return "Lorem";
        }

        public static String sentence() {
            return "Lorem";
        }

        public static String word() {
            return "Lorem";
        }

        private Lorem() {
        }
    }

    public final static class Name {
        public static String findName() {
            return "John Doe";
        }

        public static String firstName() {
            return "John";
        }

        public static String lastName() {
            return "Doe";
        }

        private Name() {
        }
    }

    public final static class PhoneNumber {
        public static String phoneNumber() {
            return "5555551212";
        }
    }

    public static byte[] randomBinary() {
        final byte[] binary = new byte[32];
        random.nextBytes(binary);
        return binary;
    }

    public static boolean randomBool() {
        return random.nextBoolean();
    }

    public static byte randomByte() {
        return (byte) random.nextInt();
    }

    public static BigDecimal randomDecimal() {
        return BigDecimal.valueOf(random.nextInt());
    }

    public static BigDecimal randomDecimal(final BigDecimal min,
            final BigDecimal max) {
        if (min == null && max == null) {
            return randomDecimal();
        } else if (min != null) {
            if (max != null) {
                return BigDecimal.valueOf(random.nextInt(max.subtract(min)
                        .intValue()) + min.intValue());
            } else {
                return BigDecimal.valueOf(random.nextInt(Integer.MAX_VALUE)
                        + min.intValue());
            }
        } else {
            return BigDecimal.valueOf(random.nextInt(max.intValue()));
        }
    }

    public static <EnumT extends Enum<?>> EnumT randomEnum(
            final ImmutableList<EnumT> enumerators) {
        checkArgument(enumerators.size() > 0);
        return enumerators.get(0);
    }

    public static float randomFloat() {
        return random.nextFloat();
    }

    public static short randomI16() {
        return (short) random.nextInt();
    }

    public static short randomI16(final int min, final int max) {
        checkArgument(min >= Short.MIN_VALUE);
        checkArgument(max <= Short.MAX_VALUE);
        return randomI16((short) min, (short) max);
    }

    public static short randomI16(final short min, final short max) {
        return (short) (random.nextInt(max - min) + min);
    }

    public static int randomI32() {
        return random.nextInt();
    }

    public static long randomI64() {
        return random.nextLong();
    }

    private Faker() {
    }

    private final static Random random = new Random();
}
