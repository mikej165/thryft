package org.thryft;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Collection;

import javax.annotation.Nullable;

public final class Preconditions {
    public static <CollectionT extends Collection<?>> CollectionT checkCollectionNotEmpty(
            final CollectionT collection) {
        return checkCollectionNotEmpty(collection, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionNotEmpty(final CollectionT collection,
            @Nullable final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.isEmpty()) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkNotEmpty(final CollectionT collection) {
        return checkCollectionNotEmpty(collection);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkNotEmpty(final CollectionT collection,
            @Nullable final Object errorMessage) {
        return checkCollectionNotEmpty(collection, errorMessage);
    }

    public static String checkNotEmpty(final String string) {
        return checkStringNotEmpty(string);
    }

    public static String checkNotEmpty(final String string, @Nullable final Object errorMessage) {
        return checkStringNotEmpty(string, errorMessage);
    }

    public static String checkStringNotEmpty(final String string) {
        return checkStringNotEmpty(string, null);
    }

    public static String checkStringNotEmpty(final String string, @Nullable final Object errorMessage) {
        checkNotNull(string, errorMessage);
        if (string.isEmpty()) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return string;
    }

    private Preconditions() {
    }
}
