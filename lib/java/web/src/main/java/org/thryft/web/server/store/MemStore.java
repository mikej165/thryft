package org.thryft.web.server.store;

import java.util.Set;

import org.apache.thrift.TBase;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Sets;
import com.google.common.collect.Table;
import com.google.common.collect.TreeBasedTable;

public final class MemStore<ModelT extends TBase<?, ?>> extends Store<ModelT> {
    public MemStore(final Class<ModelT> modelClass) {
        super(modelClass);
    }

    @Override
    protected synchronized boolean _deleteModelById(final String modelId,
            final String username) {
        return models.remove(username, modelId) != null;
    }

    @Override
    protected synchronized void _deleteModels(final String username) {
        for (final String columnKey : ImmutableSet.copyOf(models.row(username)
                .keySet())) {
            models.remove(username, columnKey);
        }
    }

    @Override
    protected synchronized ModelT _getModelById(final String modelId,
            final String username) throws NoSuchModelException {
        final ModelT model = models.get(username, modelId);
        if (model != null) {
            return model;
        } else {
            throw new NoSuchModelException(modelId);
        }
    }

    @Override
    protected synchronized int _getModelCount(final String username) {
        return models.row(username).size();
    }

    @Override
    protected synchronized ImmutableSet<String> _getModelIds(
            final String username) {
        return ImmutableSet.copyOf(models.row(username).keySet());
    }

    @Override
    protected synchronized ImmutableSet<ModelT> _getModels(final String username) {
        return ImmutableSet.copyOf(models.row(username).values());
    }

    @Override
    protected synchronized ImmutableSet<ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws NoSuchModelException {
        final Set<ModelT> models = Sets.newLinkedHashSet();
        for (final String modelId : modelIds) {
            models.add(getModelById(modelId, username));
        }
        return ImmutableSet.copyOf(models);
    }

    @Override
    protected ImmutableSet<String> _getUsernames() {
        return ImmutableSet.copyOf(models.rowKeySet());
    }

    @Override
    protected synchronized boolean _headModelById(final String modelId,
            final String username) {
        return models.get(username, modelId) != null;
    }

    @Override
    protected synchronized void _putModel(final ModelT model,
            final String modelId, final String username) {
        models.put(username, modelId, model);
    }

    @Override
    protected synchronized void _putModels(
            final ImmutableMap<String, ModelT> models, final String username) {
        for (final ImmutableMap.Entry<String, ModelT> model : models.entrySet()) {
            this.models.put(username, model.getKey(), model.getValue());
        }
    }

    private final Table<String, String, ModelT> models = TreeBasedTable
            .create(); // Username, model ID, model
}
