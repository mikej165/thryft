package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

public final class JsonRpcInputProtocol extends ForwardingInputProtocol {
    public JsonRpcInputProtocol(final JsonInputProtocol jsonInputProtocol) {
        this.jsonInputProtocol = checkNotNull(jsonInputProtocol);
    }

    @Override
    public MessageBegin readMessageBegin() throws InputProtocolException {
        Object id = null;
        String jsonrpc = null;

        // Two passes: one to get "id" and "jsonrpc", the other to get the
        // message type-specific fields
        readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin fieldBegin = readFieldBegin();
            if (fieldBegin.getType() == org.thryft.protocol.Type.STOP) {
                break;
            } else if (fieldBegin.getName().equalsIgnoreCase("id")) {
                id = readMixed();
            } else if (fieldBegin.getName().equalsIgnoreCase("jsonrpc")) {
                jsonrpc = readString();
            }
            readFieldEnd();
        }
        if (id == null) {
            throw new InputProtocolException("missing id field");
        }
        if (jsonrpc == null) {
            throw new InputProtocolException("missing jsonrpc field");
        } else if (!jsonrpc.equals("2.0")) {
            throw new org.thryft.protocol.InputProtocolException(
                    "expected jsonrpc in response to be 2.0, got " + jsonrpc);
        }

        jsonInputProtocol.reset();

        String name = "";
        MessageType type = null;

        readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin fieldBegin = readFieldBegin();
            if (fieldBegin.getType() == org.thryft.protocol.Type.STOP) {
                break;
            } else if (fieldBegin.getName().equalsIgnoreCase("error")) {
                int errorCode = 0;
                String errorMessage = "";
                readStructBegin();
                while (true) {
                    final org.thryft.protocol.FieldBegin errorFieldBegin = readFieldBegin();
                    if (errorFieldBegin.getType() == org.thryft.protocol.Type.STOP) {
                        break;
                    } else if (errorFieldBegin.getName().equalsIgnoreCase(
                            "code")) {
                        errorCode = readI32();
                    } else if (errorFieldBegin.getName().equalsIgnoreCase(
                            "name")) {
                        errorMessage = readString();
                    }
                    readFieldEnd();
                }
                readStructEnd(); // error struct
                readFieldEnd(); // error field
                readStructEnd(); // message struct
                throw new JsonRpcErrorResponseException(errorCode, errorMessage);
            } else if (fieldBegin.getName().equalsIgnoreCase("method")) {
                name = readString();
                type = MessageType.CALL;
                break;
            } else if (fieldBegin.getName().equalsIgnoreCase("results")) {
                type = MessageType.REPLY;
                break;
            }
            readFieldEnd();
        }
        if (type == null) {
            throw new InputProtocolException("unable to determine message type");
        } else if ((type == MessageType.CALL || type == MessageType.ONEWAY)
                && name.isEmpty()) {
            throw new InputProtocolException("missing method field");
        }
        return new MessageBegin(name, type, id);
    }

    @Override
    public void readMessageEnd() throws InputProtocolException {
        readFieldEnd();
        readStructEnd();
    }

    @Override
    protected InputProtocol _delegate() {
        return jsonInputProtocol;
    }

    private final JsonInputProtocol jsonInputProtocol;
}
