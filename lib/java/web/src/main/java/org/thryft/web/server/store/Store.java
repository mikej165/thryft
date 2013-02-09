package org.thryft.web.server.store;

import static com.google.common.base.Preconditions.checkNotNull;

import java.lang.reflect.InvocationTargetException;

import org.apache.shiro.subject.Subject;
import org.apache.thrift.TBase;
import org.apache.thrift.protocol.TProtocol;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;

public abstract class Store<ModelT extends TBase<?, ?>> {
    @SuppressWarnings("serial")
    public final static class NoSuchModelException extends Exception {
        public NoSuchModelException(final String id) {
            super(id);
            this.id = id;
        }

        public String getId() {
            return id;
        }

        private final String id;
    }

    protected Store(final Class<ModelT> modelClass) {
        logger = LoggerFactory.getLogger(getClass());
        this.modelClass = checkNotNull(modelClass);
    }

    public final boolean deleteModelById(final String modelId,
            final String username) {
        checkNotNull(modelId);
        checkNotNull(username);
        return _deleteModelById(modelId, username);
    }

    public final boolean deleteModelById(final String modelId,
            final Subject user) {
        checkNotNull(user);
        return deleteModelById(modelId, user.getPrincipal().toString());
    }

    public final void deleteModels(final String username) {
        checkNotNull(username);
        _deleteModels(username);
    }

    public final void deleteModels(final Subject user) {
        checkNotNull(user);
        deleteModels(user.getPrincipal().toString());
    }

    public final ModelT getModelById(final String modelId, final String username)
            throws NoSuchModelException {
        checkNotNull(modelId);
        checkNotNull(username);
        return checkNotNull(_getModelById(modelId, username));
    }

    public final ModelT getModelById(final String modelId, final Subject user)
            throws NoSuchModelException {
        checkNotNull(user);
        return getModelById(modelId, user.getPrincipal().toString());
    }

    public final int getModelCount(final String username) {
        checkNotNull(username);
        return _getModelCount(username);
    }

    public final int getModelCount(final Subject user) {
        checkNotNull(user);
        return getModelCount(user.getPrincipal().toString());
    }

    public final ImmutableSet<String> getModelIds(final String username) {
        checkNotNull(username);
        return checkNotNull(_getModelIds(username));
    }

    public final ImmutableSet<String> getModelIds(final Subject user) {
        checkNotNull(user);
        return getModelIds(user.getPrincipal().toString());
    }

    public final ImmutableSet<ModelT> getModels(final String username) {
        checkNotNull(username);
        return checkNotNull(_getModels(username));
    }

    public final ImmutableSet<ModelT> getModels(final Subject user) {
        checkNotNull(user);
        return getModels(user.getPrincipal().toString());
    }

    public final ImmutableSet<ModelT> getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws NoSuchModelException {
        checkNotNull(modelIds);
        if (modelIds.isEmpty()) {
            return ImmutableSet.of();
        }
        checkNotNull(username);
        return checkNotNull(_getModelsByIds(modelIds, username));
    }

    public final ImmutableSet<ModelT> getModelsByIds(
            final ImmutableSet<String> modelIds, final Subject user)
            throws NoSuchModelException {
        checkNotNull(user);
        return getModelsByIds(modelIds, user.getPrincipal().toString());
    }

    public final ImmutableSet<String> getUsernames() {
        return checkNotNull(_getUsernames());
    }

    public final boolean headModelById(final String modelId,
            final String username) {
        checkNotNull(modelId);
        checkNotNull(username);
        return _headModelById(modelId, username);
    }

    public final boolean headModelById(final String modelId, final Subject user) {
        checkNotNull(user);
        return headModelById(modelId, user.getPrincipal().toString());
    }

    public final void putModel(final ModelT model, final String modelId,
            final String username) {
        checkNotNull(model);
        checkNotNull(modelId);
        checkNotNull(username);
        _putModel(model, modelId, username);
    }

    public final void putModel(final ModelT model, final String modelId,
            final Subject user) {
        checkNotNull(user);
        putModel(model, modelId, user.getPrincipal().toString());
    }

    public final void putModels(final ImmutableMap<String, ModelT> models,
            final String username) {
        checkNotNull(models);
        if (models.isEmpty()) {
            return;
        }
        checkNotNull(username);
        _putModels(models, username);
    }

    public final void putModels(final ImmutableMap<String, ModelT> models,
            final Subject user) {
        checkNotNull(user);
        putModels(models, user.getPrincipal().toString());
    }

    protected abstract boolean _deleteModelById(final String modelId,
            final String username);

    protected abstract void _deleteModels(final String username);

    protected ModelT _getModel(final TProtocol iprot) {
        try {
            return modelClass.getConstructor(TProtocol.class)
                    .newInstance(iprot);
        } catch (final IllegalArgumentException e) {
            logger.error("exception reading:", e);
        } catch (final SecurityException e) {
            logger.error("exception reading model:", e);
        } catch (final InstantiationException e) {
            logger.error("exception reading model:", e);
        } catch (final IllegalAccessException e) {
            logger.error("exception reading model:", e);
        } catch (final InvocationTargetException e) {
            logger.error("exception reading model:", e);
        } catch (final NoSuchMethodException e) {
            logger.error("exception reading model:", e);
        }

        return null;
    }

    protected abstract ModelT _getModelById(final String modelId,
            final String username) throws NoSuchModelException;

    protected final Class<ModelT> _getModelClass() {
        return modelClass;
    }

    protected abstract int _getModelCount(final String username);

    protected abstract ImmutableSet<String> _getModelIds(final String username);

    protected abstract ImmutableSet<ModelT> _getModels(final String username);

    protected abstract ImmutableSet<ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws NoSuchModelException;

    protected abstract ImmutableSet<String> _getUsernames();

    protected abstract boolean _headModelById(final String modelId,
            final String username);

    protected abstract void _putModel(final ModelT model, final String modelId,
            final String username);

    protected abstract void _putModels(
            final ImmutableMap<String, ModelT> models, final String username);

    protected final Logger logger;

    private final Class<ModelT> modelClass;
}
