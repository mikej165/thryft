package thryft.util;

@SuppressWarnings({"serial"})
public class Date implements org.apache.thrift.TBase<Date, org.apache.thrift.TFieldIdEnum> {
    public static class Builder {
        public Builder() {
        }

        public Builder(final Date other) {
            this.timestampMs = other.getTimestampMs();
        }

        protected Date _build(final long timestampMs) {
            return new Date(timestampMs);
        }

        public Date build() {
            return _build(timestampMs);
        }

        public Builder setTimestampMs(final long timestampMs) {
            this.timestampMs = timestampMs;
            return this;
        }

        private Long timestampMs;
    }

    public Date(final Date other) {
        this(other.getTimestampMs());
    }

    public Date(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        this(iprot, org.apache.thrift.protocol.TType.STRUCT);
    }

    public Date(final org.apache.thrift.protocol.TProtocol iprot, final byte readAsTType) throws org.apache.thrift.TException {
        long timestampMs = ((long)0);

        switch (readAsTType) {
            case org.apache.thrift.protocol.TType.LIST:
                iprot.readListBegin();
                try {
                    timestampMs = iprot.readI64();
                } catch (NumberFormatException e) {
                }
                iprot.readListEnd();
                break;

            case org.apache.thrift.protocol.TType.STRUCT:
                iprot.readStructBegin();
                while (true) {
                    org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
                    if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
                        break;
                    } else                 if (ifield.name.equals("timestamp_ms")) {
                        try {
                            timestampMs = iprot.readI64();
                        } catch (NumberFormatException e) {
                        }
                    }
                    iprot.readFieldEnd();
                }
                iprot.readStructEnd();
                break;

            default:
                throw new org.apache.thrift.TException("unknown readAsType");
        }

        this.timestampMs = timestampMs;
    }

    public Date(final long timestampMs) {
        this.timestampMs = timestampMs;
    }

    public Date(final Long timestampMs) {
        this.timestampMs = timestampMs;
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public int compareTo(final Date other) {
        throw new UnsupportedOperationException();
    }

    @Override
    public org.apache.thrift.TBase<Date, org.apache.thrift.TFieldIdEnum> deepCopy() {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean equals(final Object otherObject) {
        if (otherObject == this) {
            return true;
        } else if (!(otherObject instanceof Date)) {
            return false;
        }

        final Date other = (Date)otherObject;
        return
            getTimestampMs() == other.getTimestampMs();
    }

    @Override
    public org.apache.thrift.TFieldIdEnum fieldForId(final int fieldId) {
        throw new UnsupportedOperationException();
    }

    public Object get(final String fieldName) {
        if (fieldName.equals("timestamp_ms")) {
            return getTimestampMs();
        }
        return null;
    }

    @Override
    public Object getFieldValue(final org.apache.thrift.TFieldIdEnum field) {
        throw new UnsupportedOperationException();
    }

    public final long getTimestampMs() {
        return timestampMs;
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        hashCode = 31 * hashCode + ((int)(getTimestampMs() ^ (getTimestampMs() >>> 32)));
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
        helper.add("timestamp_ms", getTimestampMs());
        return helper.toString();
    }

    @Override
    public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
        oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct("Date"));

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("timestamp_ms", org.apache.thrift.protocol.TType.I64, (short)-1));
        oprot.writeI64(getTimestampMs());
        oprot.writeFieldEnd();

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }

    private final long timestampMs;
}
