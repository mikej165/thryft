package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

import java.io.Serializable;

@SuppressWarnings("serial")
public final class EmailAddress implements Comparable<EmailAddress>,
Serializable {
    public EmailAddress(final String string) {
        this.string = checkNotNull(string);
    }

    @Override
    public int compareTo(final EmailAddress other) {
        return string.compareTo(other.string);
    }

    @Override
    public boolean equals(final Object other) {
        if (other == this) {
            return true;
        } else if (!(other instanceof EmailAddress)) {
            return false;
        }
        return string.equals(((EmailAddress) other).string);
    }

    @Override
    public int hashCode() {
        return string.hashCode();
    }

    @Override
    public String toString() {
        return string;
    }

    private final String string;
}
