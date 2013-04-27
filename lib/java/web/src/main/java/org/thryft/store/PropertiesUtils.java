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

package org.thryft.store;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Properties;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PropertiesUtils {
    public static Properties loadPropertiesFromFile(final String etcSubdirectoryName,
            final String fileName) {
        final Properties properties = new Properties();
        try {
            final String filePath = "/etc/" + etcSubdirectoryName + "/" + fileName;
            final InputStream inputStream = new FileInputStream(filePath);
            try {
                properties.load(inputStream);
                if (!properties.isEmpty()) {
                    logger.info("loaded " + filePath + " from the file system");
                    return properties;
                }
            } finally {
                inputStream.close();
            }
        } catch (final Exception e) {
        }
        try {
            final InputStream inputStream = PropertiesUtils.class
                    .getClassLoader().getResourceAsStream(fileName);
            if (inputStream == null) {
                return properties;
            }
            try {
                properties.load(inputStream);
                logger.info("loaded " + fileName + " from CLASSPATH");
            } finally {
                inputStream.close();
            }
        } catch (final Exception e) {
            logger.error("error loading " + fileName + ": ", e);
        }
        return properties;
    }

    private final static Logger logger = LoggerFactory
            .getLogger(PropertiesUtils.class);
}
