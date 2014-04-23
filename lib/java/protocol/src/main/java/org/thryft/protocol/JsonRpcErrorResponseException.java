package org.thryft.protocol;

@SuppressWarnings("serial")
public final class JsonRpcErrorResponseException extends RuntimeException {
    public JsonRpcErrorResponseException(final int code, final String message) {
        super(message);
        this.code = code;
    }

    public int getCode() {
        return code;
    }

    private final int code;
}
