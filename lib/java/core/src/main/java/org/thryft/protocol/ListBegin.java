package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Objects;

public final class ListBegin {
    public ListBegin(final Type elementType, final int size) {
        this.elementType = checkNotNull(elementType);
        this.size = size;
    }

    public Type getElementType() {
        return elementType;
    }

    public int getSize() {
        return size;
    }

    @Override
    public String toString() {
        return Objects.toStringHelper(this).add("elementType", elementType)
                .add("size", size).toString();
    }

    private final Type elementType;
    private final int size;
}
