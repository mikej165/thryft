package org.thryft.protocol;

@SuppressWarnings("serial")
public class InputProtocolException extends ProtocolException {
    public InputProtocolException(final Exception cause) {
        super(cause);
    }

    public InputProtocolException(final String message) {
        super(message);
    }
}
