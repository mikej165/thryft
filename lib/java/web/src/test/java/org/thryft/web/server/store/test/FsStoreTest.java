package org.thryft.web.server.store.test;

import java.io.File;
import java.io.IOException;

import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.FsStore;
import org.thryft.web.server.util.FileUtils;

public class FsStoreTest extends StoreTest {
    public static FsStore.Configuration getFsStoreConfiguration()
            throws IOException {
        if (fsStoreConfiguration == null) {
            final File rootDirectoryPath = FileUtils.createTempDirectory(
                    FsStoreTest.class.getSimpleName(), null);
            fsStoreConfiguration = new FsStore.Configuration(rootDirectoryPath);
        }

        return fsStoreConfiguration;
    }

    @Before
    public void setUp() throws IOException {
        org.apache.commons.io.FileUtils
                .deleteDirectory(getFsStoreConfiguration()
                        .getRootDirectoryPath());
        super._setUp(new FsStore<ProtocolTestStruct>(getFsStoreConfiguration(),
                ProtocolTestStruct.class));
    }

    private static FsStore.Configuration fsStoreConfiguration = null;
}
