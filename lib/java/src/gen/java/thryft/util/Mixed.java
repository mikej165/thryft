package thryft.util;

@SuppressWarnings("serial")
public class Mixed implements org.apache.thrift.TBase<Mixed, org.apache.thrift.TFieldIdEnum> {
    public static class Builder {
        public Builder() {
        }

        public Builder(final Mixed other) {
        }

        protected Mixed _build() {
            return new Mixed();
        }

        public Mixed build() {
            return _build();
        }


    }

    public Mixed() {
    }

    public Mixed(final Mixed other) {
    }

    public Mixed(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        iprot.readStructBegin();
        while (true) {
            org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
            if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
                break;
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public int compareTo(final Mixed other) {
        throw new UnsupportedOperationException();
    }

    @Override
    public org.apache.thrift.TBase<Mixed, org.apache.thrift.TFieldIdEnum> deepCopy() {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean equals(final Object otherObject) {
        if (otherObject == this) {
            return true;
        } else if (!(otherObject instanceof Mixed)) {
            return false;
        }

        return true;
    }

    @Override
    public org.apache.thrift.TFieldIdEnum fieldForId(final int fieldId) {
        throw new UnsupportedOperationException();
    }

    public Object get(final String fieldName) {
        return null;
    }

    @Override
    public Object getFieldValue(final org.apache.thrift.TFieldIdEnum field) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
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
    public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
        oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct("Mixed"));

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }


}
