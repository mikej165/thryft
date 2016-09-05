package org.thryft;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.Collection;
import java.util.Map;

import javax.annotation.Nullable;

import com.google.common.base.Optional;
import com.google.common.primitives.UnsignedInteger;

public final class Preconditions {
    public static boolean checkBooleanTrue(final boolean boolean_) {
        return checkBooleanTrue(boolean_, null);
    }

    public static boolean checkBooleanTrue(final boolean boolean_, @Nullable final Object errorMessage) {
        if (!boolean_) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return boolean_;
    }

    public static byte[] checkByteArrayNotEmpty(final byte[] byteArray) {
        return checkByteArrayNotEmpty(byteArray, null);
    }

    public static byte[] checkByteArrayNotEmpty(final byte[] byteArray, @Nullable final Object errorMessage) {
        checkNotNull(byteArray, errorMessage);
        if (byteArray.length == 0) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return byteArray;
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMaxLength(final CollectionT collection,
            final int minLength) {
        return checkCollectionMaxLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMaxLength(final CollectionT collection,
            final int maxLength, @Nullable final Object errorMessage) {
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

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMinLength(final CollectionT collection,
            final int minLength) {
        return checkCollectionMinLength(collection, minLength, null);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkCollectionMinLength(final CollectionT collection,
            final int minLength, @Nullable final Object errorMessage) {
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

    public static int checkIntegerMax(final int integer, final int max) {
        return checkIntegerMax(integer, max, null);
    }

    public static int checkIntegerMax(final int integer, final long max, @Nullable final Object errorMessage) {
        if (integer > max) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return integer;
    }

    public static int checkIntegerMin(final int integer, final int min) {
        return checkIntegerMin(integer, min, null);
    }

    public static int checkIntegerMin(final int integer, final int min, @Nullable final Object errorMessage) {
        if (integer < min) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return integer;
    }

    public static <MapT extends Map<?, ?>> MapT checkMapNotEmpty(final MapT map) {
        return checkMapNotEmpty(map, null);
    }

    public static <MapT extends Map<?, ?>> MapT checkMapNotEmpty(final MapT map, @Nullable final Object errorMessage) {
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

    public static <CollectionT extends Collection<?>> CollectionT checkMaxLength(final CollectionT collection,
            final int maxLength) {
        return checkCollectionMaxLength(collection, maxLength);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMaxLength(final CollectionT collection,
            final int maxLength, @Nullable final Object errorMessage) {
        return checkCollectionMaxLength(collection, maxLength, errorMessage);
    }

    public static String checkMaxLength(final String string, final int maxLength) {
        return checkStringMaxLength(string, maxLength);
    }

    public static String checkMaxLength(final String string, final int maxLength, @Nullable final Object errorMessage) {
        return checkStringMaxLength(string, maxLength, errorMessage);
    }

    public static UnsignedInteger checkMin(final UnsignedInteger unsignedInteger, final int min) {
        return checkUnsignedIntegerMin(unsignedInteger, min);
    }

    public static UnsignedInteger checkMin(final UnsignedInteger unsignedInteger, final int min,
            @Nullable final Object errorMessage) {
        return checkUnsignedIntegerMin(unsignedInteger, min, errorMessage);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMinLength(final CollectionT collection,
            final int minLength) {
        return checkCollectionMinLength(collection, minLength);
    }

    public static <CollectionT extends Collection<?>> CollectionT checkMinLength(final CollectionT collection,
            final int minLength, @Nullable final Object errorMessage) {
        return checkCollectionMinLength(collection, minLength, errorMessage);
    }

    public static String checkMinLength(final String string, final int minLength) {
        return checkStringMinLength(string, minLength);
    }

    public static String checkMinLength(final String string, final int minLength, @Nullable final Object errorMessage) {
        return checkStringMinLength(string, minLength, errorMessage);
    }

    public static byte[] checkNotEmpty(final byte[] byteArray) {
        return checkByteArrayNotEmpty(byteArray);
    }

    public static byte[] checkNotEmpty(final byte[] byteArray, @Nullable final Object errorMessage) {
        return checkByteArrayNotEmpty(byteArray, errorMessage);
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

    public static Optional<Boolean> checkOptionalBooleanTrue(final Optional<Boolean> boolean_) {
        return checkOptionalBooleanTrue(boolean_, null);
    }

    public static Optional<Boolean> checkOptionalBooleanTrue(final Optional<Boolean> boolean_,
            @Nullable final Object errorMessage) {
        if (boolean_.isPresent()) {
            checkBooleanTrue(boolean_.get().booleanValue(), errorMessage);
        }
        return boolean_;
    }

    public static Optional<byte[]> checkOptionalByteArrayNotEmpty(final Optional<byte[]> byteArray) {
        return checkOptionalByteArrayNotEmpty(byteArray, null);
    }

    public static Optional<byte[]> checkOptionalByteArrayNotEmpty(final Optional<byte[]> byteArray,
            @Nullable final Object errorMessage) {
        if (byteArray.isPresent()) {
            checkByteArrayNotEmpty(byteArray.get(), errorMessage);
        }
        return byteArray;
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionMaxLength(
            final Optional<CollectionT> collection, final int maxLength) {
        return checkOptionalCollectionMaxLength(collection, maxLength, null);
    }

    public static <CollectionT extends Collection<?>> Optional<CollectionT> checkOptionalCollectionMaxLength(
            final Optional<CollectionT> collection, final int maxLength, @Nullable final Object errorMessage) {
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
            final Optional<CollectionT> collection, final int minLength, @Nullable final Object errorMessage) {
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
            final Optional<CollectionT> collection, @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkCollectionNotEmpty(collection.get(), errorMessage);
        }
        return collection;
    }

    public static <MapT extends Map<?, ?>> Optional<MapT> checkOptionalMapNotEmpty(final Optional<MapT> map) {
        return checkOptionalMapNotEmpty(map, null);
    }

    public static <MapT extends Map<?, ?>> Optional<MapT> checkOptionalMapNotEmpty(final Optional<MapT> collection,
            @Nullable final Object errorMessage) {
        checkNotNull(collection);
        if (collection.isPresent()) {
            checkMapNotEmpty(collection.get(), errorMessage);
        }
        return collection;
    }

    public static Optional<String> checkOptionalStringMaxLength(final Optional<String> string, final int maxLength) {
        return checkOptionalStringMaxLength(string, maxLength, null);
    }

    public static Optional<String> checkOptionalStringMaxLength(final Optional<String> string, final int maxLength,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringMaxLength(string.get(), maxLength, errorMessage);
        }
        return string;
    }

    public static Optional<String> checkOptionalStringMinLength(final Optional<String> string, final int minLength) {
        return checkOptionalStringMinLength(string, minLength, null);
    }

    public static Optional<String> checkOptionalStringMinLength(final Optional<String> string, final int minLength,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringMinLength(string.get(), minLength, errorMessage);
        }
        return string;
    }

    public static Optional<String> checkOptionalStringNotEmpty(final Optional<String> string) {
        return checkOptionalStringNotEmpty(string, null);
    }

    public static Optional<String> checkOptionalStringNotEmpty(final Optional<String> string,
            @Nullable final Object errorMessage) {
        if (string.isPresent()) {
            checkStringNotEmpty(string.get(), errorMessage);
        }
        return string;
    }

    public static Optional<UnsignedInteger> checkOptionalUnsignedIntegerMin(
            final Optional<UnsignedInteger> unsignedInteger, final long min) {
        return checkOptionalUnsignedIntegerMin(unsignedInteger, min, null);
    }

    public static Optional<UnsignedInteger> checkOptionalUnsignedIntegerMin(
            final Optional<UnsignedInteger> unsignedInteger, final long min, @Nullable final Object errorMessage) {
        if (unsignedInteger.isPresent()) {
            checkUnsignedIntegerMin(unsignedInteger.get(), min, errorMessage);
        }
        return unsignedInteger;
    }

    public static String checkStringMaxLength(final String string, final int maxLength) {
        return checkStringMaxLength(string, maxLength, null);
    }

    public static String checkStringMaxLength(final String string, final int maxLength,
            @Nullable final Object errorMessage) {
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

    public static String checkStringMinLength(final String string, final int minLength) {
        return checkStringMinLength(string, minLength, null);
    }

    public static String checkStringMinLength(final String string, final int minLength,
            @Nullable final Object errorMessage) {
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

    public static UnsignedInteger checkUnsignedIntegerMin(final UnsignedInteger unsignedInteger, final long min) {
        return checkUnsignedIntegerMin(unsignedInteger, min, null);
    }

    public static UnsignedInteger checkUnsignedIntegerMin(final UnsignedInteger unsignedInteger, final long min,
            @Nullable final Object errorMessage) {
        if (unsignedInteger.longValue() < min) {
            if (errorMessage != null) {
                throw new IllegalArgumentException(String.valueOf(errorMessage));
            } else {
                throw new IllegalArgumentException();
            }
        }
        return unsignedInteger;
    }

    private Preconditions() {
    }
}
