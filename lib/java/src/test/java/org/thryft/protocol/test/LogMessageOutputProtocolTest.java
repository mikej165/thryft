package org.thryft.protocol.test;

import java.io.StringWriter;

import org.thryft.protocol.LogMessageOutputProtocol;

public final class LogMessageOutputProtocolTest extends ProtocolTest {
    @Override
    protected void _test(final ProtocolTestStruct expected) throws Exception {
        final StringWriter writer = new StringWriter();
        final LogMessageOutputProtocol oprot = new LogMessageOutputProtocol(writer);
        expected.writeAsStruct(oprot);
        oprot.flush();
        // System.out.println(writer.toString());
    }
}
