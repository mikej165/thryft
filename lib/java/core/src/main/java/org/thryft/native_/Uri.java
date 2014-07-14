package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;
import static org.thryft.Preconditions.checkNotEmpty;

import com.google.common.base.Optional;

public interface Uri extends Comparable<Uri> {
    public final static class Authority {
        Authority(final String authority, final String host,
                final Optional<Integer> port, final Optional<String> userInfo) {
            this.authority = checkNotEmpty(authority);
            this.host = checkNotEmpty(host);

            checkNotNull(port);
            if (port.isPresent() && port.get() > 0) {
                this.port = port;
            } else {
                this.port = Optional.absent();
            }

            checkNotNull(userInfo);
            if (userInfo.isPresent() && !userInfo.get().isEmpty()) {
                this.userInfo = userInfo;
            } else {
                this.userInfo = Optional.absent();
            }
        }

        public String getAuthority() {
            return authority;
        }

        public String getHost() {
            return host;
        }

        public Optional<Integer> getPort() {
            return port;
        }

        public Optional<String> getUserInfo() {
            return userInfo;
        }

        @Override
        public String toString() {
            return authority;
        }

        private final String authority;
        private final String host;
        private final Optional<Integer> port;
        private final Optional<String> userInfo;
    }

    public Optional<String> getFragment();

    public Optional<Authority> getOptionalAuthority();

    public Optional<String> getPath();

    public Optional<String> getQuery();

    public String getScheme();
}
