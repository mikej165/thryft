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

import java.util.Collection;

import com.google.common.collect.ImmutableMap;

public final class Comparators {
    public static int compare(final byte[] left, final byte[] right) {
        int result = ((Integer) left.length).compareTo(right.length);
        if (result != 0) {
            return result;
        }

        for (int i = 0; i < left.length; i++) {
            result = ((Byte) left[i]).compareTo(right[i]);
            if (result != 0) {
                return result;
            }
        }

        return 0;
    }

    public static <E extends Comparable<E>> int compare(
            final Collection<E> left, final Collection<E> right) {
        int result = ((Integer) left.size()).compareTo(right.size());
        if (result != 0) {
            return result;
        }

        final java.util.List<E> leftSortedList = com.google.common.collect.Lists
                .newArrayList(left);
        java.util.Collections.sort(leftSortedList);
        final java.util.Iterator<E> leftI = leftSortedList.iterator();

        final java.util.List<E> rightSortedList = com.google.common.collect.Lists
                .newArrayList(right);
        java.util.Collections.sort(rightSortedList);
        final java.util.Iterator<E> rightI = leftSortedList.iterator();

        while (leftI.hasNext()) {
            final E leftElement = leftI.next();
            final E rightElement = rightI.next();

            result = leftElement.compareTo(rightElement);
            if (result != 0) {
                return result;
            }
        }

        return 0;
    }

    public static <K, V extends Comparable<V>> int compare(
            final ImmutableMap<K, V> left, final ImmutableMap<K, V> right) {
        for (final com.google.common.collect.ImmutableMap.Entry<K, V> leftEntry : left
                .entrySet()) {
            final V rightValue = right.get(leftEntry.getKey());
            if (rightValue == null) {
                return 1;
            }
            final int result = leftEntry.getValue().compareTo(rightValue);
            if (result != 0) {
                return result;
            }
        }

        return 0;
    }

    public static int compare(final Object left, final Object right) {
        if (left.equals(right)) {
            return 0;
        } else {
            return -1;
        }
    }

    private Comparators() {
    }
}
