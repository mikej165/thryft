package org.thryft.web.server.util.test;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.thryft.web.server.util.FileNameCodec;

public class FileNameCodecTest {
    @Test
    public void runTest() {
        final String[] fileNames = { "test@example.com", "test/example", "test" };
        for (final String fileName : fileNames) {
            final String encodedFileName = FileNameCodec
                    .encodeFileName(fileName);
            final String decodedFileName = FileNameCodec
                    .decodeFileName(encodedFileName);
            assertEquals(fileName, decodedFileName);
        }
    }
}
