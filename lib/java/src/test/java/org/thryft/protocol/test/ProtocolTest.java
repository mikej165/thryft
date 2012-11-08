package org.thryft.protocol.test;

import java.math.BigDecimal;

import org.apache.thrift.TBase;
import org.joda.time.DateTime;
import org.junit.Test;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class ProtocolTest {
    @Test
    public void testBool() throws Exception {
        _test(new ProtocolTestStruct.Builder().setBoolField(true).build());
    }

    @Test
    public void testByte() throws Exception {
        _test(new ProtocolTestStruct.Builder().setByteField((byte) 1).build());
    }

    @Test
    public void testDate() throws Exception {
        _test(new ProtocolTestStruct.Builder().setDateField(DateTime.now())
                .build());
    }

    @Test
    public void testDateTime() throws Exception {
        _test(new ProtocolTestStruct.Builder().setDateTimeField(DateTime.now())
                .build());
    }

    @Test
    public void testDecimal() throws Exception {
        _test(new ProtocolTestStruct.Builder().setDecimalField(
                new BigDecimal(100)).build());
    }

    @Test
    public void testEnum() throws Exception {
        _test(new ProtocolTestStruct.Builder().setEnumField(
                ProtocolTestEnum.ENUMERATOR2).build());
    }

    @Test
    public void testI16() throws Exception {
        _test(new ProtocolTestStruct.Builder().setI16Field((short) 1).build());
    }

    @Test
    public void testI32() throws Exception {
        _test(new ProtocolTestStruct.Builder().setI32Field(1).build());
    }

    @Test
    public void testI64() throws Exception {
        _test(new ProtocolTestStruct.Builder().setI64Field((long) 1).build());
    }

    @Test
    public void testListString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setListStringField(
                ImmutableList.of("test")).build());

        // Empty list
        _test(new ProtocolTestStruct.Builder().setListStringField(
                ImmutableList.<String> of()).build());
    }

    @Test
    public void testMapStringString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setMapStringStringField(
                ImmutableMap.of("testkey", "testvalue")).build());

        // Empty map
        _test(new ProtocolTestStruct.Builder().setMapStringStringField(
                ImmutableMap.<String, String> of()).build());
    }

    @Test
    public void testSetString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setSetStringField(
                ImmutableSet.of("test")).build());

        // Empty set
        _test(new ProtocolTestStruct.Builder().setSetStringField(
                ImmutableSet.<String> of()).build());
    }

    @Test
    public void testString() throws Exception {
        _test(new ProtocolTestStruct.Builder().setStringField("test").build());
    }

    @Test
    public void testStruct() throws Exception {
        _test(new ProtocolTestStruct.Builder().setStructField(
                new ProtocolTestStruct.Builder().setI32Field(1).build())
                .build());

        // Empty struct
        _test(new ProtocolTestStruct.Builder().setStructField(
                new ProtocolTestStruct()).build());
    }

    protected abstract void _test(final TBase<?, ?> expected) throws Exception;
}
