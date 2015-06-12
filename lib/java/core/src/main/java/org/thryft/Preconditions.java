package org.thryft;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Collection;
import java.util.Map;

import javax.annotation.Nullable;

import com.google.common.base.Optional;

public final class Preconditions {
    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMaxLength(
            final CollectionT collection, final int minLength) {
        return checkCollectionMaxLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMaxLength(
            final CollectionT collection, final int maxLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.size() > maxLength) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMinLength(
            final CollectionT collection, final int minLength) {
        return checkCollectionMinLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMinLength(
            final CollectionT collection, final int minLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection, errorMessage);
        if (collection.size() < minLength) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
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

    public static <MapT extends Map<?, ?>> MapT checkMapNotEmpty(final MapT map) {
        return checkMapNotEmpty(map, null);
    }

    public static <MapT extends Map<?, ?>> MapT checkMapNotEmpty(
            final MapT map, @Nullable final Object errorMessage) {
        checkNotNull(map, errorMessage);
        if (map.isEmpty()) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return map;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMaxLength(
            final CollectionT collection, final int maxLength) {
        return checkCollectionMaxLength(collection, maxLength);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMaxLength(
            final CollectionT collection, final int maxLength,
            @Nullable final Object errorMessage) {
        return checkCollectionMaxLength(collection, maxLength, errorMessage);
    }

    public static String checkMaxLength(final String string, final int maxLength) {
        return checkStringMaxLength(string, maxLength);
    }

    public static String checkMaxLength(final String string,
            final int maxLength, @Nullable final Object errorMessage) {
        return checkStringMaxLength(string, maxLength, errorMessage);
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

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionMaxLength(
            final Optional<CollectionT> collection, final int maxLength) {
        return checkOptionalCollectionMaxLength(collection, maxLength, null);
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionMaxLength(
            final Optional<CollectionT> collection, final int maxLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkCollectionMaxLength(collection.get(), maxLength, errorMessage);
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionMinLength(
            final Optional<CollectionT> collection, final int minLength) {
        return checkOptionalCollectionMinLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionMinLength(
            final Optional<CollectionT> collection, final int minLength,
            @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkCollectionMinLength(collection.get(), minLength, errorMessage);
        }
        return collection;
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionNotEmpty(
            final Optional<CollectionT> collection) {
        return checkOptionalCollectionNotEmpty(collection, null);
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionNotEmpty(
            final Optional<CollectionT> collection,
            @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkCollectionNotEmpty(collection.get(), errorMessage);
        }
        return collection;
    }

    public static <MapT extends Map<?, ?>> Optional<MapT> checkOptionalMapNotEmpty(
            final Optional<MapT> map) {
        return checkOptionalMapNotEmpty(map, null);
    }

    public static <MapT extends Map<?, ?>> Optional<MapT> checkOptionalMapNotEmpty(
            final Optional<MapT> collection, @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkMapNotEmpty(collection.get(), errorMessage);
        }
        return collection;
    }

    public static Optional<String> checkOptionalStringMaxLength(
            final Optional<String> string, final int maxLength) {
        return checkOptionalStringMaxLength(string, maxLength, null);
    }

    public static Optional<String> checkOptionalStringMaxLength(
            final Optional<String> string, final int maxLength,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringMaxLength(string.get(), maxLength, errorMessage);
        }
        return string;
    }

    public static Optional<String> checkOptionalStringMinLength(
            final Optional<String> string, final int minLength) {
        return checkOptionalStringMinLength(string, minLength, null);
    }

    public static Optional<String> checkOptionalStringMinLength(
            final Optional<String> string, final int minLength,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringMinLength(string.get(), minLength, errorMessage);
        }
        return string;
    }

    public static Optional<String> checkOptionalStringNotEmpty(
            final Optional<String> string) {
        return checkOptionalStringNotEmpty(string, null);
    }

    public static Optional<String> checkOptionalStringNotEmpty(
            final Optional<String> string, @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringNotEmpty(string.get(), errorMessage);
        }
        return string;
    }

    public static String checkStringMaxLength(final String string,
            final int maxLength) {
        return checkStringMaxLength(string, maxLength, null);
    }

    public static String checkStringMaxLength(final String string,
            final int maxLength, @Nullable final Object errorMessage) {
        checkNotNull(string, errorMessage);
        if (string.length() > maxLength) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
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
