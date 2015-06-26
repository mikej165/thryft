package org.thryft.store;

import org.apache.commons.codec.digest.DigestUtils;

public final class PasswordUtils {
    public static String hashPassword(final String password) {
        return DigestUtils.shaHex(password);
    }

    public static boolean isPasswordHashed(final String hashedPassword) {
        return hashedPassword.matches("[a-fA-F0-9]{40}");
    }

    private PasswordUtils() {

    }
}
