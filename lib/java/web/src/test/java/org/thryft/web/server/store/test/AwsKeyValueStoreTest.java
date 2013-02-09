package org.thryft.web.server.store.test;

import java.io.IOException;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.PropertiesCredentials;

public abstract class AwsKeyValueStoreTest extends StoreTest {
    public static AWSCredentials getCredentials() throws IOException {
        if (credentials == null) {
            credentials = new PropertiesCredentials(
                    AwsKeyValueStoreTest.class
                            .getResourceAsStream("/store.properties.test"));
        }

        return credentials;
    }

    private static AWSCredentials credentials = null;
}
