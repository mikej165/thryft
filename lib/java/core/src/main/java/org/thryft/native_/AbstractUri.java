package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

import com.google.common.base.Optional;

public abstract class AbstractUri implements Uri {
    protected static Optional<String> _checkOptionalString(
            final Optional<String> string) {
        checkNotNull(string);
        if (string.isPresent() && !string.get().isEmpty()) {
            return string;
        } else {
            return Optional.absent();
        }
    }

    protected AbstractUri() {
    }

    protected AbstractUri(final AbstractUri uri) {
        checkNotNull(uri);
        scheme = uri.getScheme();
        this.uri = uri.toString();
    }

    protected AbstractUri(final String scheme, final String uri) {
        checkNotNull(scheme);
        checkNotNull(uri);

        this.scheme = scheme;
        this.uri = uri;
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
        } else if (!(other instanceof AbstractUri)) {
            return false;
        }
        return uri.equals(((AbstractUri) other).uri);
    }

    @Override
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
