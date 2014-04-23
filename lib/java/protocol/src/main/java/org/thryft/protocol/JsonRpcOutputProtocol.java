package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

public final class JsonRpcOutputProtocol extends ForwardingOutputProtocol {
    public JsonRpcOutputProtocol(final JacksonJsonOutputProtocol jsonOutputProtocol) {
        this.jsonOutputProtocol = checkNotNull(jsonOutputProtocol);
    }

    @Override
    public void writeMessageBegin(final String name, final MessageType type,
            final Object id) throws OutputProtocolException {
        writeStructBegin("JSON-RPC");

        writeFieldBegin("jsonrpc", org.thryft.protocol.Type.STRING, (short) -1);
        writeString("2.0");
        writeFieldEnd();

        if (id instanceof Integer) {
            writeFieldBegin("id", org.thryft.protocol.Type.I32, (short) -1);
            writeI32((Integer) id);
            writeFieldEnd();
        } else if (id instanceof Long) {
            writeFieldBegin("id", org.thryft.protocol.Type.I32, (short) -1);
            writeI64((Long) id);
            writeFieldEnd();
        } else if (id instanceof String) {
            writeFieldBegin("id", org.thryft.protocol.Type.STRING, (short) -1);
            writeString((String) id);
            writeFieldEnd();
        } else {
            throw new IllegalArgumentException(id.getClass().getCanonicalName());
        }

        switch (type) {
        case CALL:
        case ONEWAY:
            writeFieldBegin("method", org.thryft.protocol.Type.STRING,
                    (short) -1);
            writeString(name);
            writeFieldEnd();

            writeFieldBegin("params", org.thryft.protocol.Type.VOID, (short) -1);
            break;

        case EXCEPTION:
            writeFieldBegin("error", org.thryft.protocol.Type.VOID, (short) -1);
            break;

        case REPLY:
            writeFieldBegin("result", org.thryft.protocol.Type.VOID, (short) -1);
            break;

        default:
            throw new UnsupportedOperationException();
        }
    }

    @Override
    public void writeMessageEnd() throws OutputProtocolException {
        writeFieldEnd();
        writeFieldStop();
        writeStructEnd();
    }

    @Override
    protected OutputProtocol _delegate() {
        return jsonOutputProtocol;
    }

    private final JacksonJsonOutputProtocol jsonOutputProtocol;
}
