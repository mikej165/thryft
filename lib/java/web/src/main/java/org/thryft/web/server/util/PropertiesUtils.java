package org.thryft.web.server.util;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Properties;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PropertiesUtils {
    public static Properties loadPropertiesFromFile(final String fileName) {
        final Properties properties = new Properties();
        try {
            final String filePath = "/etc/yogento/" + fileName;
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
