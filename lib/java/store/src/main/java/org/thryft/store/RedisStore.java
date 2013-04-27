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

import java.util.Map;
import java.util.Properties;
import java.util.Set;

import org.apache.thrift.TBase;
import org.apache.thrift.TException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.thryft.core.protocol.StringMapProtocol;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.exceptions.JedisException;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Sets;

public final class RedisStore<ModelT extends TBase<?, ?>> extends
        KeyValueStore<ModelT> {
    public final static class Configuration {
        public Configuration(final Properties properties) {
            host = properties.getProperty(this.getClass().getCanonicalName()
                    + ".host");
            if (host == null) {
                throw new IllegalArgumentException("missing Redis host");
            }
            final String port = properties.getProperty(this.getClass()
                    .getCanonicalName() + ".port");
            try {
                this.port = Integer.parseInt(port);
            } catch (final NumberFormatException e) {
            }
        }

        public Configuration(final String host) {
            this.host = checkNotNull(host);
            this.port = null;
        }

        public Configuration(final String host, final int port) {
            this.host = checkNotNull(host);
            this.port = port;
        }

        public String getHost() {
            return host;
        }

        public Integer getPort() {
            return port;
        }

        private final String host;
        private Integer port;
    }

    public RedisStore(final Configuration configuration,
            final Class<ModelT> modelClass) {
        super(modelClass);
        checkNotNull(configuration);
        if (configuration.getPort() != null) {
            jedisPool = new JedisPool(configuration.getHost(),
                    configuration.getPort());
        } else {
            jedisPool = new JedisPool(configuration.getHost());
        }
    }

    @Override
    protected boolean _deleteModelById(final Key modelKey) {
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                if (jedis.del(modelKey.toString()) > 0) {
                    jedis.srem(modelKey.getEncodedUsername(),
                            modelKey.getModelId());
                    return true;
                } else {
                    return false;
                }
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            logger.error("JedisException on _deleteModelById: ", e);
            return false;
        }
    }

    @Override
    protected void _deleteModels(final String username) {
        final ImmutableSet<String> modelIds = _getModelIds(username);
        if (modelIds.isEmpty()) {
            return;
        }
        final Set<String> jedisKeys = Sets.newLinkedHashSet();
        for (final String modelId : modelIds) {
            jedisKeys.add(new Key(modelId, username).toString());
        }
        jedisKeys.add(_getKeyPrefix(username));
        final String[] jedisKeysArray = new String[jedisKeys.size()];
        jedisKeys.toArray(jedisKeysArray);
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                jedis.del(jedisKeysArray);
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            logger.error("JedisException on _deleteModelById: ", e);
        }
    }

    @Override
    protected ModelT _getModelById(final Key modelKey)
            throws org.thryft.store.Store.NoSuchModelException {
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                final Map<String, String> hash = jedis.hgetAll(modelKey
                        .toString());
                if (hash.isEmpty()) {
                    throw new NoSuchModelException(modelKey.getModelId());
                }
                final StringMapProtocol iprot = new StringMapProtocol(hash);
                final ModelT model = _getModel(iprot);
                if (model != null) {
                    return model;
                } else {
                    throw new NoSuchModelException(modelKey.getModelId());
                }
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            logger.error("JedisException on _getModelById: ", e);
            throw new NoSuchModelException(modelKey.getModelId());
        }
    }

    @Override
    protected int _getModelCount(final String username) {
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                return jedis.scard(_getKeyPrefix(username)).intValue();
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            logger.error("JedisException on _getModelCount: ", e);
            return 0;
        }
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String username) {
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                return ImmutableSet.copyOf(jedis
                        .smembers(_getKeyPrefix(username)));
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            logger.error("JedisException on _getModelIds: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModels(final String username) {
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                final ImmutableMap.Builder<String, ModelT> models = ImmutableMap
                        .builder();
                for (final String modelId : jedis
                        .smembers(_getKeyPrefix(username))) {
                    try {
                        models.put(modelId, _getModelById(modelId, username));
                    } catch (final org.thryft.store.Store.NoSuchModelException e) {
                    }
                }
                return models.build();
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            logger.error("JedisException on _getModels: ", e);
            return ImmutableMap.of();
        }
    }

    @Override
    protected ImmutableMap<String, ModelT> _getModelsByIds(
            final ImmutableSet<Key> modelKeys)
            throws org.thryft.store.Store.NoSuchModelException {
        final ImmutableMap.Builder<String, ModelT> models = ImmutableMap
                .builder();
        for (final Key modelKey : modelKeys) {
            models.put(modelKey.getModelId(), _getModelById(modelKey));
        }
        return models.build();
    }

    @Override
    protected void _putModel(final ModelT model, final Key modelKey)
            throws ModelIoException {
        try {
            final Jedis jedis = jedisPool.getResource();
            try {
                final StringMapProtocol oprot = new StringMapProtocol();
                try {
                    model.write(oprot);
                } catch (final TException e) {
                    return;
                }
                final ImmutableMap<String, String> hash = oprot.toStringMap();
                jedis.hmset(modelKey.toString(), hash);
                jedis.sadd(modelKey.getEncodedUsername(), modelKey.getModelId());
            } finally {
                jedisPool.returnResource(jedis);
            }
        } catch (final JedisException e) {
            throw new ModelIoException(e, modelKey.getModelId());
        }
    }

    @Override
    protected void _putModels(final ImmutableMap<Key, ModelT> models)
            throws ModelIoException {
        for (final ImmutableMap.Entry<Key, ModelT> model : models.entrySet()) {
            _putModel(model.getValue(), model.getKey());
        }
    }

    private final JedisPool jedisPool;
    private final static Logger logger = LoggerFactory
            .getLogger(RedisStore.class);
}
