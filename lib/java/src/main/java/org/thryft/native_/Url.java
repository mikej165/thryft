package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.ImmutableMultimap;
import com.google.common.collect.Multimap;

public final class Url extends Uri {
    // public URL(final String url) {
    // this(parse(checkNotNull(url, "url")));
    // }
    //
    // public URL(final String scheme, final String authority, final String
    // path) {
    // this((checkNotNull(scheme, "scheme") + "://"
    // + checkNotNull(authority, "authority") + (path != null ? path
    // : "")));
    // }

    public final static class Builder {
        public Url build() {
            return Url.parse(scheme, authority, path);
        }

        public Builder setAuthority(final String authority) {
            this.authority = authority;
            return this;
        }

        public Builder setPath(final String path) {
            this.path = path;
            return this;
        }

        public Builder setScheme(final String scheme) {
            this.scheme = scheme;
            return this;
        }

        private String authority;
        private String path;
        private String scheme;
    }

    public static Url parse(final String url) {
        return UrlParser.parseUrl(checkNotNull(url, "url"));
    }

    public static Url parse(final String scheme, final String authority,
            final String path) {
        return parse(checkNotNull(scheme, "scheme") + "://"
                + checkNotNull(authority, "authority")
                + (path != null ? path : ""));
    }

    public Url(final Url url) {
        super(url);
        rawAuthority = url.rawAuthority;
        rawUserInfo = url.rawUserInfo;
        rawHost = url.rawHost;
        port = url.port;
        rawPath = url.rawPath;
        rawQuery = url.rawQuery;
        rawFragment = url.rawFragment;
    }

    Url(final String scheme, final String rawAuthority,
            final String rawUserInfo, final String rawHost, final int port,
            final String rawPath, final String rawQuery,
            final String rawFragment, final String url) {
        super(scheme, url);
        this.rawAuthority = rawAuthority;
        this.rawUserInfo = rawUserInfo;
        this.rawHost = rawHost;
        this.port = port;
        this.rawPath = rawPath;
        this.rawQuery = rawQuery;
        this.rawFragment = rawFragment;
    }

    @SuppressWarnings("unused")
    private Url() {
    }

    public String getAuthority() {
        return getRawAuthority();
    }

    public String getFragment() {
        return getRawFragment();
    }

    public String getHost() {
        return getRawHost();
    }

    public String getPath() {
        return getRawPath();
    }

    public int getPort() {
        return port;
    }

    public String getQuery() {
        return getQueryString();
    }

    public ImmutableMultimap<String, String> getQueryMap() {
        if (getQueryString() == null) {
            return ImmutableMultimap.of();
        }

        final Multimap<String, String> queryMap = ArrayListMultimap.create();
        for (final String keyValueString : getQueryString().split("&")) {
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

    public String getQueryString() {
        return getRawQueryString();
    }

    public String getRawAuthority() {
        return rawAuthority;
    }

    public String getRawFragment() {
        return rawFragment;
    }

    public String getRawHost() {
        return rawHost;
    }

    public String getRawPath() {
        return rawPath;
    }

    public String getRawQuery() {
        return getRawQueryString();
    }

    public String getRawQueryString() {
        return rawQuery;
    }

    public String getRawUserInfo() {
        return rawUserInfo;
    }

    public String getUserInfo() {
        return getRawUserInfo();
    }

    private static final long serialVersionUID = 1L;

    private String rawAuthority;
    private String rawFragment;
    private String rawHost;
    private String rawPath;
    private int port;
    private String rawQuery;
    private String rawUserInfo;
}
