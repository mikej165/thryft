package org.thryft.web.server.store.test;

import java.io.IOException;

import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.MemStore;

public class MemStoreTest extends StoreTest {
    @Before
    public void setUp() throws IOException {
        super._setUp(new MemStore<ProtocolTestStruct>(ProtocolTestStruct.class));
    }
}
