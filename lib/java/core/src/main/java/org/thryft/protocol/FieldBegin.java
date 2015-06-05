package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.MoreObjects;

public final class FieldBegin {
    public FieldBegin(final String name) {
        this(name, Type.VOID_, ABSENT_ID);
    }

    public FieldBegin(final String name, final Type type) {
        this(name, type, ABSENT_ID);
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

    public boolean hasId() {
        return id != ABSENT_ID;
    }

    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this).omitNullValues()
                .add("id", id != ABSENT_ID ? id : null).add("name", name)
                .add("type", type).toString();
    }

    private final short id;

    private final String name;
    private final Type type;
    public final static short ABSENT_ID = (short) 0;
    public final static FieldBegin STOP = new FieldBegin("", Type.STOP,
            (short) 0);
}
