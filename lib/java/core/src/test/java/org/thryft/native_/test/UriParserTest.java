package org.thryft.native_.test;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.fail;

import org.junit.Test;
import org.thryft.native_.Uri;

public final class UriParserTest {
    @Test
    public void testParseMailtoUrl() {
        final Uri uri = Uri.parse("mailto:test@example.com");
        assertThat(uri.getScheme(), equalTo("mailto"));
        assertThat(uri.getPath().get(), equalTo("test@example.com"));
    }

    @Test
    public void testParseNoScheme() {
        try {
            Uri.parse("/test/path");
            fail();
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testParseScheme_user_passwordHost() {
        final Uri uri = Uri.parse("http://minorg:minorg@localhost");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
        assertThat(uri.getOptionalAuthority().get().getUserInfo().get(),
                equalTo("minorg:minorg"));
    }

    @Test
    public void testParseScheme_userHost() {
        final Uri uri = Uri.parse("http://minorg@localhost");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
        assertThat(uri.getOptionalAuthority().get().getUserInfo().get(),
                equalTo("minorg"));
    }

    @Test
    public void testParseSchemeHost1() {
        final Uri uri = Uri.parse("http://localhost/1/2/3");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
    }

    @Test
    public void testParseSchemeHost2() {
        final Uri uri = Uri.parse("http://localhost");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
        assertFalse(uri.getPath().isPresent());
    }

    @Test
    public void testParseSchemeHostPath1() {
        final Uri uri = Uri.parse("http://localhost/mydir/");
        assertThat(uri.getPath().get(), equalTo("/mydir/"));
    }

    @Test
    public void testParseSchemeHostPath2() {
        final Uri uri = Uri.parse("http://localhost/mypath");
        assertThat(uri.getPath().get(), equalTo("/mypath"));
    }

    @Test
    public void testParseSchemeHostPath3() {
        final Uri uri = Uri.parse("http://localhost/mydir/mypath");
        assertThat(uri.getPath().get(), equalTo("/mydir/mypath"));
    }

    @Test
    public void testParseSchemeHostPathQuery1() {
        final Uri uri = Uri.parse("http://localhost/mypath?key=value");
        assertThat(uri.getPath().get(), equalTo("/mypath"));
    }

    @Test
    public void testParseSchemeHostPathQuery2() {
        final Uri uri = Uri
                .parse("http://localhost/mypath?key1=value1&key2=value2");
        assertThat(uri.getPath().get(), equalTo("/mypath"));
    }

    @Test
    public void testParseSchemeHostPort1() {
        final Uri uri = Uri.parse("http://*:80");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(), equalTo("*"));
        assertFalse(uri.getPath().isPresent());
    }

    @Test
    public void testParseSchemeHostPort2() {
        final Uri uri = Uri.parse("http://localhost:1");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
        assertThat(uri.getOptionalAuthority().get().getPort().get(), equalTo(1));
    }

    @Test
    public void testParseSchemeHostPort3() {
        final Uri uri = Uri.parse("http://localhost:1");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
        assertThat(uri.getOptionalAuthority().get().getPort().get(), equalTo(1));
        assertFalse(uri.getPath().isPresent());
    }

    @Test
    public void testParseSchemeHostPort4() {
        final Uri uri = Uri.parse("http://localhost:8080");
        assertThat(uri.getScheme(), equalTo("http"));
        assertThat(uri.getOptionalAuthority().get().getHost(),
                equalTo("localhost"));
        assertThat(uri.getOptionalAuthority().get().getPort().get(),
                equalTo(8080));
        assertFalse(uri.getPath().isPresent());
    }
}
