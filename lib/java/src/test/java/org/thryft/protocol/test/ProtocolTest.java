package org.thryft.protocol.test;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;
import java.io.StringWriter;
import java.io.Writer;
import java.math.BigDecimal;

import org.apache.thrift.TBase;
import org.apache.thrift.protocol.TProtocol;
import org.joda.time.DateTime;
import org.junit.Test;
import org.thryft.protocol.Protocol;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class ProtocolTest {
    @Test
    public void testBool() throws Exception {
        __test(new ProtocolTestStruct.Builder().setBoolField(true).build());
    }

    @Test
    public void testByte() throws Exception {
        __test(new ProtocolTestStruct.Builder().setByteField((byte) 1).build());
    }

    @Test
    public void testDate() throws Exception {
        __test(new ProtocolTestStruct.Builder().setDateField(DateTime.now())
                .build());
    }

    @Test
    public void testDateTime() throws Exception {
        __test(new ProtocolTestStruct.Builder()
                .setDateTimeField(DateTime.now()).build());
    }

    @Test
    public void testDecimal() throws Exception {
        __test(new ProtocolTestStruct.Builder().setDecimalField(
                new BigDecimal(100)).build());
    }

    @Test
    public void testEnum() throws Exception {
        __test(new ProtocolTestStruct.Builder().setEnumField(
                ProtocolTestEnum.ENUMERATOR2).build());
    }

    @Test
    public void testI16() throws Exception {
        __test(new ProtocolTestStruct.Builder().setI16Field((short) 1).build());
    }

    @Test
    public void testI32() throws Exception {
        __test(new ProtocolTestStruct.Builder().setI32Field(1).build());
    }

    @Test
    public void testI64() throws Exception {
        __test(new ProtocolTestStruct.Builder().setI64Field((long) 1).build());
    }

    @Test
    public void testListString() throws Exception {
        __test(new ProtocolTestStruct.Builder().setListStringField(
                ImmutableList.of("test")).build());
    }

    @Test
    public void testMapStringString() throws Exception {
        __test(new ProtocolTestStruct.Builder().setMapStringStringField(
                ImmutableMap.of("testkey", "testvalue")).build());
    }

    @Test
    public void testSetString() throws Exception {
        __test(new ProtocolTestStruct.Builder().setSetStringField(
                ImmutableSet.of("test")).build());
    }

    @Test
    public void testString() throws Exception {
        __test(new ProtocolTestStruct.Builder().setStringField("test").build());
    }

    @Test
    public void testStruct() throws Exception {
        __test(new ProtocolTestStruct.Builder().setStructField(
                new ProtocolTestStruct()).build());
    }

    protected abstract Protocol _newProtocol(Reader reader)
            throws IOException;

    protected abstract Protocol _newProtocol(Writer writer)
            throws IOException;

    private void __test(final TBase<?, ?> expected) throws Exception {
        final StringWriter writer = new StringWriter();
        final Protocol oprot = _newProtocol(writer);
        expected.write(oprot);
        oprot.flush();

        final String ostring = writer.toString();

        final StringReader reader = new StringReader(ostring);
        final Protocol iprot = _newProtocol(reader);
        final TBase<?, ?> actual = expected.getClass()
                .getConstructor(TProtocol.class).newInstance(iprot);
        assertEquals(expected, actual);
    }
}
