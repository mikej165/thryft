package org.thryft.native_.test;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.junit.Assert.assertThat;

import org.junit.Test;
import org.thryft.native_.Urn;
import org.thryft.native_.UrnParser;

public class UrnParserTest {
    @Test
    public void testParseMultiColon() {
        final Urn urn = UrnParser.parseUrn("urn:nid:nss1:nss2");
        assertThat(urn.getNamespaceIdentifier(), equalTo("nid"));
        assertThat(urn.getNamespaceSpecificString(), equalTo("nss1:nss2"));

    }

    @Test
    public void testParseSimple() {
        final Urn urn = UrnParser.parseUrn("urn:nid:nss");
        assertThat(urn.getNamespaceIdentifier(), equalTo("nid"));
        assertThat(urn.getNamespaceSpecificString(), equalTo("nss"));
    }
}
