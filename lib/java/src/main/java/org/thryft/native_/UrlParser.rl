package org.thryft.native_;

public final class UrlParser {
    public static URL parseUrl(final String url) {
        if (url == null) {
            throw new NullPointerException();
        }

        // Ragel state machine variables
        byte[] data = url.getBytes();
        int p = 0;
        int pe = data.length;
        int eof = pe;
        int cs = 0;

        // Variables used by actions
        int authorityMark = 0;
        int mark = 0;
        String authority = null;
        String fragment = null;
        String host = null;
        String path = null;
        int port = -1;
        String query = null;
        String scheme = null;
        String userInfo = null;

%%{
    machine UrlParser;
    include Rfc3986 "Rfc3986.rl";
    main := scheme '://' authority path_abempty ("?" query)? ("#" fragment)?;
    write init;
    write exec;
}%%

        if (scheme == null) {
            throw new IllegalArgumentException(url);
        }

        return new URL(scheme, authority, userInfo, host, port, path, query, fragment, url);
    }

%% write data;
}
