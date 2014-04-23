package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Objects;

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

    @Override
    public String toString() {
        return Objects.toStringHelper(this).add("keyType", keyType)
                .add("valueType", valueType).add("size", size).toString();
    }

    private final Type keyType;
    private final int size;
    private final Type valueType;
}
