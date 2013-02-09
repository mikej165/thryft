package org.thryft.web.server.store.test;

import java.io.IOException;

import org.junit.Before;
import org.thryft.core.protocol.test.ProtocolTestStruct;
import org.thryft.web.server.store.S3Store;

public class S3StoreTest extends AwsKeyValueStoreTest {
    public static S3Store.Configuration getS3StoreConfiguration()
            throws IOException {
        if (s3StoreConfiguration == null) {
            s3StoreConfiguration = new S3Store.Configuration("yogento-test-",
                    AwsKeyValueStoreTest.getCredentials());
        }

        return s3StoreConfiguration;
    }

    @Before
    public void setUp() throws IOException {
        super._setUp(new S3Store<ProtocolTestStruct>(getS3StoreConfiguration(),
                ProtocolTestStruct.class));
    }

    private static S3Store.Configuration s3StoreConfiguration = null;
}
