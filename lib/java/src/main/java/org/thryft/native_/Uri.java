package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;
import static org.thryft.Preconditions.checkNotEmpty;

import com.google.common.base.Optional;

public abstract class Uri implements Comparable<Uri> {
    public final static class Authority {
        Authority(final String authority, final String host, final Optional<Integer> port,
                final Optional<String> userInfo) {
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

        @Override
        public boolean equals(final Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null) {
                return false;
            }
            if (getClass() != obj.getClass()) {
                return false;
            }
            final Authority other = (Authority) obj;
            if (!authority.equals(other.authority)) {
                return false;
            }
            if (!host.equals(other.host)) {
                return false;
            }
            if (!port.equals(other.port)) {
                return false;
            }
            if (!userInfo.equals(other.userInfo)) {
                return false;
            }
            return true;
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
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = prime * result + authority.hashCode();
            result = prime * result + host.hashCode();
            result = prime * result + port.hashCode();
            result = prime * result + userInfo.hashCode();
            return result;
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

    public static Uri parse(final String uri) {
        return UriParser.parseUri(uri);
    }

    protected static Optional<String> _checkOptionalString(final Optional<String> string) {
        checkNotNull(string);
        if (string.isPresent() && !string.get().isEmpty()) {
            return string;
        } else {
            return Optional.absent();
        }
    }

    protected Uri() {
    }

    protected Uri(final String scheme, final String uri) {
        checkNotNull(scheme);
        checkNotNull(uri);

        this.scheme = scheme;
        this.uri = uri;
    }

    protected Uri(final Uri uri) {
        checkNotNull(uri);
        scheme = uri.getScheme();
        this.uri = uri.toString();
    }

    @Override
    public final int compareTo(final Uri otherUri) {
        return toString().compareTo(otherUri.toString());
    }

    @Override
    public final boolean equals(final Object other) {
        if (other == null) {
            return false;
        } else if (other == this) {
            return true;
        } else if (!(other instanceof Uri)) {
            return false;
        }
        return uri.equals(((Uri) other).uri);
    }

    public abstract Optional<Authority> getAuthority();

    public abstract Optional<String> getFragment();

    public abstract Optional<String> getPath();

    public abstract Optional<String> getQuery();

    public final String getScheme() {
        return scheme;
    }

    @Override
    public final int hashCode() {
        return uri.hashCode();
    }

    @Override
    public final String toString() {
        return uri;
    }

    private String scheme;
    private String uri;
}
