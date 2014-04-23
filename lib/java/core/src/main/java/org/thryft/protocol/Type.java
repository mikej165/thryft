package org.thryft.protocol;

public enum Type {
    STOP(0), VOID(1), BOOL(2), BYTE(3), DOUBLE(4), I16(6), I32(8), I64(10), STRING(
            11), STRUCT(12), MAP(13), SET(14), LIST(15), ENUM(16);

    private Type(final int value) {
        this.value = value;
    }

    public int value() {
        return value;
    }

    private int value;
}
