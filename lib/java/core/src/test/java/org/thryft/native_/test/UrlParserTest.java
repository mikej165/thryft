package org.thryft.native_.test;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThat;

import org.junit.Test;
import org.thryft.native_.Url;
import org.thryft.native_.UrlParser;

public class UrlParserTest {
    @Test
    public void testParseScheme_user_passwordHost() {
        final Url url = UrlParser.parseUrl("http://minorg:minorg@localhost");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
        assertThat(url.getUserInfo().get(), equalTo("minorg:minorg"));
    }

    @Test
    public void testParseScheme_userHost() {
        final Url url = UrlParser.parseUrl("http://minorg@localhost");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
        assertThat(url.getUserInfo().get(), equalTo("minorg"));
    }

    @Test
    public void testParseSchemeHost1() {
        final Url url = UrlParser.parseUrl("http://localhost/1/2/3");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
    }

    @Test
    public void testParseSchemeHost2() {
        final Url url = UrlParser.parseUrl("http://localhost");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
        assertFalse(url.getPath().isPresent());
    }

    @Test
    public void testParseSchemeHostPath1() {
        final Url url = UrlParser.parseUrl("http://localhost/mydir/");
        assertThat(url.getPath().get(), equalTo("/mydir/"));
    }

    @Test
    public void testParseSchemeHostPath2() {
        final Url url = UrlParser.parseUrl("http://localhost/mypath");
        assertThat(url.getPath().get(), equalTo("/mypath"));
    }

    @Test
    public void testParseSchemeHostPath3() {
        final Url url = UrlParser.parseUrl("http://localhost/mydir/mypath");
        assertThat(url.getPath().get(), equalTo("/mydir/mypath"));
    }

    @Test
    public void testParseSchemeHostPathQuery1() {
        final Url url = UrlParser.parseUrl("http://localhost/mypath?key=value");
        assertThat(url.getPath().get(), equalTo("/mypath"));
    }

    @Test
    public void testParseSchemeHostPathQuery2() {
        final Url url = UrlParser
                .parseUrl("http://localhost/mypath?key1=value1&key2=value2");
        assertThat(url.getPath().get(), equalTo("/mypath"));
    }

    @Test
    public void testParseSchemeHostPort1() {
        final Url url = UrlParser.parseUrl("http://*:80");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("*"));
        assertFalse(url.getPath().isPresent());
    }

    @Test
    public void testParseSchemeHostPort2() {
        final Url url = UrlParser.parseUrl("http://localhost:1");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
        assertThat(url.getPort().get(), equalTo(1));
    }

    @Test
    public void testParseSchemeHostPort3() {
        final Url url = UrlParser.parseUrl("http://localhost:1");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
        assertThat(url.getPort().get(), equalTo(1));
        assertFalse(url.getPath().isPresent());
    }

    @Test
    public void testParseSchemeHostPort4() {
        final Url url = UrlParser.parseUrl("http://localhost:8080");
        assertThat(url.getScheme(), equalTo("http"));
        assertThat(url.getHost(), equalTo("localhost"));
        assertThat(url.getPort().get(), equalTo(8080));
        assertFalse(url.getPath().isPresent());
    }
}
