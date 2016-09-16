package org.thryft.protocol;

@SuppressWarnings("serial")
public class OutputProtocolException extends ProtocolException {
    public OutputProtocolException(final String message) {
        super(message);
    }

    public OutputProtocolException(final Throwable cause) {
        super(cause);
    }
}
