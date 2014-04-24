package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import org.thryft.Base;

@SuppressWarnings("serial")
public final class JsonRpcErrorResponse extends RuntimeException implements
        Base<JsonRpcErrorResponse> {
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

    @Override
    public int compareTo(final JsonRpcErrorResponse other) {
        throw new UnsupportedOperationException();
    }

    public int getCode() {
        return code;
    }

    @Override
    public void write(final OutputProtocol oprot)
            throws OutputProtocolException {
        oprot.writeStructBegin("error");

        oprot.writeFieldBegin("code", org.thryft.protocol.Type.I32, (short) -1);
        oprot.writeI32(code);
        oprot.writeFieldEnd();

        // if (jsonRpcErrorData != null && jsonRpcErrorData instanceof
        // org.thryft.TBase<?>) {
        // oprot.writeFieldBegin(new org.thryft.protocol.TField("@class",
        // org.thryft.protocol.TType.STRING, (short)-1));
        // oprot.writeString(jsonRpcErrorData.getClass().getName());
        // oprot.writeFieldEnd();
        // oprot.writeFieldBegin(new org.thryft.protocol.TField("data",
        // org.thryft.protocol.TType.STRUCT, (short)-1));
        // ((org.thryft.TBase<?>)jsonRpcErrorData).write(oprot);
        // oprot.writeFieldEnd();
        // }

        oprot.writeFieldBegin("message", org.thryft.protocol.Type.STRING,
                (short) -1);
        oprot.writeString(getMessage());
        oprot.writeFieldEnd();

        oprot.writeStructEnd();
    }

    private final int code;
}
