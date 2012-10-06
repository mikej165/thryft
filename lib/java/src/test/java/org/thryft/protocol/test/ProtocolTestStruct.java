package org.thryft.protocol.test;

@SuppressWarnings("serial")
public class ProtocolTestStruct implements org.apache.thrift.TBase<ProtocolTestStruct, org.apache.thrift.TFieldIdEnum> {
    public static class Builder {
        public Builder() {
        }

        public Builder(final ProtocolTestStruct other) {
            this.boolField = other.isBoolField();
            this.byteField = other.getByteField();
            this.dateField = other.getDateField();
            this.dateTimeField = other.getDateTimeField();
            this.decimalField = other.getDecimalField();
            this.enumField = other.getEnumField();
            this.i16Field = other.getI16Field();
            this.i32Field = other.getI32Field();
            this.i64Field = other.getI64Field();
            this.listStringField = other.getListStringField();
            this.mapStringStringField = other.getMapStringStringField();
            this.setStringField = other.getSetStringField();
            this.stringField = other.getStringField();
            this.structField = other.getStructField();
        }

        protected ProtocolTestStruct _build(final Boolean boolField, final Byte byteField, final org.joda.time.DateTime dateField, final org.joda.time.DateTime dateTimeField, final java.math.BigDecimal decimalField, final org.thryft.protocol.test.ProtocolTestEnum enumField, final Short i16Field, final Integer i32Field, final Long i64Field, final com.google.common.collect.ImmutableList<String> listStringField, final com.google.common.collect.ImmutableMap<String, String> mapStringStringField, final com.google.common.collect.ImmutableSet<String> setStringField, final String stringField, final org.thryft.protocol.test.ProtocolTestStruct structField) {
            return new ProtocolTestStruct(boolField, byteField, dateField, dateTimeField, decimalField, enumField, i16Field, i32Field, i64Field, listStringField, mapStringStringField, setStringField, stringField, structField);
        }

        public ProtocolTestStruct build() {
            return _build(boolField, byteField, dateField, dateTimeField, decimalField, enumField, i16Field, i32Field, i64Field, listStringField, mapStringStringField, setStringField, stringField, structField);
        }

        public Builder setBoolField(final Boolean boolField) {
            this.boolField = boolField;
            return this;
        }

        public Builder setByteField(final Byte byteField) {
            this.byteField = byteField;
            return this;
        }

        public Builder setDateField(final org.joda.time.DateTime dateField) {
            this.dateField = dateField;
            return this;
        }

        public Builder setDateTimeField(final org.joda.time.DateTime dateTimeField) {
            this.dateTimeField = dateTimeField;
            return this;
        }

        public Builder setDecimalField(final java.math.BigDecimal decimalField) {
            this.decimalField = decimalField;
            return this;
        }

        public Builder setEnumField(final org.thryft.protocol.test.ProtocolTestEnum enumField) {
            this.enumField = enumField;
            return this;
        }

        public Builder setI16Field(final Short i16Field) {
            this.i16Field = i16Field;
            return this;
        }

        public Builder setI32Field(final Integer i32Field) {
            this.i32Field = i32Field;
            return this;
        }

        public Builder setI64Field(final Long i64Field) {
            this.i64Field = i64Field;
            return this;
        }

        public Builder setListStringField(final com.google.common.collect.ImmutableList<String> listStringField) {
            this.listStringField = listStringField;
            return this;
        }

        public Builder setMapStringStringField(final com.google.common.collect.ImmutableMap<String, String> mapStringStringField) {
            this.mapStringStringField = mapStringStringField;
            return this;
        }

        public Builder setSetStringField(final com.google.common.collect.ImmutableSet<String> setStringField) {
            this.setStringField = setStringField;
            return this;
        }

        public Builder setStringField(final String stringField) {
            this.stringField = stringField;
            return this;
        }

        public Builder setStructField(final org.thryft.protocol.test.ProtocolTestStruct structField) {
            this.structField = structField;
            return this;
        }

        private Boolean boolField;
        private Byte byteField;
        private org.joda.time.DateTime dateField;
        private org.joda.time.DateTime dateTimeField;
        private java.math.BigDecimal decimalField;
        private org.thryft.protocol.test.ProtocolTestEnum enumField;
        private Short i16Field;
        private Integer i32Field;
        private Long i64Field;
        private com.google.common.collect.ImmutableList<String> listStringField;
        private com.google.common.collect.ImmutableMap<String, String> mapStringStringField;
        private com.google.common.collect.ImmutableSet<String> setStringField;
        private String stringField;
        private org.thryft.protocol.test.ProtocolTestStruct structField;
    }

    public ProtocolTestStruct() {
        this.boolField = null;
        this.byteField = null;
        this.dateField = null;
        this.dateTimeField = null;
        this.decimalField = null;
        this.enumField = null;
        this.i16Field = null;
        this.i32Field = null;
        this.i64Field = null;
        this.listStringField = null;
        this.mapStringStringField = null;
        this.setStringField = null;
        this.stringField = null;
        this.structField = null;
    }

    public ProtocolTestStruct(final ProtocolTestStruct other) {
        this(other.isBoolField(), other.getByteField(), other.getDateField(), other.getDateTimeField(), other.getDecimalField(), other.getEnumField(), other.getI16Field(), other.getI32Field(), other.getI64Field(), other.getListStringField(), other.getMapStringStringField(), other.getSetStringField(), other.getStringField(), other.getStructField());
    }

    public ProtocolTestStruct(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        Boolean boolField = null;
        Byte byteField = null;
        org.joda.time.DateTime dateField = null;
        org.joda.time.DateTime dateTimeField = null;
        java.math.BigDecimal decimalField = null;
        org.thryft.protocol.test.ProtocolTestEnum enumField = null;
        Short i16Field = null;
        Integer i32Field = null;
        Long i64Field = null;
        com.google.common.collect.ImmutableList<String> listStringField = null;
        com.google.common.collect.ImmutableMap<String, String> mapStringStringField = null;
        com.google.common.collect.ImmutableSet<String> setStringField = null;
        String stringField = null;
        org.thryft.protocol.test.ProtocolTestStruct structField = null;

        iprot.readStructBegin();
        while (true) {
            org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
            if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
                break;
            } else         if (ifield.name.equals("bool_field")) {
                boolField = iprot.readBool();
            } else if (ifield.name.equals("byte_field")) {
                try {
                    byteField = iprot.readByte();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("date_field")) {
                try {
                    dateField = (iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readDateTime() : new org.joda.time.DateTime(iprot.readI64());
                } catch (IllegalArgumentException e) {
                }
            } else if (ifield.name.equals("date_time_field")) {
                try {
                    dateTimeField = (iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readDateTime() : new org.joda.time.DateTime(iprot.readI64());
                } catch (IllegalArgumentException e) {
                }
            } else if (ifield.name.equals("decimal_field")) {
                try {
                    decimalField = (iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readDecimal() : new java.math.BigDecimal(iprot.readString());
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("enum_field")) {
                try {
                    enumField = (iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readEnum(org.thryft.protocol.test.ProtocolTestEnum.class) : org.thryft.protocol.test.ProtocolTestEnum.valueOf(iprot.readString().trim().toUpperCase());
                } catch (IllegalArgumentException e) {
                }
            } else if (ifield.name.equals("i16_field")) {
                try {
                    i16Field = iprot.readI16();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("i32_field")) {
                try {
                    i32Field = iprot.readI32();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("i64_field")) {
                try {
                    i64Field = iprot.readI64();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("list_string_field")) {
                listStringField = (new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.ImmutableList<String>>() {
                    @Override
                    public com.google.common.collect.ImmutableList<String> apply(org.apache.thrift.protocol.TProtocol iprot) {
                        try {
                            org.apache.thrift.protocol.TList sequenceBegin = iprot.readListBegin();
                            java.util.List<String> sequence = new java.util.ArrayList<String>();
                            for (int elementI = 0; elementI < sequenceBegin.size; elementI++) {
                                sequence.add(iprot.readString());
                            }
                            iprot.readListEnd();
                            return com.google.common.collect.ImmutableList.copyOf(sequence);
                        } catch (org.apache.thrift.TException e) {
                            return com.google.common.collect.ImmutableList.of();
                        }
                    }
                }).apply(iprot);
            } else if (ifield.name.equals("map_string_string_field")) {
                mapStringStringField = (new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.ImmutableMap<String, String>>() {
                    @Override
                    public com.google.common.collect.ImmutableMap<String, String> apply(org.apache.thrift.protocol.TProtocol iprot) {
                        try {
                            org.apache.thrift.protocol.TMap mapBegin = iprot.readMapBegin();
                            java.util.Map<String, String> map = new java.util.HashMap<String, String>();
                            for (int entryI = 0; entryI < mapBegin.size; entryI++) {
                                map.put(iprot.readString(), iprot.readString());
                            }
                            iprot.readMapEnd();
                            return com.google.common.collect.ImmutableMap.copyOf(map);
                        } catch (org.apache.thrift.TException e) {
                            return com.google.common.collect.ImmutableMap.of();
                        }
                    }
                }).apply(iprot);
            } else if (ifield.name.equals("set_string_field")) {
                setStringField = (new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.ImmutableSet<String>>() {
                    @Override
                    public com.google.common.collect.ImmutableSet<String> apply(org.apache.thrift.protocol.TProtocol iprot) {
                        try {
                            org.apache.thrift.protocol.TSet sequenceBegin = iprot.readSetBegin();
                            java.util.Set<String> sequence = new java.util.LinkedHashSet<String>();
                            for (int elementI = 0; elementI < sequenceBegin.size; elementI++) {
                                sequence.add(iprot.readString());
                            }
                            iprot.readSetEnd();
                            return com.google.common.collect.ImmutableSet.copyOf(sequence);
                        } catch (org.apache.thrift.TException e) {
                            return com.google.common.collect.ImmutableSet.of();
                        }
                    }
                }).apply(iprot);
            } else if (ifield.name.equals("string_field")) {
                stringField = iprot.readString();
            } else if (ifield.name.equals("struct_field")) {
                structField = new org.thryft.protocol.test.ProtocolTestStruct(iprot);
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();

        this.boolField = boolField;
        this.byteField = byteField;
        this.dateField = dateField;
        this.dateTimeField = dateTimeField;
        this.decimalField = decimalField;
        this.enumField = enumField;
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.listStringField = listStringField;
        this.mapStringStringField = mapStringStringField;
        this.setStringField = setStringField;
        this.stringField = stringField;
        this.structField = structField;
    }

    public ProtocolTestStruct(final Boolean boolField, final Byte byteField, final org.joda.time.DateTime dateField, final org.joda.time.DateTime dateTimeField, final java.math.BigDecimal decimalField, final org.thryft.protocol.test.ProtocolTestEnum enumField, final Short i16Field, final Integer i32Field, final Long i64Field, final com.google.common.collect.ImmutableList<String> listStringField, final com.google.common.collect.ImmutableMap<String, String> mapStringStringField, final com.google.common.collect.ImmutableSet<String> setStringField, final String stringField, final org.thryft.protocol.test.ProtocolTestStruct structField) {
        this.boolField = boolField;
        this.byteField = byteField;
        this.dateField = dateField;
        this.dateTimeField = dateTimeField;
        this.decimalField = decimalField;
        this.enumField = enumField;
        this.i16Field = i16Field;
        this.i32Field = i32Field;
        this.i64Field = i64Field;
        this.listStringField = listStringField;
        this.mapStringStringField = mapStringStringField;
        this.setStringField = setStringField;
        this.stringField = stringField;
        this.structField = structField;
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public int compareTo(final ProtocolTestStruct other) {
        throw new UnsupportedOperationException();
    }

    @Override
    public org.apache.thrift.TBase<ProtocolTestStruct, org.apache.thrift.TFieldIdEnum> deepCopy() {
        throw new UnsupportedOperationException();
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
            ((isBoolField() == null && other.isBoolField() == null) ||
            (isBoolField() != null && other.isBoolField() != null &&
            isBoolField().equals(other.isBoolField()))) &&
            ((getByteField() == null && other.getByteField() == null) ||
            (getByteField() != null && other.getByteField() != null &&
            getByteField().equals(other.getByteField()))) &&
            ((getDateField() == null && other.getDateField() == null) ||
            (getDateField() != null && other.getDateField() != null &&
            getDateField().equals(other.getDateField()))) &&
            ((getDateTimeField() == null && other.getDateTimeField() == null) ||
            (getDateTimeField() != null && other.getDateTimeField() != null &&
            getDateTimeField().equals(other.getDateTimeField()))) &&
            ((getDecimalField() == null && other.getDecimalField() == null) ||
            (getDecimalField() != null && other.getDecimalField() != null &&
            getDecimalField().equals(other.getDecimalField()))) &&
            ((getEnumField() == null && other.getEnumField() == null) ||
            (getEnumField() != null && other.getEnumField() != null &&
            getEnumField().equals(other.getEnumField()))) &&
            ((getI16Field() == null && other.getI16Field() == null) ||
            (getI16Field() != null && other.getI16Field() != null &&
            getI16Field().equals(other.getI16Field()))) &&
            ((getI32Field() == null && other.getI32Field() == null) ||
            (getI32Field() != null && other.getI32Field() != null &&
            getI32Field().equals(other.getI32Field()))) &&
            ((getI64Field() == null && other.getI64Field() == null) ||
            (getI64Field() != null && other.getI64Field() != null &&
            getI64Field().equals(other.getI64Field()))) &&
            ((getListStringField() == null && other.getListStringField() == null) ||
            (getListStringField() != null && other.getListStringField() != null &&
            getListStringField().equals(other.getListStringField()))) &&
            ((getMapStringStringField() == null && other.getMapStringStringField() == null) ||
            (getMapStringStringField() != null && other.getMapStringStringField() != null &&
            getMapStringStringField().equals(other.getMapStringStringField()))) &&
            ((getSetStringField() == null && other.getSetStringField() == null) ||
            (getSetStringField() != null && other.getSetStringField() != null &&
            getSetStringField().equals(other.getSetStringField()))) &&
            ((getStringField() == null && other.getStringField() == null) ||
            (getStringField() != null && other.getStringField() != null &&
            getStringField().equals(other.getStringField()))) &&
            ((getStructField() == null && other.getStructField() == null) ||
            (getStructField() != null && other.getStructField() != null &&
            getStructField().equals(other.getStructField())));
    }

    @Override
    public org.apache.thrift.TFieldIdEnum fieldForId(final int fieldId) {
        throw new UnsupportedOperationException();
    }

    public Object get(final String fieldName) {
        if (fieldName.equals("bool_field")) {
            return isBoolField();
        } else if (fieldName.equals("byte_field")) {
            return getByteField();
        } else if (fieldName.equals("date_field")) {
            return getDateField();
        } else if (fieldName.equals("date_time_field")) {
            return getDateTimeField();
        } else if (fieldName.equals("decimal_field")) {
            return getDecimalField();
        } else if (fieldName.equals("enum_field")) {
            return getEnumField();
        } else if (fieldName.equals("i16_field")) {
            return getI16Field();
        } else if (fieldName.equals("i32_field")) {
            return getI32Field();
        } else if (fieldName.equals("i64_field")) {
            return getI64Field();
        } else if (fieldName.equals("list_string_field")) {
            return getListStringField();
        } else if (fieldName.equals("map_string_string_field")) {
            return getMapStringStringField();
        } else if (fieldName.equals("set_string_field")) {
            return getSetStringField();
        } else if (fieldName.equals("string_field")) {
            return getStringField();
        } else if (fieldName.equals("struct_field")) {
            return getStructField();
        }
        return null;
    }

    public final Byte getByteField() {
        return byteField;
    }

    public final org.joda.time.DateTime getDateField() {
        return dateField;
    }

    public final org.joda.time.DateTime getDateTimeField() {
        return dateTimeField;
    }

    public final java.math.BigDecimal getDecimalField() {
        return decimalField;
    }

    public final org.thryft.protocol.test.ProtocolTestEnum getEnumField() {
        return enumField;
    }

    @Override
    public Object getFieldValue(final org.apache.thrift.TFieldIdEnum field) {
        throw new UnsupportedOperationException();
    }

    public final Short getI16Field() {
        return i16Field;
    }

    public final Integer getI32Field() {
        return i32Field;
    }

    public final Long getI64Field() {
        return i64Field;
    }

    public final com.google.common.collect.ImmutableList<String> getListStringField() {
        return listStringField;
    }

    public final com.google.common.collect.ImmutableMap<String, String> getMapStringStringField() {
        return mapStringStringField;
    }

    public final com.google.common.collect.ImmutableSet<String> getSetStringField() {
        return setStringField;
    }

    public final String getStringField() {
        return stringField;
    }

    public final org.thryft.protocol.test.ProtocolTestStruct getStructField() {
        return structField;
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        if (isBoolField() != null) {
            hashCode = 31 * hashCode + (isBoolField() ? 1 : 0);
        }
        if (getByteField() != null) {
            hashCode = 31 * hashCode + ((byte)getByteField());
        }
        if (getDateField() != null) {
            hashCode = 31 * hashCode + getDateField().hashCode();
        }
        if (getDateTimeField() != null) {
            hashCode = 31 * hashCode + getDateTimeField().hashCode();
        }
        if (getDecimalField() != null) {
            hashCode = 31 * hashCode + getDecimalField().hashCode();
        }
        if (getEnumField() != null) {
            hashCode = 31 * hashCode + getEnumField().ordinal();
        }
        if (getI16Field() != null) {
            hashCode = 31 * hashCode + ((int)getI16Field());
        }
        if (getI32Field() != null) {
            hashCode = 31 * hashCode + ((int)getI32Field());
        }
        if (getI64Field() != null) {
            hashCode = 31 * hashCode + ((int)(getI64Field() ^ (getI64Field() >>> 32)));
        }
        if (getListStringField() != null) {
            hashCode = 31 * hashCode + getListStringField().hashCode();
        }
        if (getMapStringStringField() != null) {
            hashCode = 31 * hashCode + getMapStringStringField().hashCode();
        }
        if (getSetStringField() != null) {
            hashCode = 31 * hashCode + getSetStringField().hashCode();
        }
        if (getStringField() != null) {
            hashCode = 31 * hashCode + getStringField().hashCode();
        }
        if (getStructField() != null) {
            hashCode = 31 * hashCode + getStructField().hashCode();
        }
        return hashCode;
    }

    public final Boolean isBoolField() {
        return boolField;
    }

    @Override
    public boolean isSet(final org.apache.thrift.TFieldIdEnum field) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void read(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void setFieldValue(final org.apache.thrift.TFieldIdEnum field, Object value) {
        throw new UnsupportedOperationException();
    }

    @Override
    public String toString() {
        final com.google.common.base.Objects.ToStringHelper helper = com.google.common.base.Objects.toStringHelper(this);
        if (isBoolField() != null) {
            helper.add("bool_field", isBoolField());
        }
        if (getByteField() != null) {
            helper.add("byte_field", getByteField());
        }
        if (getDateField() != null) {
            helper.add("date_field", getDateField());
        }
        if (getDateTimeField() != null) {
            helper.add("date_time_field", getDateTimeField());
        }
        if (getDecimalField() != null) {
            helper.add("decimal_field", getDecimalField());
        }
        if (getEnumField() != null) {
            helper.add("enum_field", getEnumField());
        }
        if (getI16Field() != null) {
            helper.add("i16_field", getI16Field());
        }
        if (getI32Field() != null) {
            helper.add("i32_field", getI32Field());
        }
        if (getI64Field() != null) {
            helper.add("i64_field", getI64Field());
        }
        if (getListStringField() != null) {
            helper.add("list_string_field", getListStringField());
        }
        if (getMapStringStringField() != null) {
            helper.add("map_string_string_field", getMapStringStringField());
        }
        if (getSetStringField() != null) {
            helper.add("set_string_field", getSetStringField());
        }
        if (getStringField() != null) {
            helper.add("string_field", getStringField());
        }
        if (getStructField() != null) {
            helper.add("struct_field", getStructField());
        }
        return helper.toString();
    }

    @Override
    public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
        oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct("ProtocolTestStruct"));

        if (isBoolField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("bool_field", org.apache.thrift.protocol.TType.BOOL, (short)-1));
            oprot.writeBool(isBoolField());
            oprot.writeFieldEnd();
        }

        if (getByteField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("byte_field", org.apache.thrift.protocol.TType.BYTE, (short)-1));
            oprot.writeByte(getByteField());
            oprot.writeFieldEnd();
        }

        if (getDateField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("date_field", org.apache.thrift.protocol.TType.STRUCT, (short)-1));
            if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeDateTime(getDateField()); } else { oprot.writeI64(getDateField().getMillis()); }
            oprot.writeFieldEnd();
        }

        if (getDateTimeField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("date_time_field", org.apache.thrift.protocol.TType.STRUCT, (short)-1));
            if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeDateTime(getDateTimeField()); } else { oprot.writeI64(getDateTimeField().getMillis()); }
            oprot.writeFieldEnd();
        }

        if (getDecimalField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("decimal_field", org.apache.thrift.protocol.TType.STRUCT, (short)-1));
            if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeDecimal(getDecimalField()); } else { oprot.writeString(getDecimalField().toString()); }
            oprot.writeFieldEnd();
        }

        if (getEnumField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("enum_field", org.apache.thrift.protocol.TType.STRING, (short)-1));
            if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeEnum(getEnumField()); } else { oprot.writeString(getEnumField().toString()); }
            oprot.writeFieldEnd();
        }

        if (getI16Field() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("i16_field", org.apache.thrift.protocol.TType.I16, (short)-1));
            oprot.writeI16(getI16Field());
            oprot.writeFieldEnd();
        }

        if (getI32Field() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("i32_field", org.apache.thrift.protocol.TType.I32, (short)-1));
            oprot.writeI32(getI32Field());
            oprot.writeFieldEnd();
        }

        if (getI64Field() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("i64_field", org.apache.thrift.protocol.TType.I64, (short)-1));
            oprot.writeI64(getI64Field());
            oprot.writeFieldEnd();
        }

        if (getListStringField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("list_string_field", org.apache.thrift.protocol.TType.LIST, (short)-1));
            oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRING, getListStringField().size()));
            for (String _iter0 : getListStringField()) {
                oprot.writeString(_iter0);
            }
            oprot.writeListEnd();
            oprot.writeFieldEnd();
        }

        if (getMapStringStringField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("map_string_string_field", org.apache.thrift.protocol.TType.MAP, (short)-1));
            oprot.writeMapBegin(new org.apache.thrift.protocol.TMap(org.apache.thrift.protocol.TType.STRING, org.apache.thrift.protocol.TType.STRING, getMapStringStringField().size()));
            for (com.google.common.collect.ImmutableMap.Entry<String, String> _iter0 : getMapStringStringField().entrySet()) {
                oprot.writeString(_iter0.getKey());
                oprot.writeString(_iter0.getValue());
            }
            oprot.writeMapEnd();
            oprot.writeFieldEnd();
        }

        if (getSetStringField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("set_string_field", org.apache.thrift.protocol.TType.SET, (short)-1));
            oprot.writeSetBegin(new org.apache.thrift.protocol.TSet(org.apache.thrift.protocol.TType.STRING, getSetStringField().size()));
            for (String _iter0 : getSetStringField()) {
                oprot.writeString(_iter0);
            }
            oprot.writeSetEnd();
            oprot.writeFieldEnd();
        }

        if (getStringField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("string_field", org.apache.thrift.protocol.TType.STRING, (short)-1));
            oprot.writeString(getStringField());
            oprot.writeFieldEnd();
        }

        if (getStructField() != null) {
            oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("struct_field", org.apache.thrift.protocol.TType.STRUCT, (short)-1));
            getStructField().write(oprot);
            oprot.writeFieldEnd();
        }

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }

    private final Boolean boolField;
    private final Byte byteField;
    private final org.joda.time.DateTime dateField;
    private final org.joda.time.DateTime dateTimeField;
    private final java.math.BigDecimal decimalField;
    private final org.thryft.protocol.test.ProtocolTestEnum enumField;
    private final Short i16Field;
    private final Integer i32Field;
    private final Long i64Field;
    private final com.google.common.collect.ImmutableList<String> listStringField;
    private final com.google.common.collect.ImmutableMap<String, String> mapStringStringField;
    private final com.google.common.collect.ImmutableSet<String> setStringField;
    private final String stringField;
    private final org.thryft.protocol.test.ProtocolTestStruct structField;
}
