package org.thryft.protocol.test;

public class NestedProtocolTestStruct implements org.thryft.Struct {
    public static class Builder {
        public Builder() {
            requiredI32Field = 0;
            requiredStringField = null;
            binaryField = com.google.common.base.Optional.absent();
            boolField = com.google.common.base.Optional.absent();
            byteField = com.google.common.base.Optional.absent();
            dateTimeField = com.google.common.base.Optional.absent();
            decimalField = com.google.common.base.Optional.absent();
            emailAddressField = com.google.common.base.Optional.absent();
            enumField = com.google.common.base.Optional.absent();
            i16Field = com.google.common.base.Optional.absent();
            i32Field = com.google.common.base.Optional.absent();
            i64Field = com.google.common.base.Optional.absent();
            stringListField = com.google.common.base.Optional.absent();
            stringStringMapField = com.google.common.base.Optional.absent();
            stringSetField = com.google.common.base.Optional.absent();
            stringField = com.google.common.base.Optional.absent();
            urlField = com.google.common.base.Optional.absent();
        }

        public Builder(final NestedProtocolTestStruct other) {
            this.requiredI32Field = other.getRequiredI32Field();
            this.requiredStringField = other.getRequiredStringField();
            this.binaryField = other.getBinaryField();
            this.boolField = other.getBoolField();
            this.byteField = other.getByteField();
            this.dateTimeField = other.getDateTimeField();
            this.decimalField = other.getDecimalField();
            this.emailAddressField = other.getEmailAddressField();
            this.enumField = other.getEnumField();
            this.i16Field = other.getI16Field();
            this.i32Field = other.getI32Field();
            this.i64Field = other.getI64Field();
            this.stringListField = other.getStringListField();
            this.stringStringMapField = other.getStringStringMapField();
            this.stringSetField = other.getStringSetField();
            this.stringField = other.getStringField();
            this.urlField = other.getUrlField();
        }

        protected NestedProtocolTestStruct _build(final i32 requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<boolean> boolField, final com.google.common.base.Optional<byte> byteField, final com.google.common.base.Optional<long> dateTimeField, final com.google.common.base.Optional<String> decimalField, final com.google.common.base.Optional<String> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<short> i16Field, final com.google.common.base.Optional<i32> i32Field, final com.google.common.base.Optional<long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<String> urlField) {
            return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField);
        }

        public NestedProtocolTestStruct build() {
            return _build(com.google.common.base.Preconditions.checkNotNull(requiredI32Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredI32Field"), com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing binaryField"), com.google.common.base.Preconditions.checkNotNull(boolField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing boolField"), com.google.common.base.Preconditions.checkNotNull(byteField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing byteField"), com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing dateTimeField"), com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing decimalField"), com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing emailAddressField"), com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing enumField"), com.google.common.base.Preconditions.checkNotNull(i16Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i16Field"), com.google.common.base.Preconditions.checkNotNull(i32Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i32Field"), com.google.common.base.Preconditions.checkNotNull(i64Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i64Field"), com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringListField"), com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringStringMapField"), com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringSetField"), com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringField"), com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing urlField"));
        }

        public final com.google.common.base.Optional<byte[]> getBinaryField() {
            return binaryField;
        }

        public final com.google.common.base.Optional<boolean> getBoolField() {
            return boolField;
        }

        public final com.google.common.base.Optional<byte> getByteField() {
            return byteField;
        }

        public final com.google.common.base.Optional<long> getDateTimeField() {
            return dateTimeField;
        }

        public final com.google.common.base.Optional<String> getDecimalField() {
            return decimalField;
        }

        public final com.google.common.base.Optional<String> getEmailAddressField() {
            return emailAddressField;
        }

        public final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> getEnumField() {
            return enumField;
        }

        public final com.google.common.base.Optional<short> getI16Field() {
            return i16Field;
        }

        public final com.google.common.base.Optional<i32> getI32Field() {
            return i32Field;
        }

        public final com.google.common.base.Optional<long> getI64Field() {
            return i64Field;
        }

        public final i32 getRequiredI32Field() {
            return requiredI32Field;
        }

        public final String getRequiredStringField() {
            return requiredStringField;
        }

        public final com.google.common.base.Optional<String> getStringField() {
            return stringField;
        }

        public final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> getStringListField() {
            return stringListField;
        }

        public final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> getStringSetField() {
            return stringSetField;
        }

        public final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> getStringStringMapField() {
            return stringStringMapField;
        }

        public final com.google.common.base.Optional<String> getUrlField() {
            return urlField;
        }

        public Builder readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
            switch (type) {
            case LIST:
                return readAsList(iprot);
            case STRUCT:
                return readAsStruct(iprot);
            default:
                throw new IllegalArgumentException("cannot read as " + type);
            }
        }

        public Builder readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            final org.thryft.protocol.ListBegin __list = iprot.readListBegin();
            requiredI32Field = iprot.readI32();
            requiredStringField = iprot.readString();
            if (__list.getSize() > 2) {
                binaryField = com.google.common.base.Optional.of(iprot.readBinary());
            }
            if (__list.getSize() > 3) {
                boolField = com.google.common.base.Optional.of(iprot.readBool());
            }
            if (__list.getSize() > 4) {
                try {
                    byteField = com.google.common.base.Optional.of(iprot.readByte());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 5) {
                try {
                    dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                } catch (final IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 6) {
                try {
                    decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 7) {
                emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
            }
            if (__list.getSize() > 8) {
                try {
                    enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                } catch (final IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 9) {
                try {
                    i16Field = com.google.common.base.Optional.of(iprot.readI16());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 10) {
                try {
                    i32Field = com.google.common.base.Optional.of(iprot.readI32());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 11) {
                try {
                    i64Field = com.google.common.base.Optional.of(iprot.readI64());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 12) {
                try {
                    stringListField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableList<String>>() {
                        @Override
                        public com.google.common.collect.ImmutableList<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.ListBegin sequenceBegin = iprot.readListBegin();
                                final com.google.common.collect.ImmutableList.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableList.builder();
                                for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                    sequenceBuilder.add(iprot.readString());
                                }
                                iprot.readListEnd();
                                return sequenceBuilder.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                }
            }
            if (__list.getSize() > 13) {
                try {
                    stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                        @Override
                        public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
                                final com.google.common.collect.ImmutableMap.Builder<String, String> map = com.google.common.collect.ImmutableMap.builder();
                                for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                                    final String key;
                                    key = iprot.readString();
                                    final String value;
                                    value = iprot.readString();
                                    map.put(key, value);
                                }
                                iprot.readMapEnd();
                                return map.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                return com.google.common.collect.ImmutableMap.of();
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                }
            }
            if (__list.getSize() > 14) {
                try {
                    stringSetField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableSet<String>>() {
                        @Override
                        public com.google.common.collect.ImmutableSet<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.SetBegin sequenceBegin = iprot.readSetBegin();
                                final com.google.common.collect.ImmutableSet.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableSet.builder();
                                for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                    sequenceBuilder.add(iprot.readString());
                                }
                                iprot.readSetEnd();
                                return sequenceBuilder.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                }
            }
            if (__list.getSize() > 15) {
                stringField = com.google.common.base.Optional.of(iprot.readString());
            }
            if (__list.getSize() > 16) {
                try {
                    urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            }
            iprot.readListEnd();
            return this;
        }

        public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
        }

        public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            iprot.readStructBegin();
            while (true) {
                final org.thryft.protocol.FieldBegin ifield = iprot.readFieldBegin();
                if (ifield.getType() == org.thryft.protocol.Type.STOP) {
                    break;
                }
                switch (ifield.getName()) {
                case "required_i32_field": {
                    requiredI32Field = iprot.readI32();
                    break;
                }
                case "required_string_field": {
                    requiredStringField = iprot.readString();
                    break;
                }
                case "binary_field": {
                    binaryField = com.google.common.base.Optional.of(iprot.readBinary());
                    break;
                }
                case "bool_field": {
                    boolField = com.google.common.base.Optional.of(iprot.readBool());
                    break;
                }
                case "byte_field": {
                    try {
                        byteField = com.google.common.base.Optional.of(iprot.readByte());
                    } catch (final NumberFormatException e) {
                    }
                    break;
                }
                case "date_time_field": {
                    try {
                        dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                    } catch (final IllegalArgumentException e) {
                    }
                    break;
                }
                case "decimal_field": {
                    try {
                        decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                    } catch (final NumberFormatException e) {
                    }
                    break;
                }
                case "email_address_field": {
                    emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                    break;
                }
                case "enum_field": {
                    try {
                        enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                    } catch (final IllegalArgumentException e) {
                    }
                    break;
                }
                case "i16_field": {
                    try {
                        i16Field = com.google.common.base.Optional.of(iprot.readI16());
                    } catch (final NumberFormatException e) {
                    }
                    break;
                }
                case "i32_field": {
                    try {
                        i32Field = com.google.common.base.Optional.of(iprot.readI32());
                    } catch (final NumberFormatException e) {
                    }
                    break;
                }
                case "i64_field": {
                    try {
                        i64Field = com.google.common.base.Optional.of(iprot.readI64());
                    } catch (final NumberFormatException e) {
                    }
                    break;
                }
                case "string_list_field": {
                    try {
                        stringListField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableList<String>>() {
                            @Override
                            public com.google.common.collect.ImmutableList<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                                try {
                                    final org.thryft.protocol.ListBegin sequenceBegin = iprot.readListBegin();
                                    final com.google.common.collect.ImmutableList.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableList.builder();
                                    for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                        sequenceBuilder.add(iprot.readString());
                                    }
                                    iprot.readListEnd();
                                    return sequenceBuilder.build();
                                } catch (final org.thryft.protocol.InputProtocolException e) {
                                    throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                                }
                            }
                        }).apply(iprot));
                    } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                    }
                    break;
                }
                case "string_string_map_field": {
                    try {
                        stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                            @Override
                            public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
                                try {
                                    final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
                                    final com.google.common.collect.ImmutableMap.Builder<String, String> map = com.google.common.collect.ImmutableMap.builder();
                                    for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                                        final String key;
                                        key = iprot.readString();
                                        final String value;
                                        value = iprot.readString();
                                        map.put(key, value);
                                    }
                                    iprot.readMapEnd();
                                    return map.build();
                                } catch (final org.thryft.protocol.InputProtocolException e) {
                                    return com.google.common.collect.ImmutableMap.of();
                                }
                            }
                        }).apply(iprot));
                    } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                    }
                    break;
                }
                case "string_set_field": {
                    try {
                        stringSetField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableSet<String>>() {
                            @Override
                            public com.google.common.collect.ImmutableSet<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                                try {
                                    final org.thryft.protocol.SetBegin sequenceBegin = iprot.readSetBegin();
                                    final com.google.common.collect.ImmutableSet.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableSet.builder();
                                    for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                        sequenceBuilder.add(iprot.readString());
                                    }
                                    iprot.readSetEnd();
                                    return sequenceBuilder.build();
                                } catch (final org.thryft.protocol.InputProtocolException e) {
                                    throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                                }
                            }
                        }).apply(iprot));
                    } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                    }
                    break;
                }
                case "string_field": {
                    stringField = com.google.common.base.Optional.of(iprot.readString());
                    break;
                }
                case "url_field": {
                    try {
                        urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                    } catch (final java.lang.IllegalArgumentException e) {
                    }
                    break;
                }
                default:
                    if (unknownFieldCallback.isPresent()) {
                        unknownFieldCallback.get().apply(ifield);
                    }
                    break;
                }
                iprot.readFieldEnd();
            }
            iprot.readStructEnd();
            return this;
        }

        public Builder setBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
            this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField);
            return this;
        }

        public Builder setBinaryField(@javax.annotation.Nullable final byte[] binaryField) {
            this.binaryField = com.google.common.base.Optional.fromNullable(binaryField);
            return this;
        }

        public Builder setBoolField(final com.google.common.base.Optional<boolean> boolField) {
            this.boolField = com.google.common.base.Preconditions.checkNotNull(boolField);
            return this;
        }

        public Builder setBoolField(@javax.annotation.Nullable final boolean boolField) {
            this.boolField = com.google.common.base.Optional.fromNullable(boolField);
            return this;
        }

        public Builder setByteField(final com.google.common.base.Optional<byte> byteField) {
            this.byteField = com.google.common.base.Preconditions.checkNotNull(byteField);
            return this;
        }

        public Builder setByteField(@javax.annotation.Nullable final byte byteField) {
            this.byteField = com.google.common.base.Optional.fromNullable(byteField);
            return this;
        }

        public Builder setDateTimeField(final com.google.common.base.Optional<long> dateTimeField) {
            this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField);
            return this;
        }

        public Builder setDateTimeField(@javax.annotation.Nullable final long dateTimeField) {
            this.dateTimeField = com.google.common.base.Optional.fromNullable(dateTimeField);
            return this;
        }

        public Builder setDecimalField(final com.google.common.base.Optional<String> decimalField) {
            this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField);
            return this;
        }

        public Builder setDecimalField(@javax.annotation.Nullable final String decimalField) {
            this.decimalField = com.google.common.base.Optional.fromNullable(decimalField);
            return this;
        }

        public Builder setEmailAddressField(final com.google.common.base.Optional<String> emailAddressField) {
            this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField);
            return this;
        }

        public Builder setEmailAddressField(@javax.annotation.Nullable final String emailAddressField) {
            this.emailAddressField = com.google.common.base.Optional.fromNullable(emailAddressField);
            return this;
        }

        public Builder setEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
            this.enumField = com.google.common.base.Preconditions.checkNotNull(enumField);
            return this;
        }

        public Builder setEnumField(@javax.annotation.Nullable final org.thryft.protocol.test.ProtocolTestEnum enumField) {
            this.enumField = com.google.common.base.Optional.fromNullable(enumField);
            return this;
        }

        public Builder setI16Field(final com.google.common.base.Optional<short> i16Field) {
            this.i16Field = com.google.common.base.Preconditions.checkNotNull(i16Field);
            return this;
        }

        public Builder setI16Field(@javax.annotation.Nullable final short i16Field) {
            this.i16Field = com.google.common.base.Optional.fromNullable(i16Field);
            return this;
        }

        public Builder setI32Field(final com.google.common.base.Optional<i32> i32Field) {
            this.i32Field = com.google.common.base.Preconditions.checkNotNull(i32Field);
            return this;
        }

        public Builder setI32Field(@javax.annotation.Nullable final i32 i32Field) {
            this.i32Field = com.google.common.base.Optional.fromNullable(i32Field);
            return this;
        }

        public Builder setI64Field(final com.google.common.base.Optional<long> i64Field) {
            this.i64Field = com.google.common.base.Preconditions.checkNotNull(i64Field);
            return this;
        }

        public Builder setI64Field(@javax.annotation.Nullable final long i64Field) {
            this.i64Field = com.google.common.base.Optional.fromNullable(i64Field);
            return this;
        }

        public Builder setIfPresent(final NestedProtocolTestStruct other) {
            com.google.common.base.Preconditions.checkNotNull(other);

            setRequiredI32Field(other.getRequiredI32Field());
            setRequiredStringField(other.getRequiredStringField());
            if (other.getBinaryField().isPresent()) {
                setBinaryField(other.getBinaryField());
            }
            if (other.getBoolField().isPresent()) {
                setBoolField(other.getBoolField());
            }
            if (other.getByteField().isPresent()) {
                setByteField(other.getByteField());
            }
            if (other.getDateTimeField().isPresent()) {
                setDateTimeField(other.getDateTimeField());
            }
            if (other.getDecimalField().isPresent()) {
                setDecimalField(other.getDecimalField());
            }
            if (other.getEmailAddressField().isPresent()) {
                setEmailAddressField(other.getEmailAddressField());
            }
            if (other.getEnumField().isPresent()) {
                setEnumField(other.getEnumField());
            }
            if (other.getI16Field().isPresent()) {
                setI16Field(other.getI16Field());
            }
            if (other.getI32Field().isPresent()) {
                setI32Field(other.getI32Field());
            }
            if (other.getI64Field().isPresent()) {
                setI64Field(other.getI64Field());
            }
            if (other.getStringListField().isPresent()) {
                setStringListField(other.getStringListField());
            }
            if (other.getStringStringMapField().isPresent()) {
                setStringStringMapField(other.getStringStringMapField());
            }
            if (other.getStringSetField().isPresent()) {
                setStringSetField(other.getStringSetField());
            }
            if (other.getStringField().isPresent()) {
                setStringField(other.getStringField());
            }
            if (other.getUrlField().isPresent()) {
                setUrlField(other.getUrlField());
            }

            return this;
        }

        public Builder setRequiredI32Field(final i32 requiredI32Field) {
            this.requiredI32Field = com.google.common.base.Preconditions.checkNotNull(requiredI32Field);
            return this;
        }

        public Builder setRequiredStringField(final String requiredStringField) {
            this.requiredStringField = com.google.common.base.Preconditions.checkNotNull(requiredStringField);
            return this;
        }

        public Builder setStringField(final com.google.common.base.Optional<String> stringField) {
            this.stringField = com.google.common.base.Preconditions.checkNotNull(stringField);
            return this;
        }

        public Builder setStringField(@javax.annotation.Nullable final String stringField) {
            this.stringField = com.google.common.base.Optional.fromNullable(stringField);
            return this;
        }

        public Builder setStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
            this.stringListField = com.google.common.base.Preconditions.checkNotNull(stringListField);
            return this;
        }

        public Builder setStringListField(@javax.annotation.Nullable final com.google.common.collect.ImmutableList<String> stringListField) {
            this.stringListField = com.google.common.base.Optional.fromNullable(stringListField);
            return this;
        }

        public Builder setStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
            this.stringSetField = com.google.common.base.Preconditions.checkNotNull(stringSetField);
            return this;
        }

        public Builder setStringSetField(@javax.annotation.Nullable final com.google.common.collect.ImmutableSet<String> stringSetField) {
            this.stringSetField = com.google.common.base.Optional.fromNullable(stringSetField);
            return this;
        }

        public Builder setStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
            this.stringStringMapField = com.google.common.base.Preconditions.checkNotNull(stringStringMapField);
            return this;
        }

        public Builder setStringStringMapField(@javax.annotation.Nullable final com.google.common.collect.ImmutableMap<String, String> stringStringMapField) {
            this.stringStringMapField = com.google.common.base.Optional.fromNullable(stringStringMapField);
            return this;
        }

        public Builder setUrlField(final com.google.common.base.Optional<String> urlField) {
            this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField);
            return this;
        }

        public Builder setUrlField(@javax.annotation.Nullable final String urlField) {
            this.urlField = com.google.common.base.Optional.fromNullable(urlField);
            return this;
        }

        @SuppressWarnings({"unchecked"})
        public Builder set(final String name, @javax.annotation.Nullable final java.lang.Object value) {
            com.google.common.base.Preconditions.checkNotNull(name);

            switch (name.toLowerCase()) {
            case "required_i32_field": setRequiredI32Field((i32)value); return this;
            case "required_string_field": setRequiredStringField((String)value); return this;
            case "binary_field": setBinaryField((byte[])value); return this;
            case "bool_field": setBoolField((boolean)value); return this;
            case "byte_field": setByteField((byte)value); return this;
            case "date_time_field": setDateTimeField((long)value); return this;
            case "decimal_field": setDecimalField((String)value); return this;
            case "email_address_field": setEmailAddressField((String)value); return this;
            case "enum_field": setEnumField((org.thryft.protocol.test.ProtocolTestEnum)value); return this;
            case "i16_field": setI16Field((short)value); return this;
            case "i32_field": setI32Field((i32)value); return this;
            case "i64_field": setI64Field((long)value); return this;
            case "string_list_field": setStringListField((com.google.common.collect.ImmutableList<String>)value); return this;
            case "string_string_map_field": setStringStringMapField((com.google.common.collect.ImmutableMap<String, String>)value); return this;
            case "string_set_field": setStringSetField((com.google.common.collect.ImmutableSet<String>)value); return this;
            case "string_field": setStringField((String)value); return this;
            case "url_field": setUrlField((String)value); return this;
            default:
                throw new IllegalArgumentException(name);
            }
        }

        public Builder unsetBinaryField() {
            this.binaryField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetBoolField() {
            this.boolField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetByteField() {
            this.byteField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetDateTimeField() {
            this.dateTimeField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetDecimalField() {
            this.decimalField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetEmailAddressField() {
            this.emailAddressField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetEnumField() {
            this.enumField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetI16Field() {
            this.i16Field = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetI32Field() {
            this.i32Field = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetI64Field() {
            this.i64Field = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetRequiredI32Field() {
            this.requiredI32Field = 0;
            return this;
        }

        public Builder unsetRequiredStringField() {
            this.requiredStringField = null;
            return this;
        }

        public Builder unsetStringField() {
            this.stringField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetStringListField() {
            this.stringListField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetStringSetField() {
            this.stringSetField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetStringStringMapField() {
            this.stringStringMapField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unsetUrlField() {
            this.urlField = com.google.common.base.Optional.absent();
            return this;
        }

        public Builder unset(final String name) {
            com.google.common.base.Preconditions.checkNotNull(name);

            switch (name.toLowerCase()) {
            case "required_i32_field": return unsetRequiredI32Field();
            case "required_string_field": return unsetRequiredStringField();
            case "binary_field": return unsetBinaryField();
            case "bool_field": return unsetBoolField();
            case "byte_field": return unsetByteField();
            case "date_time_field": return unsetDateTimeField();
            case "decimal_field": return unsetDecimalField();
            case "email_address_field": return unsetEmailAddressField();
            case "enum_field": return unsetEnumField();
            case "i16_field": return unsetI16Field();
            case "i32_field": return unsetI32Field();
            case "i64_field": return unsetI64Field();
            case "string_list_field": return unsetStringListField();
            case "string_string_map_field": return unsetStringStringMapField();
            case "string_set_field": return unsetStringSetField();
            case "string_field": return unsetStringField();
            case "url_field": return unsetUrlField();
            default:
                throw new IllegalArgumentException(name);
            }
        }

        private i32 requiredI32Field;
        private String requiredStringField;
        private com.google.common.base.Optional<byte[]> binaryField;
        private com.google.common.base.Optional<boolean> boolField;
        private com.google.common.base.Optional<byte> byteField;
        private com.google.common.base.Optional<long> dateTimeField;
        private com.google.common.base.Optional<String> decimalField;
        private com.google.common.base.Optional<String> emailAddressField;
        private com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;
        private com.google.common.base.Optional<short> i16Field;
        private com.google.common.base.Optional<i32> i32Field;
        private com.google.common.base.Optional<long> i64Field;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;
        private com.google.common.base.Optional<String> stringField;
        private com.google.common.base.Optional<String> urlField;
    }

    @SuppressWarnings("serial")
    public enum FieldMetadata implements org.thryft.CompoundType.FieldMetadata {
        REQUIRED_I32_FIELD("requiredI32Field", new com.google.common.reflect.TypeToken<i32>() {}, true, 0, "required_i32_field", org.thryft.protocol.Type.I32),
        REQUIRED_STRING_FIELD("requiredStringField", new com.google.common.reflect.TypeToken<String>() {}, true, 0, "required_string_field", org.thryft.protocol.Type.STRING),
        BINARY_FIELD("binaryField", new com.google.common.reflect.TypeToken<byte[]>() {}, false, 0, "binary_field", org.thryft.protocol.Type.STRING),
        BOOL_FIELD("boolField", new com.google.common.reflect.TypeToken<boolean>() {}, false, 0, "bool_field", org.thryft.protocol.Type.BOOL),
        BYTE_FIELD("byteField", new com.google.common.reflect.TypeToken<byte>() {}, false, 0, "byte_field", org.thryft.protocol.Type.BYTE),
        DATE_TIME_FIELD("dateTimeField", new com.google.common.reflect.TypeToken<long>() {}, false, 0, "date_time_field", org.thryft.protocol.Type.I64),
        DECIMAL_FIELD("decimalField", new com.google.common.reflect.TypeToken<String>() {}, false, 0, "decimal_field", org.thryft.protocol.Type.STRING),
        EMAIL_ADDRESS_FIELD("emailAddressField", new com.google.common.reflect.TypeToken<String>() {}, false, 0, "email_address_field", org.thryft.protocol.Type.STRING),
        ENUM_FIELD("enumField", new com.google.common.reflect.TypeToken<org.thryft.protocol.test.ProtocolTestEnum>() {}, false, 0, "enum_field", org.thryft.protocol.Type.STRING),
        I16_FIELD("i16Field", new com.google.common.reflect.TypeToken<short>() {}, false, 0, "i16_field", org.thryft.protocol.Type.I16),
        I32_FIELD("i32Field", new com.google.common.reflect.TypeToken<i32>() {}, false, 0, "i32_field", org.thryft.protocol.Type.I32),
        I64_FIELD("i64Field", new com.google.common.reflect.TypeToken<long>() {}, false, 0, "i64_field", org.thryft.protocol.Type.I64),
        STRING_LIST_FIELD("stringListField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableList<String>>() {}, false, 0, "string_list_field", org.thryft.protocol.Type.LIST),
        STRING_STRING_MAP_FIELD("stringStringMapField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableMap<String, String>>() {}, false, 0, "string_string_map_field", org.thryft.protocol.Type.MAP),
        STRING_SET_FIELD("stringSetField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableSet<String>>() {}, false, 0, "string_set_field", org.thryft.protocol.Type.SET),
        STRING_FIELD("stringField", new com.google.common.reflect.TypeToken<String>() {}, false, 0, "string_field", org.thryft.protocol.Type.STRING),
        URL_FIELD("urlField", new com.google.common.reflect.TypeToken<String>() {}, false, 0, "url_field", org.thryft.protocol.Type.STRING);

        @Override
        public String getJavaName() {
            return javaName;
        }

        @Override
        public com.google.common.reflect.TypeToken<?> getJavaType() {
            return javaType;
        }

        @Override
        public int getThriftId() {
            return thriftId;
        }

        @Override
        public String getThriftProtocolKey() {
            return thriftProtocolKey;
        }

        @Override
        public org.thryft.protocol.Type getThriftProtocolType() {
            return thriftProtocolType;
        }

        @Override
        public String getThriftName() {
            return thriftName;
        }

        @Override
        public boolean hasThriftId() {
            return thriftId != org.thryft.protocol.FieldBegin.ABSENT_ID;
        }

        @Override
        public boolean isRequired()  {
            return required;
        }

        public static FieldMetadata valueOfJavaName(final String javaName) {
            switch (javaName) {
            case "requiredI32Field": return REQUIRED_I32_FIELD;
            case "requiredStringField": return REQUIRED_STRING_FIELD;
            case "binaryField": return BINARY_FIELD;
            case "boolField": return BOOL_FIELD;
            case "byteField": return BYTE_FIELD;
            case "dateTimeField": return DATE_TIME_FIELD;
            case "decimalField": return DECIMAL_FIELD;
            case "emailAddressField": return EMAIL_ADDRESS_FIELD;
            case "enumField": return ENUM_FIELD;
            case "i16Field": return I16_FIELD;
            case "i32Field": return I32_FIELD;
            case "i64Field": return I64_FIELD;
            case "stringListField": return STRING_LIST_FIELD;
            case "stringStringMapField": return STRING_STRING_MAP_FIELD;
            case "stringSetField": return STRING_SET_FIELD;
            case "stringField": return STRING_FIELD;
            case "urlField": return URL_FIELD;
            default:
                throw new IllegalArgumentException(javaName);
            }
        }

        public static FieldMetadata valueOfThriftName(final String thriftName) {
            switch (thriftName) {
            case "required_i32_field": return REQUIRED_I32_FIELD;
            case "required_string_field": return REQUIRED_STRING_FIELD;
            case "binary_field": return BINARY_FIELD;
            case "bool_field": return BOOL_FIELD;
            case "byte_field": return BYTE_FIELD;
            case "date_time_field": return DATE_TIME_FIELD;
            case "decimal_field": return DECIMAL_FIELD;
            case "email_address_field": return EMAIL_ADDRESS_FIELD;
            case "enum_field": return ENUM_FIELD;
            case "i16_field": return I16_FIELD;
            case "i32_field": return I32_FIELD;
            case "i64_field": return I64_FIELD;
            case "string_list_field": return STRING_LIST_FIELD;
            case "string_string_map_field": return STRING_STRING_MAP_FIELD;
            case "string_set_field": return STRING_SET_FIELD;
            case "string_field": return STRING_FIELD;
            case "url_field": return URL_FIELD;
            default:
                throw new IllegalArgumentException(thriftName);
            }
        }

        private FieldMetadata(final String javaName, final com.google.common.reflect.TypeToken<?> javaType, final boolean required, final int thriftId, final String thriftName, final org.thryft.protocol.Type thriftProtocolType) {
            this.javaName = javaName;
            this.javaType = javaType;
            this.required = required;
            this.thriftId = thriftId;
            this.thriftName = thriftName;
            if (thriftId != org.thryft.protocol.FieldBegin.ABSENT_ID) {
                this.thriftProtocolKey = Integer.toString(thriftId) + ":" + thriftName;
            } else {
                this.thriftProtocolKey = thriftName;
            }
            this.thriftProtocolType = thriftProtocolType;
        }

        private final String javaName;
        private final com.google.common.reflect.TypeToken<?> javaType;
        private final boolean required;
        private final int thriftId;
        private final String thriftName;
        private final String thriftProtocolKey;
        private final org.thryft.protocol.Type thriftProtocolType;
    }

    /**
     * Copy constructor
     */
    public NestedProtocolTestStruct(final NestedProtocolTestStruct other) {
        this(other.getRequiredI32Field(), other.getRequiredStringField(), other.getBinaryField(), other.getBoolField(), other.getByteField(), other.getDateTimeField(), other.getDecimalField(), other.getEmailAddressField(), other.getEnumField(), other.getI16Field(), other.getI32Field(), other.getI64Field(), other.getStringListField(), other.getStringStringMapField(), other.getStringSetField(), other.getStringField(), other.getUrlField());
    }

    /**
     * Required constructor
     */
    public NestedProtocolTestStruct(final i32 requiredI32Field, final String requiredStringField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkStringNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Optional.absent();
        this.boolField = com.google.common.base.Optional.absent();
        this.byteField = com.google.common.base.Optional.absent();
        this.dateTimeField = com.google.common.base.Optional.absent();
        this.decimalField = com.google.common.base.Optional.absent();
        this.emailAddressField = com.google.common.base.Optional.absent();
        this.enumField = com.google.common.base.Optional.absent();
        this.i16Field = com.google.common.base.Optional.absent();
        this.i32Field = com.google.common.base.Optional.absent();
        this.i64Field = com.google.common.base.Optional.absent();
        this.stringListField = com.google.common.base.Optional.absent();
        this.stringStringMapField = com.google.common.base.Optional.absent();
        this.stringSetField = com.google.common.base.Optional.absent();
        this.stringField = com.google.common.base.Optional.absent();
        this.urlField = com.google.common.base.Optional.absent();
    }

    /**
     * Total Nullable constructor
     */
    public NestedProtocolTestStruct(final i32 requiredI32Field, final String requiredStringField, final @javax.annotation.Nullable byte[] binaryField, final @javax.annotation.Nullable boolean boolField, final @javax.annotation.Nullable byte byteField, final @javax.annotation.Nullable long dateTimeField, final @javax.annotation.Nullable String decimalField, final @javax.annotation.Nullable String emailAddressField, final @javax.annotation.Nullable org.thryft.protocol.test.ProtocolTestEnum enumField, final @javax.annotation.Nullable short i16Field, final @javax.annotation.Nullable i32 i32Field, final @javax.annotation.Nullable long i64Field, final @javax.annotation.Nullable com.google.common.collect.ImmutableList<String> stringListField, final @javax.annotation.Nullable com.google.common.collect.ImmutableMap<String, String> stringStringMapField, final @javax.annotation.Nullable com.google.common.collect.ImmutableSet<String> stringSetField, final @javax.annotation.Nullable String stringField, final @javax.annotation.Nullable String urlField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkStringNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Optional.fromNullable(binaryField);
        this.boolField = com.google.common.base.Optional.fromNullable(boolField);
        this.byteField = com.google.common.base.Optional.fromNullable(byteField);
        this.dateTimeField = com.google.common.base.Optional.fromNullable(dateTimeField);
        this.decimalField = com.google.common.base.Optional.fromNullable(decimalField);
        this.emailAddressField = com.google.common.base.Optional.fromNullable(emailAddressField);
        this.enumField = com.google.common.base.Optional.fromNullable(enumField);
        this.i16Field = com.google.common.base.Optional.fromNullable(i16Field);
        this.i32Field = com.google.common.base.Optional.fromNullable(i32Field);
        this.i64Field = com.google.common.base.Optional.fromNullable(i64Field);
        this.stringListField = com.google.common.base.Optional.fromNullable(stringListField);
        this.stringStringMapField = com.google.common.base.Optional.fromNullable(stringStringMapField);
        this.stringSetField = com.google.common.base.Optional.fromNullable(stringSetField);
        this.stringField = org.thryft.Preconditions.checkOptionalStringNotEmpty(com.google.common.base.Optional.fromNullable(stringField), "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is empty");
        this.urlField = com.google.common.base.Optional.fromNullable(urlField);
    }

    /**
     * Optional constructor
     */
    public NestedProtocolTestStruct(final i32 requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<boolean> boolField, final com.google.common.base.Optional<byte> byteField, final com.google.common.base.Optional<long> dateTimeField, final com.google.common.base.Optional<String> decimalField, final com.google.common.base.Optional<String> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<short> i16Field, final com.google.common.base.Optional<i32> i32Field, final com.google.common.base.Optional<long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<String> urlField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkStringNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing binaryField");
        this.boolField = com.google.common.base.Preconditions.checkNotNull(boolField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing boolField");
        this.byteField = com.google.common.base.Preconditions.checkNotNull(byteField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing byteField");
        this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing dateTimeField");
        this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing decimalField");
        this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing emailAddressField");
        this.enumField = com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing enumField");
        this.i16Field = com.google.common.base.Preconditions.checkNotNull(i16Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i16Field");
        this.i32Field = com.google.common.base.Preconditions.checkNotNull(i32Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i32Field");
        this.i64Field = com.google.common.base.Preconditions.checkNotNull(i64Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i64Field");
        this.stringListField = com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringListField");
        this.stringStringMapField = com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringStringMapField");
        this.stringSetField = com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringSetField");
        this.stringField = org.thryft.Preconditions.checkOptionalStringNotEmpty(com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is empty");
        this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing urlField");
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(final NestedProtocolTestStruct other) {
        return new Builder(other);
    }

    public static Builder builder(final com.google.common.base.Optional<NestedProtocolTestStruct> other) {
        return other.isPresent() ? new Builder(other.get()) : new Builder();
    }

    @Override
    public boolean equals(final java.lang.Object otherObject) {
        if (otherObject == this) {
            return true;
        } else if (!(otherObject instanceof NestedProtocolTestStruct)) {
            return false;
        }

        final NestedProtocolTestStruct other = (NestedProtocolTestStruct)otherObject;
        return
            getRequiredI32Field() == other.getRequiredI32Field() &&
            getRequiredStringField().equals(other.getRequiredStringField()) &&
            getBinaryField().equals(other.getBinaryField()) &&
            getBoolField().equals(other.getBoolField()) &&
            getByteField().equals(other.getByteField()) &&
            getDateTimeField().equals(other.getDateTimeField()) &&
            getDecimalField().equals(other.getDecimalField()) &&
            getEmailAddressField().equals(other.getEmailAddressField()) &&
            getEnumField().equals(other.getEnumField()) &&
            getI16Field().equals(other.getI16Field()) &&
            getI32Field().equals(other.getI32Field()) &&
            getI64Field().equals(other.getI64Field()) &&
            getStringListField().equals(other.getStringListField()) &&
            getStringStringMapField().equals(other.getStringStringMapField()) &&
            getStringSetField().equals(other.getStringSetField()) &&
            getStringField().equals(other.getStringField()) &&
            getUrlField().equals(other.getUrlField());
    }

    @Override
    public java.lang.Object get(final String fieldThriftName) {
        return get(FieldMetadata.valueOfThriftName(fieldThriftName));
    }

    @Override
    public java.lang.Object get(final org.thryft.CompoundType.FieldMetadata fieldMetadata) {
        if (!(fieldMetadata instanceof FieldMetadata)) {
            throw new IllegalArgumentException();
        }
        return get((FieldMetadata)fieldMetadata);
    }

    public java.lang.Object get(final FieldMetadata fieldMetadata) {
        switch (fieldMetadata) {
        case REQUIRED_I32_FIELD: return getRequiredI32Field();
        case REQUIRED_STRING_FIELD: return getRequiredStringField();
        case BINARY_FIELD: return getBinaryField();
        case BOOL_FIELD: return getBoolField();
        case BYTE_FIELD: return getByteField();
        case DATE_TIME_FIELD: return getDateTimeField();
        case DECIMAL_FIELD: return getDecimalField();
        case EMAIL_ADDRESS_FIELD: return getEmailAddressField();
        case ENUM_FIELD: return getEnumField();
        case I16_FIELD: return getI16Field();
        case I32_FIELD: return getI32Field();
        case I64_FIELD: return getI64Field();
        case STRING_LIST_FIELD: return getStringListField();
        case STRING_STRING_MAP_FIELD: return getStringStringMapField();
        case STRING_SET_FIELD: return getStringSetField();
        case STRING_FIELD: return getStringField();
        case URL_FIELD: return getUrlField();
        default:
            throw new IllegalStateException();
        }
    }

    public final com.google.common.base.Optional<byte[]> getBinaryField() {
        return binaryField;
    }

    public final com.google.common.base.Optional<boolean> getBoolField() {
        return boolField;
    }

    public final com.google.common.base.Optional<byte> getByteField() {
        return byteField;
    }

    public final com.google.common.base.Optional<long> getDateTimeField() {
        return dateTimeField;
    }

    public final com.google.common.base.Optional<String> getDecimalField() {
        return decimalField;
    }

    public final com.google.common.base.Optional<String> getEmailAddressField() {
        return emailAddressField;
    }

    public final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> getEnumField() {
        return enumField;
    }

    public final com.google.common.base.Optional<short> getI16Field() {
        return i16Field;
    }

    public final com.google.common.base.Optional<i32> getI32Field() {
        return i32Field;
    }

    public final com.google.common.base.Optional<long> getI64Field() {
        return i64Field;
    }

    public final i32 getRequiredI32Field() {
        return requiredI32Field;
    }

    public final String getRequiredStringField() {
        return requiredStringField;
    }

    public final com.google.common.base.Optional<String> getStringField() {
        return stringField;
    }

    public final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> getStringListField() {
        return stringListField;
    }

    public final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> getStringSetField() {
        return stringSetField;
    }

    public final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> getStringStringMapField() {
        return stringStringMapField;
    }

    public final com.google.common.base.Optional<String> getUrlField() {
        return urlField;
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        hashCode = 31 * hashCode + getRequiredI32Field();
        hashCode = 31 * hashCode + getRequiredStringField().hashCode();
        if (getBinaryField().isPresent()) {
            hashCode = 31 * hashCode + java.util.Arrays.hashCode(getBinaryField().get());
        }
        if (getBoolField().isPresent()) {
            hashCode = 31 * hashCode + (getBoolField().get() ? 1 : 0);
        }
        if (getByteField().isPresent()) {
            hashCode = 31 * hashCode + getByteField().get().hashCode();
        }
        if (getDateTimeField().isPresent()) {
            hashCode = 31 * hashCode + getDateTimeField().get().hashCode();
        }
        if (getDecimalField().isPresent()) {
            hashCode = 31 * hashCode + getDecimalField().get().hashCode();
        }
        if (getEmailAddressField().isPresent()) {
            hashCode = 31 * hashCode + getEmailAddressField().get().hashCode();
        }
        if (getEnumField().isPresent()) {
            hashCode = 31 * hashCode + getEnumField().get().ordinal();
        }
        if (getI16Field().isPresent()) {
            hashCode = 31 * hashCode + getI16Field().get().hashCode();
        }
        if (getI32Field().isPresent()) {
            hashCode = 31 * hashCode + getI32Field().get().hashCode();
        }
        if (getI64Field().isPresent()) {
            hashCode = 31 * hashCode + ((int)(getI64Field().get() ^ (getI64Field().get() >>> 32)));
        }
        if (getStringListField().isPresent()) {
            hashCode = 31 * hashCode + getStringListField().get().hashCode();
        }
        if (getStringStringMapField().isPresent()) {
            hashCode = 31 * hashCode + getStringStringMapField().get().hashCode();
        }
        if (getStringSetField().isPresent()) {
            hashCode = 31 * hashCode + getStringSetField().get().hashCode();
        }
        if (getStringField().isPresent()) {
            hashCode = 31 * hashCode + getStringField().get().hashCode();
        }
        if (getUrlField().isPresent()) {
            hashCode = 31 * hashCode + getUrlField().get().hashCode();
        }
        return hashCode;
    }

    @Override
    public boolean isEmpty() {
        return false;
    }

    public static NestedProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
        switch (type) {
        case LIST:
            return readAsList(iprot);
        case STRUCT:
            return readAsStruct(iprot);
        default:
            throw new IllegalArgumentException("cannot read as " + type);
        }
    }

    public static NestedProtocolTestStruct readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        i32 requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<boolean> boolField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<byte> byteField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<long> dateTimeField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> decimalField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> emailAddressField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<short> i16Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<i32> i32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<long> i64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> urlField = com.google.common.base.Optional.absent();

        final org.thryft.protocol.ListBegin __list = iprot.readListBegin();
        requiredI32Field = iprot.readI32();
        requiredStringField = iprot.readString();
        if (__list.getSize() > 2) {
            binaryField = com.google.common.base.Optional.of(iprot.readBinary());
        }
        if (__list.getSize() > 3) {
            boolField = com.google.common.base.Optional.of(iprot.readBool());
        }
        if (__list.getSize() > 4) {
            try {
                byteField = com.google.common.base.Optional.of(iprot.readByte());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 5) {
            try {
                dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
            } catch (final IllegalArgumentException e) {
            }
        }
        if (__list.getSize() > 6) {
            try {
                decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 7) {
            emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
        }
        if (__list.getSize() > 8) {
            try {
                enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
            } catch (final IllegalArgumentException e) {
            }
        }
        if (__list.getSize() > 9) {
            try {
                i16Field = com.google.common.base.Optional.of(iprot.readI16());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 10) {
            try {
                i32Field = com.google.common.base.Optional.of(iprot.readI32());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 11) {
            try {
                i64Field = com.google.common.base.Optional.of(iprot.readI64());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 12) {
            try {
                stringListField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableList<String>>() {
                    @Override
                    public com.google.common.collect.ImmutableList<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                        try {
                            final org.thryft.protocol.ListBegin sequenceBegin = iprot.readListBegin();
                            final com.google.common.collect.ImmutableList.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableList.builder();
                            for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                sequenceBuilder.add(iprot.readString());
                            }
                            iprot.readListEnd();
                            return sequenceBuilder.build();
                        } catch (final org.thryft.protocol.InputProtocolException e) {
                            throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                        }
                    }
                }).apply(iprot));
            } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
            }
        }
        if (__list.getSize() > 13) {
            try {
                stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                    @Override
                    public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
                        try {
                            final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
                            final com.google.common.collect.ImmutableMap.Builder<String, String> map = com.google.common.collect.ImmutableMap.builder();
                            for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                                final String key;
                                key = iprot.readString();
                                final String value;
                                value = iprot.readString();
                                map.put(key, value);
                            }
                            iprot.readMapEnd();
                            return map.build();
                        } catch (final org.thryft.protocol.InputProtocolException e) {
                            return com.google.common.collect.ImmutableMap.of();
                        }
                    }
                }).apply(iprot));
            } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
            }
        }
        if (__list.getSize() > 14) {
            try {
                stringSetField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableSet<String>>() {
                    @Override
                    public com.google.common.collect.ImmutableSet<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                        try {
                            final org.thryft.protocol.SetBegin sequenceBegin = iprot.readSetBegin();
                            final com.google.common.collect.ImmutableSet.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableSet.builder();
                            for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                sequenceBuilder.add(iprot.readString());
                            }
                            iprot.readSetEnd();
                            return sequenceBuilder.build();
                        } catch (final org.thryft.protocol.InputProtocolException e) {
                            throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                        }
                    }
                }).apply(iprot));
            } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
            }
        }
        if (__list.getSize() > 15) {
            stringField = com.google.common.base.Optional.of(iprot.readString());
        }
        if (__list.getSize() > 16) {
            try {
                urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
            } catch (final java.lang.IllegalArgumentException e) {
            }
        }
        iprot.readListEnd();
        try {
            return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField);
        } catch (final IllegalArgumentException | NullPointerException e) {
            throw new org.thryft.protocol.InputProtocolException(e);
        }
    }

    public static NestedProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
    }

    public static NestedProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        i32 requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<boolean> boolField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<byte> byteField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<long> dateTimeField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> decimalField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> emailAddressField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<short> i16Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<i32> i32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<long> i64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> urlField = com.google.common.base.Optional.absent();

        iprot.readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin ifield = iprot.readFieldBegin();
            if (ifield.getType() == org.thryft.protocol.Type.STOP) {
                break;
            }
            switch (ifield.getName()) {
            case "required_i32_field": {
                requiredI32Field = iprot.readI32();
                break;
            }
            case "required_string_field": {
                requiredStringField = iprot.readString();
                break;
            }
            case "binary_field": {
                binaryField = com.google.common.base.Optional.of(iprot.readBinary());
                break;
            }
            case "bool_field": {
                boolField = com.google.common.base.Optional.of(iprot.readBool());
                break;
            }
            case "byte_field": {
                try {
                    byteField = com.google.common.base.Optional.of(iprot.readByte());
                } catch (final NumberFormatException e) {
                }
                break;
            }
            case "date_time_field": {
                try {
                    dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                } catch (final IllegalArgumentException e) {
                }
                break;
            }
            case "decimal_field": {
                try {
                    decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                } catch (final NumberFormatException e) {
                }
                break;
            }
            case "email_address_field": {
                emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                break;
            }
            case "enum_field": {
                try {
                    enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                } catch (final IllegalArgumentException e) {
                }
                break;
            }
            case "i16_field": {
                try {
                    i16Field = com.google.common.base.Optional.of(iprot.readI16());
                } catch (final NumberFormatException e) {
                }
                break;
            }
            case "i32_field": {
                try {
                    i32Field = com.google.common.base.Optional.of(iprot.readI32());
                } catch (final NumberFormatException e) {
                }
                break;
            }
            case "i64_field": {
                try {
                    i64Field = com.google.common.base.Optional.of(iprot.readI64());
                } catch (final NumberFormatException e) {
                }
                break;
            }
            case "string_list_field": {
                try {
                    stringListField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableList<String>>() {
                        @Override
                        public com.google.common.collect.ImmutableList<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.ListBegin sequenceBegin = iprot.readListBegin();
                                final com.google.common.collect.ImmutableList.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableList.builder();
                                for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                    sequenceBuilder.add(iprot.readString());
                                }
                                iprot.readListEnd();
                                return sequenceBuilder.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                }
                break;
            }
            case "string_string_map_field": {
                try {
                    stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                        @Override
                        public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
                                final com.google.common.collect.ImmutableMap.Builder<String, String> map = com.google.common.collect.ImmutableMap.builder();
                                for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                                    final String key;
                                    key = iprot.readString();
                                    final String value;
                                    value = iprot.readString();
                                    map.put(key, value);
                                }
                                iprot.readMapEnd();
                                return map.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                return com.google.common.collect.ImmutableMap.of();
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                }
                break;
            }
            case "string_set_field": {
                try {
                    stringSetField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableSet<String>>() {
                        @Override
                        public com.google.common.collect.ImmutableSet<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.SetBegin sequenceBegin = iprot.readSetBegin();
                                final com.google.common.collect.ImmutableSet.Builder<String> sequenceBuilder = com.google.common.collect.ImmutableSet.builder();
                                for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                    sequenceBuilder.add(iprot.readString());
                                }
                                iprot.readSetEnd();
                                return sequenceBuilder.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                }
                break;
            }
            case "string_field": {
                stringField = com.google.common.base.Optional.of(iprot.readString());
                break;
            }
            case "url_field": {
                try {
                    urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
                break;
            }
            default:
                if (unknownFieldCallback.isPresent()) {
                    unknownFieldCallback.get().apply(ifield);
                }
                break;
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();
        try {
            return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField);
        } catch (final IllegalArgumentException | NullPointerException e) {
            throw new org.thryft.protocol.InputProtocolException(e);
        }
    }

    public NestedProtocolTestStruct replaceBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceBinaryField(final byte[] binaryField) {
        return replaceBinaryField(com.google.common.base.Optional.fromNullable(binaryField));
    }

    public NestedProtocolTestStruct replaceBoolField(final com.google.common.base.Optional<boolean> boolField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceBoolField(final boolean boolField) {
        return replaceBoolField(com.google.common.base.Optional.fromNullable(boolField));
    }

    public NestedProtocolTestStruct replaceByteField(final com.google.common.base.Optional<byte> byteField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceByteField(final byte byteField) {
        return replaceByteField(com.google.common.base.Optional.fromNullable(byteField));
    }

    public NestedProtocolTestStruct replaceDateTimeField(final com.google.common.base.Optional<long> dateTimeField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceDateTimeField(final java.util.Date dateTimeField) {
        return replaceDateTimeField(com.google.common.base.Optional.fromNullable(dateTimeField));
    }

    public NestedProtocolTestStruct replaceDecimalField(final com.google.common.base.Optional<String> decimalField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceDecimalField(final java.math.BigDecimal decimalField) {
        return replaceDecimalField(com.google.common.base.Optional.fromNullable(decimalField));
    }

    public NestedProtocolTestStruct replaceEmailAddressField(final com.google.common.base.Optional<String> emailAddressField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceEmailAddressField(final org.thryft.native_.EmailAddress emailAddressField) {
        return replaceEmailAddressField(com.google.common.base.Optional.fromNullable(emailAddressField));
    }

    public NestedProtocolTestStruct replaceEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceEnumField(final org.thryft.protocol.test.ProtocolTestEnum enumField) {
        return replaceEnumField(com.google.common.base.Optional.fromNullable(enumField));
    }

    public NestedProtocolTestStruct replaceI16Field(final com.google.common.base.Optional<short> i16Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceI16Field(final short i16Field) {
        return replaceI16Field(com.google.common.base.Optional.fromNullable(i16Field));
    }

    public NestedProtocolTestStruct replaceI32Field(final com.google.common.base.Optional<i32> i32Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceI32Field(final i32 i32Field) {
        return replaceI32Field(com.google.common.base.Optional.fromNullable(i32Field));
    }

    public NestedProtocolTestStruct replaceI64Field(final com.google.common.base.Optional<long> i64Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceI64Field(final long i64Field) {
        return replaceI64Field(com.google.common.base.Optional.fromNullable(i64Field));
    }

    public NestedProtocolTestStruct replaceRequiredI32Field(final i32 requiredI32Field) {
        return new NestedProtocolTestStruct(requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceRequiredStringField(final String requiredStringField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceStringField(final com.google.common.base.Optional<String> stringField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceStringField(final String stringField) {
        return replaceStringField(com.google.common.base.Optional.fromNullable(stringField));
    }

    public NestedProtocolTestStruct replaceStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceStringListField(final com.google.common.collect.ImmutableList<String> stringListField) {
        return replaceStringListField(com.google.common.base.Optional.fromNullable(stringListField));
    }

    public NestedProtocolTestStruct replaceStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceStringSetField(final com.google.common.collect.ImmutableSet<String> stringSetField) {
        return replaceStringSetField(com.google.common.base.Optional.fromNullable(stringSetField));
    }

    public NestedProtocolTestStruct replaceStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceStringStringMapField(final com.google.common.collect.ImmutableMap<String, String> stringStringMapField) {
        return replaceStringStringMapField(com.google.common.base.Optional.fromNullable(stringStringMapField));
    }

    public NestedProtocolTestStruct replaceUrlField(final com.google.common.base.Optional<String> urlField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, urlField);
    }

    public NestedProtocolTestStruct replaceUrlField(final org.thryft.native_.Url urlField) {
        return replaceUrlField(com.google.common.base.Optional.fromNullable(urlField));
    }

    @Override
    public String toString() {
        return com.google.common.base.MoreObjects.toStringHelper(this).omitNullValues().add("required_i32_field", getRequiredI32Field()).add("required_string_field", getRequiredStringField()).add("binary_field", getBinaryField().orNull()).add("bool_field", getBoolField().orNull()).add("byte_field", getByteField().orNull()).add("date_time_field", getDateTimeField().orNull()).add("decimal_field", getDecimalField().orNull()).add("email_address_field", getEmailAddressField().orNull()).add("enum_field", getEnumField().orNull()).add("i16_field", getI16Field().orNull()).add("i32_field", getI32Field().orNull()).add("i64_field", getI64Field().orNull()).add("string_list_field", getStringListField().orNull()).add("string_string_map_field", getStringStringMapField().orNull()).add("string_set_field", getStringSetField().orNull()).add("string_field", getStringField().orNull()).add("url_field", getUrlField().orNull()).toString();
    }

    @Override
    public void writeAsList(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeListBegin(org.thryft.protocol.Type.VOID_, 17);

        oprot.writeI32(getRequiredI32Field());

        oprot.writeString(getRequiredStringField());

        if (getBinaryField().isPresent()) {
            oprot.writeBinary(getBinaryField().get());
        } else {
            oprot.writeNull();
        }

        if (getBoolField().isPresent()) {
            oprot.writeBool(getBoolField().get());
        } else {
            oprot.writeNull();
        }

        if (getByteField().isPresent()) {
            oprot.writeByte(getByteField().get());
        } else {
            oprot.writeNull();
        }

        if (getDateTimeField().isPresent()) {
            oprot.writeDateTime(getDateTimeField().get());
        } else {
            oprot.writeNull();
        }

        if (getDecimalField().isPresent()) {
            oprot.writeDecimal(getDecimalField().get());
        } else {
            oprot.writeNull();
        }

        if (getEmailAddressField().isPresent()) {
            oprot.writeString(getEmailAddressField().get().toString());
        } else {
            oprot.writeNull();
        }

        if (getEnumField().isPresent()) {
            oprot.writeEnum(getEnumField().get());
        } else {
            oprot.writeNull();
        }

        if (getI16Field().isPresent()) {
            oprot.writeI16(getI16Field().get());
        } else {
            oprot.writeNull();
        }

        if (getI32Field().isPresent()) {
            oprot.writeI32(getI32Field().get());
        } else {
            oprot.writeNull();
        }

        if (getI64Field().isPresent()) {
            oprot.writeI64(getI64Field().get());
        } else {
            oprot.writeNull();
        }

        if (getStringListField().isPresent()) {
            oprot.writeListBegin(org.thryft.protocol.Type.STRING, getStringListField().get().size());
            for (final String _iter0 : getStringListField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeListEnd();
        } else {
            oprot.writeNull();
        }

        if (getStringStringMapField().isPresent()) {
            oprot.writeMapBegin(org.thryft.protocol.Type.STRING, org.thryft.protocol.Type.STRING, getStringStringMapField().get().size());
            for (com.google.common.collect.ImmutableMap.Entry<String, String> _iter0 : getStringStringMapField().get().entrySet()) {
                oprot.writeString(_iter0.getKey());
                oprot.writeString(_iter0.getValue());
            }
            oprot.writeMapEnd();
        } else {
            oprot.writeNull();
        }

        if (getStringSetField().isPresent()) {
            oprot.writeSetBegin(org.thryft.protocol.Type.STRING, getStringSetField().get().size());
            for (final String _iter0 : getStringSetField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeSetEnd();
        } else {
            oprot.writeNull();
        }

        if (getStringField().isPresent()) {
            oprot.writeString(getStringField().get());
        } else {
            oprot.writeNull();
        }

        if (getUrlField().isPresent()) {
            oprot.writeString(getUrlField().get().toString());
        } else {
            oprot.writeNull();
        }

        oprot.writeListEnd();
    }

    @Override
    public void writeAsStruct(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeStructBegin("org.thryft.protocol.test.NestedProtocolTestStruct");
        writeFields(oprot);
        oprot.writeStructEnd();
    }

    @Override
    public void writeFields(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeFieldBegin("required_i32_field", org.thryft.protocol.Type.I32, (short)0);
        oprot.writeI32(getRequiredI32Field());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin("required_string_field", org.thryft.protocol.Type.STRING, (short)0);
        oprot.writeString(getRequiredStringField());
        oprot.writeFieldEnd();

        if (getBinaryField().isPresent()) {
            oprot.writeFieldBegin("binary_field", org.thryft.protocol.Type.STRING, (short)0);
            oprot.writeBinary(getBinaryField().get());
            oprot.writeFieldEnd();
        }

        if (getBoolField().isPresent()) {
            oprot.writeFieldBegin("bool_field", org.thryft.protocol.Type.BOOL, (short)0);
            oprot.writeBool(getBoolField().get());
            oprot.writeFieldEnd();
        }

        if (getByteField().isPresent()) {
            oprot.writeFieldBegin("byte_field", org.thryft.protocol.Type.BYTE, (short)0);
            oprot.writeByte(getByteField().get());
            oprot.writeFieldEnd();
        }

        if (getDateTimeField().isPresent()) {
            oprot.writeFieldBegin("date_time_field", org.thryft.protocol.Type.I64, (short)0);
            oprot.writeDateTime(getDateTimeField().get());
            oprot.writeFieldEnd();
        }

        if (getDecimalField().isPresent()) {
            oprot.writeFieldBegin("decimal_field", org.thryft.protocol.Type.STRING, (short)0);
            oprot.writeDecimal(getDecimalField().get());
            oprot.writeFieldEnd();
        }

        if (getEmailAddressField().isPresent()) {
            oprot.writeFieldBegin("email_address_field", org.thryft.protocol.Type.STRING, (short)0);
            oprot.writeString(getEmailAddressField().get().toString());
            oprot.writeFieldEnd();
        }

        if (getEnumField().isPresent()) {
            oprot.writeFieldBegin("enum_field", org.thryft.protocol.Type.STRING, (short)0);
            oprot.writeEnum(getEnumField().get());
            oprot.writeFieldEnd();
        }

        if (getI16Field().isPresent()) {
            oprot.writeFieldBegin("i16_field", org.thryft.protocol.Type.I16, (short)0);
            oprot.writeI16(getI16Field().get());
            oprot.writeFieldEnd();
        }

        if (getI32Field().isPresent()) {
            oprot.writeFieldBegin("i32_field", org.thryft.protocol.Type.I32, (short)0);
            oprot.writeI32(getI32Field().get());
            oprot.writeFieldEnd();
        }

        if (getI64Field().isPresent()) {
            oprot.writeFieldBegin("i64_field", org.thryft.protocol.Type.I64, (short)0);
            oprot.writeI64(getI64Field().get());
            oprot.writeFieldEnd();
        }

        if (getStringListField().isPresent()) {
            oprot.writeFieldBegin("string_list_field", org.thryft.protocol.Type.LIST, (short)0);
            oprot.writeListBegin(org.thryft.protocol.Type.STRING, getStringListField().get().size());
            for (final String _iter0 : getStringListField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeListEnd();
            oprot.writeFieldEnd();
        }

        if (getStringStringMapField().isPresent()) {
            oprot.writeFieldBegin("string_string_map_field", org.thryft.protocol.Type.MAP, (short)0);
            oprot.writeMapBegin(org.thryft.protocol.Type.STRING, org.thryft.protocol.Type.STRING, getStringStringMapField().get().size());
            for (com.google.common.collect.ImmutableMap.Entry<String, String> _iter0 : getStringStringMapField().get().entrySet()) {
                oprot.writeString(_iter0.getKey());
                oprot.writeString(_iter0.getValue());
            }
            oprot.writeMapEnd();
            oprot.writeFieldEnd();
        }

        if (getStringSetField().isPresent()) {
            oprot.writeFieldBegin("string_set_field", org.thryft.protocol.Type.SET, (short)0);
            oprot.writeSetBegin(org.thryft.protocol.Type.STRING, getStringSetField().get().size());
            for (final String _iter0 : getStringSetField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeSetEnd();
            oprot.writeFieldEnd();
        }

        if (getStringField().isPresent()) {
            oprot.writeFieldBegin("string_field", org.thryft.protocol.Type.STRING, (short)0);
            oprot.writeString(getStringField().get());
            oprot.writeFieldEnd();
        }

        if (getUrlField().isPresent()) {
            oprot.writeFieldBegin("url_field", org.thryft.protocol.Type.STRING, (short)0);
            oprot.writeString(getUrlField().get().toString());
            oprot.writeFieldEnd();
        }

        oprot.writeFieldStop();
    }

    private final i32 requiredI32Field;

    private final String requiredStringField;

    private final com.google.common.base.Optional<byte[]> binaryField;

    private final com.google.common.base.Optional<boolean> boolField;

    private final com.google.common.base.Optional<byte> byteField;

    private final com.google.common.base.Optional<long> dateTimeField;

    private final com.google.common.base.Optional<String> decimalField;

    private final com.google.common.base.Optional<String> emailAddressField;

    private final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;

    private final com.google.common.base.Optional<short> i16Field;

    private final com.google.common.base.Optional<i32> i32Field;

    private final com.google.common.base.Optional<long> i64Field;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;

    private final com.google.common.base.Optional<String> stringField;

    private final com.google.common.base.Optional<String> urlField;
}
