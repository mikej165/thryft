package org.thryft.native_;

public abstract class Url extends Uri {
    public static Url parse(final String url) {
        final Uri uri = UriParser.parseUri(url);
        if (uri instanceof Url) {
            return (Url) uri;
        } else {
            throw new IllegalArgumentException(url + " is not a URL");
        }
    }

    protected Url(final String scheme, final String url) {
        super(scheme, url);
    }
}
