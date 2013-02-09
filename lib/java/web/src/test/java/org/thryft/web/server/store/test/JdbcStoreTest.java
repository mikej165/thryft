package org.thryft.web.server.store.test;

import java.io.File;
import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.JdbcStore;
import org.thryft.web.server.util.FileUtils;

public class JdbcStoreTest extends StoreTest {
    @Before
    public void setUp() throws IOException {
        rootDirectoryPath = FileUtils.createTempDirectory(getClass()
                .getSimpleName(), null);
        jdbcStore = new JdbcStore<ProtocolTestStruct>(
                new JdbcStore.Configuration(new File(rootDirectoryPath,
                        "yogento")), ProtocolTestStruct.class);
        super._setUp(jdbcStore);
    }

    @Override
    @After
    public void tearDown() throws IOException {
        jdbcStore.dispose();
        org.apache.commons.io.FileUtils.deleteDirectory(rootDirectoryPath);
    }

    private JdbcStore<ProtocolTestStruct> jdbcStore;

    private File rootDirectoryPath;
}
