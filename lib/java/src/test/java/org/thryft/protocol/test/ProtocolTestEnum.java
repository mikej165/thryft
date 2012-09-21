package org.thryft.protocol.test;

public enum ProtocolTestEnum {
    ENUMERATOR1(1),
    ENUMERATOR2(2);

    private ProtocolTestEnum(int value) {
        this.value = value;
    }

    public static ProtocolTestEnum byName(final String name) {
        try {
            return valueOf(name);
        } catch (IllegalArgumentException e1) {
            try {
                return byValue(Integer.parseInt(name));
            } catch (NumberFormatException e2) {
                throw e1;
            }
        }
    }
    
    public static ProtocolTestEnum byValue(final int value) {
        switch (value) {
        case 1: return ENUMERATOR1;
        case 2: return ENUMERATOR2;
        default: throw new IllegalArgumentException();
        }
    }

    public final int value() {
        return value;
    }
        
    private final int value;
}
