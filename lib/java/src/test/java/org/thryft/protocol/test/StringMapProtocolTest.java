package org.thryft.protocol.test;

import static org.junit.Assert.assertEquals;

import org.apache.thrift.TBase;
import org.apache.thrift.protocol.TProtocol;
import org.thryft.protocol.StringMapProtocol;

import com.google.common.collect.ImmutableMap;

public class StringMapProtocolTest extends ProtocolTest {
    @Override
    protected void _test(final TBase<?, ?> expected) throws Exception {
        final StringMapProtocol oprot = new StringMapProtocol();
        expected.write(oprot);
        final ImmutableMap<String, String> ostringMap = oprot.toStringMap();

        final StringMapProtocol iprot = new StringMapProtocol(ostringMap);
        final TBase<?, ?> actual = expected.getClass()
                .getConstructor(TProtocol.class).newInstance(iprot);
        assertEquals(expected, actual);
    }
}
