package org.thryft.core.protocol.test;

public enum ProtocolTestEnum {
    ENUMERATOR1(1),
    ENUMERATOR2(2);

    private ProtocolTestEnum(int value) {
        this.value = value;
    }
    
    public static ProtocolTestEnum valueOf(final int value) {
        switch (value) {
        case 1: return ENUMERATOR1;
        case 2: return ENUMERATOR2;
        default: throw new IllegalArgumentException();
        }
    }

    public static ProtocolTestEnum valueOf(final Integer value) {
        return valueOf(value.intValue());
    }

    public final int value() {
        return value;
    }
        
    private final int value;
}
