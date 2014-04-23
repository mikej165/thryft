package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

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

    private final Type elementType;
    private final int size;
}
