package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;
import static org.thryft.Preconditions.checkNotEmpty;

import com.google.common.base.Optional;
import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.ImmutableMultimap;
import com.google.common.collect.Multimap;

public final class GenericUri extends Uri {
    public final static class Builder {
        public Builder() {
            authority = null;
            path = null;
            query = null;
            scheme = null;
        }

        public Builder(final Uri template) {
            authority = template.getAuthority().orNull();
            path = template.getPath().orNull();
            query = template.getQuery().orNull();
            scheme = template.getScheme();
        }

        public Uri build() {
            final StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append(checkNotNull(scheme));
            if (scheme.charAt(scheme.length() - 1) != ':') {
                stringBuilder.append(':');
            }
            stringBuilder.append("//");
            if (authority != null) {
                stringBuilder.append(authority.toString());
            }
            if (path != null) {
                stringBuilder.append(path);
            }
            if (query != null) {
                stringBuilder.append('?');
                stringBuilder.append(query);
            }
            final String string = stringBuilder.toString();
            return UriParser.parseUri(string);
        }

        public Builder setAuthority(final Authority authority) {
            this.authority = checkNotNull(authority);
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

        public Builder setQuery(final String query) {
            checkNotNull(query);
            if (!query.isEmpty()) {
                this.query = query;
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

        public Builder unsetPath() {
            path = null;
            return this;
        }

        public Builder unsetQuery() {
            query = null;
            return this;
        }

        public Builder unsetScheme() {
            scheme = null;
            return this;
        }

        private Authority authority;
        private String path;
        private String query;
        private String scheme;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(final Uri template) {
        return new Builder(template);
    }

    public static Uri parse(final String uri) {
        return UriParser.parseUri(uri);
    }

    public GenericUri(final Uri uri) {
        super(uri.getScheme(), uri.toString());
        authority = uri.getAuthority();
        fragment = uri.getFragment();
        path = uri.getPath();
        query = uri.getQuery();
    }

    GenericUri(final String scheme, final Optional<Authority> authority,
            final Optional<String> path, final Optional<String> query,
            final Optional<String> fragment, final String uri) {
        super(scheme, uri);

        this.authority = checkNotNull(authority);
        this.fragment = _checkOptionalString(fragment);
        this.path = _checkOptionalString(path);
        this.query = _checkOptionalString(query);
    }

    @SuppressWarnings("unused")
    private GenericUri() {
        authority = Optional.absent();
        fragment = Optional.absent();
        path = Optional.absent();
        query = Optional.absent();
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

    public ImmutableMultimap<String, String> getQueryMap() {
        if (!query.isPresent()) {
            return ImmutableMultimap.of();
        }

        final Multimap<String, String> queryMap = ArrayListMultimap.create();
        for (final String keyValueString : query.get().split("&")) {
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

    private final Optional<Authority> authority;
    private final Optional<String> fragment;
    private final Optional<String> path;
    private final Optional<String> query;
}
