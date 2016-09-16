package org.thryft.protocol;

@SuppressWarnings("serial")
public abstract class ProtocolException extends Exception {
    public ProtocolException(final Throwable cause) {
        super(cause);
    }

    protected ProtocolException(final String message) {
        super(message);
    }
}
