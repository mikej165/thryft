package org.thryft.protocol;

import java.io.IOException;
import java.nio.ByteBuffer;

import org.apache.thrift.TException;
import org.apache.thrift.protocol.TField;
import org.apache.thrift.protocol.TList;
import org.apache.thrift.protocol.TMap;
import org.apache.thrift.protocol.TMessage;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.protocol.TSet;
import org.apache.thrift.protocol.TStruct;
import org.apache.thrift.transport.TTransport;

public abstract class AbstractProtocol extends TProtocol {
    protected AbstractProtocol() {
        super(null);
    }

    protected AbstractProtocol(final TTransport trans) {
        super(trans);
    }

    public void flush() throws IOException {
    }

    @Override
    public ByteBuffer readBinary() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean readBool() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public byte readByte() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public double readDouble() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TField readFieldBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readFieldEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public short readI16() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public int readI32() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public long readI64() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TList readListBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readListEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TMap readMapBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readMapEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TMessage readMessageBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readMessageEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TSet readSetBegin() throws TException {
        final TList list = readListBegin();
        return new TSet(list.elemType, list.size);
    }

    @Override
    public void readSetEnd() throws TException {
        readListEnd();
    }

    @Override
    public String readString() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public TStruct readStructBegin() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void readStructEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeBinary(final ByteBuffer buf) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeBool(final boolean b) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeByte(final byte b) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeDouble(final double dub) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldBegin(final TField field) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeFieldStop() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI16(final short i16) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI32(final int i32) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeI64(final long i64) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeListBegin(final TList list) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeListEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMapBegin(final TMap map) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMapEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMessageBegin(final TMessage message) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeMessageEnd() throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeSetBegin(final TSet set) throws TException {
        writeListBegin(new TList(set.elemType, set.size));
    }

    @Override
    public void writeSetEnd() throws TException {
        writeListEnd();
    }

    @Override
    public void writeString(final String str) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeStructBegin(final TStruct struct) throws TException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void writeStructEnd() throws TException {
        throw new UnsupportedOperationException();
    }
}