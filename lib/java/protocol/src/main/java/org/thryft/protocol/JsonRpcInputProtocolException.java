package org.thryft.protocol;

@SuppressWarnings("serial")
public final class JsonRpcInputProtocolException extends InputProtocolException {
    public JsonRpcInputProtocolException(final Exception cause, final int code) {
        super(cause);
        this.code = code;
    }

    public JsonRpcInputProtocolException(final int code, final String message) {
        super(message);
        this.code = code;
    }

    public int getCode() {
        return code;
    }

    private final int code;
}
