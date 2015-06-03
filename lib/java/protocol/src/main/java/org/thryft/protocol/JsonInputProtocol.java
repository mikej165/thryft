package org.thryft.protocol;

public abstract class JsonInputProtocol<InputProtocolT extends JsonInputProtocol<?>.NestedInputProtocol>
extends StackedInputProtocol<InputProtocolT> {
    public abstract class NestedInputProtocol extends AbstractInputProtocol {
        public abstract Type getType();

        @Override
        public final byte[] readBinary() throws InputProtocolException {
            return _decodeBase64(readString());
        }

        @Override
        public final byte readByte() throws InputProtocolException {
            return (byte) readI32();
        }

        @Override
        public final short readI16() throws InputProtocolException {
            return (short) readI32();
        }

        protected abstract byte[] _decodeBase64(final String base64String);
    }

    public final Type getCurrentFieldType() {
        if (!_getInputProtocolStack().isEmpty()) {
            return _getInputProtocolStack().peek().getType();
        } else {
            return Type.VOID_;
        }
    }

    public abstract void reset();
}
