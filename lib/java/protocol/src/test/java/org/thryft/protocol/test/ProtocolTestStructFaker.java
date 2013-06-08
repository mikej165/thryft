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

public final class ProtocolTestStructFaker {
    public static org.thryft.protocol.test.ProtocolTestStruct fake() {
        org.thryft.protocol.test.ProtocolTestStruct.Builder builder = new org.thryft.protocol.test.ProtocolTestStruct.Builder();
        builder.setBinaryField(org.thryft.Faker.randomBinary());
        builder.setBoolField(org.thryft.Faker.randomBool());
        builder.setByteField(org.thryft.Faker.randomByte());
        builder.setDateTimeField(org.joda.time.DateTime.now());
        builder.setDecimalField(org.thryft.Faker.randomDecimal());
        builder.setEmailAddressField(org.thryft.Faker.Internet.email());
        builder.setEnumField(org.thryft.Faker.randomEnum(com.google.common.collect.ImmutableList.of(org.thryft.protocol.test.ProtocolTestEnum.ENUMERATOR1, org.thryft.protocol.test.ProtocolTestEnum.ENUMERATOR2)));
        builder.setI16Field(org.thryft.Faker.randomI16());
        builder.setI32Field(org.thryft.Faker.randomI32());
        builder.setI64Field(org.thryft.Faker.randomI64());
        builder.setListStringField(com.google.common.collect.ImmutableList.of(org.thryft.Faker.Lorem.word()));
        builder.setMapStringStringField(com.google.common.collect.ImmutableMap.of(org.thryft.Faker.Lorem.word(), org.thryft.Faker.Lorem.word()));
        builder.setRequiredI32Field(org.thryft.Faker.randomI32());
        builder.setRequiredStringField(org.thryft.Faker.Name.firstName());
        builder.setSetStringField(com.google.common.collect.ImmutableSet.of(org.thryft.Faker.Lorem.word()));
        builder.setStringField(org.thryft.Faker.Lorem.word());
        builder.setStructField(org.thryft.protocol.test.ProtocolTestStructFaker.fake());
        builder.setUrlField(org.thryft.Faker.Internet.url());
        return builder.build();
    }

    private ProtocolTestStructFaker() {
    }
}
