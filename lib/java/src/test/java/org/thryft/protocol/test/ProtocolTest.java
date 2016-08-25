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

import java.math.BigDecimal;
import java.util.Date;

import org.junit.Test;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Uri;
import org.thryft.native_.Url;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.primitives.UnsignedInteger;
import com.google.common.primitives.UnsignedLong;

public abstract class ProtocolTest {
    @Test
    public void testBool() throws Exception {
        _test(ProtocolTestStruct.builder().setBoolField(true));
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testDateTime() throws Exception {
        _test(ProtocolTestStruct.builder().setDateTimeField(new Date()));
        final Date oldDate = new Date(-21, 1, 1);
        _test(ProtocolTestStruct.builder().setDateTimeField(oldDate));
    }

    @Test
    public void testDecimal() throws Exception {
        _test(ProtocolTestStruct.builder().setDecimalField(new BigDecimal(100)));
    }

    @Test
    public void testDouble() throws Exception {
        _test(ProtocolTestStruct.builder().setDoubleField(12.0));
    }

    @Test
    public void testEmailAddress() throws Exception {
        _test(ProtocolTestStruct.builder().setEmailAddressField(new EmailAddress("test@example.com")));
    }

    @Test
    public void testEnum() throws Exception {
        _test(ProtocolTestStruct.builder().setEnumField(ProtocolTestEnum.ENUMERATOR2));
    }

    @Test
    public void testFloat() throws Exception {
        _test(ProtocolTestStruct.builder().setFloatField((float) 12.0));
    }

    @Test
    public void testI16() throws Exception {
        _test(ProtocolTestStruct.builder().setI16Field((short) 1));
    }

    @Test
    public void testI32() throws Exception {
        _test(ProtocolTestStruct.builder().setI32Field(1));
    }

    @Test
    public void testI64() throws Exception {
        _test(ProtocolTestStruct.builder().setI64Field(1l));
    }

    @Test
    public void testI8() throws Exception {
        _test(ProtocolTestStruct.builder().setI8Field((byte) 1));
    }

    @Test
    public void testString() throws Exception {
        _test(ProtocolTestStruct.builder().setStringField("test"));
    }

    @Test
    public void testStringList() throws Exception {
        _test(ProtocolTestStruct.builder().setStringListField(ImmutableList.of("test")));

        // Empty list
        _test(ProtocolTestStruct.builder().setStringListField(ImmutableList.<String> of()));
    }

    @Test
    public void testStringListLong() throws Exception {
        final ImmutableList.Builder<String> stringListBuilder = ImmutableList.builder();
        for (int i = 0; i < 32; i++) {
            stringListBuilder.add("test" + i);
        }
        _test(ProtocolTestStruct.builder().setStringListField(stringListBuilder.build()));
    }

    @Test
    public void testStringSet() throws Exception {
        _test(ProtocolTestStruct.builder().setStringSetField(ImmutableSet.of("test")));

        // Empty set
        _test(ProtocolTestStruct.builder().setStringSetField(ImmutableSet.<String> of()));
    }

    @Test
    public void testStringStringMap() throws Exception {
        _test(ProtocolTestStruct.builder().setStringStringMapField(ImmutableMap.of("testkey", "testvalue")));

        // Empty map
        _test(ProtocolTestStruct.builder().setStringStringMapField(ImmutableMap.<String, String> of()));
    }

    @Test
    public void testStruct() throws Exception {
        _test(ProtocolTestStruct.builder().setStructField(new NestedProtocolTestStruct.Builder().setI32Field(1)
                .setRequiredI32Field(1).setRequiredStringField("test").build()));

        // Empty struct
        _test(ProtocolTestStruct.builder().setStructField(
                new NestedProtocolTestStruct.Builder().setRequiredI32Field(1).setRequiredStringField("test").build()));
    }

    @Test
    public void testU32() throws Exception {
        _test(ProtocolTestStruct.builder().setRequiredI32Field(1).setRequiredStringField("test")
                .setU32Field(UnsignedInteger.valueOf(1)).build());
    }

    @Test
    public void testU64() throws Exception {
        _test(ProtocolTestStruct.builder().setRequiredI32Field(1).setRequiredStringField("test")
                .setU64Field(UnsignedLong.valueOf(1)).build());
    }

    @Test
    public void testUri() throws Exception {
        _test(ProtocolTestStruct.builder().setUriField(Uri.parse("urn:test:test")));
    }

    @Test
    public void testUrl() throws Exception {
        _test(ProtocolTestStruct.builder().setUrlField(Url.parse("http://example.com/test")));
    }

    @Test
    public void testVariant() throws Exception {
        try {
            _test(ProtocolTestStruct.builder().setVariantField("test"));
        } catch (final UnsupportedOperationException e) {
        }
    }

    protected abstract void _test(final ProtocolTestStruct expected) throws Exception;

    protected void _test(final ProtocolTestStruct.Builder expectedBuilder) throws Exception {
        _test(expectedBuilder.setRequiredI32Field(1).setRequiredStringField("test").build());
    }
}
