package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

public abstract class Uri implements Comparable<Uri> {
    public static Uri parse(final String uri) {
        checkNotNull(uri);

        if (uri.startsWith("urn:")) {
            return Urn.parse(uri);
        } else {
            return Url.parse(uri);
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

    public final String getScheme() {
        return scheme;
    }

    @Override
    public final int hashCode() {
        return uri.hashCode();
    }

    @Override
    public final String toString() {
        return uri.toString();
    }

    private String scheme;
    private String uri;
}
