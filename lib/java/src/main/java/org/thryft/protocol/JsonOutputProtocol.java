package org.thryft.protocol;

import java.util.Base64;
import java.util.Date;

public abstract class JsonOutputProtocol extends StackedOutputProtocol<JsonOutputProtocol.NestedOutputProtocol> {
    protected interface JsonGenerator {
        public void flush() throws OutputProtocolException;

        public void writeBoolean(boolean value) throws OutputProtocolException;

        public void writeDateTime(Date value) throws OutputProtocolException;

        public void writeEndArray() throws OutputProtocolException;

        public void writeEndObject() throws OutputProtocolException;

        public void writeFieldName(String value) throws OutputProtocolException;

        public void writeNull() throws OutputProtocolException;

        public void writeNumber(double value) throws OutputProtocolException;

        public void writeNumber(int value) throws OutputProtocolException;

        public void writeNumber(long value) throws OutputProtocolException;

        public void writeStartArray() throws OutputProtocolException;

        public void writeStartObject() throws OutputProtocolException;

        public void writeString(String value) throws OutputProtocolException;
    }

    protected abstract class NestedOutputProtocol extends AbstractOutputProtocol {
        @Override
        public void writeBinary(final byte[] value) throws OutputProtocolException {
            writeString(Base64.getEncoder().encodeToString(value));
        }

        @Override
        public void writeBool(final boolean value) throws OutputProtocolException {
            generator.writeBoolean(value);
        }

        @Override
        public void writeByte(final byte value) throws OutputProtocolException {
            generator.writeNumber(value);
        }

        @Override
        public void writeDateTime(final Date value) throws OutputProtocolException {
            generator.writeDateTime(value);
        }

        @Override
        public void writeDouble(final double value) throws OutputProtocolException {
            generator.writeNumber(value);
        }

        @Override
        public void writeI16(final short value) throws OutputProtocolException {
            generator.writeNumber(value);
        }

        @Override
        public void writeI32(final int value) throws OutputProtocolException {
            generator.writeNumber(value);
        }

        @Override
        public void writeI64(final long value) throws OutputProtocolException {
            generator.writeNumber(value);
        }

        @Override
        public void writeListBegin(final Type elementType, final int size) throws OutputProtocolException {
            generator.writeStartArray();
            _getOutputProtocolStack().push(_createArrayOutputProtocol());
        }

        @Override
        public void writeListEnd() throws OutputProtocolException {
            generator.writeEndArray();
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType, final int size)
                throws OutputProtocolException {
            generator.writeStartObject();
            _getOutputProtocolStack().push(_createMapObjectOutputProtocol());
        }

        @Override
        public void writeMapEnd() throws OutputProtocolException {
            generator.writeEndObject();
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            generator.writeNull();
        }

        @Override
        public void writeString(final String value) throws OutputProtocolException {
            generator.writeString(value);
        }

        @Override
        public void writeStructBegin(final String name) throws OutputProtocolException {
            generator.writeStartObject();
            _getOutputProtocolStack().push(_createStructObjectOutputProtocol());
        }

        @Override
        public void writeStructEnd() throws OutputProtocolException {
            generator.writeEndObject();
        }
    }

    protected class RootOutputProtocol extends NestedOutputProtocol {
        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }
    }

    protected class StructObjectOutputProtocol extends NestedOutputProtocol {
        @Override
        public void writeFieldBegin(final String name, final Type type, final short id) throws OutputProtocolException {
            if (id != FieldBegin.ABSENT_ID) {
                generator.writeFieldName(id + ":" + name);
            } else {
                generator.writeFieldName(name);
            }
        }

        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }
    }

    private class ArrayOutputProtocol extends NestedOutputProtocol {
    }

    private class MapObjectOutputProtocol extends NestedOutputProtocol {
        @Override
        public final void writeBool(final boolean value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Boolean.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeBool(value);
            }
        }

        @Override
        public void writeByte(final byte value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Byte.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeByte(value);
            }
        }

        @Override
        public void writeDouble(final double value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Double.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeDouble(value);
            }
        }

        @Override
        public void writeI16(final short value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Short.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeI16(value);
            }
        }

        @Override
        public void writeI32(final int value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Integer.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeI32(value);
            }
        }

        @Override
        public void writeI64(final long value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                writeString(Long.toString(value));
            } else {
                nextWriteIsKey = true;
                super.writeI64(value);
            }
        }

        @Override
        public void writeListBegin(final Type elementType, final int size) throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new OutputProtocolException("expected value");
            } else {
                nextWriteIsKey = true;
                super.writeListBegin(elementType, size);
            }
        }

        @Override
        public void writeMapBegin(final Type keyType, final Type valueType, final int size)
                throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new OutputProtocolException("expected value");
            } else {
                nextWriteIsKey = true;
                super.writeMapBegin(keyType, valueType, size);
            }
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new OutputProtocolException("expected value");
            } else {
                nextWriteIsKey = true;
                super.writeNull();
            }
        }

        @Override
        public void writeString(final String value) throws OutputProtocolException {
            if (nextWriteIsKey) {
                nextWriteIsKey = false;
                generator.writeFieldName(value);
            } else {
                nextWriteIsKey = true;
                super.writeString(value);
            }
        }

        @Override
        public void writeStructBegin(final String name) throws OutputProtocolException {
            if (nextWriteIsKey) {
                throw new OutputProtocolException("expected value");
            } else {
                nextWriteIsKey = true;
                super.writeStructBegin(name);
            }
        }

        private boolean nextWriteIsKey = true;
    }

    protected JsonOutputProtocol(final JsonGenerator generator) {
        this.generator = generator;
        _getOutputProtocolStack().push(_createRootOutputProtocol());
    }

    @Override
    public void flush() throws OutputProtocolException {
        generator.flush();
    }

    protected ArrayOutputProtocol _createArrayOutputProtocol() {
        return new ArrayOutputProtocol();
    }

    protected MapObjectOutputProtocol _createMapObjectOutputProtocol() {
        return new MapObjectOutputProtocol();
    }

    protected RootOutputProtocol _createRootOutputProtocol() {
        return new RootOutputProtocol();
    }

    protected StructObjectOutputProtocol _createStructObjectOutputProtocol() {
        return new StructObjectOutputProtocol();
    }

    private final JsonGenerator generator;
}
