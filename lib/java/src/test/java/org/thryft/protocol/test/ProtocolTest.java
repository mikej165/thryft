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

package org.thryft.protocol.test;

import static org.junit.Assert.assertEquals;

import java.math.BigDecimal;
import java.util.Date;

import org.junit.Test;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;
import org.thryft.protocol.UnsupportedOperationInputProtocolException;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class ProtocolTest {
    @Test
    public void testBool() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setBoolField(true));
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testDateTime() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setDateTimeField(new Date()));
        final Date oldDate = new Date(-21, 1, 1);
        __testEquals(ProtocolTestStruct.builder().setDateTimeField(oldDate));
    }

    @Test
    public void testDecimal() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setDecimalField(new BigDecimal(100)));
    }

    @Test
    public void testDouble() throws Exception {
        final ProtocolTestStruct expected = __build(ProtocolTestStruct.builder().setDoubleField(12.0));
        final ProtocolTestStruct actual = _writeRead(expected);
        assertEquals(expected.getDoubleField().get(), actual.getDoubleField().get(), 0.1);
    }

    @Test
    public void testEmailAddress() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setEmailAddressField(new EmailAddress("test@example.com")));
    }

    @Test
    public void testEnum() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setEnumField(ProtocolTestEnum.ENUMERATOR2));
    }

    @Test
    public void testFloat() throws Exception {
        final ProtocolTestStruct expected = __build(ProtocolTestStruct.builder().setFloatField((float) 12.0));
        final ProtocolTestStruct actual = _writeRead(expected);
        assertEquals(expected.getFloatField().get(), actual.getFloatField().get(), 0.1);
    }

    @Test
    public void testI16() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setI16Field((short) 1));
    }

    @Test
    public void testI32() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setI32Field(1));
    }

    @Test
    public void testI64() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setI64Field(1l));
    }

    @Test
    public void testI8() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setI8Field((byte) 1));
    }

    @Test
    public void testString() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setStringField("test"));
    }

    @Test
    public void testStringList() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setStringListField(ImmutableList.of("test")));

        // Empty list
        __testEquals(ProtocolTestStruct.builder().setStringListField(ImmutableList.<String>of()));
    }

    @Test
    public void testStringListLong() throws Exception {
        final ImmutableList.Builder<String> stringListBuilder = ImmutableList.builder();
        for (int i = 0; i < 32; i++) {
            stringListBuilder.add("test" + i);
        }
        __testEquals(ProtocolTestStruct.builder().setStringListField(stringListBuilder.build()));
    }

    @Test
    public void testStringSet() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setStringSetField(ImmutableSet.of("test")));

        // Empty set
        __testEquals(ProtocolTestStruct.builder().setStringSetField(ImmutableSet.<String>of()));
    }

    @Test
    public void testStringStringMap() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setStringStringMapField(ImmutableMap.of("testkey", "testvalue")));

        // Empty map
        __testEquals(ProtocolTestStruct.builder().setStringStringMapField(ImmutableMap.<String, String>of()));
    }

    @Test
    public void testStruct() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setStructField(new NestedProtocolTestStruct.Builder().setI32Field(1)
                .setRequiredI32Field(1).setRequiredStringField("test").build()));

        // Empty struct
        __testEquals(ProtocolTestStruct.builder().setStructField(
                new NestedProtocolTestStruct.Builder().setRequiredI32Field(1).setRequiredStringField("test").build()));
    }

    @Test
    public void testU32() throws Exception {
        _writeRead(ProtocolTestStruct.builder().setRequiredI32Field(1).setRequiredStringField("test")
                .setU32Field(UnsignedInteger.valueOf(1)).build());
    }

    @Test
    public void testU64() throws Exception {
        _writeRead(ProtocolTestStruct.builder().setRequiredI32Field(1).setRequiredStringField("test")
                .setU64Field(UnsignedLong.valueOf(1)).build());
    }

    @Test
    public void testUri() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setUriField(Uri.parse("urn:test:test")));
    }

    @Test
    public void testUrl() throws Exception {
        __testEquals(ProtocolTestStruct.builder().setUrlField(Url.parse("http://example.com/test")));
    }

    @Test
    public void testVariant() throws Exception {
        try {
            __testEquals(ProtocolTestStruct.builder().setVariantField("test"));
        } catch (final UnsupportedOperationInputProtocolException e) {
        }
    }

    protected abstract ProtocolTestStruct _writeRead(final ProtocolTestStruct expected) throws Exception;

    private ProtocolTestStruct __build(final ProtocolTestStruct.Builder expectedBuilder) {
        return expectedBuilder.setRequiredI32Field(1).setRequiredStringField("test").build();
    }

    private void __testEquals(final ProtocolTestStruct.Builder expectedBuilder) throws Exception {
        final ProtocolTestStruct expected = __build(expectedBuilder);
        assertEquals(expected, _writeRead(expected));
    }
}
