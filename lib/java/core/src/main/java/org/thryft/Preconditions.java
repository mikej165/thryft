package org.thryft;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Collection;

import javax.annotation.Nullable;

import com.google.common.base.Optional;

public final class Preconditions {
    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMinLength(
            final CollectionT collection, final int minLength) {
        return checkCollectionMinLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMinLength(
            final CollectionT collection, final int minLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.size() < minLength) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkCollectionMinLength(
            final Optional<CollectionT> collection, final int minLength) {
        return checkCollectionMinLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkCollectionMinLength(
            final Optional<CollectionT> collection, final int minLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            if (collection.get().size() < minLength) {
                if (errorMessage != null) {
                    throw new IllegalArgumentException(errorMessage.toString());
                } else {
                    throw new IllegalArgumentException();
                }
            }
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionNotEmpty(
            final CollectionT collection) {
        return checkCollectionNotEmpty(collection, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionNotEmpty(
            final CollectionT collection, @Nullable final Object errorMessage) {
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

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkCollectionNotEmpty(
            final Optional<CollectionT> collection) {
        return checkCollectionNotEmpty(collection, null);
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkCollectionNotEmpty(
            final Optional<CollectionT> collection,
            @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkCollectionNotEmpty(collection.get(), errorMessage);
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMinLength(
            final CollectionT collection, final int minLength) {
        return checkCollectionMinLength(collection, minLength);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMinLength(
            final CollectionT collection, final int minLength,
            @Nullable final Object errorMessage) {
        return checkCollectionMinLength(collection, minLength, errorMessage);
    }

    public static String checkMinLength(final String string, final int minLength) {
        return checkStringMinLength(string, minLength);
    }

    public static String checkMinLength(final String string,
            final int minLength, @Nullable final Object errorMessage) {
        return checkStringMinLength(string, minLength, errorMessage);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkNotEmpty(
            final CollectionT collection) {
        return checkCollectionNotEmpty(collection);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkNotEmpty(
            final CollectionT collection, @Nullable final Object errorMessage) {
        return checkCollectionNotEmpty(collection, errorMessage);
    }

    public static String checkNotEmpty(final String string) {
        return checkStringNotEmpty(string);
    }

    public static String checkNotEmpty(final String string,
            @Nullable final Object errorMessage) {
        return checkStringNotEmpty(string, errorMessage);
    }

    public static Optional<String> checkStringMinLength(
            final Optional<String> string, final int minLength) {
        return checkStringMinLength(string, minLength, null);
    }

    public static Optional<String> checkStringMinLength(
            final Optional<String> string, final int minLength,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringMinLength(string.get(), minLength, errorMessage);
        }
        return string;
    }

    public static String checkStringMinLength(final String string,
            final int minLength) {
        return checkStringMinLength(string, minLength, null);
    }

    public static String checkStringMinLength(final String string,
            final int minLength, @Nullable final Object errorMessage) {
        checkNotNull(string, errorMessage);
        if (string.length() < minLength) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return string;
    }

    public static Optional<String> checkStringNotEmpty(
            final Optional<String> string) {
        if (string.isPresent()) {
            checkStringNotEmpty(string.get());
        }
        return string;
    }

    public static Optional<String> checkStringNotEmpty(
            final Optional<String> string, @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringNotEmpty(string.get(), errorMessage);
        }
        return string;
    }

    public static String checkStringNotEmpty(final String string) {
        return checkStringNotEmpty(string, null);
    }

    public static String checkStringNotEmpty(final String string,
            @Nullable final Object errorMessage) {
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
