package org.thryft.native_;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static org.thryft.Preconditions.checkNotEmpty;

import com.google.common.base.Optional;
import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.ImmutableMultimap;
import com.google.common.collect.Multimap;

public final class Url extends Uri {
    public final static class Builder {
        public Builder() {
            authority = null;
            host = null;
            path = null;
            port = -1;
            scheme = null;
        }

        public Builder(final Url template) {
            authority = template.rawAuthority;
            host = template.rawHost;
            path = template.rawPath.orNull();
            port = template.port.or(-1);
            queryString = template.rawQueryString.orNull();
            scheme = template.getScheme();
        }

        public Url build() {
            final StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append(checkNotNull(scheme));
            if (scheme.charAt(scheme.length() - 1) != ':') {
                stringBuilder.append(':');
            }
            stringBuilder.append("//");
            if (authority != null) {
                stringBuilder.append(authority);
            } else if (host != null) {
                stringBuilder.append(host);
                if (port != -1) {
                    stringBuilder.append(':');
                    stringBuilder.append(port);
                }
            }
            if (path != null) {
                stringBuilder.append(path);
            }
            if (queryString != null) {
                stringBuilder.append('?');
                stringBuilder.append(queryString);
            }
            final String string = stringBuilder.toString();
            return Url.parse(string);
        }

        public Builder setAuthority(final String authority) {
            this.authority = checkNotEmpty(authority);
            return this;
        }

        public Builder setHost(final String host) {
            this.host = checkNotEmpty(host);
            return this;
        }

        public Builder setPath(final Optional<String> path) {
            checkNotNull(path);
            if (path.isPresent() && !path.get().isEmpty()) {
                this.path = path.get();
            }
            return this;
        }

        public Builder setPath(final String path) {
            checkNotNull(path);
            if (!path.isEmpty()) {
                this.path = path;
            }
            return this;
        }

        public Builder setPort(final int port) {
            checkArgument(port >= 0 && port <= 65535);
            this.port = port;
            return this;
        }

        public Builder setQueryString(final String queryString) {
            checkNotNull(queryString);
            if (!queryString.isEmpty()) {
                this.queryString = queryString;
            }
            return this;
        }

        public Builder setScheme(final String scheme) {
            this.scheme = checkNotEmpty(scheme);
            return this;
        }

        public Builder unsetAuthority() {
            authority = null;
            return this;
        }

        public Builder unsetHost() {
            host = null;
            return this;
        }

        public Builder unsetPath() {
            path = null;
            return this;
        }

        public Builder unsetPort() {
            port = -1;
            return this;
        }

        public Builder unsetQueryString() {
            queryString = null;
            return this;
        }

        public Builder unsetScheme() {
            scheme = null;
            return this;
        }

        private String authority;
        private String host;
        private String path;
        private int port;
        private String queryString;
        private String scheme;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(final Url template) {
        return new Builder(template);
    }

    public static Url parse(final String url) {
        return UrlParser.parseUrl(checkNotNull(url, "url"));
    }

    public Url(final Url url) {
        super(url);
        rawAuthority = url.rawAuthority;
        rawUserInfo = url.rawUserInfo;
        rawHost = url.rawHost;
        port = url.port;
        rawPath = url.rawPath;
        rawQueryString = url.rawQueryString;
        rawFragment = url.rawFragment;
    }

    Url(final String scheme, final String rawAuthority,
            final Optional<String> rawUserInfo, final String rawHost,
            final Optional<Integer> port, final Optional<String> rawPath,
            final Optional<String> rawQuery,
            final Optional<String> rawFragment, final String url) {
        super(scheme, url);

        this.rawAuthority = checkNotEmpty(rawAuthority);

        checkNotNull(rawUserInfo);
        if (rawUserInfo.isPresent() && !rawUserInfo.get().isEmpty()) {
            this.rawUserInfo = rawUserInfo;
        } else {
            this.rawUserInfo = Optional.absent();
        }

        this.rawHost = checkNotEmpty(rawHost);

        this.port = checkNotNull(port);

        checkNotNull(rawPath);
        if (rawPath.isPresent() && !rawPath.get().isEmpty()) {
            this.rawPath = rawPath;
        } else {
            this.rawPath = Optional.absent();
        }

        checkNotNull(rawQuery);
        if (rawQuery.isPresent() && !rawQuery.get().isEmpty()) {
            rawQueryString = rawQuery;
        } else {
            rawQueryString = Optional.absent();
        }

        checkNotNull(rawFragment);
        if (rawFragment.isPresent() && !rawFragment.isPresent()) {
            this.rawFragment = rawFragment;
        } else {
            this.rawFragment = Optional.absent();
        }
    }

    @SuppressWarnings("unused")
    private Url() {
    }

    public String getAuthority() {
        return getRawAuthority();
    }

    public Optional<String> getFragment() {
        return getRawFragment();
    }

    public String getHost() {
        return getRawHost();
    }

    public Optional<String> getPath() {
        return getRawPath();
    }

    public Optional<Integer> getPort() {
        return port;
    }

    public Optional<String> getQuery() {
        return getQueryString();
    }

    public ImmutableMultimap<String, String> getQueryMap() {
        if (!getQueryString().isPresent()) {
            return ImmutableMultimap.of();
        }

        final Multimap<String, String> queryMap = ArrayListMultimap.create();
        for (final String keyValueString : getQueryString().get().split("&")) {
            if (keyValueString.isEmpty()) {
                continue;
            }

            final String[] keyValueStrings = keyValueString.split("=", 1);
            final String key, value;
            key = keyValueStrings[0];
            value = (keyValueStrings.length > 1) ? keyValueStrings[1] : "";

            queryMap.put(key, value);
        }
        return ImmutableMultimap.copyOf(queryMap);
    }

    public Optional<String> getQueryString() {
        return getRawQueryString();
    }

    public String getRawAuthority() {
        return rawAuthority;
    }

    public Optional<String> getRawFragment() {
        return rawFragment;
    }

    public String getRawHost() {
        return rawHost;
    }

    public Optional<String> getRawPath() {
        return rawPath;
    }

    public Optional<String> getRawQuery() {
        return getRawQueryString();
    }

    public Optional<String> getRawQueryString() {
        return rawQueryString;
    }

    public Optional<String> getRawUserInfo() {
        return rawUserInfo;
    }

    public Optional<String> getUserInfo() {
        return getRawUserInfo();
    }

    private String rawAuthority;
    private Optional<String> rawFragment;
    private String rawHost;
    private Optional<String> rawPath;
    private Optional<Integer> port;
    private Optional<String> rawQueryString;
    private Optional<String> rawUserInfo;
}
