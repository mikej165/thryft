package org.thryft.protocol.test;

import static org.hamcrest.Matchers.instanceOf;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertThat;

import java.util.Map;

import org.thryft.protocol.BuiltinsOutputProtocol;

public final class BuiltinsOutputProtocolTest extends ProtocolTest {
    @Override
    protected void _test(final ProtocolTestStruct expected) throws Exception {
        final BuiltinsOutputProtocol oprot = new BuiltinsOutputProtocol();
        expected.writeAsStruct(oprot);
        assertNotEquals(null, oprot.getValue());
        assertThat(oprot.getValue(), instanceOf(Map.class));
    }
}
