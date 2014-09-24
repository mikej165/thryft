package org.thryft.protocol;

public enum Type {
    STOP(0),
    VOID_(1),
    BOOL(2),
    BYTE(3),
    DOUBLE(4),
    FLOAT(18),
    I16(6),
    I32(8),
    I64(10),
    LIST(15),
    MAP(13),
    SET(14),
    STRING(11),
    STRUCT(12),
    U64(9);

    private Type(int value) {
        this.value = value;
    }

    public static Type valueOf(final int value) {
        switch (value) {
        case 0: return STOP;
        case 1: return VOID_;
        case 2: return BOOL;
        case 3: return BYTE;
        case 4: return DOUBLE;
        case 18: return FLOAT;
        case 6: return I16;
        case 8: return I32;
        case 10: return I64;
        case 15: return LIST;
        case 13: return MAP;
        case 14: return SET;
        case 11: return STRING;
        case 12: return STRUCT;
        case 9: return U64;
        default: throw new IllegalArgumentException();
        }
    }

    public static Type valueOf(final Integer value) {
        return valueOf(value.intValue());
    }

    public final int value() {
        return value;
    }

    private final int value;
}
