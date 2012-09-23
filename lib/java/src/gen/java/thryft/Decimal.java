package thryft;

@SuppressWarnings("serial")
public class Decimal implements org.apache.thrift.TBase<Decimal, org.apache.thrift.TFieldIdEnum> {
    public static class Builder {
        public Builder() {
        }

        public Builder(final Decimal other) {
            this.value = other.getValue();
        }

        protected Decimal _build(final String value) {
            return new Decimal(value);
        }

        public Decimal build() {
            return _build(value);
        }

        public Builder setValue(final String value) {
            this.value = value;
            return this;
        }

        private String value;
    }

    public Decimal(final Decimal other) {
        this(other.getValue());
    }

    public Decimal(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        String value = null;

        iprot.readStructBegin();
        while (true) {
            org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
            if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
                break;
            } else         if (ifield.name.equals("value")) {
                value = iprot.readString();
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();

        this.value = com.google.common.base.Preconditions.checkNotNull(value);
    }

    public Decimal(final String value) {
        this.value = com.google.common.base.Preconditions.checkNotNull(value);
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public int compareTo(final Decimal other) {
        throw new UnsupportedOperationException();
    }

    @Override
    public org.apache.thrift.TBase<Decimal, org.apache.thrift.TFieldIdEnum> deepCopy() {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean equals(final Object otherObject) {
        if (otherObject == this) {
            return true;
        } else if (!(otherObject instanceof Decimal)) {
            return false;
        }

        final Decimal other = (Decimal)otherObject;
        return
            getValue().equals(other.getValue());
    }

    @Override
    public org.apache.thrift.TFieldIdEnum fieldForId(final int fieldId) {
        throw new UnsupportedOperationException();
    }

    public Object get(final String fieldName) {
        if (fieldName.equals("value")) {
            return getValue();
        }
        return null;
    }

    @Override
    public Object getFieldValue(final org.apache.thrift.TFieldIdEnum field) {
        throw new UnsupportedOperationException();
    }

    public final String getValue() {
        return value;
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        hashCode = 31 * hashCode + getValue().hashCode();
        return hashCode;
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
        helper.add("value", getValue());
        return helper.toString();
    }

    @Override
    public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
        oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct("Decimal"));

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("value", org.apache.thrift.protocol.TType.STRING, (short)-1));
        oprot.writeString(getValue());
        oprot.writeFieldEnd();

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }

    private final String value;
}
