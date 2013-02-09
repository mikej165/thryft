package org.thryft.web.server.store.test;

import java.io.IOException;

import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.SimpleDbStore;

public class SimpleDbStoreTest extends AwsKeyValueStoreTest {
    public static SimpleDbStore.Configuration getSimpleDbStoreConfiguration()
            throws IOException {
        if (simpleDbStoreConfiguration == null) {
            simpleDbStoreConfiguration = new SimpleDbStore.Configuration(
                    AwsKeyValueStoreTest.getCredentials(), "yogento-test-");
        }

        return simpleDbStoreConfiguration;
    }

    @Before
    public void setUp() throws IOException {
        super._setUp(new SimpleDbStore<ProtocolTestStruct>(
                getSimpleDbStoreConfiguration(), ProtocolTestStruct.class));
    }

    private static SimpleDbStore.Configuration simpleDbStoreConfiguration = null;
}
