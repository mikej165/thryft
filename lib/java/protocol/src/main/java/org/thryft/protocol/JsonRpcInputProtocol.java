package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

public final class JsonRpcInputProtocol extends ForwardingInputProtocol {
    public JsonRpcInputProtocol(final JsonInputProtocol<?> jsonInputProtocol) {
        this.jsonInputProtocol = checkNotNull(jsonInputProtocol);
    }

    public Type getCurrentFieldType() {
        return jsonInputProtocol.getCurrentFieldType();
    }

    @Override
    public MessageBegin readMessageBegin() throws InputProtocolException {
        Object id = null;
        String jsonrpc = null;
        String method = "";
        MessageType type = null;
        boolean haveParams = false;

        // Two passes:
        // 1. Read "id", "jsonrpc", and infer the message type
        // 2. Read type-specific fields
        readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin fieldBegin = readFieldBegin();
            if (fieldBegin.getType() == org.thryft.protocol.Type.STOP) {
                break;
            }
            switch (fieldBegin.getName().toLowerCase()) {
            case "id":
                id = readMixed();
                break;
            case "jsonrpc":
                jsonrpc = readString();
                break;
            case "method":
                if (type != null) {
                    throw new JsonRpcInputProtocolException(-32700,
                            "unable to determine message type");
                }
                method = readString();
                type = MessageType.CALL;
                break;
            case "params":
                haveParams = true;
                break;
            case "error":
                if (type != null) {
                    throw new JsonRpcInputProtocolException(-32700,
                            "unable to determine message type");
                }
                type = MessageType.EXCEPTION;
                break;
            case "result":
                if (type != null) {
                    throw new JsonRpcInputProtocolException(-32700,
                            "unable to determine message type");
                }
                type = MessageType.REPLY;
                break;
            }
            readFieldEnd();
        }
        if (type == null) {
            throw new JsonRpcInputProtocolException(-32700,
                    "unable to determine message type");
        }
        if (id == null) {
            throw new JsonRpcInputProtocolException(-32700, "missing id field");
        }
        if (jsonrpc == null) {
            throw new JsonRpcInputProtocolException(-32700,
                    "missing jsonrpc field");
        } else if (!jsonrpc.equals("2.0")) {
            throw new JsonRpcInputProtocolException(-32700,
                    "expected \"jsonrpc\" to be 2.0, got " + jsonrpc);
        }
        if (type == MessageType.CALL) {
            if (method.isEmpty()) {
                throw new JsonRpcInputProtocolException(-32601,
                        "missing method field");
            }
            if (!haveParams) {
                throw new JsonRpcInputProtocolException(-32601,
                        "missing params field");
            }
        }

        jsonInputProtocol.reset();

        readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin fieldBegin = readFieldBegin();
            if (fieldBegin.getType() == org.thryft.protocol.Type.STOP) {
                break;
            } else if (type == MessageType.CALL
                    && fieldBegin.getName().equalsIgnoreCase("params")) {
                break;
            } else if (type == MessageType.EXCEPTION
                    && fieldBegin.getName().equalsIgnoreCase("error")) {
                break;
            } else if (type == MessageType.REPLY
                    && fieldBegin.getName().equalsIgnoreCase("result")) {
                break;
            } else {
                readFieldEnd();
            }
        }
        return new MessageBegin(method, type, id);
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

    private final JsonInputProtocol<?> jsonInputProtocol;
}
