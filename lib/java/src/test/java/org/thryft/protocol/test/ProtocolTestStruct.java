package org.thryft.protocol.test;

public final class ProtocolTestStruct implements org.thryft.Struct {
    public final static class Builder {
        public Builder() {
            requiredI32Field = 0;
            requiredStringField = null;
            binaryField = com.google.common.base.Optional.<byte[]> absent();
            boolField = com.google.common.base.Optional.<Boolean> absent();
            dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
            decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
            doubleField = com.google.common.base.Optional.<Double> absent();
            emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
            enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
            floatField = com.google.common.base.Optional.<Float> absent();
            i16Field = com.google.common.base.Optional.<Short> absent();
            i32Field = com.google.common.base.Optional.<Integer> absent();
            i64Field = com.google.common.base.Optional.<Long> absent();
            i8Field = com.google.common.base.Optional.<Byte> absent();
            stringField = com.google.common.base.Optional.<String> absent();
            stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
            stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
            stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
            structField = com.google.common.base.Optional.<org.thryft.protocol.test.NestedProtocolTestStruct> absent();
            u32Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedInteger> absent();
            u64Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedLong> absent();
            uriField = com.google.common.base.Optional.<org.thryft.native_.Uri> absent();
            urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();
            variantField = com.google.common.base.Optional.<java.lang.Object> absent();
        }

        public Builder(final ProtocolTestStruct other) {
            this.requiredI32Field = other.getRequiredI32Field();
            this.requiredStringField = other.getRequiredStringField();
            this.binaryField = other.getBinaryField();
            this.boolField = other.getBoolField();
            this.dateTimeField = other.getDateTimeField();
            this.decimalField = other.getDecimalField();
            this.doubleField = other.getDoubleField();
            this.emailAddressField = other.getEmailAddressField();
            this.enumField = other.getEnumField();
            this.floatField = other.getFloatField();
            this.i16Field = other.getI16Field();
            this.i32Field = other.getI32Field();
            this.i64Field = other.getI64Field();
            this.i8Field = other.getI8Field();
            this.stringField = other.getStringField();
            this.stringListField = other.getStringListField();
            this.stringSetField = other.getStringSetField();
            this.stringStringMapField = other.getStringStringMapField();
            this.structField = other.getStructField();
            this.u32Field = other.getU32Field();
            this.u64Field = other.getU64Field();
            this.uriField = other.getUriField();
            this.urlField = other.getUrlField();
            this.variantField = other.getVariantField();
        }

        protected ProtocolTestStruct _build(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<Double> doubleField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Float> floatField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<Byte> i8Field, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, final com.google.common.base.Optional<org.thryft.native_.Uri> uriField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, final com.google.common.base.Optional<java.lang.Object> variantField) {
            return new ProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, doubleField, emailAddressField, enumField, floatField, i16Field, i32Field, i64Field, i8Field, stringField, stringListField, stringSetField, stringStringMapField, structField, u32Field, u64Field, uriField, urlField, variantField, DefaultConstructionValidator.getInstance());
        }

        public ProtocolTestStruct build() {
            return _build(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, doubleField, emailAddressField, enumField, floatField, i16Field, i32Field, i64Field, i8Field, stringField, stringListField, stringSetField, stringStringMapField, structField, u32Field, u64Field, uriField, urlField, variantField);
        }

        public final com.google.common.base.Optional<byte[]> getBinaryField() {
            return binaryField;
        }

        public final com.google.common.base.Optional<Boolean> getBoolField() {
            return boolField;
        }

        public final com.google.common.base.Optional<java.util.Date> getDateTimeField() {
            return dateTimeField;
        }

        public final com.google.common.base.Optional<java.math.BigDecimal> getDecimalField() {
            return decimalField;
        }

        public final com.google.common.base.Optional<Double> getDoubleField() {
            return doubleField;
        }

        public final com.google.common.base.Optional<org.thryft.native_.EmailAddress> getEmailAddressField() {
            return emailAddressField;
        }

        public final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> getEnumField() {
            return enumField;
        }

        public final com.google.common.base.Optional<Float> getFloatField() {
            return floatField;
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

        public final com.google.common.base.Optional<Byte> getI8Field() {
            return i8Field;
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

        public final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> getStructField() {
            return structField;
        }

        public final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> getU32Field() {
            return u32Field;
        }

        public final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> getU64Field() {
            return u64Field;
        }

        public final com.google.common.base.Optional<org.thryft.native_.Uri> getUriField() {
            return uriField;
        }

        public final com.google.common.base.Optional<org.thryft.native_.Url> getUrlField() {
            return urlField;
        }

        public final com.google.common.base.Optional<java.lang.Object> getVariantField() {
            return variantField;
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
            try {
                final org.thryft.protocol.ListBegin __list = iprot.readListBegin();
                try {
                    requiredI32Field = iprot.readI32();
                } catch (final NumberFormatException e) {
                     throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.REQUIRED_I32_FIELD, e);
                }
                requiredStringField = iprot.readString();
                if (__list.getSize() > 2) {
                    binaryField = com.google.common.base.Optional.of(iprot.readBinary());
                }
                if (__list.getSize() > 3) {
                    boolField = com.google.common.base.Optional.of(iprot.readBool());
                }
                if (__list.getSize() > 4) {
                    try {
                        dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                    } catch (final IllegalArgumentException e) {
                    }
                }
                if (__list.getSize() > 5) {
                    try {
                        decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 6) {
                    try {
                        doubleField = com.google.common.base.Optional.of(iprot.readDouble());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 7) {
                    emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                }
                if (__list.getSize() > 8) {
                    enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                }
                if (__list.getSize() > 9) {
                    try {
                        floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 10) {
                    try {
                        i16Field = com.google.common.base.Optional.of(iprot.readI16());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 11) {
                    try {
                        i32Field = com.google.common.base.Optional.of(iprot.readI32());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 12) {
                    try {
                        i64Field = com.google.common.base.Optional.of(iprot.readI64());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 13) {
                    try {
                        i8Field = com.google.common.base.Optional.of(iprot.readByte());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 14) {
                    stringField = com.google.common.base.Optional.of(iprot.readString());
                }
                if (__list.getSize() > 15) {
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
                         throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_LIST_FIELD, e.getCause());
                    }
                }
                if (__list.getSize() > 16) {
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
                         throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_SET_FIELD, e.getCause());
                    }
                }
                if (__list.getSize() > 17) {
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
                                    throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                                }
                            }
                        }).apply(iprot));
                    } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                         throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_STRING_MAP_FIELD, e.getCause());
                    }
                }
                if (__list.getSize() > 18) {
                    structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
                }
                if (__list.getSize() > 19) {
                    try {
                        u32Field = com.google.common.base.Optional.of(iprot.readU32());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 20) {
                    try {
                        u64Field = com.google.common.base.Optional.of(iprot.readU64());
                    } catch (final NumberFormatException e) {
                    }
                }
                if (__list.getSize() > 21) {
                    try {
                        uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                    } catch (final java.lang.IllegalArgumentException e) {
                    }
                }
                if (__list.getSize() > 22) {
                    try {
                        urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                    } catch (final java.lang.IllegalArgumentException e) {
                    }
                }
                if (__list.getSize() > 23) {
                    variantField = com.google.common.base.Optional.of(iprot.readVariant());
                }
                iprot.readListEnd();
            } catch (final RuntimeException e) {
                throw new IllegalStateException(e);
            }
            return this;
        }

        public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
        }

        public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            try {
                iprot.readStructBegin();
                while (true) {
                    final org.thryft.protocol.FieldBegin ifield = iprot.readFieldBegin();
                    if (ifield.getType() == org.thryft.protocol.Type.STOP) {
                        break;
                    }
                    switch (ifield.getName()) {
                    case "required_i32_field": {
                        if (!ifield.hasId() || ifield.getId() == 1) {
                            try {
                                requiredI32Field = iprot.readI32();
                            } catch (final NumberFormatException e) {
                                 throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.REQUIRED_I32_FIELD, e);
                            }
                        }
                        break;
                    }
                    case "required_string_field": {
                        if (!ifield.hasId() || ifield.getId() == 2) {
                            requiredStringField = iprot.readString();
                        }
                        break;
                    }
                    case "binary_field": {
                        if (!ifield.hasId() || ifield.getId() == 3) {
                            binaryField = com.google.common.base.Optional.of(iprot.readBinary());
                        }
                        break;
                    }
                    case "bool_field": {
                        if (!ifield.hasId() || ifield.getId() == 4) {
                            boolField = com.google.common.base.Optional.of(iprot.readBool());
                        }
                        break;
                    }
                    case "date_time_field": {
                        if (!ifield.hasId() || ifield.getId() == 5) {
                            try {
                                dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                            } catch (final IllegalArgumentException e) {
                            }
                        }
                        break;
                    }
                    case "decimal_field": {
                        if (!ifield.hasId() || ifield.getId() == 6) {
                            try {
                                decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "double_field": {
                        if (!ifield.hasId() || ifield.getId() == 7) {
                            try {
                                doubleField = com.google.common.base.Optional.of(iprot.readDouble());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "email_address_field": {
                        if (!ifield.hasId() || ifield.getId() == 8) {
                            emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                        }
                        break;
                    }
                    case "enum_field": {
                        if (!ifield.hasId() || ifield.getId() == 9) {
                            enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                        }
                        break;
                    }
                    case "float_field": {
                        if (!ifield.hasId() || ifield.getId() == 10) {
                            try {
                                floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "i16_field": {
                        if (!ifield.hasId() || ifield.getId() == 12) {
                            try {
                                i16Field = com.google.common.base.Optional.of(iprot.readI16());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "i32_field": {
                        if (!ifield.hasId() || ifield.getId() == 13) {
                            try {
                                i32Field = com.google.common.base.Optional.of(iprot.readI32());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "i64_field": {
                        if (!ifield.hasId() || ifield.getId() == 14) {
                            try {
                                i64Field = com.google.common.base.Optional.of(iprot.readI64());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "i8_field": {
                        if (!ifield.hasId() || ifield.getId() == 11) {
                            try {
                                i8Field = com.google.common.base.Optional.of(iprot.readByte());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "string_field": {
                        if (!ifield.hasId() || ifield.getId() == 18) {
                            stringField = com.google.common.base.Optional.of(iprot.readString());
                        }
                        break;
                    }
                    case "string_list_field": {
                        if (!ifield.hasId() || ifield.getId() == 15) {
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
                                 throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_LIST_FIELD, e.getCause());
                            }
                        }
                        break;
                    }
                    case "string_set_field": {
                        if (!ifield.hasId() || ifield.getId() == 17) {
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
                                 throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_SET_FIELD, e.getCause());
                            }
                        }
                        break;
                    }
                    case "string_string_map_field": {
                        if (!ifield.hasId() || ifield.getId() == 16) {
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
                                            throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                                        }
                                    }
                                }).apply(iprot));
                            } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                                 throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_STRING_MAP_FIELD, e.getCause());
                            }
                        }
                        break;
                    }
                    case "struct_field": {
                        if (!ifield.hasId() || ifield.getId() == 19) {
                            structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
                        }
                        break;
                    }
                    case "u32_field": {
                        if (!ifield.hasId() || ifield.getId() == 20) {
                            try {
                                u32Field = com.google.common.base.Optional.of(iprot.readU32());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "u64_field": {
                        if (!ifield.hasId() || ifield.getId() == 21) {
                            try {
                                u64Field = com.google.common.base.Optional.of(iprot.readU64());
                            } catch (final NumberFormatException e) {
                            }
                        }
                        break;
                    }
                    case "uri_field": {
                        if (!ifield.hasId() || ifield.getId() == 22) {
                            try {
                                uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                            } catch (final java.lang.IllegalArgumentException e) {
                            }
                        }
                        break;
                    }
                    case "url_field": {
                        if (!ifield.hasId() || ifield.getId() == 23) {
                            try {
                                urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                            } catch (final java.lang.IllegalArgumentException e) {
                            }
                        }
                        break;
                    }
                    case "variant_field": {
                        if (!ifield.hasId() || ifield.getId() == 24) {
                            variantField = com.google.common.base.Optional.of(iprot.readVariant());
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
            } catch (final RuntimeException e) {
                throw new IllegalStateException(e);
            }
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
            case DATE_TIME_FIELD: setDateTimeField((java.util.Date)value); return this;
            case DECIMAL_FIELD: setDecimalField((java.math.BigDecimal)value); return this;
            case DOUBLE_FIELD: setDoubleField((Double)value); return this;
            case EMAIL_ADDRESS_FIELD: setEmailAddressField((org.thryft.native_.EmailAddress)value); return this;
            case ENUM_FIELD: setEnumField((org.thryft.protocol.test.ProtocolTestEnum)value); return this;
            case FLOAT_FIELD: setFloatField((Float)value); return this;
            case I16_FIELD: setI16Field((Short)value); return this;
            case I32_FIELD: setI32Field((Integer)value); return this;
            case I64_FIELD: setI64Field((Long)value); return this;
            case I8_FIELD: setI8Field((Byte)value); return this;
            case STRING_FIELD: setStringField((String)value); return this;
            case STRING_LIST_FIELD: setStringListField((com.google.common.collect.ImmutableList<String>)value); return this;
            case STRING_SET_FIELD: setStringSetField((com.google.common.collect.ImmutableSet<String>)value); return this;
            case STRING_STRING_MAP_FIELD: setStringStringMapField((com.google.common.collect.ImmutableMap<String, String>)value); return this;
            case STRUCT_FIELD: setStructField((org.thryft.protocol.test.NestedProtocolTestStruct)value); return this;
            case U32_FIELD: setU32Field((com.google.common.primitives.UnsignedInteger)value); return this;
            case U64_FIELD: setU64Field((com.google.common.primitives.UnsignedLong)value); return this;
            case URI_FIELD: setUriField((org.thryft.native_.Uri)value); return this;
            case URL_FIELD: setUrlField((org.thryft.native_.Url)value); return this;
            case VARIANT_FIELD: setVariantField(value); return this;
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

        public Builder setDoubleField(final com.google.common.base.Optional<Double> doubleField) {
            this.doubleField = DefaultConstructionValidator.getInstance().validateDoubleField(doubleField);
            return this;
        }

        public Builder setDoubleField(@javax.annotation.Nullable final Double doubleField) {
            return setDoubleField(com.google.common.base.Optional.fromNullable(doubleField));
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

        public Builder setFloatField(final com.google.common.base.Optional<Float> floatField) {
            this.floatField = DefaultConstructionValidator.getInstance().validateFloatField(floatField);
            return this;
        }

        public Builder setFloatField(@javax.annotation.Nullable final Float floatField) {
            return setFloatField(com.google.common.base.Optional.fromNullable(floatField));
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

        public Builder setI8Field(final com.google.common.base.Optional<Byte> i8Field) {
            this.i8Field = DefaultConstructionValidator.getInstance().validateI8Field(i8Field);
            return this;
        }

        public Builder setI8Field(@javax.annotation.Nullable final Byte i8Field) {
            return setI8Field(com.google.common.base.Optional.fromNullable(i8Field));
        }

        public Builder setIfPresent(final ProtocolTestStruct other) {
            com.google.common.base.Preconditions.checkNotNull(other);

            setRequiredI32Field(other.getRequiredI32Field());
            setRequiredStringField(other.getRequiredStringField());
            if (other.getBinaryField().isPresent()) {
                setBinaryField(other.getBinaryField());
            }
            if (other.getBoolField().isPresent()) {
                setBoolField(other.getBoolField());
            }
            if (other.getDateTimeField().isPresent()) {
                setDateTimeField(other.getDateTimeField());
            }
            if (other.getDecimalField().isPresent()) {
                setDecimalField(other.getDecimalField());
            }
            if (other.getDoubleField().isPresent()) {
                setDoubleField(other.getDoubleField());
            }
            if (other.getEmailAddressField().isPresent()) {
                setEmailAddressField(other.getEmailAddressField());
            }
            if (other.getEnumField().isPresent()) {
                setEnumField(other.getEnumField());
            }
            if (other.getFloatField().isPresent()) {
                setFloatField(other.getFloatField());
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
            if (other.getI8Field().isPresent()) {
                setI8Field(other.getI8Field());
            }
            if (other.getStringField().isPresent()) {
                setStringField(other.getStringField());
            }
            if (other.getStringListField().isPresent()) {
                setStringListField(other.getStringListField());
            }
            if (other.getStringSetField().isPresent()) {
                setStringSetField(other.getStringSetField());
            }
            if (other.getStringStringMapField().isPresent()) {
                setStringStringMapField(other.getStringStringMapField());
            }
            if (other.getStructField().isPresent()) {
                setStructField(other.getStructField());
            }
            if (other.getU32Field().isPresent()) {
                setU32Field(other.getU32Field());
            }
            if (other.getU64Field().isPresent()) {
                setU64Field(other.getU64Field());
            }
            if (other.getUriField().isPresent()) {
                setUriField(other.getUriField());
            }
            if (other.getUrlField().isPresent()) {
                setUrlField(other.getUrlField());
            }
            if (other.getVariantField().isPresent()) {
                setVariantField(other.getVariantField());
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

        public Builder setStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) {
            this.structField = DefaultConstructionValidator.getInstance().validateStructField(structField);
            return this;
        }

        public Builder setStructField(@javax.annotation.Nullable final org.thryft.protocol.test.NestedProtocolTestStruct structField) {
            return setStructField(com.google.common.base.Optional.fromNullable(structField));
        }

        public Builder setU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) {
            this.u32Field = DefaultConstructionValidator.getInstance().validateU32Field(u32Field);
            return this;
        }

        public Builder setU32Field(@javax.annotation.Nullable final com.google.common.primitives.UnsignedInteger u32Field) {
            return setU32Field(com.google.common.base.Optional.fromNullable(u32Field));
        }

        public Builder setU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) {
            this.u64Field = DefaultConstructionValidator.getInstance().validateU64Field(u64Field);
            return this;
        }

        public Builder setU64Field(@javax.annotation.Nullable final com.google.common.primitives.UnsignedLong u64Field) {
            return setU64Field(com.google.common.base.Optional.fromNullable(u64Field));
        }

        public Builder setUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) {
            this.uriField = DefaultConstructionValidator.getInstance().validateUriField(uriField);
            return this;
        }

        public Builder setUriField(@javax.annotation.Nullable final org.thryft.native_.Uri uriField) {
            return setUriField(com.google.common.base.Optional.fromNullable(uriField));
        }

        public Builder setUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            this.urlField = DefaultConstructionValidator.getInstance().validateUrlField(urlField);
            return this;
        }

        public Builder setUrlField(@javax.annotation.Nullable final org.thryft.native_.Url urlField) {
            return setUrlField(com.google.common.base.Optional.fromNullable(urlField));
        }

        public Builder setVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) {
            this.variantField = DefaultConstructionValidator.getInstance().validateVariantField(variantField);
            return this;
        }

        public Builder setVariantField(@javax.annotation.Nullable final java.lang.Object variantField) {
            return setVariantField(com.google.common.base.Optional.fromNullable(variantField));
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
            case DATE_TIME_FIELD: return unsetDateTimeField();
            case DECIMAL_FIELD: return unsetDecimalField();
            case DOUBLE_FIELD: return unsetDoubleField();
            case EMAIL_ADDRESS_FIELD: return unsetEmailAddressField();
            case ENUM_FIELD: return unsetEnumField();
            case FLOAT_FIELD: return unsetFloatField();
            case I16_FIELD: return unsetI16Field();
            case I32_FIELD: return unsetI32Field();
            case I64_FIELD: return unsetI64Field();
            case I8_FIELD: return unsetI8Field();
            case STRING_FIELD: return unsetStringField();
            case STRING_LIST_FIELD: return unsetStringListField();
            case STRING_SET_FIELD: return unsetStringSetField();
            case STRING_STRING_MAP_FIELD: return unsetStringStringMapField();
            case STRUCT_FIELD: return unsetStructField();
            case U32_FIELD: return unsetU32Field();
            case U64_FIELD: return unsetU64Field();
            case URI_FIELD: return unsetUriField();
            case URL_FIELD: return unsetUrlField();
            case VARIANT_FIELD: return unsetVariantField();
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

        public Builder unsetDateTimeField() {
            this.dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
            return this;
        }

        public Builder unsetDecimalField() {
            this.decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
            return this;
        }

        public Builder unsetDoubleField() {
            this.doubleField = com.google.common.base.Optional.<Double> absent();
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

        public Builder unsetFloatField() {
            this.floatField = com.google.common.base.Optional.<Float> absent();
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

        public Builder unsetI8Field() {
            this.i8Field = com.google.common.base.Optional.<Byte> absent();
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

        public Builder unsetStructField() {
            this.structField = com.google.common.base.Optional.<org.thryft.protocol.test.NestedProtocolTestStruct> absent();
            return this;
        }

        public Builder unsetU32Field() {
            this.u32Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedInteger> absent();
            return this;
        }

        public Builder unsetU64Field() {
            this.u64Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedLong> absent();
            return this;
        }

        public Builder unsetUriField() {
            this.uriField = com.google.common.base.Optional.<org.thryft.native_.Uri> absent();
            return this;
        }

        public Builder unsetUrlField() {
            this.urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();
            return this;
        }

        public Builder unsetVariantField() {
            this.variantField = com.google.common.base.Optional.<java.lang.Object> absent();
            return this;
        }

        private Integer requiredI32Field;
        private String requiredStringField;
        private com.google.common.base.Optional<byte[]> binaryField;
        private com.google.common.base.Optional<Boolean> boolField;
        private com.google.common.base.Optional<java.util.Date> dateTimeField;
        private com.google.common.base.Optional<java.math.BigDecimal> decimalField;
        private com.google.common.base.Optional<Double> doubleField;
        private com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField;
        private com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;
        private com.google.common.base.Optional<Float> floatField;
        private com.google.common.base.Optional<Short> i16Field;
        private com.google.common.base.Optional<Integer> i32Field;
        private com.google.common.base.Optional<Long> i64Field;
        private com.google.common.base.Optional<Byte> i8Field;
        private com.google.common.base.Optional<String> stringField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;
        private com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField;
        private com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field;
        private com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field;
        private com.google.common.base.Optional<org.thryft.native_.Uri> uriField;
        private com.google.common.base.Optional<org.thryft.native_.Url> urlField;
        private com.google.common.base.Optional<java.lang.Object> variantField;
    }

    public final static class Factory implements org.thryft.CompoundType.Factory<ProtocolTestStruct> {
        @Override
        public ProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
            return ProtocolTestStruct.readAs(iprot, type);
        }

        @Override
        public ProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type,
                final com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            return ProtocolTestStruct.readAs(iprot, type, unknownFieldCallback);
        }

        @Override
        public ProtocolTestStruct readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            return ProtocolTestStruct.readAsList(iprot);
        }

        @Override
        public ProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
            return ProtocolTestStruct.readAsStruct(iprot);
        }

        @Override
        public ProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot,
                final com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
            return ProtocolTestStruct.readAsStruct(iprot, unknownFieldCallback);
        }
    }

    @SuppressWarnings("serial")
    public enum FieldMetadata implements org.thryft.CompoundType.FieldMetadata {
        REQUIRED_I32_FIELD("requiredI32Field", new com.google.common.reflect.TypeToken<Integer>() {}, true, 1, "required_i32_field", org.thryft.protocol.Type.I32),
        REQUIRED_STRING_FIELD("requiredStringField", new com.google.common.reflect.TypeToken<String>() {}, true, 2, "required_string_field", org.thryft.protocol.Type.STRING),
        BINARY_FIELD("binaryField", new com.google.common.reflect.TypeToken<byte[]>() {}, false, 3, "binary_field", org.thryft.protocol.Type.STRING),
        BOOL_FIELD("boolField", new com.google.common.reflect.TypeToken<Boolean>() {}, false, 4, "bool_field", org.thryft.protocol.Type.BOOL),
        DATE_TIME_FIELD("dateTimeField", new com.google.common.reflect.TypeToken<java.util.Date>() {}, false, 5, "date_time_field", org.thryft.protocol.Type.I64),
        DECIMAL_FIELD("decimalField", new com.google.common.reflect.TypeToken<java.math.BigDecimal>() {}, false, 6, "decimal_field", org.thryft.protocol.Type.STRING),
        DOUBLE_FIELD("doubleField", new com.google.common.reflect.TypeToken<Double>() {}, false, 7, "double_field", org.thryft.protocol.Type.DOUBLE),
        EMAIL_ADDRESS_FIELD("emailAddressField", new com.google.common.reflect.TypeToken<org.thryft.native_.EmailAddress>() {}, false, 8, "email_address_field", org.thryft.protocol.Type.STRING),
        ENUM_FIELD("enumField", new com.google.common.reflect.TypeToken<org.thryft.protocol.test.ProtocolTestEnum>() {}, false, 9, "enum_field", org.thryft.protocol.Type.STRING),
        FLOAT_FIELD("floatField", new com.google.common.reflect.TypeToken<Float>() {}, false, 10, "float_field", org.thryft.protocol.Type.DOUBLE),
        I16_FIELD("i16Field", new com.google.common.reflect.TypeToken<Short>() {}, false, 12, "i16_field", org.thryft.protocol.Type.I16),
        I32_FIELD("i32Field", new com.google.common.reflect.TypeToken<Integer>() {}, false, 13, "i32_field", org.thryft.protocol.Type.I32),
        I64_FIELD("i64Field", new com.google.common.reflect.TypeToken<Long>() {}, false, 14, "i64_field", org.thryft.protocol.Type.I64),
        I8_FIELD("i8Field", new com.google.common.reflect.TypeToken<Byte>() {}, false, 11, "i8_field", org.thryft.protocol.Type.BYTE),
        STRING_FIELD("stringField", new com.google.common.reflect.TypeToken<String>() {}, false, 18, "string_field", org.thryft.protocol.Type.STRING),
        STRING_LIST_FIELD("stringListField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableList<String>>() {}, false, 15, "string_list_field", org.thryft.protocol.Type.LIST),
        STRING_SET_FIELD("stringSetField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableSet<String>>() {}, false, 17, "string_set_field", org.thryft.protocol.Type.SET),
        STRING_STRING_MAP_FIELD("stringStringMapField", new com.google.common.reflect.TypeToken<com.google.common.collect.ImmutableMap<String, String>>() {}, false, 16, "string_string_map_field", org.thryft.protocol.Type.MAP),
        STRUCT_FIELD("structField", new com.google.common.reflect.TypeToken<org.thryft.protocol.test.NestedProtocolTestStruct>() {}, false, 19, "struct_field", org.thryft.protocol.Type.STRUCT),
        U32_FIELD("u32Field", new com.google.common.reflect.TypeToken<com.google.common.primitives.UnsignedInteger>() {}, false, 20, "u32_field", org.thryft.protocol.Type.I32),
        U64_FIELD("u64Field", new com.google.common.reflect.TypeToken<com.google.common.primitives.UnsignedLong>() {}, false, 21, "u64_field", org.thryft.protocol.Type.I64),
        URI_FIELD("uriField", new com.google.common.reflect.TypeToken<org.thryft.native_.Uri>() {}, false, 22, "uri_field", org.thryft.protocol.Type.STRING),
        URL_FIELD("urlField", new com.google.common.reflect.TypeToken<org.thryft.native_.Url>() {}, false, 23, "url_field", org.thryft.protocol.Type.STRING),
        VARIANT_FIELD("variantField", new com.google.common.reflect.TypeToken<java.lang.Object>() {}, false, 24, "variant_field", org.thryft.protocol.Type.STRUCT);

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
            case "dateTimeField": return DATE_TIME_FIELD;
            case "decimalField": return DECIMAL_FIELD;
            case "doubleField": return DOUBLE_FIELD;
            case "emailAddressField": return EMAIL_ADDRESS_FIELD;
            case "enumField": return ENUM_FIELD;
            case "floatField": return FLOAT_FIELD;
            case "i16Field": return I16_FIELD;
            case "i32Field": return I32_FIELD;
            case "i64Field": return I64_FIELD;
            case "i8Field": return I8_FIELD;
            case "stringField": return STRING_FIELD;
            case "stringListField": return STRING_LIST_FIELD;
            case "stringSetField": return STRING_SET_FIELD;
            case "stringStringMapField": return STRING_STRING_MAP_FIELD;
            case "structField": return STRUCT_FIELD;
            case "u32Field": return U32_FIELD;
            case "u64Field": return U64_FIELD;
            case "uriField": return URI_FIELD;
            case "urlField": return URL_FIELD;
            case "variantField": return VARIANT_FIELD;
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
            case "date_time_field": return DATE_TIME_FIELD;
            case "decimal_field": return DECIMAL_FIELD;
            case "double_field": return DOUBLE_FIELD;
            case "email_address_field": return EMAIL_ADDRESS_FIELD;
            case "enum_field": return ENUM_FIELD;
            case "float_field": return FLOAT_FIELD;
            case "i16_field": return I16_FIELD;
            case "i32_field": return I32_FIELD;
            case "i64_field": return I64_FIELD;
            case "i8_field": return I8_FIELD;
            case "string_field": return STRING_FIELD;
            case "string_list_field": return STRING_LIST_FIELD;
            case "string_set_field": return STRING_SET_FIELD;
            case "string_string_map_field": return STRING_STRING_MAP_FIELD;
            case "struct_field": return STRUCT_FIELD;
            case "u32_field": return U32_FIELD;
            case "u64_field": return U64_FIELD;
            case "uri_field": return URI_FIELD;
            case "url_field": return URL_FIELD;
            case "variant_field": return VARIANT_FIELD;
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

        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) throws ExceptionT;

        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) throws ExceptionT;

        public com.google.common.base.Optional<Double> validateDoubleField(final com.google.common.base.Optional<Double> doubleField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) throws ExceptionT;

        public com.google.common.base.Optional<Float> validateFloatField(final com.google.common.base.Optional<Float> floatField) throws ExceptionT;

        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) throws ExceptionT;

        public com.google.common.base.Optional<Integer> validateI32Field(final com.google.common.base.Optional<Integer> i32Field) throws ExceptionT;

        public com.google.common.base.Optional<Long> validateI64Field(final com.google.common.base.Optional<Long> i64Field) throws ExceptionT;

        public com.google.common.base.Optional<Byte> validateI8Field(final com.google.common.base.Optional<Byte> i8Field) throws ExceptionT;

        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> validateStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> validateU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) throws ExceptionT;

        public com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> validateU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.native_.Uri> validateUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) throws ExceptionT;

        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) throws ExceptionT;

        public com.google.common.base.Optional<java.lang.Object> validateVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) throws ExceptionT;
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
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is null");
            }
            if (requiredStringField.isEmpty()) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is less than min length 1");
            }
            return requiredStringField;
        }

        @Override
        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) throws RuntimeException {
            if (binaryField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: binaryField is null");
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
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) throws RuntimeException {
            if (dateTimeField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: dateTimeField is null");
            }
            if (!dateTimeField.isPresent()) {
                return dateTimeField;
            }
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) throws RuntimeException {
            if (decimalField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: decimalField is null");
            }
            if (!decimalField.isPresent()) {
                return decimalField;
            }
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<Double> validateDoubleField(final com.google.common.base.Optional<Double> doubleField) throws RuntimeException {
            if (!doubleField.isPresent()) {
                return doubleField;
            }
            return doubleField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) throws RuntimeException {
            if (emailAddressField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: emailAddressField is null");
            }
            if (!emailAddressField.isPresent()) {
                return emailAddressField;
            }
            return emailAddressField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) throws RuntimeException {
            if (enumField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: enumField is null");
            }
            if (!enumField.isPresent()) {
                return enumField;
            }
            return enumField;
        }

        @Override
        public com.google.common.base.Optional<Float> validateFloatField(final com.google.common.base.Optional<Float> floatField) throws RuntimeException {
            if (!floatField.isPresent()) {
                return floatField;
            }
            return floatField;
        }

        @Override
        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) throws RuntimeException {
            if (!i16Field.isPresent()) {
                return i16Field;
            }
            if (i16Field.get().shortValue() > ((short)100)) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: i16Field is greater than max 100");
            }
            if (i16Field.get().shortValue() < ((short)1)) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: i16Field is less than min 1");
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
        public com.google.common.base.Optional<Byte> validateI8Field(final com.google.common.base.Optional<Byte> i8Field) throws RuntimeException {
            if (!i8Field.isPresent()) {
                return i8Field;
            }
            return i8Field;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) throws RuntimeException {
            if (stringField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: stringField is null");
            }
            if (!stringField.isPresent()) {
                return stringField;
            }
            if (stringField.get().isEmpty()) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: stringField is less than min length 1");
            }
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) throws RuntimeException {
            if (stringListField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: stringListField is null");
            }
            if (!stringListField.isPresent()) {
                return stringListField;
            }
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) throws RuntimeException {
            if (stringSetField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: stringSetField is null");
            }
            if (!stringSetField.isPresent()) {
                return stringSetField;
            }
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) throws RuntimeException {
            if (stringStringMapField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: stringStringMapField is null");
            }
            if (!stringStringMapField.isPresent()) {
                return stringStringMapField;
            }
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> validateStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) throws RuntimeException {
            if (structField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: structField is null");
            }
            if (!structField.isPresent()) {
                return structField;
            }
            return structField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> validateU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) throws RuntimeException {
            if (u32Field == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: u32Field is null");
            }
            if (!u32Field.isPresent()) {
                return u32Field;
            }
            if (u32Field.get().compareTo(com.google.common.primitives.UnsignedInteger.valueOf(100)) > 0) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: u32Field is greater than max 100");
            }
            if (u32Field.get().compareTo(com.google.common.primitives.UnsignedInteger.ONE) < 0) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: u32Field is less than min 1");
            }
            return u32Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> validateU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) throws RuntimeException {
            if (u64Field == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: u64Field is null");
            }
            if (!u64Field.isPresent()) {
                return u64Field;
            }
            if (u64Field.get().compareTo(com.google.common.primitives.UnsignedLong.valueOf(100)) > 0) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: u64Field is greater than max 100");
            }
            if (u64Field.get().compareTo(com.google.common.primitives.UnsignedLong.ONE) < 0) {
                throw new IllegalArgumentException("org.thryft.protocol.test.ProtocolTestStruct: u64Field is less than min 1");
            }
            return u64Field;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Uri> validateUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) throws RuntimeException {
            if (uriField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: uriField is null");
            }
            if (!uriField.isPresent()) {
                return uriField;
            }
            return uriField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) throws RuntimeException {
            if (urlField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: urlField is null");
            }
            if (!urlField.isPresent()) {
                return urlField;
            }
            return urlField;
        }

        @Override
        public com.google.common.base.Optional<java.lang.Object> validateVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) throws RuntimeException {
            if (variantField == null) {
                throw new NullPointerException("org.thryft.protocol.test.ProtocolTestStruct: variantField is null");
            }
            if (!variantField.isPresent()) {
                return variantField;
            }
            return variantField;
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
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<Double> validateDoubleField(final com.google.common.base.Optional<Double> doubleField) {
            return doubleField;
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
        public com.google.common.base.Optional<Float> validateFloatField(final com.google.common.base.Optional<Float> floatField) {
            return floatField;
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
        public com.google.common.base.Optional<Byte> validateI8Field(final com.google.common.base.Optional<Byte> i8Field) {
            return i8Field;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) {
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> validateStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) {
            return structField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> validateU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) {
            return u32Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> validateU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) {
            return u64Field;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Uri> validateUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) {
            return uriField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            return urlField;
        }

        @Override
        public com.google.common.base.Optional<java.lang.Object> validateVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) {
            return variantField;
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
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.REQUIRED_STRING_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is null");
            }
            if (requiredStringField.isEmpty()) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.REQUIRED_STRING_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is less than min length 1");
            }
            return requiredStringField;
        }

        @Override
        public com.google.common.base.Optional<byte[]> validateBinaryField(final com.google.common.base.Optional<byte[]> binaryField) throws org.thryft.protocol.InputProtocolException {
            if (binaryField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.BINARY_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: binaryField is null");
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
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) throws org.thryft.protocol.InputProtocolException {
            if (dateTimeField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.DATE_TIME_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: dateTimeField is null");
            }
            if (!dateTimeField.isPresent()) {
                return dateTimeField;
            }
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) throws org.thryft.protocol.InputProtocolException {
            if (decimalField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.DECIMAL_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: decimalField is null");
            }
            if (!decimalField.isPresent()) {
                return decimalField;
            }
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<Double> validateDoubleField(final com.google.common.base.Optional<Double> doubleField) throws org.thryft.protocol.InputProtocolException {
            if (!doubleField.isPresent()) {
                return doubleField;
            }
            return doubleField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.EmailAddress> validateEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) throws org.thryft.protocol.InputProtocolException {
            if (emailAddressField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.EMAIL_ADDRESS_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: emailAddressField is null");
            }
            if (!emailAddressField.isPresent()) {
                return emailAddressField;
            }
            return emailAddressField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> validateEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) throws org.thryft.protocol.InputProtocolException {
            if (enumField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.ENUM_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: enumField is null");
            }
            if (!enumField.isPresent()) {
                return enumField;
            }
            return enumField;
        }

        @Override
        public com.google.common.base.Optional<Float> validateFloatField(final com.google.common.base.Optional<Float> floatField) throws org.thryft.protocol.InputProtocolException {
            if (!floatField.isPresent()) {
                return floatField;
            }
            return floatField;
        }

        @Override
        public com.google.common.base.Optional<Short> validateI16Field(final com.google.common.base.Optional<Short> i16Field) throws org.thryft.protocol.InputProtocolException {
            if (!i16Field.isPresent()) {
                return i16Field;
            }
            if (i16Field.get().shortValue() > ((short)100)) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.I16_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: i16Field is greater than max 100");
            }
            if (i16Field.get().shortValue() < ((short)1)) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.I16_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: i16Field is less than min 1");
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
        public com.google.common.base.Optional<Byte> validateI8Field(final com.google.common.base.Optional<Byte> i8Field) throws org.thryft.protocol.InputProtocolException {
            if (!i8Field.isPresent()) {
                return i8Field;
            }
            return i8Field;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) throws org.thryft.protocol.InputProtocolException {
            if (stringField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: stringField is null");
            }
            if (!stringField.isPresent()) {
                return stringField;
            }
            if (stringField.get().isEmpty()) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: stringField is less than min length 1");
            }
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) throws org.thryft.protocol.InputProtocolException {
            if (stringListField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_LIST_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: stringListField is null");
            }
            if (!stringListField.isPresent()) {
                return stringListField;
            }
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) throws org.thryft.protocol.InputProtocolException {
            if (stringSetField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_SET_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: stringSetField is null");
            }
            if (!stringSetField.isPresent()) {
                return stringSetField;
            }
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) throws org.thryft.protocol.InputProtocolException {
            if (stringStringMapField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRING_STRING_MAP_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: stringStringMapField is null");
            }
            if (!stringStringMapField.isPresent()) {
                return stringStringMapField;
            }
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> validateStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) throws org.thryft.protocol.InputProtocolException {
            if (structField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.STRUCT_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: structField is null");
            }
            if (!structField.isPresent()) {
                return structField;
            }
            return structField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> validateU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) throws org.thryft.protocol.InputProtocolException {
            if (u32Field == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.U32_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: u32Field is null");
            }
            if (!u32Field.isPresent()) {
                return u32Field;
            }
            if (u32Field.get().compareTo(com.google.common.primitives.UnsignedInteger.valueOf(100)) > 0) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.U32_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: u32Field is greater than max 100");
            }
            if (u32Field.get().compareTo(com.google.common.primitives.UnsignedInteger.ONE) < 0) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.U32_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: u32Field is less than min 1");
            }
            return u32Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> validateU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) throws org.thryft.protocol.InputProtocolException {
            if (u64Field == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.U64_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: u64Field is null");
            }
            if (!u64Field.isPresent()) {
                return u64Field;
            }
            if (u64Field.get().compareTo(com.google.common.primitives.UnsignedLong.valueOf(100)) > 0) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.U64_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: u64Field is greater than max 100");
            }
            if (u64Field.get().compareTo(com.google.common.primitives.UnsignedLong.ONE) < 0) {
                throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.U64_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: u64Field is less than min 1");
            }
            return u64Field;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Uri> validateUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) throws org.thryft.protocol.InputProtocolException {
            if (uriField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.URI_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: uriField is null");
            }
            if (!uriField.isPresent()) {
                return uriField;
            }
            return uriField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) throws org.thryft.protocol.InputProtocolException {
            if (urlField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.URL_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: urlField is null");
            }
            if (!urlField.isPresent()) {
                return urlField;
            }
            return urlField;
        }

        @Override
        public com.google.common.base.Optional<java.lang.Object> validateVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) throws org.thryft.protocol.InputProtocolException {
            if (variantField == null) {
                throw new org.thryft.protocol.MissingFieldInputProtocolException(FieldMetadata.VARIANT_FIELD, "org.thryft.protocol.test.ProtocolTestStruct: variantField is null");
            }
            if (!variantField.isPresent()) {
                return variantField;
            }
            return variantField;
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
        public com.google.common.base.Optional<java.util.Date> validateDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
            return dateTimeField;
        }

        @Override
        public com.google.common.base.Optional<java.math.BigDecimal> validateDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
            return decimalField;
        }

        @Override
        public com.google.common.base.Optional<Double> validateDoubleField(final com.google.common.base.Optional<Double> doubleField) {
            return doubleField;
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
        public com.google.common.base.Optional<Float> validateFloatField(final com.google.common.base.Optional<Float> floatField) {
            return floatField;
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
        public com.google.common.base.Optional<Byte> validateI8Field(final com.google.common.base.Optional<Byte> i8Field) {
            return i8Field;
        }

        @Override
        public com.google.common.base.Optional<String> validateStringField(final com.google.common.base.Optional<String> stringField) {
            return stringField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> validateStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
            return stringListField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> validateStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
            return stringSetField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> validateStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
            return stringStringMapField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> validateStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) {
            return structField;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> validateU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) {
            return u32Field;
        }

        @Override
        public com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> validateU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) {
            return u64Field;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Uri> validateUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) {
            return uriField;
        }

        @Override
        public com.google.common.base.Optional<org.thryft.native_.Url> validateUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
            return urlField;
        }

        @Override
        public com.google.common.base.Optional<java.lang.Object> validateVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) {
            return variantField;
        }

        private final static NopReadValidator instance = new NopReadValidator();
    }

    /**
     * Copy constructor
     */
    public ProtocolTestStruct(final ProtocolTestStruct other) {
        this(other.getRequiredI32Field(), other.getRequiredStringField(), other.getBinaryField(), other.getBoolField(), other.getDateTimeField(), other.getDecimalField(), other.getDoubleField(), other.getEmailAddressField(), other.getEnumField(), other.getFloatField(), other.getI16Field(), other.getI32Field(), other.getI64Field(), other.getI8Field(), other.getStringField(), other.getStringListField(), other.getStringSetField(), other.getStringStringMapField(), other.getStructField(), other.getU32Field(), other.getU64Field(), other.getUriField(), other.getUrlField(), other.getVariantField(), NopConstructionValidator.getInstance());
    }

    protected ProtocolTestStruct(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<Double> doubleField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Float> floatField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<Byte> i8Field, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, final com.google.common.base.Optional<org.thryft.native_.Uri> uriField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, final com.google.common.base.Optional<java.lang.Object> variantField, ConstructionValidator validator) {
        this.requiredI32Field = validator.validateRequiredI32Field(requiredI32Field);
        this.requiredStringField = validator.validateRequiredStringField(requiredStringField);
        this.binaryField = validator.validateBinaryField(binaryField);
        this.boolField = validator.validateBoolField(boolField);
        this.dateTimeField = validator.validateDateTimeField(dateTimeField);
        this.decimalField = validator.validateDecimalField(decimalField);
        this.doubleField = validator.validateDoubleField(doubleField);
        this.emailAddressField = validator.validateEmailAddressField(emailAddressField);
        this.enumField = validator.validateEnumField(enumField);
        this.floatField = validator.validateFloatField(floatField);
        this.i16Field = validator.validateI16Field(i16Field);
        this.i32Field = validator.validateI32Field(i32Field);
        this.i64Field = validator.validateI64Field(i64Field);
        this.i8Field = validator.validateI8Field(i8Field);
        this.stringField = validator.validateStringField(stringField);
        this.stringListField = validator.validateStringListField(stringListField);
        this.stringSetField = validator.validateStringSetField(stringSetField);
        this.stringStringMapField = validator.validateStringStringMapField(stringStringMapField);
        this.structField = validator.validateStructField(structField);
        this.u32Field = validator.validateU32Field(u32Field);
        this.u64Field = validator.validateU64Field(u64Field);
        this.uriField = validator.validateUriField(uriField);
        this.urlField = validator.validateUrlField(urlField);
        this.variantField = validator.validateVariantField(variantField);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(final ProtocolTestStruct other) {
        return new Builder(other);
    }

    public static Builder builder(final com.google.common.base.Optional<ProtocolTestStruct> other) {
        return other.isPresent() ? new Builder(other.get()) : new Builder();
    }

    /**
     * Required factory method
     */
    public static ProtocolTestStruct create(final int requiredI32Field, final String requiredStringField) {
        return new ProtocolTestStruct(requiredI32Field, requiredStringField, com.google.common.base.Optional.<byte[]> absent(), com.google.common.base.Optional.<Boolean> absent(), com.google.common.base.Optional.<java.util.Date> absent(), com.google.common.base.Optional.<java.math.BigDecimal> absent(), com.google.common.base.Optional.<Double> absent(), com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent(), com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent(), com.google.common.base.Optional.<Float> absent(), com.google.common.base.Optional.<Short> absent(), com.google.common.base.Optional.<Integer> absent(), com.google.common.base.Optional.<Long> absent(), com.google.common.base.Optional.<Byte> absent(), com.google.common.base.Optional.<String> absent(), com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent(), com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent(), com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent(), com.google.common.base.Optional.<org.thryft.protocol.test.NestedProtocolTestStruct> absent(), com.google.common.base.Optional.<com.google.common.primitives.UnsignedInteger> absent(), com.google.common.base.Optional.<com.google.common.primitives.UnsignedLong> absent(), com.google.common.base.Optional.<org.thryft.native_.Uri> absent(), com.google.common.base.Optional.<org.thryft.native_.Url> absent(), com.google.common.base.Optional.<java.lang.Object> absent(), DefaultConstructionValidator.getInstance());
    }

    /**
     * Total boxed factory method
     */
    public static ProtocolTestStruct create(Integer requiredI32Field, String requiredStringField, com.google.common.base.Optional<byte[]> binaryField, com.google.common.base.Optional<Boolean> boolField, com.google.common.base.Optional<java.util.Date> dateTimeField, com.google.common.base.Optional<java.math.BigDecimal> decimalField, com.google.common.base.Optional<Double> doubleField, com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, com.google.common.base.Optional<Float> floatField, com.google.common.base.Optional<Short> i16Field, com.google.common.base.Optional<Integer> i32Field, com.google.common.base.Optional<Long> i64Field, com.google.common.base.Optional<Byte> i8Field, com.google.common.base.Optional<String> stringField, com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, com.google.common.base.Optional<org.thryft.native_.Uri> uriField, com.google.common.base.Optional<org.thryft.native_.Url> urlField, com.google.common.base.Optional<java.lang.Object> variantField) {
        return new ProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, doubleField, emailAddressField, enumField, floatField, i16Field, i32Field, i64Field, i8Field, stringField, stringListField, stringSetField, stringStringMapField, structField, u32Field, u64Field, uriField, urlField, variantField, DefaultConstructionValidator.getInstance());
    }

    /**
     * Total Nullable factory method
     */
    public static ProtocolTestStruct create(final int requiredI32Field, final String requiredStringField, final @javax.annotation.Nullable byte[] binaryField, final @javax.annotation.Nullable Boolean boolField, final @javax.annotation.Nullable java.util.Date dateTimeField, final @javax.annotation.Nullable java.math.BigDecimal decimalField, final @javax.annotation.Nullable Double doubleField, final @javax.annotation.Nullable org.thryft.native_.EmailAddress emailAddressField, final @javax.annotation.Nullable org.thryft.protocol.test.ProtocolTestEnum enumField, final @javax.annotation.Nullable Float floatField, final @javax.annotation.Nullable Short i16Field, final @javax.annotation.Nullable Integer i32Field, final @javax.annotation.Nullable Long i64Field, final @javax.annotation.Nullable Byte i8Field, final @javax.annotation.Nullable String stringField, final @javax.annotation.Nullable com.google.common.collect.ImmutableList<String> stringListField, final @javax.annotation.Nullable com.google.common.collect.ImmutableSet<String> stringSetField, final @javax.annotation.Nullable com.google.common.collect.ImmutableMap<String, String> stringStringMapField, final @javax.annotation.Nullable org.thryft.protocol.test.NestedProtocolTestStruct structField, final @javax.annotation.Nullable com.google.common.primitives.UnsignedInteger u32Field, final @javax.annotation.Nullable com.google.common.primitives.UnsignedLong u64Field, final @javax.annotation.Nullable org.thryft.native_.Uri uriField, final @javax.annotation.Nullable org.thryft.native_.Url urlField, final @javax.annotation.Nullable java.lang.Object variantField) {
        return new ProtocolTestStruct(requiredI32Field, requiredStringField, com.google.common.base.Optional.fromNullable(binaryField), com.google.common.base.Optional.fromNullable(boolField), com.google.common.base.Optional.fromNullable(dateTimeField), com.google.common.base.Optional.fromNullable(decimalField), com.google.common.base.Optional.fromNullable(doubleField), com.google.common.base.Optional.fromNullable(emailAddressField), com.google.common.base.Optional.fromNullable(enumField), com.google.common.base.Optional.fromNullable(floatField), com.google.common.base.Optional.fromNullable(i16Field), com.google.common.base.Optional.fromNullable(i32Field), com.google.common.base.Optional.fromNullable(i64Field), com.google.common.base.Optional.fromNullable(i8Field), com.google.common.base.Optional.fromNullable(stringField), com.google.common.base.Optional.fromNullable(stringListField), com.google.common.base.Optional.fromNullable(stringSetField), com.google.common.base.Optional.fromNullable(stringStringMapField), com.google.common.base.Optional.fromNullable(structField), com.google.common.base.Optional.fromNullable(u32Field), com.google.common.base.Optional.fromNullable(u64Field), com.google.common.base.Optional.fromNullable(uriField), com.google.common.base.Optional.fromNullable(urlField), com.google.common.base.Optional.fromNullable(variantField), DefaultConstructionValidator.getInstance());
    }

    /**
     * Optional factory method
     */
    public static ProtocolTestStruct create(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<Double> doubleField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Float> floatField, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<Byte> i8Field, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, final com.google.common.base.Optional<org.thryft.native_.Uri> uriField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, final com.google.common.base.Optional<java.lang.Object> variantField) {
        return new ProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, doubleField, emailAddressField, enumField, floatField, i16Field, i32Field, i64Field, i8Field, stringField, stringListField, stringSetField, stringStringMapField, structField, u32Field, u64Field, uriField, urlField, variantField, DefaultConstructionValidator.getInstance());
    }

    @Override
    public boolean equals(final java.lang.Object otherObject) {
        if (otherObject == this) {
            return true;
        }
        if (!(otherObject instanceof ProtocolTestStruct)) {
            return false;
        }

        final ProtocolTestStruct other = (ProtocolTestStruct)otherObject;

        if (!(getRequiredI32Field() == other.getRequiredI32Field())) {
            return false;
        }

        if (!(getRequiredStringField().equals(other.getRequiredStringField()))) {
            return false;
        }

        if (!(((getBinaryField().isPresent() && other.getBinaryField().isPresent()) ? (java.util.Arrays.equals(getBinaryField().get(), other.getBinaryField().get())) : (!getBinaryField().isPresent() && !other.getBinaryField().isPresent())))) {
            return false;
        }

        if (!(((getBoolField().isPresent() && other.getBoolField().isPresent()) ? (getBoolField().get().booleanValue() == other.getBoolField().get().booleanValue()) : (!getBoolField().isPresent() && !other.getBoolField().isPresent())))) {
            return false;
        }

        if (!(((getDateTimeField().isPresent() && other.getDateTimeField().isPresent()) ? (getDateTimeField().get().equals(other.getDateTimeField().get())) : (!getDateTimeField().isPresent() && !other.getDateTimeField().isPresent())))) {
            return false;
        }

        if (!(((getDecimalField().isPresent() && other.getDecimalField().isPresent()) ? (getDecimalField().get().equals(other.getDecimalField().get())) : (!getDecimalField().isPresent() && !other.getDecimalField().isPresent())))) {
            return false;
        }

        if (!(((getDoubleField().isPresent() && other.getDoubleField().isPresent()) ? (getDoubleField().get().doubleValue() == other.getDoubleField().get().doubleValue()) : (!getDoubleField().isPresent() && !other.getDoubleField().isPresent())))) {
            return false;
        }

        if (!(((getEmailAddressField().isPresent() && other.getEmailAddressField().isPresent()) ? (getEmailAddressField().get().equals(other.getEmailAddressField().get())) : (!getEmailAddressField().isPresent() && !other.getEmailAddressField().isPresent())))) {
            return false;
        }

        if (!(((getEnumField().isPresent() && other.getEnumField().isPresent()) ? (getEnumField().get().equals(other.getEnumField().get())) : (!getEnumField().isPresent() && !other.getEnumField().isPresent())))) {
            return false;
        }

        if (!(((getFloatField().isPresent() && other.getFloatField().isPresent()) ? (getFloatField().get().floatValue() == other.getFloatField().get().floatValue()) : (!getFloatField().isPresent() && !other.getFloatField().isPresent())))) {
            return false;
        }

        if (!(((getI16Field().isPresent() && other.getI16Field().isPresent()) ? (getI16Field().get().shortValue() == other.getI16Field().get().shortValue()) : (!getI16Field().isPresent() && !other.getI16Field().isPresent())))) {
            return false;
        }

        if (!(((getI32Field().isPresent() && other.getI32Field().isPresent()) ? (getI32Field().get().intValue() == other.getI32Field().get().intValue()) : (!getI32Field().isPresent() && !other.getI32Field().isPresent())))) {
            return false;
        }

        if (!(((getI64Field().isPresent() && other.getI64Field().isPresent()) ? (getI64Field().get().longValue() == other.getI64Field().get().longValue()) : (!getI64Field().isPresent() && !other.getI64Field().isPresent())))) {
            return false;
        }

        if (!(((getI8Field().isPresent() && other.getI8Field().isPresent()) ? (getI8Field().get().byteValue() == other.getI8Field().get().byteValue()) : (!getI8Field().isPresent() && !other.getI8Field().isPresent())))) {
            return false;
        }

        if (!(((getStringField().isPresent() && other.getStringField().isPresent()) ? (getStringField().get().equals(other.getStringField().get())) : (!getStringField().isPresent() && !other.getStringField().isPresent())))) {
            return false;
        }

        if (!(((getStringListField().isPresent() && other.getStringListField().isPresent()) ? (getStringListField().get().equals(other.getStringListField().get())) : (!getStringListField().isPresent() && !other.getStringListField().isPresent())))) {
            return false;
        }

        if (!(((getStringSetField().isPresent() && other.getStringSetField().isPresent()) ? (getStringSetField().get().equals(other.getStringSetField().get())) : (!getStringSetField().isPresent() && !other.getStringSetField().isPresent())))) {
            return false;
        }

        if (!(((getStringStringMapField().isPresent() && other.getStringStringMapField().isPresent()) ? (getStringStringMapField().get().equals(other.getStringStringMapField().get())) : (!getStringStringMapField().isPresent() && !other.getStringStringMapField().isPresent())))) {
            return false;
        }

        if (!(((getStructField().isPresent() && other.getStructField().isPresent()) ? (getStructField().get().equals(other.getStructField().get())) : (!getStructField().isPresent() && !other.getStructField().isPresent())))) {
            return false;
        }

        if (!(((getU32Field().isPresent() && other.getU32Field().isPresent()) ? (getU32Field().get().equals(other.getU32Field().get())) : (!getU32Field().isPresent() && !other.getU32Field().isPresent())))) {
            return false;
        }

        if (!(((getU64Field().isPresent() && other.getU64Field().isPresent()) ? (getU64Field().get().equals(other.getU64Field().get())) : (!getU64Field().isPresent() && !other.getU64Field().isPresent())))) {
            return false;
        }

        if (!(((getUriField().isPresent() && other.getUriField().isPresent()) ? (getUriField().get().equals(other.getUriField().get())) : (!getUriField().isPresent() && !other.getUriField().isPresent())))) {
            return false;
        }

        if (!(((getUrlField().isPresent() && other.getUrlField().isPresent()) ? (getUrlField().get().equals(other.getUrlField().get())) : (!getUrlField().isPresent() && !other.getUrlField().isPresent())))) {
            return false;
        }

        if (!(((getVariantField().isPresent() && other.getVariantField().isPresent()) ? (getVariantField().get().equals(other.getVariantField().get())) : (!getVariantField().isPresent() && !other.getVariantField().isPresent())))) {
            return false;
        }

        return true;
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
        case DATE_TIME_FIELD: return getDateTimeField();
        case DECIMAL_FIELD: return getDecimalField();
        case DOUBLE_FIELD: return getDoubleField();
        case EMAIL_ADDRESS_FIELD: return getEmailAddressField();
        case ENUM_FIELD: return getEnumField();
        case FLOAT_FIELD: return getFloatField();
        case I16_FIELD: return getI16Field();
        case I32_FIELD: return getI32Field();
        case I64_FIELD: return getI64Field();
        case I8_FIELD: return getI8Field();
        case STRING_FIELD: return getStringField();
        case STRING_LIST_FIELD: return getStringListField();
        case STRING_SET_FIELD: return getStringSetField();
        case STRING_STRING_MAP_FIELD: return getStringStringMapField();
        case STRUCT_FIELD: return getStructField();
        case U32_FIELD: return getU32Field();
        case U64_FIELD: return getU64Field();
        case URI_FIELD: return getUriField();
        case URL_FIELD: return getUrlField();
        case VARIANT_FIELD: return getVariantField();
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

    public final com.google.common.base.Optional<java.util.Date> getDateTimeField() {
        return dateTimeField;
    }

    public final com.google.common.base.Optional<java.math.BigDecimal> getDecimalField() {
        return decimalField;
    }

    public final com.google.common.base.Optional<Double> getDoubleField() {
        return doubleField;
    }

    public final com.google.common.base.Optional<org.thryft.native_.EmailAddress> getEmailAddressField() {
        return emailAddressField;
    }

    public final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> getEnumField() {
        return enumField;
    }

    public final com.google.common.base.Optional<Float> getFloatField() {
        return floatField;
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

    public final com.google.common.base.Optional<Byte> getI8Field() {
        return i8Field;
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

    public final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> getStructField() {
        return structField;
    }

    public final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> getU32Field() {
        return u32Field;
    }

    public final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> getU64Field() {
        return u64Field;
    }

    public final com.google.common.base.Optional<org.thryft.native_.Uri> getUriField() {
        return uriField;
    }

    public final com.google.common.base.Optional<org.thryft.native_.Url> getUrlField() {
        return urlField;
    }

    public final com.google.common.base.Optional<java.lang.Object> getVariantField() {
        return variantField;
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
        if (getDateTimeField().isPresent()) {
            hashCode = 31 * hashCode + getDateTimeField().get().hashCode();
        }
        if (getDecimalField().isPresent()) {
            hashCode = 31 * hashCode + getDecimalField().get().hashCode();
        }
        if (getDoubleField().isPresent()) {
            hashCode = 31 * hashCode + ((int)(Double.doubleToLongBits(getDoubleField().get()) ^ (Double.doubleToLongBits(getDoubleField().get()) >>> 32)));
        }
        if (getEmailAddressField().isPresent()) {
            hashCode = 31 * hashCode + getEmailAddressField().get().hashCode();
        }
        if (getEnumField().isPresent()) {
            hashCode = 31 * hashCode + getEnumField().get().ordinal();
        }
        if (getFloatField().isPresent()) {
            hashCode = 31 * hashCode + ((int)(Double.doubleToLongBits(getFloatField().get()) ^ (Double.doubleToLongBits(getFloatField().get()) >>> 32)));
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
        if (getI8Field().isPresent()) {
            hashCode = 31 * hashCode + getI8Field().get().hashCode();
        }
        if (getStringField().isPresent()) {
            hashCode = 31 * hashCode + getStringField().get().hashCode();
        }
        if (getStringListField().isPresent()) {
            hashCode = 31 * hashCode + getStringListField().get().hashCode();
        }
        if (getStringSetField().isPresent()) {
            hashCode = 31 * hashCode + getStringSetField().get().hashCode();
        }
        if (getStringStringMapField().isPresent()) {
            hashCode = 31 * hashCode + getStringStringMapField().get().hashCode();
        }
        if (getStructField().isPresent()) {
            hashCode = 31 * hashCode + getStructField().get().hashCode();
        }
        if (getU32Field().isPresent()) {
            hashCode = 31 * hashCode + getU32Field().get().hashCode();
        }
        if (getU64Field().isPresent()) {
            hashCode = 31 * hashCode + getU64Field().get().hashCode();
        }
        if (getUriField().isPresent()) {
            hashCode = 31 * hashCode + getUriField().get().hashCode();
        }
        if (getUrlField().isPresent()) {
            hashCode = 31 * hashCode + getUrlField().get().hashCode();
        }
        if (getVariantField().isPresent()) {
            hashCode = 31 * hashCode + getVariantField().get().hashCode();
        }
        return hashCode;
    }

    public static ProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
        return readAs(iprot, type, com.google.common.base.Optional.<UnknownFieldCallback> absent());
    }

    public static ProtocolTestStruct readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        switch (type) {
        case LIST:
            return readAsList(iprot);
        case STRUCT:
            return readAsStruct(iprot, unknownFieldCallback);
        default:
            throw new IllegalArgumentException("cannot read as " + type);
        }
    }

    public static ProtocolTestStruct readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.<byte[]> absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.<Boolean> absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
        com.google.common.base.Optional<Double> doubleField = com.google.common.base.Optional.<Double> absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
        com.google.common.base.Optional<Float> floatField = com.google.common.base.Optional.<Float> absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.<Short> absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.<Integer> absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.<Long> absent();
        com.google.common.base.Optional<Byte> i8Field = com.google.common.base.Optional.<Byte> absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.<String> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
        com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField = com.google.common.base.Optional.<org.thryft.protocol.test.NestedProtocolTestStruct> absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedInteger> absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedLong> absent();
        com.google.common.base.Optional<org.thryft.native_.Uri> uriField = com.google.common.base.Optional.<org.thryft.native_.Uri> absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();
        com.google.common.base.Optional<java.lang.Object> variantField = com.google.common.base.Optional.<java.lang.Object> absent();

        try {
            final org.thryft.protocol.ListBegin __list = iprot.readListBegin();
            try {
                requiredI32Field = iprot.readI32();
            } catch (final NumberFormatException e) {
                 throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.REQUIRED_I32_FIELD, e);
            }
            requiredStringField = iprot.readString();
            if (__list.getSize() > 2) {
                binaryField = com.google.common.base.Optional.of(iprot.readBinary());
            }
            if (__list.getSize() > 3) {
                boolField = com.google.common.base.Optional.of(iprot.readBool());
            }
            if (__list.getSize() > 4) {
                try {
                    dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                } catch (final IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 5) {
                try {
                    decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 6) {
                try {
                    doubleField = com.google.common.base.Optional.of(iprot.readDouble());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 7) {
                emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
            }
            if (__list.getSize() > 8) {
                enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
            }
            if (__list.getSize() > 9) {
                try {
                    floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 10) {
                try {
                    i16Field = com.google.common.base.Optional.of(iprot.readI16());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 11) {
                try {
                    i32Field = com.google.common.base.Optional.of(iprot.readI32());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 12) {
                try {
                    i64Field = com.google.common.base.Optional.of(iprot.readI64());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 13) {
                try {
                    i8Field = com.google.common.base.Optional.of(iprot.readByte());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 14) {
                stringField = com.google.common.base.Optional.of(iprot.readString());
            }
            if (__list.getSize() > 15) {
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
                     throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_LIST_FIELD, e.getCause());
                }
            }
            if (__list.getSize() > 16) {
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
                     throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_SET_FIELD, e.getCause());
                }
            }
            if (__list.getSize() > 17) {
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
                                throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                            }
                        }
                    }).apply(iprot));
                } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                     throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_STRING_MAP_FIELD, e.getCause());
                }
            }
            if (__list.getSize() > 18) {
                structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
            }
            if (__list.getSize() > 19) {
                try {
                    u32Field = com.google.common.base.Optional.of(iprot.readU32());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 20) {
                try {
                    u64Field = com.google.common.base.Optional.of(iprot.readU64());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 21) {
                try {
                    uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 22) {
                try {
                    urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 23) {
                variantField = com.google.common.base.Optional.of(iprot.readVariant());
            }
            iprot.readListEnd();
        } catch (final RuntimeException e) {
            throw new IllegalStateException(e);
        }
        return new ProtocolTestStruct(DefaultReadValidator.getInstance().validateRequiredI32Field(requiredI32Field), DefaultReadValidator.getInstance().validateRequiredStringField(requiredStringField), DefaultReadValidator.getInstance().validateBinaryField(binaryField), DefaultReadValidator.getInstance().validateBoolField(boolField), DefaultReadValidator.getInstance().validateDateTimeField(dateTimeField), DefaultReadValidator.getInstance().validateDecimalField(decimalField), DefaultReadValidator.getInstance().validateDoubleField(doubleField), DefaultReadValidator.getInstance().validateEmailAddressField(emailAddressField), DefaultReadValidator.getInstance().validateEnumField(enumField), DefaultReadValidator.getInstance().validateFloatField(floatField), DefaultReadValidator.getInstance().validateI16Field(i16Field), DefaultReadValidator.getInstance().validateI32Field(i32Field), DefaultReadValidator.getInstance().validateI64Field(i64Field), DefaultReadValidator.getInstance().validateI8Field(i8Field), DefaultReadValidator.getInstance().validateStringField(stringField), DefaultReadValidator.getInstance().validateStringListField(stringListField), DefaultReadValidator.getInstance().validateStringSetField(stringSetField), DefaultReadValidator.getInstance().validateStringStringMapField(stringStringMapField), DefaultReadValidator.getInstance().validateStructField(structField), DefaultReadValidator.getInstance().validateU32Field(u32Field), DefaultReadValidator.getInstance().validateU64Field(u64Field), DefaultReadValidator.getInstance().validateUriField(uriField), DefaultReadValidator.getInstance().validateUrlField(urlField), DefaultReadValidator.getInstance().validateVariantField(variantField), NopConstructionValidator.getInstance());
    }

    public static ProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
    }

    public static ProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.<byte[]> absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.<Boolean> absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.<java.util.Date> absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.<java.math.BigDecimal> absent();
        com.google.common.base.Optional<Double> doubleField = com.google.common.base.Optional.<Double> absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.<org.thryft.native_.EmailAddress> absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.<org.thryft.protocol.test.ProtocolTestEnum> absent();
        com.google.common.base.Optional<Float> floatField = com.google.common.base.Optional.<Float> absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.<Short> absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.<Integer> absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.<Long> absent();
        com.google.common.base.Optional<Byte> i8Field = com.google.common.base.Optional.<Byte> absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.<String> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.<com.google.common.collect.ImmutableList<String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.<com.google.common.collect.ImmutableSet<String>> absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.<com.google.common.collect.ImmutableMap<String, String>> absent();
        com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField = com.google.common.base.Optional.<org.thryft.protocol.test.NestedProtocolTestStruct> absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedInteger> absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field = com.google.common.base.Optional.<com.google.common.primitives.UnsignedLong> absent();
        com.google.common.base.Optional<org.thryft.native_.Uri> uriField = com.google.common.base.Optional.<org.thryft.native_.Uri> absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.<org.thryft.native_.Url> absent();
        com.google.common.base.Optional<java.lang.Object> variantField = com.google.common.base.Optional.<java.lang.Object> absent();

        try {
            iprot.readStructBegin();
            while (true) {
                final org.thryft.protocol.FieldBegin ifield = iprot.readFieldBegin();
                if (ifield.getType() == org.thryft.protocol.Type.STOP) {
                    break;
                }
                switch (ifield.getName()) {
                case "required_i32_field": {
                    if (!ifield.hasId() || ifield.getId() == 1) {
                        try {
                            requiredI32Field = iprot.readI32();
                        } catch (final NumberFormatException e) {
                             throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.REQUIRED_I32_FIELD, e);
                        }
                    }
                    break;
                }
                case "required_string_field": {
                    if (!ifield.hasId() || ifield.getId() == 2) {
                        requiredStringField = iprot.readString();
                    }
                    break;
                }
                case "binary_field": {
                    if (!ifield.hasId() || ifield.getId() == 3) {
                        binaryField = com.google.common.base.Optional.of(iprot.readBinary());
                    }
                    break;
                }
                case "bool_field": {
                    if (!ifield.hasId() || ifield.getId() == 4) {
                        boolField = com.google.common.base.Optional.of(iprot.readBool());
                    }
                    break;
                }
                case "date_time_field": {
                    if (!ifield.hasId() || ifield.getId() == 5) {
                        try {
                            dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                        } catch (final IllegalArgumentException e) {
                        }
                    }
                    break;
                }
                case "decimal_field": {
                    if (!ifield.hasId() || ifield.getId() == 6) {
                        try {
                            decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "double_field": {
                    if (!ifield.hasId() || ifield.getId() == 7) {
                        try {
                            doubleField = com.google.common.base.Optional.of(iprot.readDouble());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "email_address_field": {
                    if (!ifield.hasId() || ifield.getId() == 8) {
                        emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                    }
                    break;
                }
                case "enum_field": {
                    if (!ifield.hasId() || ifield.getId() == 9) {
                        enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                    }
                    break;
                }
                case "float_field": {
                    if (!ifield.hasId() || ifield.getId() == 10) {
                        try {
                            floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "i16_field": {
                    if (!ifield.hasId() || ifield.getId() == 12) {
                        try {
                            i16Field = com.google.common.base.Optional.of(iprot.readI16());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "i32_field": {
                    if (!ifield.hasId() || ifield.getId() == 13) {
                        try {
                            i32Field = com.google.common.base.Optional.of(iprot.readI32());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "i64_field": {
                    if (!ifield.hasId() || ifield.getId() == 14) {
                        try {
                            i64Field = com.google.common.base.Optional.of(iprot.readI64());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "i8_field": {
                    if (!ifield.hasId() || ifield.getId() == 11) {
                        try {
                            i8Field = com.google.common.base.Optional.of(iprot.readByte());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "string_field": {
                    if (!ifield.hasId() || ifield.getId() == 18) {
                        stringField = com.google.common.base.Optional.of(iprot.readString());
                    }
                    break;
                }
                case "string_list_field": {
                    if (!ifield.hasId() || ifield.getId() == 15) {
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
                             throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_LIST_FIELD, e.getCause());
                        }
                    }
                    break;
                }
                case "string_set_field": {
                    if (!ifield.hasId() || ifield.getId() == 17) {
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
                             throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_SET_FIELD, e.getCause());
                        }
                    }
                    break;
                }
                case "string_string_map_field": {
                    if (!ifield.hasId() || ifield.getId() == 16) {
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
                                        throw new org.thryft.protocol.UncheckedInputProtocolException(e);
                                    }
                                }
                            }).apply(iprot));
                        } catch (final org.thryft.protocol.UncheckedInputProtocolException e) {
                             throw new org.thryft.protocol.InvalidFieldInputProtocolException(FieldMetadata.STRING_STRING_MAP_FIELD, e.getCause());
                        }
                    }
                    break;
                }
                case "struct_field": {
                    if (!ifield.hasId() || ifield.getId() == 19) {
                        structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
                    }
                    break;
                }
                case "u32_field": {
                    if (!ifield.hasId() || ifield.getId() == 20) {
                        try {
                            u32Field = com.google.common.base.Optional.of(iprot.readU32());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "u64_field": {
                    if (!ifield.hasId() || ifield.getId() == 21) {
                        try {
                            u64Field = com.google.common.base.Optional.of(iprot.readU64());
                        } catch (final NumberFormatException e) {
                        }
                    }
                    break;
                }
                case "uri_field": {
                    if (!ifield.hasId() || ifield.getId() == 22) {
                        try {
                            uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                        } catch (final java.lang.IllegalArgumentException e) {
                        }
                    }
                    break;
                }
                case "url_field": {
                    if (!ifield.hasId() || ifield.getId() == 23) {
                        try {
                            urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                        } catch (final java.lang.IllegalArgumentException e) {
                        }
                    }
                    break;
                }
                case "variant_field": {
                    if (!ifield.hasId() || ifield.getId() == 24) {
                        variantField = com.google.common.base.Optional.of(iprot.readVariant());
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
        } catch (final RuntimeException e) {
            throw new IllegalStateException(e);
        }
        return new ProtocolTestStruct(DefaultReadValidator.getInstance().validateRequiredI32Field(requiredI32Field), DefaultReadValidator.getInstance().validateRequiredStringField(requiredStringField), DefaultReadValidator.getInstance().validateBinaryField(binaryField), DefaultReadValidator.getInstance().validateBoolField(boolField), DefaultReadValidator.getInstance().validateDateTimeField(dateTimeField), DefaultReadValidator.getInstance().validateDecimalField(decimalField), DefaultReadValidator.getInstance().validateDoubleField(doubleField), DefaultReadValidator.getInstance().validateEmailAddressField(emailAddressField), DefaultReadValidator.getInstance().validateEnumField(enumField), DefaultReadValidator.getInstance().validateFloatField(floatField), DefaultReadValidator.getInstance().validateI16Field(i16Field), DefaultReadValidator.getInstance().validateI32Field(i32Field), DefaultReadValidator.getInstance().validateI64Field(i64Field), DefaultReadValidator.getInstance().validateI8Field(i8Field), DefaultReadValidator.getInstance().validateStringField(stringField), DefaultReadValidator.getInstance().validateStringListField(stringListField), DefaultReadValidator.getInstance().validateStringSetField(stringSetField), DefaultReadValidator.getInstance().validateStringStringMapField(stringStringMapField), DefaultReadValidator.getInstance().validateStructField(structField), DefaultReadValidator.getInstance().validateU32Field(u32Field), DefaultReadValidator.getInstance().validateU64Field(u64Field), DefaultReadValidator.getInstance().validateUriField(uriField), DefaultReadValidator.getInstance().validateUrlField(urlField), DefaultReadValidator.getInstance().validateVariantField(variantField), NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, DefaultConstructionValidator.getInstance().validateBinaryField(binaryField), this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceBinaryField(final byte[] binaryField) {
        return replaceBinaryField(com.google.common.base.Optional.fromNullable(binaryField));
    }

    public ProtocolTestStruct replaceBoolField(final com.google.common.base.Optional<Boolean> boolField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, DefaultConstructionValidator.getInstance().validateBoolField(boolField), this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceBoolField(final boolean boolField) {
        return replaceBoolField(com.google.common.base.Optional.fromNullable(boolField));
    }

    public ProtocolTestStruct replaceDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, DefaultConstructionValidator.getInstance().validateDateTimeField(dateTimeField), this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceDateTimeField(final java.util.Date dateTimeField) {
        return replaceDateTimeField(com.google.common.base.Optional.fromNullable(dateTimeField));
    }

    public ProtocolTestStruct replaceDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, DefaultConstructionValidator.getInstance().validateDecimalField(decimalField), this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceDecimalField(final java.math.BigDecimal decimalField) {
        return replaceDecimalField(com.google.common.base.Optional.fromNullable(decimalField));
    }

    public ProtocolTestStruct replaceDoubleField(final com.google.common.base.Optional<Double> doubleField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, DefaultConstructionValidator.getInstance().validateDoubleField(doubleField), this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceDoubleField(final double doubleField) {
        return replaceDoubleField(com.google.common.base.Optional.fromNullable(doubleField));
    }

    public ProtocolTestStruct replaceEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, DefaultConstructionValidator.getInstance().validateEmailAddressField(emailAddressField), this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceEmailAddressField(final org.thryft.native_.EmailAddress emailAddressField) {
        return replaceEmailAddressField(com.google.common.base.Optional.fromNullable(emailAddressField));
    }

    public ProtocolTestStruct replaceEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, DefaultConstructionValidator.getInstance().validateEnumField(enumField), this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceEnumField(final org.thryft.protocol.test.ProtocolTestEnum enumField) {
        return replaceEnumField(com.google.common.base.Optional.fromNullable(enumField));
    }

    public ProtocolTestStruct replaceFloatField(final com.google.common.base.Optional<Float> floatField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, DefaultConstructionValidator.getInstance().validateFloatField(floatField), this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceFloatField(final float floatField) {
        return replaceFloatField(com.google.common.base.Optional.fromNullable(floatField));
    }

    public ProtocolTestStruct replaceI16Field(final com.google.common.base.Optional<Short> i16Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, DefaultConstructionValidator.getInstance().validateI16Field(i16Field), this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceI16Field(final short i16Field) {
        return replaceI16Field(com.google.common.base.Optional.fromNullable(i16Field));
    }

    public ProtocolTestStruct replaceI32Field(final com.google.common.base.Optional<Integer> i32Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, DefaultConstructionValidator.getInstance().validateI32Field(i32Field), this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceI32Field(final int i32Field) {
        return replaceI32Field(com.google.common.base.Optional.fromNullable(i32Field));
    }

    public ProtocolTestStruct replaceI64Field(final com.google.common.base.Optional<Long> i64Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, DefaultConstructionValidator.getInstance().validateI64Field(i64Field), this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceI64Field(final long i64Field) {
        return replaceI64Field(com.google.common.base.Optional.fromNullable(i64Field));
    }

    public ProtocolTestStruct replaceI8Field(final com.google.common.base.Optional<Byte> i8Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, DefaultConstructionValidator.getInstance().validateI8Field(i8Field), this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceI8Field(final byte i8Field) {
        return replaceI8Field(com.google.common.base.Optional.fromNullable(i8Field));
    }

    public ProtocolTestStruct replaceRequiredI32Field(final int requiredI32Field) {
        return new ProtocolTestStruct(DefaultConstructionValidator.getInstance().validateRequiredI32Field(requiredI32Field), this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceRequiredStringField(final String requiredStringField) {
        return new ProtocolTestStruct(this.requiredI32Field, DefaultConstructionValidator.getInstance().validateRequiredStringField(requiredStringField), this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceStringField(final com.google.common.base.Optional<String> stringField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, DefaultConstructionValidator.getInstance().validateStringField(stringField), this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceStringField(final String stringField) {
        return replaceStringField(com.google.common.base.Optional.fromNullable(stringField));
    }

    public ProtocolTestStruct replaceStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, DefaultConstructionValidator.getInstance().validateStringListField(stringListField), this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceStringListField(final com.google.common.collect.ImmutableList<String> stringListField) {
        return replaceStringListField(com.google.common.base.Optional.fromNullable(stringListField));
    }

    public ProtocolTestStruct replaceStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, DefaultConstructionValidator.getInstance().validateStringSetField(stringSetField), this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceStringSetField(final com.google.common.collect.ImmutableSet<String> stringSetField) {
        return replaceStringSetField(com.google.common.base.Optional.fromNullable(stringSetField));
    }

    public ProtocolTestStruct replaceStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, DefaultConstructionValidator.getInstance().validateStringStringMapField(stringStringMapField), this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceStringStringMapField(final com.google.common.collect.ImmutableMap<String, String> stringStringMapField) {
        return replaceStringStringMapField(com.google.common.base.Optional.fromNullable(stringStringMapField));
    }

    public ProtocolTestStruct replaceStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, DefaultConstructionValidator.getInstance().validateStructField(structField), this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceStructField(final org.thryft.protocol.test.NestedProtocolTestStruct structField) {
        return replaceStructField(com.google.common.base.Optional.fromNullable(structField));
    }

    public ProtocolTestStruct replaceU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, DefaultConstructionValidator.getInstance().validateU32Field(u32Field), this.u64Field, this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceU32Field(final com.google.common.primitives.UnsignedInteger u32Field) {
        return replaceU32Field(com.google.common.base.Optional.fromNullable(u32Field));
    }

    public ProtocolTestStruct replaceU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, DefaultConstructionValidator.getInstance().validateU64Field(u64Field), this.uriField, this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceU64Field(final com.google.common.primitives.UnsignedLong u64Field) {
        return replaceU64Field(com.google.common.base.Optional.fromNullable(u64Field));
    }

    public ProtocolTestStruct replaceUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, DefaultConstructionValidator.getInstance().validateUriField(uriField), this.urlField, this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceUriField(final org.thryft.native_.Uri uriField) {
        return replaceUriField(com.google.common.base.Optional.fromNullable(uriField));
    }

    public ProtocolTestStruct replaceUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, DefaultConstructionValidator.getInstance().validateUrlField(urlField), this.variantField, NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceUrlField(final org.thryft.native_.Url urlField) {
        return replaceUrlField(com.google.common.base.Optional.fromNullable(urlField));
    }

    public ProtocolTestStruct replaceVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.doubleField, this.emailAddressField, this.enumField, this.floatField, this.i16Field, this.i32Field, this.i64Field, this.i8Field, this.stringField, this.stringListField, this.stringSetField, this.stringStringMapField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, DefaultConstructionValidator.getInstance().validateVariantField(variantField), NopConstructionValidator.getInstance());
    }

    public ProtocolTestStruct replaceVariantField(final java.lang.Object variantField) {
        return replaceVariantField(com.google.common.base.Optional.fromNullable(variantField));
    }

    @Override
    public String toString() {
        return com.google.common.base.MoreObjects.toStringHelper(this).omitNullValues().add("required_i32_field", getRequiredI32Field()).add("required_string_field", getRequiredStringField()).add("binary_field", getBinaryField().orNull()).add("bool_field", getBoolField().orNull()).add("date_time_field", getDateTimeField().orNull()).add("decimal_field", getDecimalField().orNull()).add("double_field", getDoubleField().orNull()).add("email_address_field", getEmailAddressField().orNull()).add("enum_field", getEnumField().orNull()).add("float_field", getFloatField().orNull()).add("i16_field", getI16Field().orNull()).add("i32_field", getI32Field().orNull()).add("i64_field", getI64Field().orNull()).add("i8_field", getI8Field().orNull()).add("string_field", getStringField().orNull()).add("string_list_field", getStringListField().orNull()).add("string_set_field", getStringSetField().orNull()).add("string_string_map_field", getStringStringMapField().orNull()).add("struct_field", getStructField().orNull()).add("u32_field", getU32Field().orNull()).add("u64_field", getU64Field().orNull()).add("uri_field", getUriField().orNull()).add("url_field", getUrlField().orNull()).add("variant_field", getVariantField().orNull()).toString();
    }

    @Override
    public void writeAsList(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeListBegin(org.thryft.protocol.Type.VOID_, 24);

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

        if (getDoubleField().isPresent()) {
            oprot.writeDouble(getDoubleField().get());
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

        if (getFloatField().isPresent()) {
            oprot.writeDouble(getFloatField().get());
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

        if (getI8Field().isPresent()) {
            oprot.writeByte(getI8Field().get());
        } else {
            oprot.writeNull();
        }

        if (getStringField().isPresent()) {
            oprot.writeString(getStringField().get());
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

        if (getStringSetField().isPresent()) {
            oprot.writeSetBegin(org.thryft.protocol.Type.STRING, getStringSetField().get().size());
            for (final String _iter0 : getStringSetField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeSetEnd();
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

        if (getStructField().isPresent()) {
            getStructField().get().writeAsStruct(oprot);
        } else {
            oprot.writeNull();
        }

        if (getU32Field().isPresent()) {
            oprot.writeU32(getU32Field().get());
        } else {
            oprot.writeNull();
        }

        if (getU64Field().isPresent()) {
            oprot.writeU64(getU64Field().get());
        } else {
            oprot.writeNull();
        }

        if (getUriField().isPresent()) {
            oprot.writeString(getUriField().get().toString());
        } else {
            oprot.writeNull();
        }

        if (getUrlField().isPresent()) {
            oprot.writeString(getUrlField().get().toString());
        } else {
            oprot.writeNull();
        }

        if (getVariantField().isPresent()) {
            oprot.writeVariant(getVariantField().get());
        } else {
            oprot.writeNull();
        }

        oprot.writeListEnd();
    }

    @Override
    public void writeAsStruct(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeStructBegin("org.thryft.protocol.test.ProtocolTestStruct");
        writeFields(oprot);
        oprot.writeStructEnd();
    }

    @Override
    public void writeFields(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeFieldBegin("required_i32_field", org.thryft.protocol.Type.I32, (short)1);
        oprot.writeI32(getRequiredI32Field());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin("required_string_field", org.thryft.protocol.Type.STRING, (short)2);
        oprot.writeString(getRequiredStringField());
        oprot.writeFieldEnd();

        if (getBinaryField().isPresent()) {
            oprot.writeFieldBegin("binary_field", org.thryft.protocol.Type.STRING, (short)3);
            oprot.writeBinary(getBinaryField().get());
            oprot.writeFieldEnd();
        }

        if (getBoolField().isPresent()) {
            oprot.writeFieldBegin("bool_field", org.thryft.protocol.Type.BOOL, (short)4);
            oprot.writeBool(getBoolField().get());
            oprot.writeFieldEnd();
        }

        if (getDateTimeField().isPresent()) {
            oprot.writeFieldBegin("date_time_field", org.thryft.protocol.Type.I64, (short)5);
            oprot.writeDateTime(getDateTimeField().get());
            oprot.writeFieldEnd();
        }

        if (getDecimalField().isPresent()) {
            oprot.writeFieldBegin("decimal_field", org.thryft.protocol.Type.STRING, (short)6);
            oprot.writeDecimal(getDecimalField().get());
            oprot.writeFieldEnd();
        }

        if (getDoubleField().isPresent()) {
            oprot.writeFieldBegin("double_field", org.thryft.protocol.Type.DOUBLE, (short)7);
            oprot.writeDouble(getDoubleField().get());
            oprot.writeFieldEnd();
        }

        if (getEmailAddressField().isPresent()) {
            oprot.writeFieldBegin("email_address_field", org.thryft.protocol.Type.STRING, (short)8);
            oprot.writeString(getEmailAddressField().get().toString());
            oprot.writeFieldEnd();
        }

        if (getEnumField().isPresent()) {
            oprot.writeFieldBegin("enum_field", org.thryft.protocol.Type.STRING, (short)9);
            oprot.writeEnum(getEnumField().get());
            oprot.writeFieldEnd();
        }

        if (getFloatField().isPresent()) {
            oprot.writeFieldBegin("float_field", org.thryft.protocol.Type.DOUBLE, (short)10);
            oprot.writeDouble(getFloatField().get());
            oprot.writeFieldEnd();
        }

        if (getI16Field().isPresent()) {
            oprot.writeFieldBegin("i16_field", org.thryft.protocol.Type.I16, (short)12);
            oprot.writeI16(getI16Field().get());
            oprot.writeFieldEnd();
        }

        if (getI32Field().isPresent()) {
            oprot.writeFieldBegin("i32_field", org.thryft.protocol.Type.I32, (short)13);
            oprot.writeI32(getI32Field().get());
            oprot.writeFieldEnd();
        }

        if (getI64Field().isPresent()) {
            oprot.writeFieldBegin("i64_field", org.thryft.protocol.Type.I64, (short)14);
            oprot.writeI64(getI64Field().get());
            oprot.writeFieldEnd();
        }

        if (getI8Field().isPresent()) {
            oprot.writeFieldBegin("i8_field", org.thryft.protocol.Type.BYTE, (short)11);
            oprot.writeByte(getI8Field().get());
            oprot.writeFieldEnd();
        }

        if (getStringField().isPresent()) {
            oprot.writeFieldBegin("string_field", org.thryft.protocol.Type.STRING, (short)18);
            oprot.writeString(getStringField().get());
            oprot.writeFieldEnd();
        }

        if (getStringListField().isPresent()) {
            oprot.writeFieldBegin("string_list_field", org.thryft.protocol.Type.LIST, (short)15);
            oprot.writeListBegin(org.thryft.protocol.Type.STRING, getStringListField().get().size());
            for (final String _iter0 : getStringListField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeListEnd();
            oprot.writeFieldEnd();
        }

        if (getStringSetField().isPresent()) {
            oprot.writeFieldBegin("string_set_field", org.thryft.protocol.Type.SET, (short)17);
            oprot.writeSetBegin(org.thryft.protocol.Type.STRING, getStringSetField().get().size());
            for (final String _iter0 : getStringSetField().get()) {
                oprot.writeString(_iter0);
            }
            oprot.writeSetEnd();
            oprot.writeFieldEnd();
        }

        if (getStringStringMapField().isPresent()) {
            oprot.writeFieldBegin("string_string_map_field", org.thryft.protocol.Type.MAP, (short)16);
            oprot.writeMapBegin(org.thryft.protocol.Type.STRING, org.thryft.protocol.Type.STRING, getStringStringMapField().get().size());
            for (com.google.common.collect.ImmutableMap.Entry<String, String> _iter0 : getStringStringMapField().get().entrySet()) {
                oprot.writeString(_iter0.getKey());
                oprot.writeString(_iter0.getValue());
            }
            oprot.writeMapEnd();
            oprot.writeFieldEnd();
        }

        if (getStructField().isPresent()) {
            oprot.writeFieldBegin("struct_field", org.thryft.protocol.Type.STRUCT, (short)19);
            getStructField().get().writeAsStruct(oprot);
            oprot.writeFieldEnd();
        }

        if (getU32Field().isPresent()) {
            oprot.writeFieldBegin("u32_field", org.thryft.protocol.Type.I32, (short)20);
            oprot.writeU32(getU32Field().get());
            oprot.writeFieldEnd();
        }

        if (getU64Field().isPresent()) {
            oprot.writeFieldBegin("u64_field", org.thryft.protocol.Type.I64, (short)21);
            oprot.writeU64(getU64Field().get());
            oprot.writeFieldEnd();
        }

        if (getUriField().isPresent()) {
            oprot.writeFieldBegin("uri_field", org.thryft.protocol.Type.STRING, (short)22);
            oprot.writeString(getUriField().get().toString());
            oprot.writeFieldEnd();
        }

        if (getUrlField().isPresent()) {
            oprot.writeFieldBegin("url_field", org.thryft.protocol.Type.STRING, (short)23);
            oprot.writeString(getUrlField().get().toString());
            oprot.writeFieldEnd();
        }

        if (getVariantField().isPresent()) {
            oprot.writeFieldBegin("variant_field", org.thryft.protocol.Type.STRUCT, (short)24);
            oprot.writeVariant(getVariantField().get());
            oprot.writeFieldEnd();
        }

        oprot.writeFieldStop();
    }

    private final int requiredI32Field;

    private final String requiredStringField;

    private final com.google.common.base.Optional<byte[]> binaryField;

    private final com.google.common.base.Optional<Boolean> boolField;

    private final com.google.common.base.Optional<java.util.Date> dateTimeField;

    private final com.google.common.base.Optional<java.math.BigDecimal> decimalField;

    private final com.google.common.base.Optional<Double> doubleField;

    private final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField;

    private final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;

    private final com.google.common.base.Optional<Float> floatField;

    private final com.google.common.base.Optional<Short> i16Field;

    private final com.google.common.base.Optional<Integer> i32Field;

    private final com.google.common.base.Optional<Long> i64Field;

    private final com.google.common.base.Optional<Byte> i8Field;

    private final com.google.common.base.Optional<String> stringField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;

    private final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField;

    private final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field;

    private final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field;

    private final com.google.common.base.Optional<org.thryft.native_.Uri> uriField;

    private final com.google.common.base.Optional<org.thryft.native_.Url> urlField;

    private final com.google.common.base.Optional<java.lang.Object> variantField;
}
