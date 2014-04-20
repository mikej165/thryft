package org.thryft.protocol;

@SuppressWarnings("serial")
public abstract class ProtocolException extends Exception {
    public ProtocolException(final Exception cause) {
        super(cause.getMessage());
    }

    protected ProtocolException(final String message) {
        super(message);
    }
}
