package org.thryft.native_;

import com.google.common.base.Optional;

public final class UrlParser {
    public static Url parseUrl(final String url) {
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
        Optional<String> fragment = Optional.absent();
        String host = null;
        Optional<String> path = Optional.absent();
        Optional<Integer> port = Optional.absent();
        Optional<String> query = Optional.absent();
        String scheme = null;
        Optional<String> userInfo = Optional.absent();

%%{
    machine UrlParser;
    include Rfc3986 "Rfc3986.rl";
    main := scheme '://' authority path_abempty ("?" query)? ("#" fragment)?;
    write init;
    write exec;
}%%

        if (authority == null || host == null || scheme == null) {
            throw new IllegalArgumentException(url);
        }

        return new Url(scheme, authority, userInfo, host, port, path, query, fragment, url);
    }

%% write data;
}
