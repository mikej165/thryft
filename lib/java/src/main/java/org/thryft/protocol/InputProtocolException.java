package org.thryft.protocol;

@SuppressWarnings("serial")
public class InputProtocolException extends ProtocolException {
    public InputProtocolException(final String message) {
        super(message);
    }

    public InputProtocolException(final Throwable cause) {
        super(cause);
    }
}
