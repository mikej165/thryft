package org.thryft.web.server.store;

import static com.google.common.base.Preconditions.checkNotNull;

import org.apache.thrift.TBase;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public class PrimaryBackupStore<ModelT extends TBase<?, ?>> extends
        Store<ModelT> {
    public PrimaryBackupStore(final Store<ModelT> primaryStore,
            final Store<ModelT> backupStore) {
        super(primaryStore._getModelClass());
        this.backupStore = checkNotNull(backupStore);
        this.primaryStore = checkNotNull(primaryStore);
    }

    @Override
    protected boolean _deleteModelById(final String modelId,
            final String username) {
        if (primaryStore._deleteModelById(modelId, username)) {
            backupStore._deleteModelById(modelId, username);
            return true;
        } else {
            return false;
        }
    }

    @Override
    protected void _deleteModels(final String username) {
        primaryStore._deleteModels(username);
        backupStore._deleteModels(username);
    }

    @Override
    protected ModelT _getModelById(final String modelId, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        return primaryStore._getModelById(modelId, username);
    }

    @Override
    protected int _getModelCount(final String username) {
        return primaryStore._getModelCount(username);
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String username) {
        return primaryStore._getModelIds(username);
    }

    @Override
    protected ImmutableSet<ModelT> _getModels(final String username) {
        return primaryStore._getModels(username);
    }

    @Override
    protected ImmutableSet<ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        return primaryStore._getModelsByIds(modelIds, username);
    }

    @Override
    protected ImmutableSet<String> _getUsernames() {
        return primaryStore._getUsernames();
    }

    @Override
    protected boolean _headModelById(final String modelId, final String username) {
        return primaryStore._headModelById(modelId, username);
    }

    @Override
    protected void _putModel(final ModelT model, final String modelId,
            final String username) {
        primaryStore.putModel(model, modelId, username);
        backupStore.putModel(model, modelId, username);
    }

    @Override
    protected void _putModels(final ImmutableMap<String, ModelT> models,
            final String username) {
        primaryStore.putModels(models, username);
        backupStore.putModels(models, username);
    }

    private final Store<ModelT> backupStore;

    private final Store<ModelT> primaryStore;
}