/*******************************************************************************
 * Copyright (c) 2013, Minor Gordon
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 * 
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in
 *       the documentation and/or other materials provided with the
 *       distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
 * CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGE.
 ******************************************************************************/

package org.thryft.native_;

import static com.google.common.base.Preconditions.checkNotNull;

import java.io.Serializable;

public abstract class Uri implements Comparable<Uri>, Serializable {
    public static Uri parse(final String uri) {
        checkNotNull(uri);

        if (uri.startsWith("urn:")) {
            return Urn.parse(uri);
        } else {
            return Url.parse(uri);
        }
    }

    protected Uri() {
    }

    protected Uri(final String scheme, final String uri) {
        checkNotNull(scheme);
        checkNotNull(uri);

        this.scheme = scheme;
        this.uri = uri;
    }

    protected Uri(final Uri uri) {
        checkNotNull(uri);
        scheme = uri.getScheme();
        this.uri = uri.toString();
    }

    @Override
    public final int compareTo(final Uri otherUri) {
        return toString().compareTo(otherUri.toString());
    }

    @Override
    public final boolean equals(final Object other) {
        if (other == null) {
            return false;
        } else if (other == this) {
            return true;
        } else if (!(other instanceof Uri)) {
            return false;
        }
        return uri.equals(((Uri) other).uri);
    }

    public final String getScheme() {
        return scheme;
    }

    @Override
    public final int hashCode() {
        return uri.hashCode();
    }

    @Override
    public final String toString() {
        return uri.toString();
    }

    private static final long serialVersionUID = 1L;

    private String scheme;
    private String uri;
}
