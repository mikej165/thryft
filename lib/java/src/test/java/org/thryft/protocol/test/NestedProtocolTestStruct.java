package org.thryft.protocol.test;

public final class NestedProtocolTestStruct implements org.thryft.Struct {
    public final static class Builder {
        public Builder() {
            requiredI32Field = 0;
            requiredStringField = null;
            binaryField = com.google.common.base.Optional.<byte[]> absent();
            boolField = com.google.common.base.Optional.<Boolean> absent();
            byteField = com.google.common.base.Optional.<Byte> absent();
            dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
            decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
            emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
            enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
            i16Field = com.google.common.base.Optional.<Short> absent();
            i32Field = com.google.common.base.Optional.<Integer> absent();
            i64Field = com.google.common.base.Optional.<Long> absent();
            stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
            stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
            stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
            stringField = com.google.common.base.Optional.<String> absent();
            urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();
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
            return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField, DefaultConstructionValidator.getInstance());
        }

        public NestedProtocolTestStruct build() {
            return _build(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField);
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

        public Builder readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
            return readAs(iprot, type, com.google.common.base.Optional.<UnknownFieldCallback> absent());
        }

        public Builder readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            switch (type) {
            case LIST:
                return readAsList(iprot);
            case STRUCT:
                return readAsStruct(iprot, unknownFieldCallback);
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
                     throw e.getCause();
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
                     throw e.getCause();
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
                     throw e.getCause();
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
                         throw e.getCause();
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
                         throw e.getCause();
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
                         throw e.getCause();
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

        public Builder set(final String fieldThriftName, @javax.annotation.Nullable final java.lang.Object value) {
            return set(FieldMetadata.valueOfThriftName(fieldThriftName), value);
        }

        public Builder set(final org.thryft.Struct.FieldMetadata fieldMetadata, @javax.annotation.Nullable final java.lang.Object value) {
            if (!(fieldMetadata instanceof FieldMetadata)) {
                throw new IllegalArgumentException();
            }
            return set((FieldMetadata)fieldMetadata, value);
        }

        @SuppressWarnings({"unchecked"})
        public Builder set(final FieldMetadata fieldMetadata, @javax.annotation.Nullable final java.lang.Object value) {
            com.google.common.base.Preconditions.checkNotNull(fieldMetadata);

            switch (fieldMetadata) {
            case REQUIRED_I32_FIELD: setRequiredI32Field((int)value); return this;
            case REQUIRED_STRING_FIELD: setRequiredStringField((String)value); return this;
            case BINARY_FIELD: setBinaryField((byte[])value); return this;
            case BOOL_FIELD: setBoolField((Boolean)value); return this;
            case BYTE_FIELD: setByteField((Byte)value); return this;
            case DATE_TIME_FIELD: setDateTimeField((java.util.Date)value); return this;
            case DECIMAL_FIELD: setDecimalField((java.math.BigDecimal)value); return this;
            case EMAIL_ADDRESS_FIELD: setEmailAddressField((org.thryft.native_.EmailAddress)value); return this;
            case ENUM_FIELD: setEnumField((org.thryft.protocol.test.ProtocolTestEnum)value); return this;
            case I16_FIELD: setI16Field((Short)value); return this;
            case I32_FIELD: setI32Field((Integer)value); return this;
            case I64_FIELD: setI64Field((Long)value); return this;
            case STRING_LIST_FIELD: setStringListField((com.google.common.collect.ImmutableList<String>)value); return this;
            case STRING_STRING_MAP_FIELD: setStringStringMapField((com.google.common.collect.ImmutableMap<String, String>)value); return this;
            case STRING_SET_FIELD: setStringSetField((com.google.common.collect.ImmutableSet<String>)value); return this;
            case STRING_FIELD: setStringField((String)value); return this;
            case URL_FIELD: setUrlField((org.thryft.native_.Url)value); return this;
            default:
                throw new IllegalStateException();
            }
        }

        public Builder setBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
            this.binaryField = DefaultConstructionValidator.getInstance().validateBinaryField(binaryField);
            return this;
        }

        public Builder setBinaryField(@javax.annotation.Nullable final byte[] binaryField) {
            return setBinaryField(com.google.common.base.Optional.fromNullable(binaryField));
        }

        public Builder setBoolField(final com.google.common.base.Optional<Boolean> boolField) {
            this.boolField = DefaultConstructionValidator.getInstance().validateBoolField(boolField);
            return this;
        }

        public Builder setBoolField(@javax.annotation.Nullable final Boolean boolField) {
            return setBoolField(com.google.common.base.Optional.fromNullable(boolField));
        }

        public Builder setByteField(final com.google.common.base.Optional<Byte> byteField) {
            this.byteField = DefaultConstructionValidator.getInstance().validateByteField(byteField);
            return this;
        }

        public Builder setByteField(@javax.annotation.Nullable final Byte byteField) {
            return setByteField(com.google.common.base.Optional.fromNullable(byteField));
        }

        public Builder setDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
            this.dateTimeField = DefaultConstructionValidator.getInstance().validateDateTimeField(dateTimeField);
            return this;
        }

        public Builder setDateTimeField(@javax.annotation.Nullable final java.util.Date dateTimeField) {
            return setDateTimeField(com.google.common.base.Optional.fromNullable(dateTimeField));
        }

        public Builder setDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
            this.decimalField = DefaultConstructionValidator.getInstance().validateDecimalField(decimalField);
            return this;
        }

        public Builder setDecimalField(@javax.annotation.Nullable final java.math.BigDecimal decimalField) {
            return setDecimalField(com.google.common.base.Optional.fromNullable(decimalField));
        }

        public Builder setEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
            this.emailAddressField = DefaultConstructionValidator.getInstance().validateEmailAddressField(emailAddressField);
            return this;
        }

        public Builder setEmailAddressField(@javax.annotation.Nullable final org.thryft.native_.EmailAddress emailAddressField) {
            return setEmailAddressField(com.google.common.base.Optional.fromNullable(emailAddressField));
        }

        public Builder setEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
            this.enumField = DefaultConstructionValidator.getInstance().validateEnumField(enumField);
            return this;
        }

        public Builder setEnumField(@javax.annotation.Nullable final org.thryft.protocol.test.ProtocolTestEnum enumField) {
            return setEnumField(com.google.common.base.Optional.fromNullable(enumField));
        }

        public Builder setI16Field(final com.google.common.base.Optional<Short> i16Field) {
            this.i16Field = DefaultConstructionValidator.getInstance().validateI16Field(i16Field);
            return this;
        }

        public Builder setI16Field(@javax.annotation.Nullable final Short i16Field) {
            return setI16Field(com.google.common.base.Optional.fromNullable(i16Field));
        }

        public Builder setI32Field(final com.google.common.base.Optional<Integer> i32Field) {
            this.i32Field = DefaultConstructionValidator.getInstance().validateI32Field(i32Field);
            return this;
        }

        public Builder setI32Field(@javax.annotation.Nullable final Integer i32Field) {
            return setI32Field(com.google.common.base.Optional.fromNullable(i32Field));
        }

        public Builder setI64Field(final com.google.common.base.Optional<Long> i64Field) {
            this.i64Field = DefaultConstructionValidator.getInstance().validateI64Field(i64Field);
            return this;
        }

        public Builder setI64Field(@javax.annotation.Nullable final Long i64Field) {
            return setI64Field(com.google.common.base.Optional.fromNullable(i64Field));
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
            this.requiredI32Field = DefaultConstructionValidator.getInstance().validateRequiredI32Field(requiredI32Field);
            return this;
        }

        public Builder setRequiredStringField(final String requiredStringField) {
            this.requiredStringField = DefaultConstructionValidator.getInstance().validateRequiredStringField(requiredStringField);
            return this;
        }

        public Builder setStringField(final com.google.common.base.Optional<String> stringField) {
            this.stringField = DefaultConstructionValidator.getInstance().validateStringField(stringField);
            return this;
        }

        public Builder setStringField(@javax.annotation.Nullable final String stringField) {
            return setStringField(com.google.common.base.Optional.fromNullable(stringField));
        }

        public Builder setStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
            this.stringListField = DefaultConstructionValidator.getInstance().validateStringListField(stringListField);
            return this;
        }

        public Builder setStringListField(@javax.annotation.Nullable final com.google.common.collect.ImmutableList<String> stringListField) {
            return setStringListField(com.google.common.base.Optional.fromNullable(stringListField));
        }

        public Builder setStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
            this.stringSetField = DefaultConstructionValidator.getInstance().validateStringSetField(stringSetField);
            return this;
        }

        public Builder setStringSetField(@javax.annotation.Nullable final com.google.common.collect.ImmutableSet<String> stringSetField) {
            return setStringSetField(com.google.common.base.Optional.fromNullable(stringSetField));
        }

        public Builder setStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
            this.stringStringMapField = DefaultConstructionValidator.getInstance().validateStringStringMapField(stringStringMapField);
            return this;
        }

        public Builder setStringStringMapField(@javax.annotation.Nullable final com.google.common.collect.ImmutableMap<String, String> stringStringMapField) {
            return setStringStringMapField(com.google.common.base.Optional.fromNullable(stringStringMapField));
        }

        public Builder setUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            this.urlField = DefaultConstructionValidator.getInstance().validateUrlField(urlField);
            return this;
        }

        public Builder setUrlField(@javax.annotation.Nullable final org.thryft.native_.Url urlField) {
            return setUrlField(com.google.common.base.Optional.fromNullable(urlField));
        }

        public Builder unset(final String fieldThriftName) {
            return unset(FieldMetadata.valueOfThriftName(fieldThriftName));
        }

        public Builder unset(final org.thryft.Struct.FieldMetadata fieldMetadata) {
            if (!(fieldMetadata instanceof FieldMetadata)) {
                throw new IllegalArgumentException();
            }
            return unset((FieldMetadata)fieldMetadata);
        }

        public Builder unset(final FieldMetadata fieldMetadata) {
            com.google.common.base.Preconditions.checkNotNull(fieldMetadata);

            switch (fieldMetadata) {
            case REQUIRED_I32_FIELD: return unsetRequiredI32Field();
            case REQUIRED_STRING_FIELD: return unsetRequiredStringField();
            case BINARY_FIELD: return unsetBinaryField();
            case BOOL_FIELD: return unsetBoolField();
            case BYTE_FIELD: return unsetByteField();
            case DATE_TIME_FIELD: return unsetDateTimeField();
            case DECIMAL_FIELD: return unsetDecimalField();
            case EMAIL_ADDRESS_FIELD: return unsetEmailAddressField();
            case ENUM_FIELD: return unsetEnumField();
            case I16_FIELD: return unsetI16Field();
            case I32_FIELD: return unsetI32Field();
            case I64_FIELD: return unsetI64Field();
            case STRING_LIST_FIELD: return unsetStringListField();
            case STRING_STRING_MAP_FIELD: return unsetStringStringMapField();
            case STRING_SET_FIELD: return unsetStringSetField();
            case STRING_FIELD: return unsetStringField();
            case URL_FIELD: return unsetUrlField();
            default:
                throw new IllegalStateException();
            }
        }

        public Builder unsetBinaryField() {
            this.binaryField = com.google.common.base.Optional.<byte[]> absent();
            return this;
        }

        public Builder unsetBoolField() {
            this.boolField = com.google.common.base.Optional.<Boolean> absent();
            return this;
        }

        public Builder unsetByteField() {
            this.byteField = com.google.common.base.Optional.<Byte> absent();
            return this;
        }

        public Builder unsetDateTimeField() {
            this.dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
            return this;
        }

        public Builder unsetDecimalField() {
            this.decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
            return this;
        }

        public Builder unsetEmailAddressField() {
            this.emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
            return this;
        }

        public Builder unsetEnumField() {
            this.enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
            return this;
        }

        public Builder unsetI16Field() {
            this.i16Field = com.google.common.base.Optional.<Short> absent();
            return this;
        }

        public Builder unsetI32Field() {
            this.i32Field = com.google.common.base.Optional.<Integer> absent();
            return this;
        }

        public Builder unsetI64Field() {
            this.i64Field = com.google.common.base.Optional.<Long> absent();
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
            this.stringField = com.google.common.base.Optional.<String> absent();
            return this;
        }

        public Builder unsetStringListField() {
            this.stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
            return this;
        }

        public Builder unsetStringSetField() {
            this.stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
            return this;
        }

        public Builder unsetStringStringMapField() {
            this.stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
            return this;
        }

        public Builder unsetUrlField() {
            this.urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();
            return this;
        }

        private Integer requiredI32Field;
        private String requiredStringField;
        private com.google.common.base.Optional<byte[]> binaryField;
        private com.google.common.base.Optional<Boolean> boolField;
        private com.google.common.base.Optional<Byte> byteField;
        private com.google.common.base.Optional<java.util.Date> dateTimeField;
        private com.google.common.base.Optional<java.math.BigDecimal> decimalField;
        private com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField;
        private com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;
        private com.google.common.base.Optional<Short> i16Field;
        private com.google.common.base.Optional<Integer> i32Field;
        private com.google.common.base.Optional<Long> i64Field;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;
        private com.google.common.base.Optional<String> stringField;
        private com.google.common.base.Optional<org.thryft.native_.Url> urlField;
    }

    public final static class Factory implements org.thryft.CompoundType.Factory<NestedProtocolTestStruct> {
        @Override
        public NestedProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
            return NestedProtocolTestStruct.readAs(iprot, type);
        }

        @Override
        public NestedProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type,
                final com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            return NestedProtocolTestStruct.readAs(iprot, type, unknownFieldCallback);
        }

        @Override
        public NestedProtocolTestStruct readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            return NestedProtocolTestStruct.readAsList(iprot);
        }

        @Override
        public NestedProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            return NestedProtocolTestStruct.readAsStruct(iprot);
        }

        @Override
        public NestedProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot,
                final com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            return NestedProtocolTestStruct.readAsStruct(iprot, unknownFieldCallback);
        }
    }

    @SuppressWarnings("serial")
    public enum FieldMetadata implements org.thryft.CompoundType.FieldMetadata {
        REQUIRED_I32_FIELD("requiredI32Field", new com.google.common.reflect.TypeToken<Integer>() {}, true, 0, "required_i32_field", org.thryft.protocol.Type.I32),
        REQUIRED_STRING_FIELD("requiredStringField", new com.google.common.reflect.TypeToken<String>() {}, true, 0, "required_string_field", org.thryft.protocol.Type.STRING),
        BINARY_FIELD("binaryField", new com.google.common.reflect.TypeToken<byte[]>() {}, false, 0, "binary_field", org.thryft.protocol.Type.STRING),
        BOOL_FIELD("boolField", new com.google.common.reflect.TypeToken<Boolean>() {}, false, 0, "bool_field", org.thryft.protocol.Type.BOOL),
        BYTE_FIELD("byteField", new com.google.common.reflect.TypeToken<Byte>() {}, false, 0, "byte_field", org.thryft.protocol.Type.BYTE),
        DATE_TIME_FIELD("dateTimeField", new com.google.common.reflect.TypeToken<java.util.Date>() {}, false, 0, "date_time_field", org.thryft.protocol.Type.I64),
        DECIMAL_FIELD("decimalField", new com.google.common.reflect.TypeToken<java.math.BigDecimal>() {}, false, 0, "decimal_field", org.thryft.protocol.Type.STRING),
        EMAIL_ADDRESS_FIELD("emailAddressField", new com.google.common.reflect.TypeToken<org.thryft.native_.EmailAddress>() {}, false, 0, "email_address_field", org.thryft.protocol.Type.STRING),
        ENUM_FIELD("enumField", new com.google.common.reflect.TypeToken<org.thryft.protocol.test.ProtocolTestEnum>() {}, false, 0, "enum_field", org.thryft.protocol.Type.STRING),
        I16_FIELD("i16Field", new com.google.common.reflect.TypeToken<Short>() {}, false, 0, "i16_field", org.thryft.protocol.Type.I16),
        I32_FIELD("i32Field", new com.google.common.reflect.TypeToken<Integer>() {}, false, 0, "i32_field", org.thryft.protocol.Type.I32),
        I64_FIELD("i64Field", new com.google.common.reflect.TypeToken<Long>() {}, false, 0, "i64_field", org.thryft.protocol.Type.I64),
        STRING_LIST_FIELD("stringListField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableList<String>>() {}, false, 0, "string_list_field", org.thryft.protocol.Type.LIST),
        STRING_STRING_MAP_FIELD("stringStringMapField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableMap<String, String>>() {}, false, 0, "string_string_map_field", org.thryft.protocol.Type.MAP),
        STRING_SET_FIELD("stringSetField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableSet<String>>() {}, false, 0, "string_set_field", org.thryft.protocol.Type.SET),
        STRING_FIELD("stringField", new com.google.common.reflect.TypeToken<String>() {}, false, 0, "string_field", org.thryft.protocol.Type.STRING),
        URL_FIELD("urlField", new com.google.common.reflect.TypeToken<org.thryft.native_.Url>() {}, false, 0, "url_field", org.thryft.protocol.Type.STRING);

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

    public interface Validator<ExceptionT extends Exception> {
        public int validateRequiredI32Field(final int requiredI32Field) throws ExceptionT;

        public String validateRequiredStringField(final String requiredStringField) throws ExceptionT;

        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) throws ExceptionT;

        public com.google.common.base.Optional<Boolean> validateBoolField(final com.google.common.base.Optional<Boolean> boolField) throws ExceptionT;

        public com.google.common.base.Optional<Byte> validateByteField(final com.google.common.base.Optional<Byte> byteField) throws ExceptionT;

        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) throws ExceptionT;

        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) throws ExceptionT;

        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) throws ExceptionT;

        public com.google.common.base.Optional<Integer> validateI32Field(final com.google.common.base.Optional<Integer> i32Field) throws ExceptionT;

        public com.google.common.base.Optional<Long> validateI64Field(final com.google.common.base.Optional<Long> i64Field) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) throws ExceptionT;

        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) throws ExceptionT;
    }

    public interface ConstructionValidator extends Validator<RuntimeException> {
    }

    public static class DefaultConstructionValidator implements ConstructionValidator {
        public static DefaultConstructionValidator getInstance() {
            return instance;
        }

        public DefaultConstructionValidator() {
        }

        @Override
        public int validateRequiredI32Field(final int requiredI32Field) throws RuntimeException {
            return requiredI32Field;
        }

        @Override
        public String validateRequiredStringField(final String requiredStringField) throws RuntimeException {
            if (requiredStringField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is null");
            }
            if (requiredStringField.isEmpty()) {
                throw new IllegalArgumentException("org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is less than min length 1");
            }
            return requiredStringField;
        }

        @Override
        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) throws RuntimeException {
            if (binaryField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: binaryField is null");
            }
            if (!binaryField.isPresent()) {
                return binaryField;
            }
            return binaryField;
        }

        @Override
        public com.google.common.base.Optional<Boolean> validateBoolField(final com.google.common.base.Optional<Boolean> boolField) throws RuntimeException {
            if (!boolField.isPresent()) {
                return boolField;
            }
            return boolField;
        }

        @Override
        public com.google.common.base.Optional<Byte> validateByteField(final com.google.common.base.Optional<Byte> byteField) throws RuntimeException {
            if (!byteField.isPresent()) {
                return byteField;
            }
            return byteField;
        }

        @Override
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) throws RuntimeException {
            if (dateTimeField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: dateTimeField is null");
            }
            if (!dateTimeField.isPresent()) {
                return dateTimeField;
            }
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) throws RuntimeException {
            if (decimalField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: decimalField is null");
            }
            if (!decimalField.isPresent()) {
                return decimalField;
            }
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) throws RuntimeException {
            if (emailAddressField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: emailAddressField is null");
            }
            if (!emailAddressField.isPresent()) {
                return emailAddressField;
            }
            return emailAddressField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) throws RuntimeException {
            if (enumField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: enumField is null");
            }
            if (!enumField.isPresent()) {
                return enumField;
            }
            return enumField;
        }

        @Override
        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) throws RuntimeException {
            if (!i16Field.isPresent()) {
                return i16Field;
            }
            return i16Field;
        }

        @Override
        public com.google.common.base.Optional<Integer> validateI32Field(final com.google.common.base.Optional<Integer> i32Field) throws RuntimeException {
            if (!i32Field.isPresent()) {
                return i32Field;
            }
            return i32Field;
        }

        @Override
        public com.google.common.base.Optional<Long> validateI64Field(final com.google.common.base.Optional<Long> i64Field) throws RuntimeException {
            if (!i64Field.isPresent()) {
                return i64Field;
            }
            return i64Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) throws RuntimeException {
            if (stringListField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: stringListField is null");
            }
            if (!stringListField.isPresent()) {
                return stringListField;
            }
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) throws RuntimeException {
            if (stringStringMapField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: stringStringMapField is null");
            }
            if (!stringStringMapField.isPresent()) {
                return stringStringMapField;
            }
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) throws RuntimeException {
            if (stringSetField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: stringSetField is null");
            }
            if (!stringSetField.isPresent()) {
                return stringSetField;
            }
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) throws RuntimeException {
            if (stringField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: stringField is null");
            }
            if (!stringField.isPresent()) {
                return stringField;
            }
            if (stringField.get().isEmpty()) {
                throw new IllegalArgumentException("org.thryft.protocol.test.NestedProtocolTestStruct: stringField is less than min length 1");
            }
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) throws RuntimeException {
            if (urlField == null) {
                throw new NullPointerException("org.thryft.protocol.test.NestedProtocolTestStruct: urlField is null");
            }
            if (!urlField.isPresent()) {
                return urlField;
            }
            return urlField;
        }

        private final static DefaultConstructionValidator instance = new DefaultConstructionValidator();
    }

    public static class NopConstructionValidator implements ConstructionValidator {
        public static NopConstructionValidator getInstance() {
            return instance;
        }

        public NopConstructionValidator() {
        }

        @Override
        public int validateRequiredI32Field(final int requiredI32Field) {
            return requiredI32Field;
        }

        @Override
        public String validateRequiredStringField(final String requiredStringField) {
            return requiredStringField;
        }

        @Override
        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
            return binaryField;
        }

        @Override
        public com.google.common.base.Optional<Boolean> validateBoolField(final com.google.common.base.Optional<Boolean> boolField) {
            return boolField;
        }

        @Override
        public com.google.common.base.Optional<Byte> validateByteField(final com.google.common.base.Optional<Byte> byteField) {
            return byteField;
        }

        @Override
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
            return emailAddressField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
            return enumField;
        }

        @Override
        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) {
            return i16Field;
        }

        @Override
        public com.google.common.base.Optional<Integer> validateI32Field(final com.google.common.base.Optional<Integer> i32Field) {
            return i32Field;
        }

        @Override
        public com.google.common.base.Optional<Long> validateI64Field(final com.google.common.base.Optional<Long> i64Field) {
            return i64Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) {
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            return urlField;
        }

        private final static NopConstructionValidator instance = new NopConstructionValidator();
    }

    public interface ReadValidator extends Validator<org.thryft.protocol.InputProtocolException> {
    }

    public static class DefaultReadValidator implements ReadValidator {
        public static DefaultReadValidator getInstance() {
            return instance;
        }

        public DefaultReadValidator() {
        }

        @Override
        public int validateRequiredI32Field(final int requiredI32Field) throws org.thryft.protocol.InputProtocolException {
            return requiredI32Field;
        }

        @Override
        public String validateRequiredStringField(final String requiredStringField) throws org.thryft.protocol.InputProtocolException {
            if (requiredStringField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.REQUIRED_STRING_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is null");
            }
            if (requiredStringField.isEmpty()) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.REQUIRED_STRING_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: requiredStringField is less than min length 1");
            }
            return requiredStringField;
        }

        @Override
        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) throws org.thryft.protocol.InputProtocolException {
            if (binaryField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.BINARY_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: binaryField is null");
            }
            if (!binaryField.isPresent()) {
                return binaryField;
            }
            return binaryField;
        }

        @Override
        public com.google.common.base.Optional<Boolean> validateBoolField(final com.google.common.base.Optional<Boolean> boolField) throws org.thryft.protocol.InputProtocolException {
            if (!boolField.isPresent()) {
                return boolField;
            }
            return boolField;
        }

        @Override
        public com.google.common.base.Optional<Byte> validateByteField(final com.google.common.base.Optional<Byte> byteField) throws org.thryft.protocol.InputProtocolException {
            if (!byteField.isPresent()) {
                return byteField;
            }
            return byteField;
        }

        @Override
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) throws org.thryft.protocol.InputProtocolException {
            if (dateTimeField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.DATE_TIME_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: dateTimeField is null");
            }
            if (!dateTimeField.isPresent()) {
                return dateTimeField;
            }
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) throws org.thryft.protocol.InputProtocolException {
            if (decimalField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.DECIMAL_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: decimalField is null");
            }
            if (!decimalField.isPresent()) {
                return decimalField;
            }
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) throws org.thryft.protocol.InputProtocolException {
            if (emailAddressField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.EMAIL_ADDRESS_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: emailAddressField is null");
            }
            if (!emailAddressField.isPresent()) {
                return emailAddressField;
            }
            return emailAddressField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) throws org.thryft.protocol.InputProtocolException {
            if (enumField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.ENUM_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: enumField is null");
            }
            if (!enumField.isPresent()) {
                return enumField;
            }
            return enumField;
        }

        @Override
        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) throws org.thryft.protocol.InputProtocolException {
            if (!i16Field.isPresent()) {
                return i16Field;
            }
            return i16Field;
        }

        @Override
        public com.google.common.base.Optional<Integer> validateI32Field(final com.google.common.base.Optional<Integer> i32Field) throws org.thryft.protocol.InputProtocolException {
            if (!i32Field.isPresent()) {
                return i32Field;
            }
            return i32Field;
        }

        @Override
        public com.google.common.base.Optional<Long> validateI64Field(final com.google.common.base.Optional<Long> i64Field) throws org.thryft.protocol.InputProtocolException {
            if (!i64Field.isPresent()) {
                return i64Field;
            }
            return i64Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) throws org.thryft.protocol.InputProtocolException {
            if (stringListField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_LIST_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: stringListField is null");
            }
            if (!stringListField.isPresent()) {
                return stringListField;
            }
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) throws org.thryft.protocol.InputProtocolException {
            if (stringStringMapField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_STRING_MAP_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: stringStringMapField is null");
            }
            if (!stringStringMapField.isPresent()) {
                return stringStringMapField;
            }
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) throws org.thryft.protocol.InputProtocolException {
            if (stringSetField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_SET_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: stringSetField is null");
            }
            if (!stringSetField.isPresent()) {
                return stringSetField;
            }
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) throws org.thryft.protocol.InputProtocolException {
            if (stringField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is null");
            }
            if (!stringField.isPresent()) {
                return stringField;
            }
            if (stringField.get().isEmpty()) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: stringField is less than min length 1");
            }
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) throws org.thryft.protocol.InputProtocolException {
            if (urlField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.URL_FIELD, "org.thryft.protocol.test.NestedProtocolTestStruct: urlField is null");
            }
            if (!urlField.isPresent()) {
                return urlField;
            }
            return urlField;
        }

        private final static DefaultReadValidator instance = new DefaultReadValidator();
    }

    public static class NopReadValidator implements ReadValidator {
        public static NopReadValidator getInstance() {
            return instance;
        }

        public NopReadValidator() {
        }

        @Override
        public int validateRequiredI32Field(final int requiredI32Field) {
            return requiredI32Field;
        }

        @Override
        public String validateRequiredStringField(final String requiredStringField) {
            return requiredStringField;
        }

        @Override
        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
            return binaryField;
        }

        @Override
        public com.google.common.base.Optional<Boolean> validateBoolField(final com.google.common.base.Optional<Boolean> boolField) {
            return boolField;
        }

        @Override
        public com.google.common.base.Optional<Byte> validateByteField(final com.google.common.base.Optional<Byte> byteField) {
            return byteField;
        }

        @Override
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
            return emailAddressField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
            return enumField;
        }

        @Override
        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) {
            return i16Field;
        }

        @Override
        public com.google.common.base.Optional<Integer> validateI32Field(final com.google.common.base.Optional<Integer> i32Field) {
            return i32Field;
        }

        @Override
        public com.google.common.base.Optional<Long> validateI64Field(final com.google.common.base.Optional<Long> i64Field) {
            return i64Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) {
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            return urlField;
        }

        private final static NopReadValidator instance = new NopReadValidator();
    }

    /**
     * Copy constructor
     */
    public NestedProtocolTestStruct(final NestedProtocolTestStruct other) {
        this(other.getRequiredI32Field(), other.getRequiredStringField(), other.getBinaryField(), other.getBoolField(), other.getByteField(), other.getDateTimeField(), other.getDecimalField(), other.getEmailAddressField(), other.getEnumField(), other.getI16Field(), other.getI32Field(), other.getI64Field(), other.getStringListField(), other.getStringStringMapField(), other.getStringSetField(), other.getStringField(), other.getUrlField(), NopConstructionValidator.getInstance());
    }

    protected NestedProtocolTestStruct(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<Byte> byteField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, ConstructionValidator validator) {
        this.requiredI32Field = validator.validateRequiredI32Field(requiredI32Field);
        this.requiredStringField = validator.validateRequiredStringField(requiredStringField);
        this.binaryField = validator.validateBinaryField(binaryField);
        this.boolField = validator.validateBoolField(boolField);
        this.byteField = validator.validateByteField(byteField);
        this.dateTimeField = validator.validateDateTimeField(dateTimeField);
        this.decimalField = validator.validateDecimalField(decimalField);
        this.emailAddressField = validator.validateEmailAddressField(emailAddressField);
        this.enumField = validator.validateEnumField(enumField);
        this.i16Field = validator.validateI16Field(i16Field);
        this.i32Field = validator.validateI32Field(i32Field);
        this.i64Field = validator.validateI64Field(i64Field);
        this.stringListField = validator.validateStringListField(stringListField);
        this.stringStringMapField = validator.validateStringStringMapField(stringStringMapField);
        this.stringSetField = validator.validateStringSetField(stringSetField);
        this.stringField = validator.validateStringField(stringField);
        this.urlField = validator.validateUrlField(urlField);
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

    /**
     * Required factory method
     */
    public static NestedProtocolTestStruct create(final int requiredI32Field, final String requiredStringField) {
        return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, com.google.common.base.Optional.<byte[]> absent(), com.google.common.base.Optional.<Boolean> absent(), com.google.common.base.Optional.<Byte> absent(), com.google.common.base.Optional.<java.util.Date> absent(), com.google.common.base.Optional.<java.math.BigDecimal> absent(), com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent(), com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent(), com.google.common.base.Optional.<Short> absent(), com.google.common.base.Optional.<Integer> absent(), com.google.common.base.Optional.<Long> absent(), com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent(), com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent(), com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent(), com.google.common.base.Optional.<String> absent(), com.google.common.base.Optional.<org.thryft.native_.Url> absent(), DefaultConstructionValidator.getInstance());
    }

    /**
     * Total boxed factory method
     */
    public static NestedProtocolTestStruct create(Integer requiredI32Field, String requiredStringField, com.google.common.base.Optional<byte[]> binaryField, com.google.common.base.Optional<Boolean> boolField, com.google.common.base.Optional<Byte> byteField, com.google.common.base.Optional<java.util.Date> dateTimeField, com.google.common.base.Optional<java.math.BigDecimal> decimalField, com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, com.google.common.base.Optional<Short> i16Field, com.google.common.base.Optional<Integer> i32Field, com.google.common.base.Optional<Long> i64Field, com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, com.google.common.base.Optional<String> stringField, com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField, DefaultConstructionValidator.getInstance());
    }

    /**
     * Total Nullable factory method
     */
    public static NestedProtocolTestStruct create(final int requiredI32Field, final String requiredStringField, final @javax.annotation.Nullable byte[] binaryField, final @javax.annotation.Nullable Boolean boolField, final @javax.annotation.Nullable Byte byteField, final @javax.annotation.Nullable java.util.Date dateTimeField, final @javax.annotation.Nullable java.math.BigDecimal decimalField, final @javax.annotation.Nullable org.thryft.native_.EmailAddress emailAddressField, final @javax.annotation.Nullable org.thryft.protocol.test.ProtocolTestEnum enumField, final @javax.annotation.Nullable Short i16Field, final @javax.annotation.Nullable Integer i32Field, final @javax.annotation.Nullable Long i64Field, final @javax.annotation.Nullable com.google.common.collect.ImmutableList<String> stringListField, final @javax.annotation.Nullable com.google.common.collect.ImmutableMap<String, String> stringStringMapField, final @javax.annotation.Nullable com.google.common.collect.ImmutableSet<String> stringSetField, final @javax.annotation.Nullable String stringField, final @javax.annotation.Nullable org.thryft.native_.Url urlField) {
        return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, com.google.common.base.Optional.fromNullable(binaryField), com.google.common.base.Optional.fromNullable(boolField), com.google.common.base.Optional.fromNullable(byteField), com.google.common.base.Optional.fromNullable(dateTimeField), com.google.common.base.Optional.fromNullable(decimalField), com.google.common.base.Optional.fromNullable(emailAddressField), com.google.common.base.Optional.fromNullable(enumField), com.google.common.base.Optional.fromNullable(i16Field), com.google.common.base.Optional.fromNullable(i32Field), com.google.common.base.Optional.fromNullable(i64Field), com.google.common.base.Optional.fromNullable(stringListField), com.google.common.base.Optional.fromNullable(stringStringMapField), com.google.common.base.Optional.fromNullable(stringSetField), com.google.common.base.Optional.fromNullable(stringField), com.google.common.base.Optional.fromNullable(urlField), DefaultConstructionValidator.getInstance());
    }

    /**
     * Optional factory method
     */
    public static NestedProtocolTestStruct create(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<Byte> byteField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        return new NestedProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, byteField, dateTimeField, decimalField, emailAddressField, enumField, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, urlField, DefaultConstructionValidator.getInstance());
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
            ((getBinaryField().isPresent() && other.getBinaryField().isPresent()) ? (java.util.Arrays.equals(getBinaryField().get(), other.getBinaryField().get())) : (!getBinaryField().isPresent() && !other.getBinaryField().isPresent())) &&
            ((getBoolField().isPresent() && other.getBoolField().isPresent()) ? (getBoolField().get() == other.getBoolField().get()) : (!getBoolField().isPresent() && !other.getBoolField().isPresent())) &&
            ((getByteField().isPresent() && other.getByteField().isPresent()) ? (getByteField().get() == other.getByteField().get()) : (!getByteField().isPresent() && !other.getByteField().isPresent())) &&
            ((getDateTimeField().isPresent() && other.getDateTimeField().isPresent()) ? (getDateTimeField().get().equals(other.getDateTimeField().get())) : (!getDateTimeField().isPresent() && !other.getDateTimeField().isPresent())) &&
            ((getDecimalField().isPresent() && other.getDecimalField().isPresent()) ? (getDecimalField().get().equals(other.getDecimalField().get())) : (!getDecimalField().isPresent() && !other.getDecimalField().isPresent())) &&
            ((getEmailAddressField().isPresent() && other.getEmailAddressField().isPresent()) ? (getEmailAddressField().get().equals(other.getEmailAddressField().get())) : (!getEmailAddressField().isPresent() && !other.getEmailAddressField().isPresent())) &&
            ((getEnumField().isPresent() && other.getEnumField().isPresent()) ? (getEnumField().get().equals(other.getEnumField().get())) : (!getEnumField().isPresent() && !other.getEnumField().isPresent())) &&
            ((getI16Field().isPresent() && other.getI16Field().isPresent()) ? (getI16Field().get() == other.getI16Field().get()) : (!getI16Field().isPresent() && !other.getI16Field().isPresent())) &&
            ((getI32Field().isPresent() && other.getI32Field().isPresent()) ? (getI32Field().get() == other.getI32Field().get()) : (!getI32Field().isPresent() && !other.getI32Field().isPresent())) &&
            ((getI64Field().isPresent() && other.getI64Field().isPresent()) ? (getI64Field().get() == other.getI64Field().get()) : (!getI64Field().isPresent() && !other.getI64Field().isPresent())) &&
            ((getStringListField().isPresent() && other.getStringListField().isPresent()) ? (getStringListField().get().equals(other.getStringListField().get())) : (!getStringListField().isPresent() && !other.getStringListField().isPresent())) &&
            ((getStringStringMapField().isPresent() && other.getStringStringMapField().isPresent()) ? (getStringStringMapField().get().equals(other.getStringStringMapField().get())) : (!getStringStringMapField().isPresent() && !other.getStringStringMapField().isPresent())) &&
            ((getStringSetField().isPresent() && other.getStringSetField().isPresent()) ? (getStringSetField().get().equals(other.getStringSetField().get())) : (!getStringSetField().isPresent() && !other.getStringSetField().isPresent())) &&
            ((getStringField().isPresent() && other.getStringField().isPresent()) ? (getStringField().get().equals(other.getStringField().get())) : (!getStringField().isPresent() && !other.getStringField().isPresent())) &&
            ((getUrlField().isPresent() && other.getUrlField().isPresent()) ? (getUrlField().get().equals(other.getUrlField().get())) : (!getUrlField().isPresent() && !other.getUrlField().isPresent()));
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

    public static NestedProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
        return readAs(iprot, type, com.google.common.base.Optional.<UnknownFieldCallback> absent());
    }

    public static NestedProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        switch (type) {
        case LIST:
            return readAsList(iprot);
        case STRUCT:
            return readAsStruct(iprot, unknownFieldCallback);
        default:
            throw new IllegalArgumentException("cannot read as " + type);
        }
    }

    public static NestedProtocolTestStruct readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.<byte[]> absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.<Boolean> absent();
        com.google.common.base.Optional<Byte> byteField = com.google.common.base.Optional.<Byte> absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.<Short> absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.<Integer> absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.<Long> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.<String> absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();

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
                 throw e.getCause();
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
                 throw e.getCause();
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
                 throw e.getCause();
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
        return new NestedProtocolTestStruct(DefaultReadValidator.getInstance().validateRequiredI32Field(requiredI32Field), DefaultReadValidator.getInstance().validateRequiredStringField(requiredStringField), DefaultReadValidator.getInstance().validateBinaryField(binaryField), DefaultReadValidator.getInstance().validateBoolField(boolField), DefaultReadValidator.getInstance().validateByteField(byteField), DefaultReadValidator.getInstance().validateDateTimeField(dateTimeField), DefaultReadValidator.getInstance().validateDecimalField(decimalField), DefaultReadValidator.getInstance().validateEmailAddressField(emailAddressField), DefaultReadValidator.getInstance().validateEnumField(enumField), DefaultReadValidator.getInstance().validateI16Field(i16Field), DefaultReadValidator.getInstance().validateI32Field(i32Field), DefaultReadValidator.getInstance().validateI64Field(i64Field), DefaultReadValidator.getInstance().validateStringListField(stringListField), DefaultReadValidator.getInstance().validateStringStringMapField(stringStringMapField), DefaultReadValidator.getInstance().validateStringSetField(stringSetField), DefaultReadValidator.getInstance().validateStringField(stringField), DefaultReadValidator.getInstance().validateUrlField(urlField), NopConstructionValidator.getInstance());
    }

    public static NestedProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
    }

    public static NestedProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.<byte[]> absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.<Boolean> absent();
        com.google.common.base.Optional<Byte> byteField = com.google.common.base.Optional.<Byte> absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.<Short> absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.<Integer> absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.<Long> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.<String> absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();

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
                     throw e.getCause();
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
                     throw e.getCause();
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
                     throw e.getCause();
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
        return new NestedProtocolTestStruct(DefaultReadValidator.getInstance().validateRequiredI32Field(requiredI32Field), DefaultReadValidator.getInstance().validateRequiredStringField(requiredStringField), DefaultReadValidator.getInstance().validateBinaryField(binaryField), DefaultReadValidator.getInstance().validateBoolField(boolField), DefaultReadValidator.getInstance().validateByteField(byteField), DefaultReadValidator.getInstance().validateDateTimeField(dateTimeField), DefaultReadValidator.getInstance().validateDecimalField(decimalField), DefaultReadValidator.getInstance().validateEmailAddressField(emailAddressField), DefaultReadValidator.getInstance().validateEnumField(enumField), DefaultReadValidator.getInstance().validateI16Field(i16Field), DefaultReadValidator.getInstance().validateI32Field(i32Field), DefaultReadValidator.getInstance().validateI64Field(i64Field), DefaultReadValidator.getInstance().validateStringListField(stringListField), DefaultReadValidator.getInstance().validateStringStringMapField(stringStringMapField), DefaultReadValidator.getInstance().validateStringSetField(stringSetField), DefaultReadValidator.getInstance().validateStringField(stringField), DefaultReadValidator.getInstance().validateUrlField(urlField), NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, DefaultConstructionValidator.getInstance().validateBinaryField(binaryField), this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceBinaryField(final byte[] binaryField) {
        return replaceBinaryField(com.google.common.base.Optional.fromNullable(binaryField));
    }

    public NestedProtocolTestStruct replaceBoolField(final com.google.common.base.Optional<Boolean> boolField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, DefaultConstructionValidator.getInstance().validateBoolField(boolField), this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceBoolField(final boolean boolField) {
        return replaceBoolField(com.google.common.base.Optional.fromNullable(boolField));
    }

    public NestedProtocolTestStruct replaceByteField(final com.google.common.base.Optional<Byte> byteField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, DefaultConstructionValidator.getInstance().validateByteField(byteField), this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceByteField(final byte byteField) {
        return replaceByteField(com.google.common.base.Optional.fromNullable(byteField));
    }

    public NestedProtocolTestStruct replaceDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, DefaultConstructionValidator.getInstance().validateDateTimeField(dateTimeField), this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceDateTimeField(final java.util.Date dateTimeField) {
        return replaceDateTimeField(com.google.common.base.Optional.fromNullable(dateTimeField));
    }

    public NestedProtocolTestStruct replaceDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, DefaultConstructionValidator.getInstance().validateDecimalField(decimalField), this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceDecimalField(final java.math.BigDecimal decimalField) {
        return replaceDecimalField(com.google.common.base.Optional.fromNullable(decimalField));
    }

    public NestedProtocolTestStruct replaceEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, DefaultConstructionValidator.getInstance().validateEmailAddressField(emailAddressField), this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceEmailAddressField(final org.thryft.native_.EmailAddress emailAddressField) {
        return replaceEmailAddressField(com.google.common.base.Optional.fromNullable(emailAddressField));
    }

    public NestedProtocolTestStruct replaceEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, DefaultConstructionValidator.getInstance().validateEnumField(enumField), this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceEnumField(final org.thryft.protocol.test.ProtocolTestEnum enumField) {
        return replaceEnumField(com.google.common.base.Optional.fromNullable(enumField));
    }

    public NestedProtocolTestStruct replaceI16Field(final com.google.common.base.Optional<Short> i16Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, DefaultConstructionValidator.getInstance().validateI16Field(i16Field), this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceI16Field(final short i16Field) {
        return replaceI16Field(com.google.common.base.Optional.fromNullable(i16Field));
    }

    public NestedProtocolTestStruct replaceI32Field(final com.google.common.base.Optional<Integer> i32Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, DefaultConstructionValidator.getInstance().validateI32Field(i32Field), this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceI32Field(final int i32Field) {
        return replaceI32Field(com.google.common.base.Optional.fromNullable(i32Field));
    }

    public NestedProtocolTestStruct replaceI64Field(final com.google.common.base.Optional<Long> i64Field) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, DefaultConstructionValidator.getInstance().validateI64Field(i64Field), this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceI64Field(final long i64Field) {
        return replaceI64Field(com.google.common.base.Optional.fromNullable(i64Field));
    }

    public NestedProtocolTestStruct replaceRequiredI32Field(final int requiredI32Field) {
        return new NestedProtocolTestStruct(DefaultConstructionValidator.getInstance().validateRequiredI32Field(requiredI32Field), this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceRequiredStringField(final String requiredStringField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, DefaultConstructionValidator.getInstance().validateRequiredStringField(requiredStringField), this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceStringField(final com.google.common.base.Optional<String> stringField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, DefaultConstructionValidator.getInstance().validateStringField(stringField), this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceStringField(final String stringField) {
        return replaceStringField(com.google.common.base.Optional.fromNullable(stringField));
    }

    public NestedProtocolTestStruct replaceStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, DefaultConstructionValidator.getInstance().validateStringListField(stringListField), this.stringStringMapField, this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceStringListField(final com.google.common.collect.ImmutableList<String> stringListField) {
        return replaceStringListField(com.google.common.base.Optional.fromNullable(stringListField));
    }

    public NestedProtocolTestStruct replaceStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, DefaultConstructionValidator.getInstance().validateStringSetField(stringSetField), this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceStringSetField(final com.google.common.collect.ImmutableSet<String> stringSetField) {
        return replaceStringSetField(com.google.common.base.Optional.fromNullable(stringSetField));
    }

    public NestedProtocolTestStruct replaceStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, DefaultConstructionValidator.getInstance().validateStringStringMapField(stringStringMapField), this.stringSetField, this.stringField, this.urlField, NopConstructionValidator.getInstance());
    }

    public NestedProtocolTestStruct replaceStringStringMapField(final com.google.common.collect.ImmutableMap<String, String> stringStringMapField) {
        return replaceStringStringMapField(com.google.common.base.Optional.fromNullable(stringStringMapField));
    }

    public NestedProtocolTestStruct replaceUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        return new NestedProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.byteField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, DefaultConstructionValidator.getInstance().validateUrlField(urlField), NopConstructionValidator.getInstance());
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
