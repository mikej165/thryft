package org.thryft.protocol;

public enum MessageType {
    CALL(1), REPLY(2), EXCEPTION(3), ONEWAY(4);

    private MessageType(final int value) {
        this.value = value;
    }

    public int value() {
        return value;
    }

    private int value;
}
