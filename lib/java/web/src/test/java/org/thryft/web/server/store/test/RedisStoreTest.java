package org.thryft.web.server.store.test;

import java.io.IOException;

import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.RedisStore;

public class RedisStoreTest extends StoreTest {
    @Before
    public void setUp() throws IOException {
        super._setUp(new RedisStore<ProtocolTestStruct>(CONFIGURATION,
                ProtocolTestStruct.class));
    }

    public final static RedisStore.Configuration CONFIGURATION = new RedisStore.Configuration(
            "localhost", 6379);
}
