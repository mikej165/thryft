package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Objects;

public final class MessageBegin {
    public MessageBegin(final String name, final MessageType type,
            final Object id) {
        this.name = checkNotNull(name);
        this.type = checkNotNull(type);
        this.id = checkNotNull(id);
    }

    public Object getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public MessageType getType() {
        return type;
    }

    @Override
    public String toString() {
        return Objects.toStringHelper(this).add("id", id).add("name", name)
                .add("type", type).toString();
    }

    private final Object id;
    private final String name;
    private final MessageType type;
}
