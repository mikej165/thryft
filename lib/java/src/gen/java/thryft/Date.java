package thryft;

@SuppressWarnings("serial")
public class Date implements org.apache.thrift.TBase<Date, org.apache.thrift.TFieldIdEnum> {
    public static class Builder {
        public Builder() {
        }

        public Builder(final Date other) {
            this.year = other.getYear();
            this.month = other.getMonth();
            this.day = other.getDay();
        }

        protected Date _build(final short year, final byte month, final byte day) {
            return new Date(year, month, day);
        }

        public Date build() {
            return _build(year, month, day);
        }

        public Builder setDay(final byte day) {
            this.day = day;
            return this;
        }

        public Builder setMonth(final byte month) {
            this.month = month;
            return this;
        }

        public Builder setYear(final short year) {
            this.year = year;
            return this;
        }

        private Short year;
        private Byte month;
        private Byte day;
    }

    public Date(final Date other) {
        this(other.getYear(), other.getMonth(), other.getDay());
    }

    public Date(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        short year = ((short)0);
        byte month = ((byte)0);
        byte day = ((byte)0);

        iprot.readStructBegin();
        while (true) {
            org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
            if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
                break;
            } else         if (ifield.name.equals("year")) {
                try {
                    year = iprot.readI16();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("month")) {
                try {
                    month = iprot.readByte();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("day")) {
                try {
                    day = iprot.readByte();
                } catch (NumberFormatException e) {
                }
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();

        this.year = year;
        this.month = month;
        this.day = day;
    }

    public Date(final short year, final byte month, final byte day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public Date(final Short year, final Byte month, final Byte day) {
        this.year = year;
        this.month = month;
        this.day = day;
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
            getYear() == other.getYear() &&
            getMonth() == other.getMonth() &&
            getDay() == other.getDay();
    }

    @Override
    public org.apache.thrift.TFieldIdEnum fieldForId(final int fieldId) {
        throw new UnsupportedOperationException();
    }

    public Object get(final String fieldName) {
        if (fieldName.equals("year")) {
            return getYear();
        } else if (fieldName.equals("month")) {
            return getMonth();
        } else if (fieldName.equals("day")) {
            return getDay();
        }
        return null;
    }

    public final byte getDay() {
        return day;
    }

    @Override
    public Object getFieldValue(final org.apache.thrift.TFieldIdEnum field) {
        throw new UnsupportedOperationException();
    }

    public final byte getMonth() {
        return month;
    }

    public final short getYear() {
        return year;
    }

    @Override
    public int hashCode() {
        int hashCode = 17;
        hashCode = 31 * hashCode + ((int)getYear());
        hashCode = 31 * hashCode + ((byte)getMonth());
        hashCode = 31 * hashCode + ((byte)getDay());
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
        helper.add("year", getYear());
        helper.add("month", getMonth());
        helper.add("day", getDay());
        return helper.toString();
    }

    @Override
    public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
        oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct("Date"));

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("year", org.apache.thrift.protocol.TType.I16, (short)-1));
        oprot.writeI16(getYear());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("month", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getMonth());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("day", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getDay());
        oprot.writeFieldEnd();

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }

    private final short year;
    private final byte month;
    private final byte day;
}
