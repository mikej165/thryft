package org.thryft.protocol;

public abstract class JsonInputProtocol<InputProtocolT extends InputProtocol>
        extends StackedInputProtocol<InputProtocolT> {
    protected abstract class NestedInputProtocol extends AbstractInputProtocol {
        public abstract Type getType();
    }

    public abstract Type getCurrentFieldType();

    public abstract void reset();
}
