package thryft;

@SuppressWarnings("serial")
public class DateTime implements org.apache.thrift.TBase<DateTime, org.apache.thrift.TFieldIdEnum> {
    public static class Builder {
        public Builder() {
        }

        public Builder(final DateTime other) {
            this.year = other.getYear();
            this.month = other.getMonth();
            this.day = other.getDay();
            this.hour = other.getHour();
            this.minute = other.getMinute();
            this.second = other.getSecond();
        }

        protected DateTime _build(final short year, final byte month, final byte day, final byte hour, final byte minute, final byte second) {
            return new DateTime(year, month, day, hour, minute, second);
        }

        public DateTime build() {
            return _build(year, month, day, hour, minute, second);
        }

        public Builder setDay(final byte day) {
            this.day = day;
            return this;
        }

        public Builder setHour(final byte hour) {
            this.hour = hour;
            return this;
        }

        public Builder setMinute(final byte minute) {
            this.minute = minute;
            return this;
        }

        public Builder setMonth(final byte month) {
            this.month = month;
            return this;
        }

        public Builder setSecond(final byte second) {
            this.second = second;
            return this;
        }

        public Builder setYear(final short year) {
            this.year = year;
            return this;
        }

        private Short year;
        private Byte month;
        private Byte day;
        private Byte hour;
        private Byte minute;
        private Byte second;
    }

    public DateTime(final DateTime other) {
        this(other.getYear(), other.getMonth(), other.getDay(), other.getHour(), other.getMinute(), other.getSecond());
    }

    public DateTime(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
        short year = ((short)0);
        byte month = ((byte)0);
        byte day = ((byte)0);
        byte hour = ((byte)0);
        byte minute = ((byte)0);
        byte second = ((byte)0);

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
            } else if (ifield.name.equals("hour")) {
                try {
                    hour = iprot.readByte();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("minute")) {
                try {
                    minute = iprot.readByte();
                } catch (NumberFormatException e) {
                }
            } else if (ifield.name.equals("second")) {
                try {
                    second = iprot.readByte();
                } catch (NumberFormatException e) {
                }
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();

        this.year = year;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    public DateTime(final short year, final byte month, final byte day, final byte hour, final byte minute, final byte second) {
        this.year = year;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    public DateTime(final Short year, final Byte month, final Byte day, final Byte hour, final Byte minute, final Byte second) {
        this.year = year;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    @Override
    public void clear() {
        throw new UnsupportedOperationException();
    }

    @Override
    public int compareTo(final DateTime other) {
        throw new UnsupportedOperationException();
    }

    @Override
    public org.apache.thrift.TBase<DateTime, org.apache.thrift.TFieldIdEnum> deepCopy() {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean equals(final Object otherObject) {
        if (otherObject == this) {
            return true;
        } else if (!(otherObject instanceof DateTime)) {
            return false;
        }

        final DateTime other = (DateTime)otherObject;
        return
            getYear() == other.getYear() &&
            getMonth() == other.getMonth() &&
            getDay() == other.getDay() &&
            getHour() == other.getHour() &&
            getMinute() == other.getMinute() &&
            getSecond() == other.getSecond();
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
        } else if (fieldName.equals("hour")) {
            return getHour();
        } else if (fieldName.equals("minute")) {
            return getMinute();
        } else if (fieldName.equals("second")) {
            return getSecond();
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

    public final byte getHour() {
        return hour;
    }

    public final byte getMinute() {
        return minute;
    }

    public final byte getMonth() {
        return month;
    }

    public final byte getSecond() {
        return second;
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
        hashCode = 31 * hashCode + ((byte)getHour());
        hashCode = 31 * hashCode + ((byte)getMinute());
        hashCode = 31 * hashCode + ((byte)getSecond());
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
        helper.add("hour", getHour());
        helper.add("minute", getMinute());
        helper.add("second", getSecond());
        return helper.toString();
    }

    @Override
    public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
        oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct("DateTime"));

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("year", org.apache.thrift.protocol.TType.I16, (short)-1));
        oprot.writeI16(getYear());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("month", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getMonth());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("day", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getDay());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("hour", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getHour());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("minute", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getMinute());
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("second", org.apache.thrift.protocol.TType.BYTE, (short)-1));
        oprot.writeByte(getSecond());
        oprot.writeFieldEnd();

        oprot.writeFieldStop();

        oprot.writeStructEnd();
    }

    private final short year;
    private final byte month;
    private final byte day;
    private final byte hour;
    private final byte minute;
    private final byte second;
}
