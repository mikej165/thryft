package org.thryft.protocol.test;

@SuppressWarnings({"serial"})
public class NestedProtocolTestStruct implements org.thryft.Base<NestedProtocolTestStruct> {
    public static class Builder {
        public Builder() {
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

        protected NestedProtocolTestStruct _build(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<Byte> byteField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField);
        }

        public NestedProtocolTestStruct build() {
            return _build(com.google.common.base.Preconditions.checkNotNull(requiredI32Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredI32Field"), com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing binaryField"), com.google.common.base.Preconditions.checkNotNull(boolField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing boolField"), com.google.common.base.Preconditions.checkNotNull(byteField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing byteField"), com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing dateTimeField"), com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing decimalField"), com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing emailAddressField"), com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing enumField"), com.google.common.base.Preconditions.checkNotNull(i16Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i16Field"), com.google.common.base.Preconditions.checkNotNull(i32Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i32Field"), com.google.common.base.Preconditions.checkNotNull(i64Field, "org.thryft.protocol.test.NestedProtocolTestStruct: missing i64Field"), com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringListField"), com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringStringMapField"), com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringSetField"), com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringField"), com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing urlField"));
        }

        public final com.google.common.base.Optional<byte[]> getBinaryField() {
            return binaryField;
        }

        public final com.google.common.base.Optional<Boolean> getBoolField() {
            return boolField;
        }

        public final com.google.common.base.Optional<Byte> getByteField() {
            return byteField;
        }

        public final com.google.common.base.Optional<java.util.Date> getDateTimeField() {
            return dateTimeField;
        }

        public final com.google.common.base.Optional<java.math.BigDecimal> getDecimalField() {
            return decimalField;
        }

        public final com.google.common.base.Optional<org.thryft.native_.EmailAddress> getEmailAddressField() {
            return emailAddressField;
        }

        public final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> getEnumField() {
            return enumField;
        }

        public final com.google.common.base.Optional<Short> getI16Field() {
            return i16Field;
        }

        public final com.google.common.base.Optional<Integer> getI32Field() {
            return i32Field;
        }

        public final com.google.common.base.Optional<Long> getI64Field() {
            return i64Field;
        }

        public final int getRequiredI32Field() {
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

        public final com.google.common.base.Optional<org.thryft.native_.Url> getUrlField() {
            return urlField;
        }

        public Builder set(final String name, @javax.annotation.Nullable final Object value) {
            com.google.common.base.Preconditions.checkNotNull(name);

            switch (name.toLowerCase()) {
            case "required_i32_field": setRequiredI32Field((int)value); return this;
            case "required_string_field": setRequiredStringField((String)value); return this;
            case "binary_field": setBinaryField((byte[])value); return this;
            case "bool_field": setBoolField((Boolean)value); return this;
            case "byte_field": setByteField((Byte)value); return this;
            case "date_time_field": setDateTimeField((java.util.Date)value); return this;
            case "decimal_field": setDecimalField((java.math.BigDecimal)value); return this;
            case "email_address_field": setEmailAddressField((org.thryft.native_.EmailAddress)value); return this;
            case "enum_field": setEnumField((org.thryft.protocol.test.ProtocolTestEnum)value); return this;
            case "i16_field": setI16Field((Short)value); return this;
            case "i32_field": setI32Field((Integer)value); return this;
            case "i64_field": setI64Field((Long)value); return this;
            case "string_field": setStringField((String)value); return this;
            case "url_field": setUrlField((org.thryft.native_.Url)value); return this;
            default:
                throw new IllegalArgumentException(name);
            }
        }

        public Builder setBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
            this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField);
            return this;
        }

        public Builder setBinaryField(@javax.annotation.Nullable final byte[] binaryField) {
            this.binaryField = com.google.common.base.Optional.fromNullable(binaryField);
            return this;
        }

        public Builder setBoolField(final com.google.common.base.Optional<Boolean> boolField) {
            this.boolField = com.google.common.base.Preconditions.checkNotNull(boolField);
            return this;
        }

        public Builder setBoolField(@javax.annotation.Nullable final Boolean boolField) {
            this.boolField = com.google.common.base.Optional.fromNullable(boolField);
            return this;
        }

        public Builder setByteField(final com.google.common.base.Optional<Byte> byteField) {
            this.byteField = com.google.common.base.Preconditions.checkNotNull(byteField);
            return this;
        }

        public Builder setByteField(@javax.annotation.Nullable final Byte byteField) {
            this.byteField = com.google.common.base.Optional.fromNullable(byteField);
            return this;
        }

        public Builder setDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
            this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField);
            return this;
        }

        public Builder setDateTimeField(@javax.annotation.Nullable final java.util.Date dateTimeField) {
            this.dateTimeField = com.google.common.base.Optional.fromNullable(dateTimeField);
            return this;
        }

        public Builder setDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
            this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField);
            return this;
        }

        public Builder setDecimalField(@javax.annotation.Nullable final java.math.BigDecimal decimalField) {
            this.decimalField = com.google.common.base.Optional.fromNullable(decimalField);
            return this;
        }

        public Builder setEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
            this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField);
            return this;
        }

        public Builder setEmailAddressField(@javax.annotation.Nullable final org.thryft.native_.EmailAddress emailAddressField) {
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

        public Builder setI16Field(final com.google.common.base.Optional<Short> i16Field) {
            this.i16Field = com.google.common.base.Preconditions.checkNotNull(i16Field);
            return this;
        }

        public Builder setI16Field(@javax.annotation.Nullable final Short i16Field) {
            this.i16Field = com.google.common.base.Optional.fromNullable(i16Field);
            return this;
        }

        public Builder setI32Field(final com.google.common.base.Optional<Integer> i32Field) {
            this.i32Field = com.google.common.base.Preconditions.checkNotNull(i32Field);
            return this;
        }

        public Builder setI32Field(@javax.annotation.Nullable final Integer i32Field) {
            this.i32Field = com.google.common.base.Optional.fromNullable(i32Field);
            return this;
        }

        public Builder setI64Field(final com.google.common.base.Optional<Long> i64Field) {
            this.i64Field = com.google.common.base.Preconditions.checkNotNull(i64Field);
            return this;
        }

        public Builder setI64Field(@javax.annotation.Nullable final Long i64Field) {
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

        public Builder setRequiredI32Field(final int requiredI32Field) {
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

        public Builder setUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField);
            return this;
        }

        public Builder setUrlField(@javax.annotation.Nullable final org.thryft.native_.Url urlField) {
            this.urlField = com.google.common.base.Optional.fromNullable(urlField);
            return this;
        }

        private Integer requiredI32Field;
        private String requiredStringField;
        private com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<Byte> byteField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.absent();
        private com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.absent();
    }

    public NestedProtocolTestStruct(final NestedProtocolTestStruct other) {
        this(other.getRequiredI32Field(), other.getRequiredStringField(), other.getBinaryField(), other.getBoolField(), other.getByteField(), other.getDateTimeField(), other.getDecimalField(), other.getEmailAddressField(), other.getEnumField(), other.getI16Field(), other.getI32Field(), other.getI64Field(), other.getStringListField(), other.getStringStringMapField(), other.getStringSetField(), other.getStringField(), other.getUrlField());
    }

    public NestedProtocolTestStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        this(iprot, org.thryft.protocol.Type.STRUCT);
    }

    public NestedProtocolTestStruct(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type readAsType) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Byte> byteField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.absent();

        switch (readAsType) {
            case LIST:
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
                    } catch (NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 5) {
                    try {
                        dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                    } catch (IllegalArgumentException e) {
                    }
                }
                if (__list.getSize() > 6) {
                    try {
                        decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                    } catch (NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 7) {
                    emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                }
                if (__list.getSize() > 8) {
                    try {
                        enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                    } catch (IllegalArgumentException e) {
                    }
                }
                if (__list.getSize() > 9) {
                    try {
                        i16Field = com.google.common.base.Optional.of(iprot.readI16());
                    } catch (NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 10) {
                    try {
                        i32Field = com.google.common.base.Optional.of(iprot.readI32());
                    } catch (NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 11) {
                    try {
                        i64Field = com.google.common.base.Optional.of(iprot.readI64());
                    } catch (NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 12) {
                    stringListField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableList<String>>() {
                        @Override
                        public com.google.common.collect.ImmutableList<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.ListBegin sequenceBegin = iprot.readListBegin();
                                final com.google.common.collect.ImmutableList.Builder<String> sequence = com.google.common.collect.ImmutableList.builder();
                                for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                    sequence.add(iprot.readString());
                                }
                                iprot.readListEnd();
                                return sequence.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                return com.google.common.collect.ImmutableList.of();
                            }
                        }
                    }).apply(iprot));
                }
                if (__list.getSize() > 13) {
                    stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                        @Override
                        public com.google.common.collect.ImmutableMap<String, String> apply(org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
                                final com.google.common.collect.ImmutableMap.Builder<String, String> map = com.google.common.collect.ImmutableMap.builder();
                                for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                                    map.put(iprot.readString(), iprot.readString());
                                }
                                iprot.readMapEnd();
                                return map.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                return com.google.common.collect.ImmutableMap.of();
                            }
                        }
                    }).apply(iprot));
                }
                if (__list.getSize() > 14) {
                    stringSetField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableSet<String>>() {
                        @Override
                        public com.google.common.collect.ImmutableSet<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                            try {
                                final org.thryft.protocol.SetBegin sequenceBegin = iprot.readSetBegin();
                                final com.google.common.collect.ImmutableSet.Builder<String> sequence = com.google.common.collect.ImmutableSet.builder();
                                for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                    sequence.add(iprot.readString());
                                }
                                iprot.readSetEnd();
                                return sequence.build();
                            } catch (final org.thryft.protocol.InputProtocolException e) {
                                return com.google.common.collect.ImmutableSet.of();
                            }
                        }
                    }).apply(iprot));
                }
                if (__list.getSize() > 15) {
                    stringField = com.google.common.base.Optional.of(iprot.readString());
                }
                if (__list.getSize() > 16) {
                    urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                }
                iprot.readListEnd();
                break;

            case STRUCT:
            default:
                iprot.readStructBegin();
                while (true) {
                    final org.thryft.protocol.FieldBegin ifield = iprot.readFieldBegin();
                    if (ifield.getType() == org.thryft.protocol.Type.STOP) {
                        break;
                    } else if (ifield.getName().equals("required_i32_field")) {
                        requiredI32Field = iprot.readI32();
                    } else if (ifield.getName().equals("required_string_field")) {
                        requiredStringField = iprot.readString();
                    } else if (ifield.getName().equals("binary_field")) {
                        binaryField = com.google.common.base.Optional.of(iprot.readBinary());
                    } else if (ifield.getName().equals("bool_field")) {
                        boolField = com.google.common.base.Optional.of(iprot.readBool());
                    } else if (ifield.getName().equals("byte_field")) {
                        try {
                            byteField = com.google.common.base.Optional.of(iprot.readByte());
                        } catch (NumberFormatException e) {
                        }
                    } else if (ifield.getName().equals("date_time_field")) {
                        try {
                            dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                        } catch (IllegalArgumentException e) {
                        }
                    } else if (ifield.getName().equals("decimal_field")) {
                        try {
                            decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                        } catch (NumberFormatException e) {
                        }
                    } else if (ifield.getName().equals("email_address_field")) {
                        emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                    } else if (ifield.getName().equals("enum_field")) {
                        try {
                            enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                        } catch (IllegalArgumentException e) {
                        }
                    } else if (ifield.getName().equals("i16_field")) {
                        try {
                            i16Field = com.google.common.base.Optional.of(iprot.readI16());
                        } catch (NumberFormatException e) {
                        }
                    } else if (ifield.getName().equals("i32_field")) {
                        try {
                            i32Field = com.google.common.base.Optional.of(iprot.readI32());
                        } catch (NumberFormatException e) {
                        }
                    } else if (ifield.getName().equals("i64_field")) {
                        try {
                            i64Field = com.google.common.base.Optional.of(iprot.readI64());
                        } catch (NumberFormatException e) {
                        }
                    } else if (ifield.getName().equals("string_list_field")) {
                        stringListField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableList<String>>() {
                            @Override
                            public com.google.common.collect.ImmutableList<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                                try {
                                    final org.thryft.protocol.ListBegin sequenceBegin = iprot.readListBegin();
                                    final com.google.common.collect.ImmutableList.Builder<String> sequence = com.google.common.collect.ImmutableList.builder();
                                    for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                        sequence.add(iprot.readString());
                                    }
                                    iprot.readListEnd();
                                    return sequence.build();
                                } catch (final org.thryft.protocol.InputProtocolException e) {
                                    return com.google.common.collect.ImmutableList.of();
                                }
                            }
                        }).apply(iprot));
                    } else if (ifield.getName().equals("string_string_map_field")) {
                        stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                            @Override
                            public com.google.common.collect.ImmutableMap<String, String> apply(org.thryft.protocol.InputProtocol iprot) {
                                try {
                                    final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
                                    final com.google.common.collect.ImmutableMap.Builder<String, String> map = com.google.common.collect.ImmutableMap.builder();
                                    for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                                        map.put(iprot.readString(), iprot.readString());
                                    }
                                    iprot.readMapEnd();
                                    return map.build();
                                } catch (final org.thryft.protocol.InputProtocolException e) {
                                    return com.google.common.collect.ImmutableMap.of();
                                }
                            }
                        }).apply(iprot));
                    } else if (ifield.getName().equals("string_set_field")) {
                        stringSetField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableSet<String>>() {
                            @Override
                            public com.google.common.collect.ImmutableSet<String> apply(final org.thryft.protocol.InputProtocol iprot) {
                                try {
                                    final org.thryft.protocol.SetBegin sequenceBegin = iprot.readSetBegin();
                                    final com.google.common.collect.ImmutableSet.Builder<String> sequence = com.google.common.collect.ImmutableSet.builder();
                                    for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
                                        sequence.add(iprot.readString());
                                    }
                                    iprot.readSetEnd();
                                    return sequence.build();
                                } catch (final org.thryft.protocol.InputProtocolException e) {
                                    return com.google.common.collect.ImmutableSet.of();
                                }
                            }
                        }).apply(iprot));
                    } else if (ifield.getName().equals("string_field")) {
                        stringField = com.google.common.base.Optional.of(iprot.readString());
                    } else if (ifield.getName().equals("url_field")) {
                        urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                    }
                    iprot.readFieldEnd();
                }
                iprot.readStructEnd();
                break;
        }

        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
        this.binaryField = binaryField;
        this.boolField = boolField;
        this.byteField = byteField;
        this.dateTimeField = dateTimeField;
        this.decimalField = decimalField;
        this.emailAddressField = emailAddressField;
        this.enumField = enumField;
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.stringListField = stringListField;
        this.stringStringMapField = stringStringMapField;
        this.stringSetField = stringSetField;
        this.stringField = org.thryft.Preconditions.checkNotEmpty(stringField, String.class, "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is empty");
        this.urlField = urlField;
    }

    public NestedProtocolTestStruct(final int requiredI32Field, final String requiredStringField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
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

    public NestedProtocolTestStruct(final Integer requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<Byte> byteField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing binaryField");
        this.boolField = boolField;
        this.byteField = byteField;
        this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing dateTimeField");
        this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing decimalField");
        this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing emailAddressField");
        this.enumField = com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing enumField");
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.stringListField = com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringListField");
        this.stringStringMapField = com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringStringMapField");
        this.stringSetField = com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringSetField");
        this.stringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringField"), String.class, "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is empty");
        this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing urlField");
    }

    public NestedProtocolTestStruct(final int requiredI32Field, final String requiredStringField, final @javax.annotation.Nullable byte[] binaryField, final @javax.annotation.Nullable Boolean boolField, final @javax.annotation.Nullable Byte byteField, final @javax.annotation.Nullable java.util.Date dateTimeField, final @javax.annotation.Nullable java.math.BigDecimal decimalField, final @javax.annotation.Nullable org.thryft.native_.EmailAddress emailAddressField, final @javax.annotation.Nullable org.thryft.protocol.test.ProtocolTestEnum enumField, final @javax.annotation.Nullable Short i16Field, final @javax.annotation.Nullable Integer i32Field, final @javax.annotation.Nullable Long i64Field, final @javax.annotation.Nullable com.google.common.collect.ImmutableList<String> stringListField, final @javax.annotation.Nullable com.google.common.collect.ImmutableMap<String, String> stringStringMapField, final @javax.annotation.Nullable com.google.common.collect.ImmutableSet<String> stringSetField, final @javax.annotation.Nullable String stringField, final @javax.annotation.Nullable org.thryft.native_.Url urlField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
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
        this.stringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Optional.fromNullable(stringField), String.class, "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is empty");
        this.urlField = com.google.common.base.Optional.fromNullable(urlField);
    }

    public NestedProtocolTestStruct(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<Byte> byteField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing binaryField");
        this.boolField = boolField;
        this.byteField = byteField;
        this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing dateTimeField");
        this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing decimalField");
        this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing emailAddressField");
        this.enumField = com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing enumField");
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.stringListField = com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringListField");
        this.stringStringMapField = com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringStringMapField");
        this.stringSetField = com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringSetField");
        this.stringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing stringField"), String.class, "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is empty");
        this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.NestedProtocolTestStruct: missing urlField");
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(final NestedProtocolTestStruct other) {
        return new Builder(other);
    }

    @Override
    public int compareTo(final NestedProtocolTestStruct other) {
        if (other == null) {
            throw new NullPointerException();
        }

        int result;
        result = Integer.compare(this.requiredI32Field, other.requiredI32Field);
        if (result != 0) {
            return result;
        }

        result = this.requiredStringField.compareTo(other.requiredStringField);
        if (result != 0) {
            return result;
        }

        if (this.binaryField.isPresent()) {
            if (other.binaryField.isPresent()) {
                result = com.google.common.primitives.SignedBytes.lexicographicalComparator().compare(this.binaryField.get(), other.binaryField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.binaryField.isPresent()) {
            return -1;
        }

        if (this.boolField.isPresent()) {
            if (other.boolField.isPresent()) {
                result = ((Boolean)this.boolField.get()).compareTo(other.boolField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.boolField.isPresent()) {
            return -1;
        }

        if (this.byteField.isPresent()) {
            if (other.byteField.isPresent()) {
                result = Byte.compare(this.byteField.get(), other.byteField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.byteField.isPresent()) {
            return -1;
        }

        if (this.dateTimeField.isPresent()) {
            if (other.dateTimeField.isPresent()) {
                result = this.dateTimeField.get().compareTo(other.dateTimeField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.dateTimeField.isPresent()) {
            return -1;
        }

        if (this.decimalField.isPresent()) {
            if (other.decimalField.isPresent()) {
                result = this.decimalField.get().compareTo(other.decimalField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.decimalField.isPresent()) {
            return -1;
        }

        if (this.emailAddressField.isPresent()) {
            if (other.emailAddressField.isPresent()) {
                result = this.emailAddressField.get().compareTo(other.emailAddressField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.emailAddressField.isPresent()) {
            return -1;
        }

        if (this.enumField.isPresent()) {
            if (other.enumField.isPresent()) {
                result = this.enumField.get().compareTo(other.enumField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.enumField.isPresent()) {
            return -1;
        }

        if (this.i16Field.isPresent()) {
            if (other.i16Field.isPresent()) {
                result = Short.compare(this.i16Field.get(), other.i16Field.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.i16Field.isPresent()) {
            return -1;
        }

        if (this.i32Field.isPresent()) {
            if (other.i32Field.isPresent()) {
                result = Integer.compare(this.i32Field.get(), other.i32Field.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.i32Field.isPresent()) {
            return -1;
        }

        if (this.i64Field.isPresent()) {
            if (other.i64Field.isPresent()) {
                result = Long.compare(this.i64Field.get(), other.i64Field.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.i64Field.isPresent()) {
            return -1;
        }

        if (this.stringListField.isPresent()) {
            if (other.stringListField.isPresent()) {
                result = org.thryft.Comparators.compare(this.stringListField.get(), other.stringListField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.stringListField.isPresent()) {
            return -1;
        }

        if (this.stringStringMapField.isPresent()) {
            if (other.stringStringMapField.isPresent()) {
                result = org.thryft.Comparators.compare(this.stringStringMapField.get(), other.stringStringMapField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.stringStringMapField.isPresent()) {
            return -1;
        }

        if (this.stringSetField.isPresent()) {
            if (other.stringSetField.isPresent()) {
                result = org.thryft.Comparators.compare(this.stringSetField.get(), other.stringSetField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.stringSetField.isPresent()) {
            return -1;
        }

        if (this.stringField.isPresent()) {
            if (other.stringField.isPresent()) {
                result = this.stringField.get().compareTo(other.stringField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.stringField.isPresent()) {
            return -1;
        }

        if (this.urlField.isPresent()) {
            if (other.urlField.isPresent()) {
                result = this.urlField.get().compareTo(other.urlField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.urlField.isPresent()) {
            return -1;
        }

        return 0;
    }

    @Override
    public boolean equals(final Object otherObject) {
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

    public Object get(final String fieldName) {
        if (fieldName.equals("required_i32_field")) {
            return getRequiredI32Field();
        } else if (fieldName.equals("required_string_field")) {
            return getRequiredStringField();
        } else if (fieldName.equals("binary_field")) {
            return getBinaryField();
        } else if (fieldName.equals("bool_field")) {
            return getBoolField();
        } else if (fieldName.equals("byte_field")) {
            return getByteField();
        } else if (fieldName.equals("date_time_field")) {
            return getDateTimeField();
        } else if (fieldName.equals("decimal_field")) {
            return getDecimalField();
        } else if (fieldName.equals("email_address_field")) {
            return getEmailAddressField();
        } else if (fieldName.equals("enum_field")) {
            return getEnumField();
        } else if (fieldName.equals("i16_field")) {
            return getI16Field();
        } else if (fieldName.equals("i32_field")) {
            return getI32Field();
        } else if (fieldName.equals("i64_field")) {
            return getI64Field();
        } else if (fieldName.equals("string_list_field")) {
            return getStringListField();
        } else if (fieldName.equals("string_string_map_field")) {
            return getStringStringMapField();
        } else if (fieldName.equals("string_set_field")) {
            return getStringSetField();
        } else if (fieldName.equals("string_field")) {
            return getStringField();
        } else if (fieldName.equals("url_field")) {
            return getUrlField();
        }
        throw new IllegalArgumentException(fieldName);
    }

    public final com.google.common.base.Optional<byte[]> getBinaryField() {
        return binaryField;
    }

    public final com.google.common.base.Optional<Boolean> getBoolField() {
        return boolField;
    }

    public final com.google.common.base.Optional<Byte> getByteField() {
        return byteField;
    }

    public final com.google.common.base.Optional<java.util.Date> getDateTimeField() {
        return dateTimeField;
    }

    public final com.google.common.base.Optional<java.math.BigDecimal> getDecimalField() {
        return decimalField;
    }

    public final com.google.common.base.Optional<org.thryft.native_.EmailAddress> getEmailAddressField() {
        return emailAddressField;
    }

    public final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> getEnumField() {
        return enumField;
    }

    public final com.google.common.base.Optional<Short> getI16Field() {
        return i16Field;
    }

    public final com.google.common.base.Optional<Integer> getI32Field() {
        return i32Field;
    }

    public final com.google.common.base.Optional<Long> getI64Field() {
        return i64Field;
    }

    public final int getRequiredI32Field() {
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

    public final com.google.common.base.Optional<org.thryft.native_.Url> getUrlField() {
        return urlField;
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        hashCode = 31 * hashCode + ((int)getRequiredI32Field());
        hashCode = 31 * hashCode + getRequiredStringField().hashCode();
        if (getBinaryField().isPresent()) {
            hashCode = 31 * hashCode + java.util.Arrays.hashCode(getBinaryField().get());
        }
        if (getBoolField().isPresent()) {
            hashCode = 31 * hashCode + (getBoolField().get() ? 1 : 0);
        }
        if (getByteField().isPresent()) {
            hashCode = 31 * hashCode + ((byte)getByteField().get());
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
            hashCode = 31 * hashCode + ((int)getI16Field().get());
        }
        if (getI32Field().isPresent()) {
            hashCode = 31 * hashCode + ((int)getI32Field().get());
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

    public NestedProtocolTestStruct replaceBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceBinaryField(final byte[] binaryField) {
        return replaceBinaryField(com.google.common.base.Optional.fromNullable(binaryField));
    }

    public NestedProtocolTestStruct replaceBoolField(final com.google.common.base.Optional<Boolean> boolField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceBoolField(final boolean boolField) {
        return replaceBoolField(com.google.common.base.Optional.fromNullable(boolField));
    }

    public NestedProtocolTestStruct replaceByteField(final com.google.common.base.Optional<Byte> byteField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceByteField(final byte byteField) {
        return replaceByteField(com.google.common.base.Optional.fromNullable(byteField));
    }

    public NestedProtocolTestStruct replaceDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceDateTimeField(final java.util.Date dateTimeField) {
        return replaceDateTimeField(com.google.common.base.Optional.fromNullable(dateTimeField));
    }

    public NestedProtocolTestStruct replaceDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceDecimalField(final java.math.BigDecimal decimalField) {
        return replaceDecimalField(com.google.common.base.Optional.fromNullable(decimalField));
    }

    public NestedProtocolTestStruct replaceEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
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

    public NestedProtocolTestStruct replaceI16Field(final com.google.common.base.Optional<Short> i16Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceI16Field(final short i16Field) {
        return replaceI16Field(com.google.common.base.Optional.fromNullable(i16Field));
    }

    public NestedProtocolTestStruct replaceI32Field(final com.google.common.base.Optional<Integer> i32Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceI32Field(final int i32Field) {
        return replaceI32Field(com.google.common.base.Optional.fromNullable(i32Field));
    }

    public NestedProtocolTestStruct replaceI64Field(final com.google.common.base.Optional<Long> i64Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField);
    }

    public NestedProtocolTestStruct replaceI64Field(final long i64Field) {
        return replaceI64Field(com.google.common.base.Optional.fromNullable(i64Field));
    }

    public NestedProtocolTestStruct replaceRequiredI32Field(final int requiredI32Field) {
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

    public NestedProtocolTestStruct replaceUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
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
    public void write(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        write(oprot, org.thryft.protocol.Type.STRUCT);
    }

    public void write(final org.thryft.protocol.OutputProtocol oprot, final org.thryft.protocol.Type writeAsType) throws org.thryft.protocol.OutputProtocolException {
        switch (writeAsType) {
            case VOID_:
            case LIST:
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
                break;

            case STRUCT:
            default:
                oprot.writeStructBegin("org.thryft.protocol.test.NestedProtocolTestStruct");

                oprot.writeFieldBegin("required_i32_field", org.thryft.protocol.Type.I32, (short)-1);
                oprot.writeI32(getRequiredI32Field());
                oprot.writeFieldEnd();

                oprot.writeFieldBegin("required_string_field", org.thryft.protocol.Type.STRING, (short)-1);
                oprot.writeString(getRequiredStringField());
                oprot.writeFieldEnd();

                if (getBinaryField().isPresent()) {
                    oprot.writeFieldBegin("binary_field", org.thryft.protocol.Type.STRING, (short)-1);
                    oprot.writeBinary(getBinaryField().get());
                    oprot.writeFieldEnd();
                }

                if (getBoolField().isPresent()) {
                    oprot.writeFieldBegin("bool_field", org.thryft.protocol.Type.BOOL, (short)-1);
                    oprot.writeBool(getBoolField().get());
                    oprot.writeFieldEnd();
                }

                if (getByteField().isPresent()) {
                    oprot.writeFieldBegin("byte_field", org.thryft.protocol.Type.BYTE, (short)-1);
                    oprot.writeByte(getByteField().get());
                    oprot.writeFieldEnd();
                }

                if (getDateTimeField().isPresent()) {
                    oprot.writeFieldBegin("date_time_field", org.thryft.protocol.Type.I64, (short)-1);
                    oprot.writeDateTime(getDateTimeField().get());
                    oprot.writeFieldEnd();
                }

                if (getDecimalField().isPresent()) {
                    oprot.writeFieldBegin("decimal_field", org.thryft.protocol.Type.STRING, (short)-1);
                    oprot.writeDecimal(getDecimalField().get());
                    oprot.writeFieldEnd();
                }

                if (getEmailAddressField().isPresent()) {
                    oprot.writeFieldBegin("email_address_field", org.thryft.protocol.Type.STRING, (short)-1);
                    oprot.writeString(getEmailAddressField().get().toString());
                    oprot.writeFieldEnd();
                }

                if (getEnumField().isPresent()) {
                    oprot.writeFieldBegin("enum_field", org.thryft.protocol.Type.STRING, (short)-1);
                    oprot.writeEnum(getEnumField().get());
                    oprot.writeFieldEnd();
                }

                if (getI16Field().isPresent()) {
                    oprot.writeFieldBegin("i16_field", org.thryft.protocol.Type.I16, (short)-1);
                    oprot.writeI16(getI16Field().get());
                    oprot.writeFieldEnd();
                }

                if (getI32Field().isPresent()) {
                    oprot.writeFieldBegin("i32_field", org.thryft.protocol.Type.I32, (short)-1);
                    oprot.writeI32(getI32Field().get());
                    oprot.writeFieldEnd();
                }

                if (getI64Field().isPresent()) {
                    oprot.writeFieldBegin("i64_field", org.thryft.protocol.Type.I64, (short)-1);
                    oprot.writeI64(getI64Field().get());
                    oprot.writeFieldEnd();
                }

                if (getStringListField().isPresent()) {
                    oprot.writeFieldBegin("string_list_field", org.thryft.protocol.Type.LIST, (short)-1);
                    oprot.writeListBegin(org.thryft.protocol.Type.STRING, getStringListField().get().size());
                    for (final String _iter0 : getStringListField().get()) {
                        oprot.writeString(_iter0);
                    }
                    oprot.writeListEnd();
                    oprot.writeFieldEnd();
                }

                if (getStringStringMapField().isPresent()) {
                    oprot.writeFieldBegin("string_string_map_field", org.thryft.protocol.Type.MAP, (short)-1);
                    oprot.writeMapBegin(org.thryft.protocol.Type.STRING, org.thryft.protocol.Type.STRING, getStringStringMapField().get().size());
                    for (com.google.common.collect.ImmutableMap.Entry<String, String> _iter0 : getStringStringMapField().get().entrySet()) {
                        oprot.writeString(_iter0.getKey());
                        oprot.writeString(_iter0.getValue());
                    }
                    oprot.writeMapEnd();
                    oprot.writeFieldEnd();
                }

                if (getStringSetField().isPresent()) {
                    oprot.writeFieldBegin("string_set_field", org.thryft.protocol.Type.SET, (short)-1);
                    oprot.writeSetBegin(org.thryft.protocol.Type.STRING, getStringSetField().get().size());
                    for (final String _iter0 : getStringSetField().get()) {
                        oprot.writeString(_iter0);
                    }
                    oprot.writeSetEnd();
                    oprot.writeFieldEnd();
                }

                if (getStringField().isPresent()) {
                    oprot.writeFieldBegin("string_field", org.thryft.protocol.Type.STRING, (short)-1);
                    oprot.writeString(getStringField().get());
                    oprot.writeFieldEnd();
                }

                if (getUrlField().isPresent()) {
                    oprot.writeFieldBegin("url_field", org.thryft.protocol.Type.STRING, (short)-1);
                    oprot.writeString(getUrlField().get().toString());
                    oprot.writeFieldEnd();
                }

                oprot.writeFieldStop();

                oprot.writeStructEnd();
                break;
        }
    }

    private final int requiredI32Field;

    private final String requiredStringField;

    private final com.google.common.base.Optional<byte[]> binaryField;

    private final com.google.common.base.Optional<Boolean> boolField;

    private final com.google.common.base.Optional<Byte> byteField;

    private final com.google.common.base.Optional<java.util.Date> dateTimeField;

    private final com.google.common.base.Optional<java.math.BigDecimal> decimalField;

    private final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField;

    private final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;

    private final com.google.common.base.Optional<Short> i16Field;

    private final com.google.common.base.Optional<Integer> i32Field;

    private final com.google.common.base.Optional<Long> i64Field;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;

    private final com.google.common.base.Optional<String> stringField;

    private final com.google.common.base.Optional<org.thryft.native_.Url> urlField;
}
