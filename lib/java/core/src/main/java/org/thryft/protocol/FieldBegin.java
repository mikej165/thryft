package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.MoreObjects;

public class FieldBegin {
    public FieldBegin() {
        this("", Type.STOP, (short) 0);
    }

    public FieldBegin(final String name, final Type type, final short id) {
        this.id = id;
        this.name = checkNotNull(name);
        this.type = checkNotNull(type);
    }

    public short getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Type getType() {
        return type;
    }

    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this).add("id", id).add("name", name)
                .add("type", type).toString();
    }

    private final short id;
    private final String name;
    private final Type type;
}
