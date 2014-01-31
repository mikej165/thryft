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

import static com.google.common.base.Preconditions.checkNotNull;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.FilenameUtils;
import org.thryft.Base;
import org.thryft.protocol.JsonProtocol;

import com.google.common.base.CaseFormat;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public final class FsStore<ModelT extends Base<?>> extends
        AbstractStore<ModelT> {
    public final static class Configuration {
        public Configuration() {
            this(ROOT_DIRECTORY_PATH_DEFAULT);
        }

        public Configuration(final File rootDirectoryPath) {
            this.rootDirectoryPath = checkNotNull(rootDirectoryPath);
        }

        public Configuration(final Properties properties) {
            final String rootDirectoryPath = properties.getProperty(this
                    .getClass().getCanonicalName() + ".rootDirectoryPath");
            if (rootDirectoryPath != null) {
                this.rootDirectoryPath = new File(rootDirectoryPath);
            } else {
                this.rootDirectoryPath = ROOT_DIRECTORY_PATH_DEFAULT;
            }
        }

        public File getRootDirectoryPath() {
            return rootDirectoryPath;
        }

        private final File rootDirectoryPath;

        public final static File ROOT_DIRECTORY_PATH_DEFAULT = new File("data");
    }

    public FsStore(final Configuration configuration,
            final Class<ModelT> modelClass) {
        super(modelClass);
        checkNotNull(configuration);
        if (!configuration.getRootDirectoryPath().exists()) {
            configuration.getRootDirectoryPath().mkdir();
        }
        this.rootDirectoryPath = configuration.rootDirectoryPath
                .getAbsoluteFile();
        final File modelSubdirectoryPath = new File(CaseFormat.UPPER_CAMEL.to(
                CaseFormat.LOWER_UNDERSCORE, modelClass.getSimpleName())
                .replace('_', File.separatorChar));
        modelSubdirectoryName = modelSubdirectoryPath.getName();
        this.modelSubdirectoryPath = modelSubdirectoryPath.toString();
    }

    @Override
    protected synchronized boolean _deleteModelById(final String modelId,
            final String userId) {
        return __getModelFilePath(modelId, userId).delete();
    }

    @Override
    protected synchronized void _deleteModels(final String userId) {
        try {
            FileUtils.deleteDirectory(__getModelDirectoryPath(userId));
        } catch (final IOException e) {
            logger.error("error deleting models: ", e);
        }
    }

    @Override
    protected synchronized ModelT _getModelById(final String modelId,
            final String userId) throws ModelIoException, NoSuchModelException {
        return __getModel(__getModelFilePath(modelId, userId));
    }

    @Override
    protected synchronized int _getModelCount(final String userId) {
        final File modelDirectoryPath = __getModelDirectoryPath(userId);
        if (!modelDirectoryPath.isDirectory()) {
            return 0;
        }

        int modelCount = 0;
        for (final File modelFilePath : modelDirectoryPath.listFiles()) {
            if (!modelFilePath.isFile()) {
                continue;
            }

            modelCount++;
        }
        return modelCount;
    }

    @Override
    protected synchronized ImmutableSet<String> _getModelIds(final String userId) {
        final File modelDirectoryPath = __getModelDirectoryPath(userId);
        if (!modelDirectoryPath.isDirectory()) {
            return ImmutableSet.of();
        }

        final ImmutableSet.Builder<String> modelIds = ImmutableSet.builder();
        for (final File modelFilePath : modelDirectoryPath.listFiles()) {
            if (!modelFilePath.isFile()) {
                continue;
            }

            modelIds.add(__getModelId(modelFilePath));
        }
        return modelIds.build();
    }

    @Override
    protected synchronized ImmutableMap<String, ModelT> _getModels(
            final String userId) throws org.thryft.store.Store.ModelIoException {
        final File modelDirectoryPath = __getModelDirectoryPath(userId);
        if (!modelDirectoryPath.isDirectory()) {
            return ImmutableMap.of();
        }

        final ImmutableMap.Builder<String, ModelT> models = ImmutableMap
                .builder();
        for (final File modelFilePath : modelDirectoryPath.listFiles()) {
            try {
                final ModelT model = __getModel(modelFilePath);
                models.put(__getModelId(modelFilePath), model);
            } catch (final NoSuchModelException e) {
                logger.error("unexpected NoSuchModelException in _getModels: ",
                        e);
                throw new IllegalStateException();
            }
        }
        return models.build();
    }

    @Override
    protected synchronized ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String userId)
            throws ModelIoException, NoSuchModelException {
        final ImmutableMap.Builder<String, ModelT> models = ImmutableMap
                .builder();
        for (final String modelId : modelIds) {
            models.put(modelId, __getModel(__getModelFilePath(modelId, userId)));
        }
        return models.build();
    }

    @Override
    protected ImmutableSet<String> _getUserIds() {
        if (!rootDirectoryPath.isDirectory()) {
            return ImmutableSet.of();
        }

        final ImmutableSet.Builder<String> userIds = ImmutableSet.builder();
        for (final File userDirectoryPath : rootDirectoryPath.listFiles()) {
            if (!userDirectoryPath.isDirectory()) {
                continue;
            }
            userIds.add(__getModelId(userDirectoryPath));
        }
        return userIds.build();
    }

    @Override
    protected synchronized boolean _headModelById(final String modelId,
            final String userId) {
        return __getModelFilePath(modelId, userId).isFile();
    }

    @Override
    protected synchronized void _putModel(final ModelT model,
            final String modelId, final String userId)
            throws org.thryft.store.AbstractStore.ModelIoException {
        final File modelDirectoryPath = __createModelDirectory(userId);
        __putModel(model, modelDirectoryPath, modelId);
    }

    @Override
    protected synchronized void _putModels(
            final ImmutableMap<String, ModelT> models, final String userId)
            throws ModelIoException {
        final File modelDirectoryPath = __createModelDirectory(userId);
        for (final ImmutableMap.Entry<String, ModelT> model : models.entrySet()) {
            __putModel(model.getValue(), modelDirectoryPath, model.getKey());
        }
    }

    private File __createModelDirectory(final String userId)
            throws org.thryft.store.AbstractStore.ModelIoException {
        final File modelDirectoryPath = __getModelDirectoryPath(userId);
        if (!modelDirectoryPath.isDirectory()) {
            if (!modelDirectoryPath.mkdirs()) {
                throw new ModelIoException("error creating user directory "
                        + modelDirectoryPath);
            }
        }
        return modelDirectoryPath;
    }

    private ModelT __getModel(final File modelFilePath)
            throws ModelIoException, NoSuchModelException {
        if (!modelFilePath.isFile()) {
            throw new NoSuchModelException(__getModelId(modelFilePath));
        }

        try {
            final FileReader fileReader = new FileReader(modelFilePath);
            try {
                return _getModel(new JsonProtocol(fileReader));
            } finally {
                fileReader.close();
            }
        } catch (final IOException e) {
            logger.error("error reading model from disk: ", e);
            throw new ModelIoException(e.getMessage());
        }
    }

    private File __getModelDirectoryPath(final String userId) {
        return new File(new File(rootDirectoryPath,
                FileNameCodec.encodeFileName(userId)), modelSubdirectoryPath);
    }

    private File __getModelFilePath(final File modelDirectoryPath,
            final String modelId) {
        return new File(modelDirectoryPath,
                FileNameCodec.encodeFileName(modelId) + ".json");
    }

    private File __getModelFilePath(final String modelId, final String userId) {
        return __getModelFilePath(__getModelDirectoryPath(userId), modelId);
    }

    private String __getModelId(final File modelFilePath) {
        return FileNameCodec.decodeFileName(FilenameUtils
                .getBaseName(modelFilePath.getName()));
    }

    private void __putModel(final ModelT model, final File modelDirectoryPath,
            final String modelId) throws ModelIoException {
        final File modelFilePath = __getModelFilePath(modelDirectoryPath,
                modelId);

        File modelTempFilePath;
        try {
            modelTempFilePath = File
                    .createTempFile(modelSubdirectoryName, null);
        } catch (final IOException e) {
            logger.error("error creating temp file for model:", e);
            return;
        }

        try {
            final FileWriter fileWriter = new FileWriter(modelTempFilePath);
            try {
                final JsonProtocol oprot = new JsonProtocol(fileWriter);
                model.write(oprot);
                oprot.flush();
            } finally {
                fileWriter.close();
            }

            // Try atomically renaming the temp file to the real file
            // Should work on POSIX systems
            if (modelTempFilePath.renameTo(modelFilePath)) {
                return;
            } else {
                // Try deleting and renaming the temp file to the real file
                if (modelFilePath.delete()
                        && modelTempFilePath.renameTo(modelFilePath)) {
                    return;
                } else {
                    modelTempFilePath.delete();
                    logger.error("error writing model to disk: cannot delete and copy");
                }
            }

        } catch (final IOException e) {
            logger.error("error writing model to disk: ", e);
            throw new ModelIoException(e, modelId);
        }
    }

    private final String modelSubdirectoryName;

    private final String modelSubdirectoryPath;

    private final File rootDirectoryPath;
}
