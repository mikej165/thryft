package org.thryft.web.server.store.test;

import java.io.File;
import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.FsStore;
import org.thryft.web.server.store.MemStore;
import org.thryft.web.server.store.PrimaryBackupStore;
import org.thryft.web.server.util.FileUtils;

public class PrimaryBackupStoreTest extends StoreTest {
    @Before
    public void setUp() throws IOException {
        rootDirectoryPath = FileUtils.createTempDirectory(getClass()
                .getSimpleName(), null);
        super._setUp(new PrimaryBackupStore<ProtocolTestStruct>(
                new MemStore<ProtocolTestStruct>(ProtocolTestStruct.class),
                new FsStore<ProtocolTestStruct>(new FsStore.Configuration(
                        rootDirectoryPath), ProtocolTestStruct.class)));
    }

    @Override
    @After
    public void tearDown() throws IOException {
        org.apache.commons.io.FileUtils.deleteDirectory(rootDirectoryPath);
    }

    private File rootDirectoryPath;
}
