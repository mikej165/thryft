package org.thryft.protocol;

@SuppressWarnings("serial")
public class OutputProtocolException extends ProtocolException {
    public OutputProtocolException(final Exception cause) {
        super(cause);
    }

    public OutputProtocolException(final String message) {
        super(message);
    }
}
