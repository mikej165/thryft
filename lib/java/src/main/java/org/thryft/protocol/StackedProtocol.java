package org.thryft.protocol;

import java.util.Stack;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TStruct;

public class StackedProtocol extends Protocol {
    @Override
    public final boolean readBool() throws TException {
        return protocolStack.peek().readBool();
    }

    @Override
    public final byte readByte() throws TException {
        return protocolStack.peek().readByte();
    }

    @Override
    public final double readDouble() throws TException {
        return protocolStack.peek().readDouble();
    }

    @Override
    public final TField readFieldBegin() throws TException {
        return protocolStack.peek().readFieldBegin();
    }

    @Override
    public final void readFieldEnd() throws TException {
        protocolStack.peek().readFieldEnd();
    }

    @Override
    public final short readI16() throws TException {
        return protocolStack.peek().readI16();
    }

    @Override
    public final int readI32() throws TException {
        return protocolStack.peek().readI32();
    }

    @Override
    public final long readI64() throws TException {
        return protocolStack.peek().readI64();
    }

    @Override
    public final TList readListBegin() throws TException {
        return protocolStack.peek().readListBegin();
    }

    @Override
    public final void readListEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public final TMap readMapBegin() throws TException {
        return protocolStack.peek().readMapBegin();
    }

    @Override
    public final void readMapEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public final String readString() throws TException {
        return protocolStack.peek().readString();
    }

    @Override
    public final TStruct readStructBegin() throws TException {
        return protocolStack.peek().readStructBegin();
    }

    @Override
    public final void readStructEnd() throws TException {
        protocolStack.pop();
    }

    @Override
    public final void writeBool(final boolean b) throws TException {
        protocolStack.peek().writeBool(b);
    }

    @Override
    public final void writeByte(final byte b) throws TException {
        protocolStack.peek().writeByte(b);
    }

    @Override
    public final void writeDouble(final double dub) throws TException {
        protocolStack.peek().writeDouble(dub);
    }

    @Override
    public final void writeFieldBegin(final TField field) throws TException {
        protocolStack.peek().writeFieldBegin(field);
    }

    @Override
    public final void writeFieldEnd() throws TException {
        protocolStack.peek().writeFieldEnd();
    }

    @Override
    public final void writeFieldStop() throws TException {
        protocolStack.peek().writeFieldStop();
    }

    @Override
    public final void writeI16(final short i16) throws TException {
        protocolStack.peek().writeI16(i16);
    }

    @Override
    public final void writeI32(final int i32) throws TException {
        protocolStack.peek().writeI32(i32);
    }

    @Override
    public final void writeI64(final long i64) throws TException {
        protocolStack.peek().writeI64(i64);
    }

    @Override
    public final void writeListBegin(final TList list) throws TException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeListBegin(list);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new TException(
                    "writeListBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public final void writeListEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeListEnd();
    }

    @Override
    public final void writeMapBegin(final TMap map) throws TException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeMapBegin(map);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new TException(
                    "writeMapBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public final void writeMapEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeMapEnd();
    }

    @Override
    public final void writeMixed(final Object value) throws TException {
        protocolStack.peek().writeMixed(value);
    }

    @Override
    public final void writeString(final String str) throws TException {
        protocolStack.peek().writeString(str);
    }

    @Override
    public final void writeStructBegin(final TStruct struct) throws TException {
        final int protocolStackSize = protocolStack.size();
        protocolStack.peek().writeStructBegin(struct);
        if (protocolStack.size() != protocolStackSize + 1) {
            throw new TException(
                    "writeStructBegin must add one protocol to the top of the stack");
        }
    }

    @Override
    public final void writeStructEnd() throws TException {
        protocolStack.pop();
        protocolStack.peek().writeStructEnd();
    }

    protected Stack<Protocol> _getProtocolStack() {
        return protocolStack;
    }

    private final Stack<Protocol> protocolStack = new Stack<Protocol>();
}