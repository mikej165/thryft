package org.thryft.core;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Collection;

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
            final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.size() < minLength) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return collection;
    }

    public static String checkMinLength(final String string, final int minLength) {
        checkNotNull(string);
        if (string.length() < minLength) {
            throw new IllegalArgumentException();
        }
        return string;
    }

    public static String checkMinLength(final String string,
            final int minLength, final Object errorMessage) {
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
            final CollectionT collection, final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return collection;
    }

    public static String checkNotEmpty(final String string) {
        checkNotNull(string);
        if (string.isEmpty()) {
            throw new IllegalArgumentException();
        }
        return string;
    }

    public static String checkNotEmpty(final String string,
            final Object errorMessage) {
        checkNotNull(string, errorMessage);
        if (string.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return string;
    }

    private Preconditions() {
    }
}
