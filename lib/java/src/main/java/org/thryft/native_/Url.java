package org.thryft.native_;

public abstract class Url extends Uri {
    public static Url parse(final String url) {
        return (Url) UriParser.parseUri(url);
    }

    protected Url(final String scheme, final String url) {
        super(scheme, url);
    }
}
