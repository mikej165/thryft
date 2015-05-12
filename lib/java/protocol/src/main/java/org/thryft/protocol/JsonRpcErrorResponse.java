package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import org.thryft.CompoundType;

@SuppressWarnings("serial")
public final class JsonRpcErrorResponse extends RuntimeException implements
CompoundType {
    public static JsonRpcErrorResponse read(final InputProtocol iprot)
            throws InputProtocolException {
        int code = 0;
        String message = "";
        iprot.readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin errorFieldBegin = iprot
                    .readFieldBegin();
            if (errorFieldBegin.getType() == org.thryft.protocol.Type.STOP) {
                break;
            } else if (errorFieldBegin.getName().equalsIgnoreCase("code")) {
                code = iprot.readI32();
            } else if (errorFieldBegin.getName().equalsIgnoreCase("message")) {
                message = iprot.readString();
            }
            iprot.readFieldEnd();
        }
        iprot.readStructEnd();
        return new JsonRpcErrorResponse(code, message);
    }

    public JsonRpcErrorResponse(final Exception cause, final int code,
            final String message) {
        super(checkNotNull(message), checkNotNull(cause));
        this.code = code;
    }

    public JsonRpcErrorResponse(final int code, final String message) {
        super(checkNotNull(message));
        this.code = code;
    }

    public JsonRpcErrorResponse(final JsonRpcInputProtocolException e) {
        this(e.getCode(), e.getMessage());
    }

    public boolean equals(final JsonRpcErrorResponse other) {
        if (code != other.code) {
            return false;
        } else if (!getMessage().equals(other.getMessage())) {
            return false;
        }
        return true;
    }

    @Override
    public boolean equals(final Object obj) {
        if (obj == this) {
            return true;
        } else if (!(obj instanceof JsonRpcErrorResponse)) {
            return false;
        } else {
            return equals((JsonRpcErrorResponse) obj);
        }
    }

    public int getCode() {
        return code;
    }

    @Override
    public int hashCode() {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeAsList(final OutputProtocol oprot)
            throws OutputProtocolException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeAsStruct(final OutputProtocol oprot)
            throws OutputProtocolException {
        oprot.writeStructBegin("error");

        oprot.writeFieldBegin("code", org.thryft.protocol.Type.I32, (short) -1);
        oprot.writeI32(code);
        oprot.writeFieldEnd();

        if (getCause() instanceof org.thryft.Exception) {
            oprot.writeFieldBegin("@class", Type.STRING, (short) -1);
            oprot.writeString(((org.thryft.Exception) getCause())
                    .getThriftQualifiedClassName());
            oprot.writeFieldEnd();
            oprot.writeFieldBegin("data", Type.STRUCT, (short) -1);
            ((CompoundType) getCause()).writeAsStruct(oprot);
            oprot.writeFieldEnd();
        }

        oprot.writeFieldBegin("message", org.thryft.protocol.Type.STRING,
                (short) -1);
        oprot.writeString(getMessage());
        oprot.writeFieldEnd();

        oprot.writeStructEnd();
    }

    private final int code;
}
