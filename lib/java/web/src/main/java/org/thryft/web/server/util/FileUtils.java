package org.thryft.web.server.util;

import java.io.File;
import java.io.IOException;

public class FileUtils {
    public static File createTempDirectory(final String prefix,
            final String suffix) throws IOException {
        final File tempDirectoryPath = File.createTempFile(prefix, suffix);
        tempDirectoryPath.delete();
        tempDirectoryPath.mkdir();
        return tempDirectoryPath;
    }
}
