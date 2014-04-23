package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Objects;

public class FieldBegin {
    public FieldBegin() {
        this("", Type.STOP, (short) 0);
    }

    public FieldBegin(final String name, final Type type, final short id) {
        this.id = id;
        this.name = checkNotNull(name);
        this.type = checkNotNull(type);
    }

    @Override
    public String toString() {
        return Objects.toStringHelper(this).add("id", id).add("name", name)
                .add("type", type).toString();
    }

    public final short id;
    public final String name;
    public final Type type;
}
