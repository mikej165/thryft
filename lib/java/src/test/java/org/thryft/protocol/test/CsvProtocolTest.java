package org.thryft.protocol.test;

import org.apache.thrift.TBase;

public class CsvProtocolTest extends ProtocolTest {
    @Override
    protected void _test(final TBase<?, ?> expected) throws Exception {
        // final StringWriter writer = new StringWriter();
        // final Protocol oprot = new CsvProtocol(writer);
        // expected.write(oprot);
        // oprot.flush();
        //
        // final String ostring = writer.toString();

        // final StringReader reader = new StringReader(ostring);
        // final Protocol iprot = new CsvProtocol(reader);
        // final TBase<?, ?> actual = expected.getClass()
        // .getConstructor(TProtocol.class).newInstance(iprot);
        // assertEquals(expected, actual);
    }
}
