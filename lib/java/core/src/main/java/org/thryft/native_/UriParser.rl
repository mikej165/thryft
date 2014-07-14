package org.thryft.native_;

import com.google.common.base.Optional;

final class UriParser {
    static Uri parseUri(final String uri) {
        if (uri == null) {
            throw new NullPointerException();
        } else if (uri.startsWith("urn:")) {
            return UrnParser.parseUrn(uri);
        }

        // Ragel state machine variables
        byte[] data = uri.getBytes();
        int p = 0;
        int pe = data.length;
        int eof = pe;
        int cs = 0;

        // Variables used by actions
        int authorityMark = 0;
        int mark = 0;
        Uri.Authority authority = null;
        Optional<String> fragment = Optional.absent();
        String host = null;
        Optional<String> path = Optional.absent();
        Integer port = null;
        Optional<String> query = Optional.absent();
        String scheme = null;
        String userInfo = null;

%%{
    machine UriParser;
    include Rfc3986 "Rfc3986.rl";
    main := uri;
    write init;
    write exec;
}%%

        switch (scheme) {
        case "http":
        case "https":
            return new GenericUrl(scheme, authority, path, query, fragment, uri);
        default:
            return new GenericUri(scheme, Optional.fromNullable(authority), path, query, fragment, uri);
         }
    }

%% write data;
}
