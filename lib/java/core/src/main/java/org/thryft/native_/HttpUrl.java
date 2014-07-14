package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Optional;

public final class HttpUrl extends AbstractUri implements Url {
    HttpUrl(final String scheme, final Authority authority,
            final Optional<String> path, final Optional<String> query,
            final Optional<String> fragment, final String url) {
        super(scheme, url);
        this.authority = checkNotNull(authority);
        optionalAuthority = Optional.of(authority);
        this.path = _checkOptionalString(path);
        this.query = _checkOptionalString(query);
        this.fragment = _checkOptionalString(fragment);
    }

    @Override
    public Authority getAuthority() {
        return authority;
    }

    @Override
    public Optional<String> getFragment() {
        return fragment;
    }

    @Override
    public Optional<Authority> getOptionalAuthority() {
        return optionalAuthority;
    }

    @Override
    public Optional<String> getPath() {
        return path;
    }

    @Override
    public Optional<String> getQuery() {
        return query;
    }

    private final Authority authority;
    private final Optional<Authority> optionalAuthority;
    private final Optional<String> path;
    private final Optional<String> query;
    private final Optional<String> fragment;
}
