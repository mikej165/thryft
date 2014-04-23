package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

public final class MapBegin {
    public MapBegin(final Type keyType, final Type valueType, final int size) {
        this.keyType = checkNotNull(keyType);
        this.size = size;
        this.valueType = checkNotNull(valueType);
    }

    public Type getKeyType() {
        return keyType;
    }

    public int getSize() {
        return size;
    }

    public Type getValueType() {
        return valueType;
    }

    private final Type keyType;
    private final int size;
    private final Type valueType;
}
