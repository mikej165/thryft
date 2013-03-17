package org.thryft.core;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableSet;

public final class Preconditions {
    public static <T> ImmutableList<T> checkNotEmpty(final ImmutableList<T> list) {
        if (list == null) {
            throw new NullPointerException();
        }
        if (list.isEmpty()) {
            throw new IllegalArgumentException();
        }
        return list;
    }

    public static <T> ImmutableList<T> checkNotEmpty(
            final ImmutableList<T> list, final Object errorMessage) {
        if (list == null) {
            throw new NullPointerException(String.valueOf(errorMessage));
        }
        if (list.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return list;
    }

    public static <T> ImmutableSet<T> checkNotEmpty(final ImmutableSet<T> set) {
        if (set == null) {
            throw new NullPointerException();
        }
        if (set.isEmpty()) {
            throw new IllegalArgumentException();
        }
        return set;
    }

    public static <T> ImmutableSet<T> checkNotEmpty(final ImmutableSet<T> set,
            final Object errorMessage) {
        if (set == null) {
            throw new NullPointerException(String.valueOf(errorMessage));
        }
        if (set.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return set;
    }

    public static String checkNotEmpty(final String string) {
        if (string == null) {
            throw new NullPointerException();
        }
        if (string.isEmpty()) {
            throw new IllegalArgumentException();
        }
        return string;
    }

    public static String checkNotEmpty(final String string,
            final Object errorMessage) {
        if (string == null) {
            throw new NullPointerException(String.valueOf(errorMessage));
        }
        if (string.isEmpty()) {
            throw new IllegalArgumentException(String.valueOf(errorMessage));
        }
        return string;
    }

    private Preconditions() {
    }
}
