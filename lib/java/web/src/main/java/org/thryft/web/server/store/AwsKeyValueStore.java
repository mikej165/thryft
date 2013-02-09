package org.thryft.web.server.store;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Properties;

import org.apache.thrift.TBase;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;

public abstract class AwsKeyValueStore<ModelT extends TBase<?, ?>> extends
        KeyValueStore<ModelT> {
    protected static class Configuration {
        protected Configuration(final AWSCredentials credentials) {
            this.credentials = checkNotNull(credentials);
        }

        protected Configuration(final Properties properties) {
            String accessKey = properties.getProperty(this.getClass()
                    .getCanonicalName() + ".accessKey");
            if (accessKey == null) {
                accessKey = properties.getProperty("accessKey");
            }
            if (accessKey == null) {
                throw new IllegalArgumentException("missing AWS accessKey");
            }

            String secretKey = properties.getProperty(this.getClass()
                    .getCanonicalName() + ".secretKey");
            if (secretKey == null) {
                secretKey = properties.getProperty("secretKey");
            }
            if (secretKey == null) {
                throw new IllegalArgumentException("missing AWS secretKey");
            }

            credentials = new BasicAWSCredentials(accessKey, secretKey);
        }

        public AWSCredentials getCredentials() {
            return credentials;
        }

        private final AWSCredentials credentials;
    }

    protected AwsKeyValueStore(final Class<ModelT> modelClass) {
        super(modelClass);
    }
}
