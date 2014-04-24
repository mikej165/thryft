package org.thryft.protocol;

public abstract class JsonInputProtocol<InputProtocolT extends InputProtocol>
        extends StackedInputProtocol<InputProtocolT> {
    public abstract Type getCurrentFieldType();

    public abstract void reset();
}
