package org.thryft.native_;

import static org.thryft.Preconditions.checkNotEmpty;

public final class Urn extends Uri {
    public static Urn parse(final String urn) {
        return UrnParser.parseUrn(urn);
    }

    public Urn(final String urn) {
        this(parse(urn));
    }

    public Urn(final String namespaceIdentifier,
            final String namespaceSpecificString) {
        super("urn", "urn:" + namespaceIdentifier + ":"
                + namespaceSpecificString);
        this.namespaceIdentifier = checkNotEmpty(namespaceIdentifier);
        this.namespaceSpecificString = checkNotEmpty(namespaceSpecificString);
    }

    public Urn(final Urn urn) {
        super(urn);
        namespaceIdentifier = urn.namespaceIdentifier;
        namespaceSpecificString = urn.namespaceSpecificString;
    }

    Urn(final String namespaceIdentifier, final String namespaceSpecificString,
            final String urn) {
        super("urn", urn);
        this.namespaceIdentifier = checkNotEmpty(namespaceIdentifier);
        this.namespaceSpecificString = checkNotEmpty(namespaceSpecificString);
    }

    @SuppressWarnings("unused")
    private Urn() {
    }

    public String getNamespaceIdentifier() {
        return namespaceIdentifier;
    }

    public String getNamespaceSpecificString() {
        return namespaceSpecificString;
    }

    private String namespaceIdentifier;
    private String namespaceSpecificString;
}
