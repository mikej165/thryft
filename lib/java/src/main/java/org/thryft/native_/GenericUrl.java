package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Optional;

public final class GenericUrl extends Url {
    GenericUrl(final String scheme, final Optional<Authority> authority,
            final Optional<String> path, final Optional<String> query,
            final Optional<String> fragment, final String url) {
        super(scheme, url);
        this.authority = checkNotNull(authority);
        this.path = _checkOptionalString(path);
        this.query = _checkOptionalString(query);
        this.fragment = _checkOptionalString(fragment);
    }

    @Override
    public Optional<Authority> getAuthority() {
        return authority;
    }

    @Override
    public Optional<String> getFragment() {
        return fragment;
    }

    @Override
    public Optional<String> getPath() {
        return path;
    }

    @Override
    public Optional<String> getQuery() {
        return query;
    }

    private final Optional<Authority> authority;
    private final Optional<String> path;
    private final Optional<String> query;
    private final Optional<String> fragment;
}
