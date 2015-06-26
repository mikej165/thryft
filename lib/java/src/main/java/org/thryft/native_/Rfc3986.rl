%%{
  machine Rfc3986;

  gen_delims    = ":" | "|" | "?" | "#" | "[" | "]" | "@";
  sub_delims    = "!" | "$" | "&" | "'" | "(" | ")" | "*" | "+" | "," | ";" | "=";
  pct_encoded   = "%" xdigit xdigit;
  reserved      = gen_delims | sub_delims;
  unreserved    = alpha | digit | "-" | "." | "_" | "~";
  pchar         = unreserved | pct_encoded | sub_delims | ":" | "@";


  IPvFuture     = "v" xdigit+ "." (unreserved | sub_delims | ":")+;

  dec_octet     = digit |
                  ([1-9] digit) |
                  ("1" digit{2} ) |
                  ("2" [0-4] digit) |
                  ("25" [0-5]);
  IPv4address   = dec_octet "." dec_octet "." dec_octet "." dec_octet;

  h16           = (xdigit{4})+;
  ls32          = (h16 ":" h16) | IPv4address;
  IPv6address   = ((h16 ":"){6} ls32) |
                  ("::" (h16 ":"){5} ls32) |
                  (h16? "::" (h16 ":"){4} ls32) |
                  ((((h16 ":"){1})* h16)? "::" (h16 ":"){3} ls32) |
                  ((((h16 ":"){2})* h16)? "::" (h16 ":"){2} ls32) |
                  ((((h16 ":"){3})* h16)? "::" h16 ":"   ls32) |
                  ((((h16 ":"){4})* h16)? "::" ls32) |
                  ((((h16 ":"){5})* h16)? "::" h16) |
                  ((((h16 ":"){6})* h16)? "::");

  ip_literal    = "[" (IPv6address | IPvFuture ) "]";


  scheme        = (alpha (alpha | digit | "+" | "-" | ".")*)
                  >{ mark = fpc; }
                  %{ scheme = new String(data, mark, fpc - mark); };

  userinfo      = (unreserved | pct_encoded | sub_delims | ":")*
                  >{ mark = fpc; }
                  %{ userInfo = new String(data, mark, fpc - mark); };

  reg_name      = (unreserved | pct_encoded | sub_delims)*;
  host          = (ip_literal | IPv4address | reg_name)
                  >{ mark = fpc; }
                  %{ host = new String(data, mark, fpc - mark); };

  port          = digit*
                  >{ mark = fpc; }
                  %{ port = Integer.parseInt(new String(data, mark, fpc - mark)); };

  authority     = ((userinfo "@")? host (":" port)?)
                  >{ authorityMark = fpc; }
                  %{ if (fpc - authorityMark > 0) { authority = Optional.of(new Uri.Authority(new String(data, authorityMark, fpc - authorityMark), host, Optional.fromNullable(port), Optional.fromNullable(userInfo))); } };

  action path_enter { mark = fpc; }
  action path_leave { path = Optional.of(new String(data, mark, fpc - mark)); }

  segment       = pchar*;
  segment_nz    = pchar+;
  segment_nz_nc = (unreserved | pct_encoded | sub_delims | "@")+;
  path_abempty  = ("/" segment)* >path_enter %path_leave;
  path_absolute = ("/" (segment_nz ("/" segment)*)?) >path_enter %path_leave;
  path_noscheme = (segment_nz_nc ("/" segment)*) >path_enter %path_leave;
  path_rootless = (segment_nz ("/" segment)*) >path_enter %path_leave;
  path_empty    = empty;

  hier_part = ("//" authority path_abempty) |
              path_absolute |
              path_rootless |
              path_empty;


  query         = (pchar | "/" | "?")*
                  >{ mark = fpc; }
                  %{ query = Optional.of(new String(data, mark, fpc - mark)); };
  fragment      = (pchar | "/" | "?")*
                  >{ mark = fpc; }
                  %{ fragment = Optional.of(new String(data, mark, fpc - mark)); };


  relative_part = ("//" authority path_abempty) |
                  path_absolute |
                  path_noscheme |
                  path_empty;
  relative_ref  = relative_part ("?" query)? ("#" fragment)?;


  absolute_uri  = scheme ":" hier_part ("?" query)?;
  uri           = scheme ":" hier_part ("?" query)? ("#" fragment)?;
  uri_reference = uri | relative_ref;
}%%
