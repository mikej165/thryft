package org.thryft.protocol;

@SuppressWarnings("serial")
public class UncheckedInputProtocolException extends RuntimeException {
    public UncheckedInputProtocolException(final InputProtocolException cause) {
        super(cause);
    }
}
