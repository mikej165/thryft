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

package org.thryft;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Collection;

import javax.annotation.Nullable;

import com.google.common.base.Optional;

public final class Preconditions {
    public static <CollectionT extends Collection<?>> CollectionT checkMinLength(
            final CollectionT collection, final int minLength) {
        checkNotNull(collection);
        if (collection.size() < minLength) {
            throw new IllegalArgumentException();
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMinLength(
            final CollectionT collection, final int minLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.size() < minLength) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkMinLength(
            final Optional<CollectionT> collection, final int minLength,
            @Nullable final Object errorMessage) {
        if (collection.isPresent()) {
            if (collection.get().size() < minLength) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            }
        }
        return collection;
    }

    @SuppressWarnings("unchecked")
    public static <T> Optional<T> checkMinLength(final Optional<T> object,
            final Class<T> objectClass, final int minLength) {
        if (object.isPresent()) {
            if (Collection.class.isAssignableFrom(objectClass)) {
                checkMinLength((Collection<T>) object.get(), minLength);
            } else if (String.class.isAssignableFrom(objectClass)) {
                checkMinLength((String) object.get(), minLength);
            } else {
                throw new IllegalArgumentException(
                        objectClass.getCanonicalName());
            }
        }
        return object;
    }

    @SuppressWarnings("unchecked")
    public static <T> Optional<T> checkMinLength(final Optional<T> object,
            final Class<T> objectClass, final int minLength,
            @Nullable final Object errorMessage) {
        if (object.isPresent()) {
            if (Collection.class.isAssignableFrom(objectClass)) {
                checkMinLength((Collection<T>) object.get(), minLength,
                        errorMessage);
            } else if (String.class.isAssignableFrom(objectClass)) {
                checkMinLength((String) object.get(), minLength, errorMessage);
            } else {
                throw new IllegalArgumentException(
                        objectClass.getCanonicalName());
            }
        }
        return object;
    }

    public static String checkMinLength(final String string, final int minLength) {
        checkNotNull(string);
        if (string.length() < minLength) {
            throw new IllegalArgumentException();
        }
        return string;
    }

    public static String checkMinLength(final String string,
            final int minLength, @Nullable final Object errorMessage) {
        checkNotNull(string, errorMessage);
        if (string.length() < minLength) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return string;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkNotEmpty(
            final CollectionT collection) {
        checkNotNull(collection);
        if (collection.isEmpty()) {
            throw new IllegalArgumentException();
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkNotEmpty(
            final CollectionT collection, @Nullable final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return collection;
    }

    public static Optional<String> checkNotEmpty(final Optional<String> string,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            if (string.get().isEmpty()) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            }
        }
        return string;
    }

    @SuppressWarnings("unchecked")
    public static <T> Optional<T> checkNotEmpty(final Optional<T> object,
            final Class<T> objectClass) {
        if (object.isPresent()) {
            if (Collection.class.isAssignableFrom(objectClass)) {
                checkNotEmpty((Collection<T>) object.get());
            } else if (String.class.isAssignableFrom(objectClass)) {
                checkNotEmpty((String) object.get());
            } else {
                throw new IllegalArgumentException(
                        objectClass.getCanonicalName());
            }
        }
        return object;
    }

    @SuppressWarnings("unchecked")
    public static <T> Optional<T> checkNotEmpty(final Optional<T> object,
            final Class<T> objectClass, @Nullable final Object errorMessage) {
        if (object.isPresent()) {
            if (Collection.class.isAssignableFrom(objectClass)) {
                checkNotEmpty((Collection<T>) object.get(), errorMessage);
            } else if (String.class.isAssignableFrom(objectClass)) {
                checkNotEmpty((String) object.get(), errorMessage);
            } else {
                throw new IllegalArgumentException(
                        objectClass.getCanonicalName());
            }
        }
        return object;
    }

    public static String checkNotEmpty(final String string) {
        checkNotNull(string);
        if (string.isEmpty()) {
            throw new IllegalArgumentException();
        }
        return string;
    }

    public static String checkNotEmpty(final String string,
            @Nullable final Object errorMessage) {
        checkNotNull(string, errorMessage);
        if (string.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return string;
    }

    private Preconditions() {
    }
}
