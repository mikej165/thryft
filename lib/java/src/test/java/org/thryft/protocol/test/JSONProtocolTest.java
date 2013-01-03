package org.thryft.protocol.test;

import static org.junit.Assert.assertEquals;

import java.io.StringReader;
import java.io.StringWriter;

import org.apache.thrift.TBase;
import org.apache.thrift.protocol.TProtocol;
import org.thryft.protocol.JSONProtocol;
import org.thryft.protocol.Protocol;

public class JSONProtocolTest extends ProtocolTest {
    @Override
    protected void _test(final TBase<?, ?> expected) throws Exception {
        final StringWriter writer = new StringWriter();
        final Protocol oprot = new JSONProtocol(writer);
        expected.write(oprot);
        oprot.flush();

        final String ostring = writer.toString();

        final StringReader reader = new StringReader(ostring);
        final Protocol iprot = new JSONProtocol(reader);
        final TBase<?, ?> actual = expected.getClass()
                .getConstructor(TProtocol.class).newInstance(iprot);
        assertEquals(expected, actual);
    }
}
