package org.thryft.protocol.test;

public final class ProtocolTestStructFaker {
    public static org.thryft.protocol.test.ProtocolTestStruct fake() {
        final org.thryft.protocol.test.ProtocolTestStruct.Builder builder = new org.thryft.protocol.test.ProtocolTestStruct.Builder();
        builder.setBinaryField(org.thryft.Faker.randomBinary());
        builder.setBoolField(org.thryft.Faker.randomBool());
        builder.setDateTimeField(org.joda.time.DateTime.now());
        builder.setDecimalField(org.thryft.Faker.randomDecimal());
        builder.setEmailAddressField(org.thryft.Faker.Internet.email());
        builder.setEnumField(org.thryft.Faker
                .randomEnum(com.google.common.collect.ImmutableList.of(
                        org.thryft.protocol.test.ProtocolTestEnum.ENUMERATOR1,
                        org.thryft.protocol.test.ProtocolTestEnum.ENUMERATOR2)));
        builder.setI8Field(org.thryft.Faker.randomI8());
        builder.setI16Field(org.thryft.Faker.randomI16());
        builder.setI32Field(org.thryft.Faker.randomI32());
        builder.setI64Field(org.thryft.Faker.randomI64());
        builder.setListStringField(com.google.common.collect.ImmutableList
                .of(org.thryft.Faker.Lorem.word()));
        builder.setMapStringStringField(com.google.common.collect.ImmutableMap
                .of(org.thryft.Faker.Lorem.word(),
                        org.thryft.Faker.Lorem.word()));
        builder.setRequiredI32Field(org.thryft.Faker.randomI32());
        builder.setRequiredStringField(org.thryft.Faker.Name.firstName());
        builder.setSetStringField(com.google.common.collect.ImmutableSet
                .of(org.thryft.Faker.Lorem.word()));
        builder.setStringField(org.thryft.Faker.Lorem.word());
        // builder.setStructField(org.thryft.protocol.test.ProtocolTestStructFaker
        // .fake());
        builder.setUrlField(org.thryft.Faker.Internet.url());
        return builder.build();
    }

    private ProtocolTestStructFaker() {
    }
}
