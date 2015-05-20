package org.thryft.protocol.test;

public class ProtocolTestStruct implements org.thryft.Struct, java.lang.Comparable<ProtocolTestStruct> {
    public static class Builder {
        public Builder() {
            requiredI32Field = 0;
            requiredStringField = null;
            binaryField = com.google.common.base.Optional.absent();
            boolField = com.google.common.base.Optional.absent();
            dateTimeField = com.google.common.base.Optional.absent();
            decimalField = com.google.common.base.Optional.absent();
            emailAddressField = com.google.common.base.Optional.absent();
            enumField = com.google.common.base.Optional.absent();
            floatField = com.google.common.base.Optional.absent();
            i8Field = com.google.common.base.Optional.absent();
            i16Field = com.google.common.base.Optional.absent();
            i32Field = com.google.common.base.Optional.absent();
            i64Field = com.google.common.base.Optional.absent();
            stringListField = com.google.common.base.Optional.absent();
            stringStringMapField = com.google.common.base.Optional.absent();
            stringSetField = com.google.common.base.Optional.absent();
            stringField = com.google.common.base.Optional.absent();
            structField = com.google.common.base.Optional.absent();
            u32Field = com.google.common.base.Optional.absent();
            u64Field = com.google.common.base.Optional.absent();
            uriField = com.google.common.base.Optional.absent();
            urlField = com.google.common.base.Optional.absent();
            variantField = com.google.common.base.Optional.absent();
        }

        public Builder(final ProtocolTestStruct other) {
            this.requiredI32Field = other.getRequiredI32Field();
            this.requiredStringField = other.getRequiredStringField();
            this.binaryField = other.getBinaryField();
            this.boolField = other.getBoolField();
            this.dateTimeField = other.getDateTimeField();
            this.decimalField = other.getDecimalField();
            this.emailAddressField = other.getEmailAddressField();
            this.enumField = other.getEnumField();
            this.floatField = other.getFloatField();
            this.i8Field = other.getI8Field();
            this.i16Field = other.getI16Field();
            this.i32Field = other.getI32Field();
            this.i64Field = other.getI64Field();
            this.stringListField = other.getStringListField();
            this.stringStringMapField = other.getStringStringMapField();
            this.stringSetField = other.getStringSetField();
            this.stringField = other.getStringField();
            this.structField = other.getStructField();
            this.u32Field = other.getU32Field();
            this.u64Field = other.getU64Field();
            this.uriField = other.getUriField();
            this.urlField = other.getUrlField();
            this.variantField = other.getVariantField();
        }

        protected ProtocolTestStruct _build(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Float> floatField, final com.google.common.base.Optional<Byte> i8Field, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, final com.google.common.base.Optional<org.thryft.native_.Uri> uriField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, final com.google.common.base.Optional<java.lang.Object> variantField) {
            return new ProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, emailAddressField, enumField, floatField, i8Field, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, structField, u32Field, u64Field, uriField, urlField, variantField);
        }

        public ProtocolTestStruct build() {
            return _build(com.google.common.base.Preconditions.checkNotNull(requiredI32Field, "org.thryft.protocol.test.ProtocolTestStruct: missing requiredI32Field"), com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.ProtocolTestStruct: missing requiredStringField"), com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.ProtocolTestStruct: missing binaryField"), com.google.common.base.Preconditions.checkNotNull(boolField, "org.thryft.protocol.test.ProtocolTestStruct: missing boolField"), com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.ProtocolTestStruct: missing dateTimeField"), com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.ProtocolTestStruct: missing decimalField"), com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.ProtocolTestStruct: missing emailAddressField"), com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.ProtocolTestStruct: missing enumField"), com.google.common.base.Preconditions.checkNotNull(floatField, "org.thryft.protocol.test.ProtocolTestStruct: missing floatField"), com.google.common.base.Preconditions.checkNotNull(i8Field, "org.thryft.protocol.test.ProtocolTestStruct: missing i8Field"), com.google.common.base.Preconditions.checkNotNull(i16Field, "org.thryft.protocol.test.ProtocolTestStruct: missing i16Field"), com.google.common.base.Preconditions.checkNotNull(i32Field, "org.thryft.protocol.test.ProtocolTestStruct: missing i32Field"), com.google.common.base.Preconditions.checkNotNull(i64Field, "org.thryft.protocol.test.ProtocolTestStruct: missing i64Field"), com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringListField"), com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringStringMapField"), com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringSetField"), com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringField"), com.google.common.base.Preconditions.checkNotNull(structField, "org.thryft.protocol.test.ProtocolTestStruct: missing structField"), com.google.common.base.Preconditions.checkNotNull(u32Field, "org.thryft.protocol.test.ProtocolTestStruct: missing u32Field"), com.google.common.base.Preconditions.checkNotNull(u64Field, "org.thryft.protocol.test.ProtocolTestStruct: missing u64Field"), com.google.common.base.Preconditions.checkNotNull(uriField, "org.thryft.protocol.test.ProtocolTestStruct: missing uriField"), com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.ProtocolTestStruct: missing urlField"), com.google.common.base.Preconditions.checkNotNull(variantField, "org.thryft.protocol.test.ProtocolTestStruct: missing variantField"));
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
                emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
            }
            if (__list.getSize() > 7) {
                try {
                    enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                } catch (final IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 8) {
                try {
                    floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 9) {
                try {
                    i8Field = com.google.common.base.Optional.of(iprot.readByte());
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
            if (__list.getSize() > 14) {
                stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                    @Override
                    public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
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
            if (__list.getSize() > 15) {
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
            if (__list.getSize() > 16) {
                stringField = com.google.common.base.Optional.of(iprot.readString());
            }
            if (__list.getSize() > 17) {
                structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
            }
            if (__list.getSize() > 18) {
                try {
                    u32Field = com.google.common.base.Optional.of(iprot.readU32());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 19) {
                try {
                    u64Field = com.google.common.base.Optional.of(iprot.readU64());
                } catch (final NumberFormatException e) {
                }
            }
            if (__list.getSize() > 20) {
                try {
                    uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 21) {
                try {
                    urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            }
            if (__list.getSize() > 22) {
                variantField = com.google.common.base.Optional.of(iprot.readVariant());
            }
            iprot.readListEnd();
            return this;
        }

        public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
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
                } else if (ifield.getName().equals("date_time_field")) {
                    try {
                        dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                    } catch (final IllegalArgumentException e) {
                    }
                } else if (ifield.getName().equals("decimal_field")) {
                    try {
                        decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("email_address_field")) {
                    emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
                } else if (ifield.getName().equals("enum_field")) {
                    try {
                        enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                    } catch (final IllegalArgumentException e) {
                    }
                } else if (ifield.getName().equals("float_field")) {
                    try {
                        floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("i8_field")) {
                    try {
                        i8Field = com.google.common.base.Optional.of(iprot.readByte());
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("i16_field")) {
                    try {
                        i16Field = com.google.common.base.Optional.of(iprot.readI16());
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("i32_field")) {
                    try {
                        i32Field = com.google.common.base.Optional.of(iprot.readI32());
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("i64_field")) {
                    try {
                        i64Field = com.google.common.base.Optional.of(iprot.readI64());
                    } catch (final NumberFormatException e) {
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
                        public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
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
                } else if (ifield.getName().equals("struct_field")) {
                    structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
                } else if (ifield.getName().equals("u32_field")) {
                    try {
                        u32Field = com.google.common.base.Optional.of(iprot.readU32());
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("u64_field")) {
                    try {
                        u64Field = com.google.common.base.Optional.of(iprot.readU64());
                    } catch (final NumberFormatException e) {
                    }
                } else if (ifield.getName().equals("uri_field")) {
                    try {
                        uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                    } catch (final java.lang.IllegalArgumentException e) {
                    }
                } else if (ifield.getName().equals("url_field")) {
                    try {
                        urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                    } catch (final java.lang.IllegalArgumentException e) {
                    }
                } else if (ifield.getName().equals("variant_field")) {
                    variantField = com.google.common.base.Optional.of(iprot.readVariant());
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

        public Builder setBoolField(final com.google.common.base.Optional<Boolean> boolField) {
            this.boolField = com.google.common.base.Preconditions.checkNotNull(boolField);
            return this;
        }

        public Builder setBoolField(@javax.annotation.Nullable final Boolean boolField) {
            this.boolField = com.google.common.base.Optional.fromNullable(boolField);
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

        public Builder setFloatField(final com.google.common.base.Optional<Float> floatField) {
            this.floatField = com.google.common.base.Preconditions.checkNotNull(floatField);
            return this;
        }

        public Builder setFloatField(@javax.annotation.Nullable final Float floatField) {
            this.floatField = com.google.common.base.Optional.fromNullable(floatField);
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

        public Builder setI8Field(final com.google.common.base.Optional<Byte> i8Field) {
            this.i8Field = com.google.common.base.Preconditions.checkNotNull(i8Field);
            return this;
        }

        public Builder setI8Field(@javax.annotation.Nullable final Byte i8Field) {
            this.i8Field = com.google.common.base.Optional.fromNullable(i8Field);
            return this;
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
            if (other.getEmailAddressField().isPresent()) {
                setEmailAddressField(other.getEmailAddressField());
            }
            if (other.getEnumField().isPresent()) {
                setEnumField(other.getEnumField());
            }
            if (other.getFloatField().isPresent()) {
                setFloatField(other.getFloatField());
            }
            if (other.getI8Field().isPresent()) {
                setI8Field(other.getI8Field());
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

        public Builder setStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) {
            this.structField = com.google.common.base.Preconditions.checkNotNull(structField);
            return this;
        }

        public Builder setStructField(@javax.annotation.Nullable final org.thryft.protocol.test.NestedProtocolTestStruct structField) {
            this.structField = com.google.common.base.Optional.fromNullable(structField);
            return this;
        }

        public Builder setU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) {
            this.u32Field = com.google.common.base.Preconditions.checkNotNull(u32Field);
            return this;
        }

        public Builder setU32Field(@javax.annotation.Nullable final com.google.common.primitives.UnsignedInteger u32Field) {
            this.u32Field = com.google.common.base.Optional.fromNullable(u32Field);
            return this;
        }

        public Builder setU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) {
            this.u64Field = com.google.common.base.Preconditions.checkNotNull(u64Field);
            return this;
        }

        public Builder setU64Field(@javax.annotation.Nullable final com.google.common.primitives.UnsignedLong u64Field) {
            this.u64Field = com.google.common.base.Optional.fromNullable(u64Field);
            return this;
        }

        public Builder setUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) {
            this.uriField = com.google.common.base.Preconditions.checkNotNull(uriField);
            return this;
        }

        public Builder setUriField(@javax.annotation.Nullable final org.thryft.native_.Uri uriField) {
            this.uriField = com.google.common.base.Optional.fromNullable(uriField);
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

        public Builder setVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) {
            this.variantField = com.google.common.base.Preconditions.checkNotNull(variantField);
            return this;
        }

        public Builder setVariantField(@javax.annotation.Nullable final java.lang.Object variantField) {
            this.variantField = com.google.common.base.Optional.fromNullable(variantField);
            return this;
        }

        public Builder set(final String name, @javax.annotation.Nullable final Object value) {
            com.google.common.base.Preconditions.checkNotNull(name);

            switch (name.toLowerCase()) {
            case "required_i32_field": setRequiredI32Field((int)value); return this;
            case "required_string_field": setRequiredStringField((String)value); return this;
            case "binary_field": setBinaryField((byte[])value); return this;
            case "bool_field": setBoolField((Boolean)value); return this;
            case "date_time_field": setDateTimeField((java.util.Date)value); return this;
            case "decimal_field": setDecimalField((java.math.BigDecimal)value); return this;
            case "email_address_field": setEmailAddressField((org.thryft.native_.EmailAddress)value); return this;
            case "enum_field": setEnumField((org.thryft.protocol.test.ProtocolTestEnum)value); return this;
            case "float_field": setFloatField((Float)value); return this;
            case "i8_field": setI8Field((Byte)value); return this;
            case "i16_field": setI16Field((Short)value); return this;
            case "i32_field": setI32Field((Integer)value); return this;
            case "i64_field": setI64Field((Long)value); return this;
            case "string_field": setStringField((String)value); return this;
            case "struct_field": setStructField((org.thryft.protocol.test.NestedProtocolTestStruct)value); return this;
            case "u32_field": setU32Field((com.google.common.primitives.UnsignedInteger)value); return this;
            case "u64_field": setU64Field((com.google.common.primitives.UnsignedLong)value); return this;
            case "uri_field": setUriField((org.thryft.native_.Uri)value); return this;
            case "url_field": setUrlField((org.thryft.native_.Url)value); return this;
            case "variant_field": setVariantField(value); return this;
            default:
                throw new IllegalArgumentException(name);
            }
        }

        private Integer requiredI32Field;
        private String requiredStringField;
        private com.google.common.base.Optional<byte[]> binaryField;
        private com.google.common.base.Optional<Boolean> boolField;
        private com.google.common.base.Optional<java.util.Date> dateTimeField;
        private com.google.common.base.Optional<java.math.BigDecimal> decimalField;
        private com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField;
        private com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;
        private com.google.common.base.Optional<Float> floatField;
        private com.google.common.base.Optional<Byte> i8Field;
        private com.google.common.base.Optional<Short> i16Field;
        private com.google.common.base.Optional<Integer> i32Field;
        private com.google.common.base.Optional<Long> i64Field;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;
        private com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;
        private com.google.common.base.Optional<String> stringField;
        private com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField;
        private com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field;
        private com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field;
        private com.google.common.base.Optional<org.thryft.native_.Uri> uriField;
        private com.google.common.base.Optional<org.thryft.native_.Url> urlField;
        private com.google.common.base.Optional<java.lang.Object> variantField;
    }

    public ProtocolTestStruct(final ProtocolTestStruct other) {
        this(other.getRequiredI32Field(), other.getRequiredStringField(), other.getBinaryField(), other.getBoolField(), other.getDateTimeField(), other.getDecimalField(), other.getEmailAddressField(), other.getEnumField(), other.getFloatField(), other.getI8Field(), other.getI16Field(), other.getI32Field(), other.getI64Field(), other.getStringListField(), other.getStringStringMapField(), other.getStringSetField(), other.getStringField(), other.getStructField(), other.getU32Field(), other.getU64Field(), other.getUriField(), other.getUrlField(), other.getVariantField());
    }

    public ProtocolTestStruct(final int requiredI32Field, final String requiredStringField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.ProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Optional.absent();
        this.boolField = com.google.common.base.Optional.absent();
        this.dateTimeField = com.google.common.base.Optional.absent();
        this.decimalField = com.google.common.base.Optional.absent();
        this.emailAddressField = com.google.common.base.Optional.absent();
        this.enumField = com.google.common.base.Optional.absent();
        this.floatField = com.google.common.base.Optional.absent();
        this.i8Field = com.google.common.base.Optional.absent();
        this.i16Field = com.google.common.base.Optional.absent();
        this.i32Field = com.google.common.base.Optional.absent();
        this.i64Field = com.google.common.base.Optional.absent();
        this.stringListField = com.google.common.base.Optional.absent();
        this.stringStringMapField = com.google.common.base.Optional.absent();
        this.stringSetField = com.google.common.base.Optional.absent();
        this.stringField = com.google.common.base.Optional.absent();
        this.structField = com.google.common.base.Optional.absent();
        this.u32Field = com.google.common.base.Optional.absent();
        this.u64Field = com.google.common.base.Optional.absent();
        this.uriField = com.google.common.base.Optional.absent();
        this.urlField = com.google.common.base.Optional.absent();
        this.variantField = com.google.common.base.Optional.absent();
    }

    public ProtocolTestStruct(final Integer requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Float> floatField, final com.google.common.base.Optional<Byte> i8Field, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, final com.google.common.base.Optional<org.thryft.native_.Uri> uriField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, final com.google.common.base.Optional<java.lang.Object> variantField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.ProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.ProtocolTestStruct: missing binaryField");
        this.boolField = boolField;
        this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.ProtocolTestStruct: missing dateTimeField");
        this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.ProtocolTestStruct: missing decimalField");
        this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.ProtocolTestStruct: missing emailAddressField");
        this.enumField = com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.ProtocolTestStruct: missing enumField");
        this.floatField = floatField;
        this.i8Field = i8Field;
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.stringListField = com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringListField");
        this.stringStringMapField = com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringStringMapField");
        this.stringSetField = com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringSetField");
        this.stringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringField"), String.class, "org.thryft.protocol.test.ProtocolTestStruct: stringField is empty");
        this.structField = com.google.common.base.Preconditions.checkNotNull(structField, "org.thryft.protocol.test.ProtocolTestStruct: missing structField");
        this.u32Field = com.google.common.base.Preconditions.checkNotNull(u32Field, "org.thryft.protocol.test.ProtocolTestStruct: missing u32Field");
        this.u64Field = com.google.common.base.Preconditions.checkNotNull(u64Field, "org.thryft.protocol.test.ProtocolTestStruct: missing u64Field");
        this.uriField = com.google.common.base.Preconditions.checkNotNull(uriField, "org.thryft.protocol.test.ProtocolTestStruct: missing uriField");
        this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.ProtocolTestStruct: missing urlField");
        this.variantField = com.google.common.base.Preconditions.checkNotNull(variantField, "org.thryft.protocol.test.ProtocolTestStruct: missing variantField");
    }

    public ProtocolTestStruct(final int requiredI32Field, final String requiredStringField, final @javax.annotation.Nullable byte[] binaryField, final @javax.annotation.Nullable Boolean boolField, final @javax.annotation.Nullable java.util.Date dateTimeField, final @javax.annotation.Nullable java.math.BigDecimal decimalField, final @javax.annotation.Nullable org.thryft.native_.EmailAddress emailAddressField, final @javax.annotation.Nullable org.thryft.protocol.test.ProtocolTestEnum enumField, final @javax.annotation.Nullable Float floatField, final @javax.annotation.Nullable Byte i8Field, final @javax.annotation.Nullable Short i16Field, final @javax.annotation.Nullable Integer i32Field, final @javax.annotation.Nullable Long i64Field, final @javax.annotation.Nullable com.google.common.collect.ImmutableList<String> stringListField, final @javax.annotation.Nullable com.google.common.collect.ImmutableMap<String, String> stringStringMapField, final @javax.annotation.Nullable com.google.common.collect.ImmutableSet<String> stringSetField, final @javax.annotation.Nullable String stringField, final @javax.annotation.Nullable org.thryft.protocol.test.NestedProtocolTestStruct structField, final @javax.annotation.Nullable com.google.common.primitives.UnsignedInteger u32Field, final @javax.annotation.Nullable com.google.common.primitives.UnsignedLong u64Field, final @javax.annotation.Nullable org.thryft.native_.Uri uriField, final @javax.annotation.Nullable org.thryft.native_.Url urlField, final @javax.annotation.Nullable java.lang.Object variantField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.ProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Optional.fromNullable(binaryField);
        this.boolField = com.google.common.base.Optional.fromNullable(boolField);
        this.dateTimeField = com.google.common.base.Optional.fromNullable(dateTimeField);
        this.decimalField = com.google.common.base.Optional.fromNullable(decimalField);
        this.emailAddressField = com.google.common.base.Optional.fromNullable(emailAddressField);
        this.enumField = com.google.common.base.Optional.fromNullable(enumField);
        this.floatField = com.google.common.base.Optional.fromNullable(floatField);
        this.i8Field = com.google.common.base.Optional.fromNullable(i8Field);
        this.i16Field = com.google.common.base.Optional.fromNullable(i16Field);
        this.i32Field = com.google.common.base.Optional.fromNullable(i32Field);
        this.i64Field = com.google.common.base.Optional.fromNullable(i64Field);
        this.stringListField = com.google.common.base.Optional.fromNullable(stringListField);
        this.stringStringMapField = com.google.common.base.Optional.fromNullable(stringStringMapField);
        this.stringSetField = com.google.common.base.Optional.fromNullable(stringSetField);
        this.stringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Optional.fromNullable(stringField), String.class, "org.thryft.protocol.test.ProtocolTestStruct: stringField is empty");
        this.structField = com.google.common.base.Optional.fromNullable(structField);
        this.u32Field = com.google.common.base.Optional.fromNullable(u32Field);
        this.u64Field = com.google.common.base.Optional.fromNullable(u64Field);
        this.uriField = com.google.common.base.Optional.fromNullable(uriField);
        this.urlField = com.google.common.base.Optional.fromNullable(urlField);
        this.variantField = com.google.common.base.Optional.fromNullable(variantField);
    }

    public ProtocolTestStruct(final int requiredI32Field, final String requiredStringField, final com.google.common.base.Optional<byte[]> binaryField, final com.google.common.base.Optional<Boolean> boolField, final com.google.common.base.Optional<java.util.Date> dateTimeField, final com.google.common.base.Optional<java.math.BigDecimal> decimalField, final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField, final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField, final com.google.common.base.Optional<Float> floatField, final com.google.common.base.Optional<Byte> i8Field, final com.google.common.base.Optional<Short> i16Field, final com.google.common.base.Optional<Integer> i32Field, final com.google.common.base.Optional<Long> i64Field, final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField, final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField, final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField, final com.google.common.base.Optional<String> stringField, final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField, final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field, final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field, final com.google.common.base.Optional<org.thryft.native_.Uri> uriField, final com.google.common.base.Optional<org.thryft.native_.Url> urlField, final com.google.common.base.Optional<java.lang.Object> variantField) {
        this.requiredI32Field = requiredI32Field;
        this.requiredStringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(requiredStringField, "org.thryft.protocol.test.ProtocolTestStruct: missing requiredStringField"), "org.thryft.protocol.test.ProtocolTestStruct: requiredStringField is empty");
        this.binaryField = com.google.common.base.Preconditions.checkNotNull(binaryField, "org.thryft.protocol.test.ProtocolTestStruct: missing binaryField");
        this.boolField = boolField;
        this.dateTimeField = com.google.common.base.Preconditions.checkNotNull(dateTimeField, "org.thryft.protocol.test.ProtocolTestStruct: missing dateTimeField");
        this.decimalField = com.google.common.base.Preconditions.checkNotNull(decimalField, "org.thryft.protocol.test.ProtocolTestStruct: missing decimalField");
        this.emailAddressField = com.google.common.base.Preconditions.checkNotNull(emailAddressField, "org.thryft.protocol.test.ProtocolTestStruct: missing emailAddressField");
        this.enumField = com.google.common.base.Preconditions.checkNotNull(enumField, "org.thryft.protocol.test.ProtocolTestStruct: missing enumField");
        this.floatField = floatField;
        this.i8Field = i8Field;
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.stringListField = com.google.common.base.Preconditions.checkNotNull(stringListField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringListField");
        this.stringStringMapField = com.google.common.base.Preconditions.checkNotNull(stringStringMapField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringStringMapField");
        this.stringSetField = com.google.common.base.Preconditions.checkNotNull(stringSetField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringSetField");
        this.stringField = org.thryft.Preconditions.checkNotEmpty(com.google.common.base.Preconditions.checkNotNull(stringField, "org.thryft.protocol.test.ProtocolTestStruct: missing stringField"), String.class, "org.thryft.protocol.test.ProtocolTestStruct: stringField is empty");
        this.structField = com.google.common.base.Preconditions.checkNotNull(structField, "org.thryft.protocol.test.ProtocolTestStruct: missing structField");
        this.u32Field = com.google.common.base.Preconditions.checkNotNull(u32Field, "org.thryft.protocol.test.ProtocolTestStruct: missing u32Field");
        this.u64Field = com.google.common.base.Preconditions.checkNotNull(u64Field, "org.thryft.protocol.test.ProtocolTestStruct: missing u64Field");
        this.uriField = com.google.common.base.Preconditions.checkNotNull(uriField, "org.thryft.protocol.test.ProtocolTestStruct: missing uriField");
        this.urlField = com.google.common.base.Preconditions.checkNotNull(urlField, "org.thryft.protocol.test.ProtocolTestStruct: missing urlField");
        this.variantField = com.google.common.base.Preconditions.checkNotNull(variantField, "org.thryft.protocol.test.ProtocolTestStruct: missing variantField");
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(final ProtocolTestStruct other) {
        return new Builder(other);
    }

    @Override
    public int compareTo(final ProtocolTestStruct other) {
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
                result = this.boolField.get().compareTo(other.boolField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.boolField.isPresent()) {
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

        if (this.floatField.isPresent()) {
            if (other.floatField.isPresent()) {
                result = this.floatField.get().compareTo(other.floatField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.floatField.isPresent()) {
            return -1;
        }

        if (this.i8Field.isPresent()) {
            if (other.i8Field.isPresent()) {
                result = Byte.compare(this.i8Field.get(), other.i8Field.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.i8Field.isPresent()) {
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
                result = new java.util.Comparator<com.google.common.collect.ImmutableList<String>>() {
                    public int compare(final com.google.common.collect.ImmutableList<String> left, final com.google.common.collect.ImmutableList<String> right) {
                        int result = ((Integer) left.size()).compareTo(right.size());
                        if (result != 0) {
                            return result;
                        }

                        final java.util.List<String> leftSortedList = com.google.common.collect.Lists
                                .newArrayList(left);
                        java.util.Collections.sort(leftSortedList);
                        final java.util.Iterator<String> leftI = leftSortedList.iterator();

                        final java.util.List<String> rightSortedList = com.google.common.collect.Lists
                                .newArrayList(right);
                        java.util.Collections.sort(rightSortedList);
                        final java.util.Iterator<String> rightI = leftSortedList.iterator();

                        while (leftI.hasNext()) {
                            final String leftElement = leftI.next();
                            final String rightElement = rightI.next();

                            result =
                                leftElement.compareTo(rightElement);
                            if (result != 0) {
                                return result;
                            }
                        }

                        return 0;
                    }
                }.compare(this.stringListField.get(), other.stringListField.get());
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
                result = new java.util.Comparator<com.google.common.collect.ImmutableMap<String, String>>() {
                    public int compare(final com.google.common.collect.ImmutableMap<String, String> left, final com.google.common.collect.ImmutableMap<String, String> right) {
                        int result = ((Integer) left.size()).compareTo(right.size());
                        if (result != 0) {
                            return result;
                        }

                        // Compare keys
                        final java.util.List<String> leftSortedKeySet = com.google.common.collect.Lists
                                .newArrayList(left.keySet());
                        java.util.Collections.sort(leftSortedKeySet);
                        final java.util.Iterator<String> leftKeyI = leftSortedKeySet.iterator();

                        final java.util.List<String> rightSortedKeySet = com.google.common.collect.Lists
                                .newArrayList(right.keySet());
                        java.util.Collections.sort(rightSortedKeySet);
                        final java.util.Iterator<String> rightKeyI = leftSortedKeySet.iterator();

                        while (leftKeyI.hasNext()) {
                            final String leftKey = leftKeyI.next();
                            final String rightKey = rightKeyI.next();

                            result = leftKey.compareTo(rightKey);
                            if (result != 0) {
                                return result;
                            }
                        }

                        // Compare values
                        for (final java.util.Map.Entry<String, String> leftEntry : left.entrySet()) {
                            final String leftValue = leftEntry.getValue();
                            final String rightValue = right.get(leftEntry.getKey());

                            result =
                                leftValue.compareTo(rightValue);
                            if (result != 0) {
                                return result;
                            }
                        }

                        return 0;
                    }
                }.compare(this.stringStringMapField.get(), other.stringStringMapField.get());
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
                result = new java.util.Comparator<com.google.common.collect.ImmutableSet<String>>() {
                    public int compare(final com.google.common.collect.ImmutableSet<String> left, final com.google.common.collect.ImmutableSet<String> right) {
                        int result = ((Integer) left.size()).compareTo(right.size());
                        if (result != 0) {
                            return result;
                        }

                        final java.util.List<String> leftSortedList = com.google.common.collect.Lists
                                .newArrayList(left);
                        java.util.Collections.sort(leftSortedList);
                        final java.util.Iterator<String> leftI = leftSortedList.iterator();

                        final java.util.List<String> rightSortedList = com.google.common.collect.Lists
                                .newArrayList(right);
                        java.util.Collections.sort(rightSortedList);
                        final java.util.Iterator<String> rightI = leftSortedList.iterator();

                        while (leftI.hasNext()) {
                            final String leftElement = leftI.next();
                            final String rightElement = rightI.next();

                            result =
                                leftElement.compareTo(rightElement);
                            if (result != 0) {
                                return result;
                            }
                        }

                        return 0;
                    }
                }.compare(this.stringSetField.get(), other.stringSetField.get());
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

        if (this.structField.isPresent()) {
            if (other.structField.isPresent()) {
                result = this.structField.get().compareTo(other.structField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.structField.isPresent()) {
            return -1;
        }

        if (this.u32Field.isPresent()) {
            if (other.u32Field.isPresent()) {
                result = this.u32Field.get().compareTo(other.u32Field.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.u32Field.isPresent()) {
            return -1;
        }

        if (this.u64Field.isPresent()) {
            if (other.u64Field.isPresent()) {
                result = this.u64Field.get().compareTo(other.u64Field.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.u64Field.isPresent()) {
            return -1;
        }

        if (this.uriField.isPresent()) {
            if (other.uriField.isPresent()) {
                result = this.uriField.get().compareTo(other.uriField.get());
                if (result != 0) {
                    return result;
                }
            } else {
                return 1;
            }
        } else if (other.uriField.isPresent()) {
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
        } else if (!(otherObject instanceof ProtocolTestStruct)) {
            return false;
        }

        final ProtocolTestStruct other = (ProtocolTestStruct)otherObject;
        return
            getRequiredI32Field() == other.getRequiredI32Field() &&
            getRequiredStringField().equals(other.getRequiredStringField()) &&
            getBinaryField().equals(other.getBinaryField()) &&
            getBoolField().equals(other.getBoolField()) &&
            getDateTimeField().equals(other.getDateTimeField()) &&
            getDecimalField().equals(other.getDecimalField()) &&
            getEmailAddressField().equals(other.getEmailAddressField()) &&
            getEnumField().equals(other.getEnumField()) &&
            getFloatField().equals(other.getFloatField()) &&
            getI8Field().equals(other.getI8Field()) &&
            getI16Field().equals(other.getI16Field()) &&
            getI32Field().equals(other.getI32Field()) &&
            getI64Field().equals(other.getI64Field()) &&
            getStringListField().equals(other.getStringListField()) &&
            getStringStringMapField().equals(other.getStringStringMapField()) &&
            getStringSetField().equals(other.getStringSetField()) &&
            getStringField().equals(other.getStringField()) &&
            getStructField().equals(other.getStructField()) &&
            getU32Field().equals(other.getU32Field()) &&
            getU64Field().equals(other.getU64Field()) &&
            getUriField().equals(other.getUriField()) &&
            getUrlField().equals(other.getUrlField()) &&
            getVariantField().equals(other.getVariantField());
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
        } else if (fieldName.equals("date_time_field")) {
            return getDateTimeField();
        } else if (fieldName.equals("decimal_field")) {
            return getDecimalField();
        } else if (fieldName.equals("email_address_field")) {
            return getEmailAddressField();
        } else if (fieldName.equals("enum_field")) {
            return getEnumField();
        } else if (fieldName.equals("float_field")) {
            return getFloatField();
        } else if (fieldName.equals("i8_field")) {
            return getI8Field();
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
        } else if (fieldName.equals("struct_field")) {
            return getStructField();
        } else if (fieldName.equals("u32_field")) {
            return getU32Field();
        } else if (fieldName.equals("u64_field")) {
            return getU64Field();
        } else if (fieldName.equals("uri_field")) {
            return getUriField();
        } else if (fieldName.equals("url_field")) {
            return getUrlField();
        } else if (fieldName.equals("variant_field")) {
            return getVariantField();
        }
        throw new IllegalArgumentException(fieldName);
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
        if (getEmailAddressField().isPresent()) {
            hashCode = 31 * hashCode + getEmailAddressField().get().hashCode();
        }
        if (getEnumField().isPresent()) {
            hashCode = 31 * hashCode + getEnumField().get().ordinal();
        }
        if (getFloatField().isPresent()) {
            hashCode = 31 * hashCode + ((int)(Double.doubleToLongBits(getFloatField().get()) ^ (Double.doubleToLongBits(getFloatField().get()) >>> 32)));
        }
        if (getI8Field().isPresent()) {
            hashCode = 31 * hashCode + getI8Field().get().hashCode();
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

    public static ProtocolTestStruct readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Float> floatField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Byte> i8Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.Uri> uriField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.lang.Object> variantField = com.google.common.base.Optional.absent();

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
            emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
        }
        if (__list.getSize() > 7) {
            try {
                enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
            } catch (final IllegalArgumentException e) {
            }
        }
        if (__list.getSize() > 8) {
            try {
                floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 9) {
            try {
                i8Field = com.google.common.base.Optional.of(iprot.readByte());
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
        if (__list.getSize() > 14) {
            stringStringMapField = com.google.common.base.Optional.of((new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                @Override
                public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
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
        if (__list.getSize() > 15) {
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
        if (__list.getSize() > 16) {
            stringField = com.google.common.base.Optional.of(iprot.readString());
        }
        if (__list.getSize() > 17) {
            structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
        }
        if (__list.getSize() > 18) {
            try {
                u32Field = com.google.common.base.Optional.of(iprot.readU32());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 19) {
            try {
                u64Field = com.google.common.base.Optional.of(iprot.readU64());
            } catch (final NumberFormatException e) {
            }
        }
        if (__list.getSize() > 20) {
            try {
                uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
            } catch (final java.lang.IllegalArgumentException e) {
            }
        }
        if (__list.getSize() > 21) {
            try {
                urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
            } catch (final java.lang.IllegalArgumentException e) {
            }
        }
        if (__list.getSize() > 22) {
            variantField = com.google.common.base.Optional.of(iprot.readVariant());
        }
        iprot.readListEnd();
        return new ProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, emailAddressField, enumField, floatField, i8Field, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, structField, u32Field, u64Field, uriField, urlField, variantField);
    }

    public static ProtocolTestStruct readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        int requiredI32Field = 0;
        String requiredStringField = null;
        com.google.common.base.Optional<byte[]> binaryField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Boolean> boolField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.util.Date> dateTimeField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.math.BigDecimal> decimalField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Float> floatField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Byte> i8Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Short> i16Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Integer> i32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<Long> i64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<String> stringField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.Uri> uriField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<org.thryft.native_.Url> urlField = com.google.common.base.Optional.absent();
        com.google.common.base.Optional<java.lang.Object> variantField = com.google.common.base.Optional.absent();

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
            } else if (ifield.getName().equals("date_time_field")) {
                try {
                    dateTimeField = com.google.common.base.Optional.of(iprot.readDateTime());
                } catch (final IllegalArgumentException e) {
                }
            } else if (ifield.getName().equals("decimal_field")) {
                try {
                    decimalField = com.google.common.base.Optional.of(iprot.readDecimal());
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("email_address_field")) {
                emailAddressField = com.google.common.base.Optional.of(new org.thryft.native_.EmailAddress(iprot.readString()));
            } else if (ifield.getName().equals("enum_field")) {
                try {
                    enumField = com.google.common.base.Optional.of(iprot.readEnum(org.thryft.protocol.test.ProtocolTestEnum.class));
                } catch (final IllegalArgumentException e) {
                }
            } else if (ifield.getName().equals("float_field")) {
                try {
                    floatField = com.google.common.base.Optional.of(((float)iprot.readDouble()));
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("i8_field")) {
                try {
                    i8Field = com.google.common.base.Optional.of(iprot.readByte());
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("i16_field")) {
                try {
                    i16Field = com.google.common.base.Optional.of(iprot.readI16());
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("i32_field")) {
                try {
                    i32Field = com.google.common.base.Optional.of(iprot.readI32());
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("i64_field")) {
                try {
                    i64Field = com.google.common.base.Optional.of(iprot.readI64());
                } catch (final NumberFormatException e) {
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
                    public com.google.common.collect.ImmutableMap<String, String> apply(final org.thryft.protocol.InputProtocol iprot) {
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
            } else if (ifield.getName().equals("struct_field")) {
                structField = com.google.common.base.Optional.of(org.thryft.protocol.test.NestedProtocolTestStruct.readAsStruct(iprot));
            } else if (ifield.getName().equals("u32_field")) {
                try {
                    u32Field = com.google.common.base.Optional.of(iprot.readU32());
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("u64_field")) {
                try {
                    u64Field = com.google.common.base.Optional.of(iprot.readU64());
                } catch (final NumberFormatException e) {
                }
            } else if (ifield.getName().equals("uri_field")) {
                try {
                    uriField = com.google.common.base.Optional.of(org.thryft.native_.Uri.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            } else if (ifield.getName().equals("url_field")) {
                try {
                    urlField = com.google.common.base.Optional.of(org.thryft.native_.Url.parse(iprot.readString()));
                } catch (final java.lang.IllegalArgumentException e) {
                }
            } else if (ifield.getName().equals("variant_field")) {
                variantField = com.google.common.base.Optional.of(iprot.readVariant());
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();
        return new ProtocolTestStruct(requiredI32Field, requiredStringField, binaryField, boolField, dateTimeField, decimalField, emailAddressField, enumField, floatField, i8Field, i16Field, i32Field, i64Field, stringListField, stringStringMapField, stringSetField, stringField, structField, u32Field, u64Field, uriField, urlField, variantField);
    }

    public ProtocolTestStruct replaceBinaryField(final com.google.common.base.Optional<byte[]> binaryField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceBinaryField(final byte[] binaryField) {
        return replaceBinaryField(com.google.common.base.Optional.fromNullable(binaryField));
    }

    public ProtocolTestStruct replaceBoolField(final com.google.common.base.Optional<Boolean> boolField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceBoolField(final boolean boolField) {
        return replaceBoolField(com.google.common.base.Optional.fromNullable(boolField));
    }

    public ProtocolTestStruct replaceDateTimeField(final com.google.common.base.Optional<java.util.Date> dateTimeField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceDateTimeField(final java.util.Date dateTimeField) {
        return replaceDateTimeField(com.google.common.base.Optional.fromNullable(dateTimeField));
    }

    public ProtocolTestStruct replaceDecimalField(final com.google.common.base.Optional<java.math.BigDecimal> decimalField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceDecimalField(final java.math.BigDecimal decimalField) {
        return replaceDecimalField(com.google.common.base.Optional.fromNullable(decimalField));
    }

    public ProtocolTestStruct replaceEmailAddressField(final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceEmailAddressField(final org.thryft.native_.EmailAddress emailAddressField) {
        return replaceEmailAddressField(com.google.common.base.Optional.fromNullable(emailAddressField));
    }

    public ProtocolTestStruct replaceEnumField(final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceEnumField(final org.thryft.protocol.test.ProtocolTestEnum enumField) {
        return replaceEnumField(com.google.common.base.Optional.fromNullable(enumField));
    }

    public ProtocolTestStruct replaceFloatField(final com.google.common.base.Optional<Float> floatField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceFloatField(final float floatField) {
        return replaceFloatField(com.google.common.base.Optional.fromNullable(floatField));
    }

    public ProtocolTestStruct replaceI16Field(final com.google.common.base.Optional<Short> i16Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceI16Field(final short i16Field) {
        return replaceI16Field(com.google.common.base.Optional.fromNullable(i16Field));
    }

    public ProtocolTestStruct replaceI32Field(final com.google.common.base.Optional<Integer> i32Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceI32Field(final int i32Field) {
        return replaceI32Field(com.google.common.base.Optional.fromNullable(i32Field));
    }

    public ProtocolTestStruct replaceI64Field(final com.google.common.base.Optional<Long> i64Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceI64Field(final long i64Field) {
        return replaceI64Field(com.google.common.base.Optional.fromNullable(i64Field));
    }

    public ProtocolTestStruct replaceI8Field(final com.google.common.base.Optional<Byte> i8Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceI8Field(final byte i8Field) {
        return replaceI8Field(com.google.common.base.Optional.fromNullable(i8Field));
    }

    public ProtocolTestStruct replaceRequiredI32Field(final int requiredI32Field) {
        return new ProtocolTestStruct(requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceRequiredStringField(final String requiredStringField) {
        return new ProtocolTestStruct(this.requiredI32Field, requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceStringField(final com.google.common.base.Optional<String> stringField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceStringField(final String stringField) {
        return replaceStringField(com.google.common.base.Optional.fromNullable(stringField));
    }

    public ProtocolTestStruct replaceStringListField(final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceStringListField(final com.google.common.collect.ImmutableList<String> stringListField) {
        return replaceStringListField(com.google.common.base.Optional.fromNullable(stringListField));
    }

    public ProtocolTestStruct replaceStringSetField(final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceStringSetField(final com.google.common.collect.ImmutableSet<String> stringSetField) {
        return replaceStringSetField(com.google.common.base.Optional.fromNullable(stringSetField));
    }

    public ProtocolTestStruct replaceStringStringMapField(final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceStringStringMapField(final com.google.common.collect.ImmutableMap<String, String> stringStringMapField) {
        return replaceStringStringMapField(com.google.common.base.Optional.fromNullable(stringStringMapField));
    }

    public ProtocolTestStruct replaceStructField(final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, structField, this.u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceStructField(final org.thryft.protocol.test.NestedProtocolTestStruct structField) {
        return replaceStructField(com.google.common.base.Optional.fromNullable(structField));
    }

    public ProtocolTestStruct replaceU32Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, u32Field, this.u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceU32Field(final com.google.common.primitives.UnsignedInteger u32Field) {
        return replaceU32Field(com.google.common.base.Optional.fromNullable(u32Field));
    }

    public ProtocolTestStruct replaceU64Field(final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, u64Field, this.uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceU64Field(final com.google.common.primitives.UnsignedLong u64Field) {
        return replaceU64Field(com.google.common.base.Optional.fromNullable(u64Field));
    }

    public ProtocolTestStruct replaceUriField(final com.google.common.base.Optional<org.thryft.native_.Uri> uriField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, uriField, this.urlField, this.variantField);
    }

    public ProtocolTestStruct replaceUriField(final org.thryft.native_.Uri uriField) {
        return replaceUriField(com.google.common.base.Optional.fromNullable(uriField));
    }

    public ProtocolTestStruct replaceUrlField(final com.google.common.base.Optional<org.thryft.native_.Url> urlField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, urlField, this.variantField);
    }

    public ProtocolTestStruct replaceUrlField(final org.thryft.native_.Url urlField) {
        return replaceUrlField(com.google.common.base.Optional.fromNullable(urlField));
    }

    public ProtocolTestStruct replaceVariantField(final com.google.common.base.Optional<java.lang.Object> variantField) {
        return new ProtocolTestStruct(this.requiredI32Field, this.requiredStringField, this.binaryField, this.boolField, this.dateTimeField, this.decimalField, this.emailAddressField, this.enumField, this.floatField, this.i8Field, this.i16Field, this.i32Field, this.i64Field, this.stringListField, this.stringStringMapField, this.stringSetField, this.stringField, this.structField, this.u32Field, this.u64Field, this.uriField, this.urlField, variantField);
    }

    public ProtocolTestStruct replaceVariantField(final java.lang.Object variantField) {
        return replaceVariantField(com.google.common.base.Optional.fromNullable(variantField));
    }

    @Override
    public String toString() {
        return com.google.common.base.MoreObjects.toStringHelper(this).omitNullValues().add("required_i32_field", getRequiredI32Field()).add("required_string_field", getRequiredStringField()).add("binary_field", getBinaryField().orNull()).add("bool_field", getBoolField().orNull()).add("date_time_field", getDateTimeField().orNull()).add("decimal_field", getDecimalField().orNull()).add("email_address_field", getEmailAddressField().orNull()).add("enum_field", getEnumField().orNull()).add("float_field", getFloatField().orNull()).add("i8_field", getI8Field().orNull()).add("i16_field", getI16Field().orNull()).add("i32_field", getI32Field().orNull()).add("i64_field", getI64Field().orNull()).add("string_list_field", getStringListField().orNull()).add("string_string_map_field", getStringStringMapField().orNull()).add("string_set_field", getStringSetField().orNull()).add("string_field", getStringField().orNull()).add("struct_field", getStructField().orNull()).add("u32_field", getU32Field().orNull()).add("u64_field", getU64Field().orNull()).add("uri_field", getUriField().orNull()).add("url_field", getUrlField().orNull()).add("variant_field", getVariantField().orNull()).toString();
    }

    @Override
    public void writeAsList(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
        oprot.writeListBegin(org.thryft.protocol.Type.VOID_, 23);

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

        if (getI8Field().isPresent()) {
            oprot.writeByte(getI8Field().get());
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

        if (getFloatField().isPresent()) {
            oprot.writeFieldBegin("float_field", org.thryft.protocol.Type.DOUBLE, (short)-1);
            oprot.writeDouble(getFloatField().get());
            oprot.writeFieldEnd();
        }

        if (getI8Field().isPresent()) {
            oprot.writeFieldBegin("i8_field", org.thryft.protocol.Type.BYTE, (short)-1);
            oprot.writeByte(getI8Field().get());
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

        if (getStructField().isPresent()) {
            oprot.writeFieldBegin("struct_field", org.thryft.protocol.Type.STRUCT, (short)-1);
            getStructField().get().writeAsStruct(oprot);
            oprot.writeFieldEnd();
        }

        if (getU32Field().isPresent()) {
            oprot.writeFieldBegin("u32_field", org.thryft.protocol.Type.I32, (short)-1);
            oprot.writeU32(getU32Field().get());
            oprot.writeFieldEnd();
        }

        if (getU64Field().isPresent()) {
            oprot.writeFieldBegin("u64_field", org.thryft.protocol.Type.I64, (short)-1);
            oprot.writeU64(getU64Field().get());
            oprot.writeFieldEnd();
        }

        if (getUriField().isPresent()) {
            oprot.writeFieldBegin("uri_field", org.thryft.protocol.Type.STRING, (short)-1);
            oprot.writeString(getUriField().get().toString());
            oprot.writeFieldEnd();
        }

        if (getUrlField().isPresent()) {
            oprot.writeFieldBegin("url_field", org.thryft.protocol.Type.STRING, (short)-1);
            oprot.writeString(getUrlField().get().toString());
            oprot.writeFieldEnd();
        }

        if (getVariantField().isPresent()) {
            oprot.writeFieldBegin("variant_field", org.thryft.protocol.Type.STRUCT, (short)-1);
            oprot.writeVariant(getVariantField().get());
            oprot.writeFieldEnd();
        }

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }

    private final int requiredI32Field;

    private final String requiredStringField;

    private final com.google.common.base.Optional<byte[]> binaryField;

    private final com.google.common.base.Optional<Boolean> boolField;

    private final com.google.common.base.Optional<java.util.Date> dateTimeField;

    private final com.google.common.base.Optional<java.math.BigDecimal> decimalField;

    private final com.google.common.base.Optional<org.thryft.native_.EmailAddress> emailAddressField;

    private final com.google.common.base.Optional<org.thryft.protocol.test.ProtocolTestEnum> enumField;

    private final com.google.common.base.Optional<Float> floatField;

    private final com.google.common.base.Optional<Byte> i8Field;

    private final com.google.common.base.Optional<Short> i16Field;

    private final com.google.common.base.Optional<Integer> i32Field;

    private final com.google.common.base.Optional<Long> i64Field;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableList<String>> stringListField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableMap<String, String>> stringStringMapField;

    private final com.google.common.base.Optional<com.google.common.collect.ImmutableSet<String>> stringSetField;

    private final com.google.common.base.Optional<String> stringField;

    private final com.google.common.base.Optional<org.thryft.protocol.test.NestedProtocolTestStruct> structField;

    private final com.google.common.base.Optional<com.google.common.primitives.UnsignedInteger> u32Field;

    private final com.google.common.base.Optional<com.google.common.primitives.UnsignedLong> u64Field;

    private final com.google.common.base.Optional<org.thryft.native_.Uri> uriField;

    private final com.google.common.base.Optional<org.thryft.native_.Url> urlField;

    private final com.google.common.base.Optional<java.lang.Object> variantField;
}
