package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

public final class MessageBegin {
    public MessageBegin(final String name, final MessageType type,
            final int sequenceId) {
        this.name = checkNotNull(name);
        this.type = checkNotNull(type);
        this.sequenceId = sequenceId;
    }

    public String getName() {
        return name;
    }

    public int getSequenceId() {
        return sequenceId;
    }

    public MessageType getType() {
        return type;
    }

    private final String name;
    private final int sequenceId;
    private final MessageType type;
}
