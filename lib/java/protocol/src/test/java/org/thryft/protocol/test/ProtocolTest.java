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

package org.thryft.protocol.test;

import java.math.BigDecimal;

import org.joda.time.DateTime;
import org.junit.Test;
import org.thryft.native_.EmailAddress;
import org.thryft.native_.Url;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class ProtocolTest {
    @Test
    public void testBool() throws Exception {
        _test(new ProtocolTestStruct.Builder().setBoolField(true));
    }

    @Test
    public void testByte() throws Exception {
        _test(new ProtocolTestStruct.Builder().setByteField((byte) 1));
    }

    @Test
    public void testDateTime() throws Exception {
        _test(new ProtocolTestStruct.Builder().setDateTimeField(DateTime.now()));
    }

    @Test
    public void testDecimal() throws Exception {
        _test(new ProtocolTestStruct.Builder().setDecimalField(new BigDecimal(
                100)));
    }

    @Test
    public void testEmailAddress() throws Exception {
        _test(new ProtocolTestStruct.Builder()
                .setEmailAddressField(new EmailAddress("test@example.com")));
    }

    @Test
    public void testEnum() throws Exception {
        _test(new ProtocolTestStruct.Builder()
                .setEnumField(ProtocolTestEnum.ENUMERATOR2));
    }

    @Test
    public void testI16() throws Exception {
        _test(new ProtocolTestStruct.Builder().setI16Field((short) 1));
    }

    @Test
    public void testI32() throws Exception {
        _test(new ProtocolTestStruct.Builder().setI32Field(1));
    }

    @Test
    public void testI64() throws Exception {
        _test(new ProtocolTestStruct.Builder().setI64Field(1));
    }

    @Test
    public void testListString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setListStringField(ImmutableList
                .of("test")));

        // Empty list
        _test(new ProtocolTestStruct.Builder().setListStringField(ImmutableList
                .<String> of()));
    }

    @Test
    public void testMapStringString() throws Exception {
        _test(new ProtocolTestStruct.Builder()
                .setMapStringStringField(ImmutableMap
                        .of("testkey", "testvalue")));

        // Empty map
        _test(new ProtocolTestStruct.Builder()
                .setMapStringStringField(ImmutableMap.<String, String> of()));
    }

    @Test
    public void testSetString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setSetStringField(ImmutableSet
                .of("test")));

        // Empty set
        _test(new ProtocolTestStruct.Builder().setSetStringField(ImmutableSet
                .<String> of()));
    }

    @Test
    public void testString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setStringField("test"));
    }

    @Test
    public void testStruct() throws Exception {
        _test(new ProtocolTestStruct.Builder()
                .setStructField(new ProtocolTestStruct.Builder().setI32Field(1)
                        .setRequiredI32Field(1).setRequiredStringField("test")
                        .build()));

        // Empty struct
        _test(new ProtocolTestStruct.Builder()
                .setStructField(new ProtocolTestStruct.Builder()
                        .setRequiredI32Field(1).setRequiredStringField("test")
                        .build()));
    }

    @Test
    public void testUrl() throws Exception {
        _test(new ProtocolTestStruct.Builder().setUrlField(Url
                .parse("http://example.com/test")));
    }

    protected abstract void _test(final ProtocolTestStruct expected)
            throws Exception;

    protected void _test(final ProtocolTestStruct.Builder expectedBuilder)
            throws Exception {
        _test(expectedBuilder.setRequiredI32Field(1)
                .setRequiredStringField("test").build());
    }
}
