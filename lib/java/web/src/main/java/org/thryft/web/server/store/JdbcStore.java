package org.thryft.web.server.store;

import static com.google.common.base.Preconditions.checkNotNull;

import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
import java.util.Set;

import org.apache.thrift.TBase;
import org.apache.thrift.TException;
import org.h2.jdbcx.JdbcConnectionPool;
import org.thryft.core.protocol.JsonProtocol;

import com.google.common.base.CaseFormat;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Sets;

public final class JdbcStore<ModelT extends TBase<?, ?>> extends Store<ModelT> {
    public final static class Configuration {
        public Configuration() {
            this(PASSWORD_DEFAULT, URL_DEFAULT, USER_DEFAULT);
        }

        public Configuration(final File filePath) {
            this(filePath, PASSWORD_DEFAULT, USER_DEFAULT);
        }

        public Configuration(final File filePath, final String password,
                final String user) {
            this(password, "jdbc:h2:" + filePath.toString()
                    + ";TRACE_LEVEL_FILE=0;TRACE_LEVEL_SYSTEM_OUT=0",
                    USER_DEFAULT);
        }

        public Configuration(final Properties properties) {
            user = properties.getProperty(this.getClass().getCanonicalName()
                    + ".password");
            if (user == null) {
                user = PASSWORD_DEFAULT;
            }

            url = properties.getProperty(this.getClass().getCanonicalName()
                    + ".url");
            if (url == null) {
                url = URL_DEFAULT;
            }

            user = properties.getProperty(this.getClass().getCanonicalName()
                    + ".user");
            if (user == null) {
                user = USER_DEFAULT;
            }
        }

        public Configuration(final String password, final String url,
                final String user) {
            this.password = checkNotNull(password);
            this.url = checkNotNull(url);
            this.user = checkNotNull(user);
        }

        public String getPassword() {
            return password;
        }

        public String getUrl() {
            return url;
        }

        public String getUser() {
            return user;
        }

        public final static String PASSWORD_DEFAULT = "";
        public final static String URL_DEFAULT = "jdbc:h2:yogento;TRACE_LEVEL_FILE=0;TRACE_LEVEL_SYSTEM_OUT=0";
        public final static String USER_DEFAULT = "yogento";

        private String password;
        private String user;
        private String url;
    }

    public JdbcStore(final Configuration configuration,
            final Class<ModelT> modelClass) {
        super(modelClass);
        checkNotNull(configuration);

        connectionPool = JdbcConnectionPool.create(configuration.getUrl(),
                configuration.getUser(), configuration.getPassword());

        tableName = CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE,
                modelClass.getSimpleName());
        final String createTableSql = "CREATE TABLE IF NOT EXISTS "
                + tableName
                + " (id int NOT NULL AUTO_INCREMENT, "
                + tableName
                + "_id VARCHAR(255) NOT NULL, "
                + tableName
                + "_json TEXT NOT NULL, username VARCHAR(255) NOT NULL, PRIMARY KEY (id));";
        deleteModelByIdSql = "DELETE FROM " + tableName + " WHERE " + tableName
                + "_id = ? AND username = ?";
        deleteModelsSql = "DELETE FROM " + tableName + " WHERE username = ?";
        getModelByIdSql = "SELECT * FROM " + tableName + " WHERE " + tableName
                + "_id = ? AND username = ?";
        getModelCountSql = "SELECT COUNT(*) FROM " + tableName
                + " WHERE username = ?";
        getModelIdsSql = "SELECT " + tableName + "_id FROM " + tableName
                + " WHERE username = ?";
        getModelsSql = "SELECT * FROM " + tableName + " WHERE username = ?";
        getUsernamesSql = "SELECT username FROM " + tableName;
        headModelByIdSql = "SELECT " + tableName + "_id FROM " + tableName
                + " WHERE " + tableName + "_id = ? AND username = ?";
        putModelSql = "INSERT INTO " + tableName + " VALUES (NULL, ?, ?, ?)";

        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final Statement statement = connection.createStatement();
                try {
                    statement.execute(createTableSql);
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception creating table: ", e);
        }
    }

    public void dispose() {
        connectionPool.dispose();
    }

    @Override
    protected boolean _deleteModelById(final String modelId,
            final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            final boolean existed = __headModelById(connection, modelId,
                    username);
            try {
                __deleteModelById(connection, modelId, username);
                return existed;
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception deleting model " + modelId + ": ", e);
            return false;
        }
    }

    @Override
    protected void _deleteModels(final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final PreparedStatement statement = connection
                        .prepareStatement(deleteModelsSql);
                try {
                    statement.setString(1, username);
                    statement.execute();
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("error deleting models: ", e);
        }
    }

    @Override
    protected ModelT _getModelById(final String modelId, final String username)
            throws NoSuchModelException {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final PreparedStatement statement = connection
                        .prepareStatement(getModelByIdSql);
                try {
                    statement.setString(1, modelId);
                    statement.setString(2, username);
                    final ResultSet resultSet = statement.executeQuery();
                    try {
                        if (resultSet.next()) {
                            final ModelT model = __getModel(resultSet);
                            if (model != null) {
                                return model;
                            } else {
                                throw new NoSuchModelException(modelId);
                            }
                        } else {
                            throw new NoSuchModelException(modelId);
                        }
                    } finally {
                        resultSet.close();
                    }
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception getting model " + modelId + ": ", e);
            throw new NoSuchModelException(modelId);
        }
    }

    @Override
    protected int _getModelCount(final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final PreparedStatement statement = connection
                        .prepareStatement(getModelCountSql);
                try {
                    statement.setString(1, username);
                    final ResultSet resultSet = statement.executeQuery();
                    try {
                        if (resultSet.next()) {
                            return resultSet.getInt(1);
                        } else {
                            return 0;
                        }
                    } finally {
                        resultSet.close();
                    }
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception getting model count: ", e);
            return 0;
        }
    }

    @Override
    protected ImmutableSet<String> _getModelIds(final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final PreparedStatement statement = connection
                        .prepareStatement(getModelIdsSql);
                try {
                    statement.setString(1, username);
                    final ResultSet resultSet = statement.executeQuery();
                    try {
                        final Set<String> modelIds = Sets.newLinkedHashSet();
                        while (resultSet.next()) {
                            modelIds.add(resultSet.getString(1));
                        }
                        return ImmutableSet.copyOf(modelIds);
                    } finally {
                        resultSet.close();
                    }
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception getting model ids: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected ImmutableSet<ModelT> _getModels(final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final PreparedStatement statement = connection
                        .prepareStatement(getModelsSql);
                try {
                    statement.setString(1, username);
                    final ResultSet resultSet = statement.executeQuery();
                    try {
                        final Set<ModelT> models = Sets.newLinkedHashSet();
                        while (resultSet.next()) {
                            final ModelT model = __getModel(resultSet);
                            if (model != null) {
                                models.add(model);
                            }
                        }
                        return ImmutableSet.copyOf(models);
                    } finally {
                        resultSet.close();
                    }
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception getting model ids: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected ImmutableSet<ModelT> _getModelsByIds(
            final ImmutableSet<String> modelIds, final String username)
            throws org.thryft.web.server.store.Store.NoSuchModelException {
        if (modelIds.isEmpty()) {
            return ImmutableSet.of();
        }

        final StringBuilder getModelsByIdsSqlBuilder = new StringBuilder();
        getModelsByIdsSqlBuilder.append("SELECT * FROM ");
        getModelsByIdsSqlBuilder.append(tableName);
        getModelsByIdsSqlBuilder.append(" WHERE username = ? AND ");
        getModelsByIdsSqlBuilder.append(tableName);
        getModelsByIdsSqlBuilder.append("_id IN (");
        for (int modelI = 0; modelI < modelIds.size(); modelI++) {
            if (modelI > 0) {
                getModelsByIdsSqlBuilder.append(", ?");
            } else {
                getModelsByIdsSqlBuilder.append("?");
            }
        }
        getModelsByIdsSqlBuilder.append(")");
        final String getModelsByIdsSql = getModelsByIdsSqlBuilder.toString();

        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final PreparedStatement statement = connection
                        .prepareStatement(getModelsByIdsSql);
                try {
                    statement.setString(1, username);
                    int parameterIndex = 2;
                    for (final String modelId : modelIds) {
                        statement.setString(parameterIndex, modelId);
                        parameterIndex++;
                    }

                    final ResultSet resultSet = statement.executeQuery();
                    try {
                        final Set<ModelT> models = Sets.newLinkedHashSet();
                        final Set<String> foundModelIds = Sets.newHashSet();
                        while (resultSet.next()) {
                            final String modelId = resultSet
                                    .getString(tableName + "_id");
                            final ModelT model = __getModel(resultSet);
                            if (model != null) {
                                foundModelIds.add(modelId);
                                models.add(model);
                            } else {
                                throw new NoSuchModelException(modelId);
                            }
                        }

                        if (foundModelIds.equals(modelIds)) {
                            return ImmutableSet.copyOf(models);
                        } else {
                            final Set<String> missingModelIds = Sets
                                    .newHashSet(modelIds);
                            missingModelIds.removeAll(foundModelIds);
                            final String missingModelId = missingModelIds
                                    .iterator().next();
                            throw new NoSuchModelException(missingModelId);
                        }
                    } finally {
                        resultSet.close();
                    }
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception getting models by ids: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected ImmutableSet<String> _getUsernames() {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                final Statement statement = connection.createStatement();
                try {
                    final ResultSet resultSet = statement
                            .executeQuery(getUsernamesSql);
                    try {
                        final Set<String> usernames = Sets.newLinkedHashSet();
                        while (resultSet.next()) {
                            usernames.add(resultSet.getString(1));
                        }
                        return ImmutableSet.copyOf(usernames);
                    } finally {
                        resultSet.close();
                    }
                } finally {
                    statement.close();
                }
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception getting usernames: ", e);
            return ImmutableSet.of();
        }
    }

    @Override
    protected boolean _headModelById(final String modelId, final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                return __headModelById(connection, modelId, username);
            } finally {
                connection.close();
            }
        } catch (final SQLException e) {
            logger.error("exception heading model by id: ", e);
            return false;
        }
    }

    @Override
    protected void _putModel(final ModelT model, final String modelId,
            final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                connection.setAutoCommit(false);
                final PreparedStatement statement = connection
                        .prepareStatement(putModelSql);
                try {
                    __putModel(connection, model, modelId, statement, username);
                } finally {
                    statement.close();
                }
                connection.commit();
            } finally {
                connection.close();
            }
        } catch (final IOException e) {
            logger.error("exception putting model: ", e);
        } catch (final SQLException e) {
            logger.error("exception putting model: ", e);
        } catch (final TException e) {
            logger.error("exception putting model: ", e);
        }
    }

    @Override
    protected void _putModels(final ImmutableMap<String, ModelT> models,
            final String username) {
        try {
            final Connection connection = connectionPool.getConnection();
            try {
                connection.setAutoCommit(false);
                final PreparedStatement statement = connection
                        .prepareStatement(putModelSql);
                try {
                    for (final ImmutableMap.Entry<String, ModelT> model : models
                            .entrySet()) {
                        __putModel(connection, model.getValue(),
                                model.getKey(), statement, username);
                    }
                } finally {
                    statement.close();
                }
                connection.commit();
            } finally {
                connection.close();
            }
        } catch (final IOException e) {
            logger.error("exception putting models: ", e);
        } catch (final SQLException e) {
            logger.error("exception putting models: ", e);
        } catch (final TException e) {
            logger.error("exception putting models: ", e);
        }
    }

    private void __deleteModelById(final Connection connection,
            final String modelId, final String username) throws SQLException {
        final PreparedStatement statement = connection
                .prepareStatement(deleteModelByIdSql);
        try {
            statement.setString(1, modelId);
            statement.setString(2, username);
            statement.execute();
        } finally {
            statement.close();
        }
    }

    private ModelT __getModel(final ResultSet resultSet) {
        try {
            return _getModel(new JsonProtocol(new StringReader(
                    resultSet.getString(tableName + "_json"))));
        } catch (final IOException e) {
            logger.error("error reading model: ", e);
        } catch (final SQLException e) {
            logger.error("error reading model: ", e);
        }
        return null;
    }

    private boolean __headModelById(final Connection connection,
            final String modelId, final String username) {
        try {
            final PreparedStatement statement = connection
                    .prepareStatement(headModelByIdSql);
            try {
                statement.setString(1, modelId);
                statement.setString(2, username);
                final ResultSet resultSet = statement.executeQuery();
                try {
                    return resultSet.next();
                } finally {
                    resultSet.close();
                }
            } finally {
                statement.close();
            }
        } catch (final SQLException e) {
            logger.error("error heading model: ", e);
            return false;
        }
    }

    private void __putModel(final Connection connection, final ModelT model,
            final String modelId, final PreparedStatement statement,
            final String username) throws SQLException, IOException, TException {
        __deleteModelById(connection, modelId, username);
        final StringWriter stringWriter = new StringWriter();
        final JsonProtocol oprot = new JsonProtocol(stringWriter);
        model.write(oprot);
        oprot.flush();
        final String json = stringWriter.toString();
        statement.setString(1, modelId);
        statement.setString(2, json);
        statement.setString(3, username);
        statement.execute();
    }

    private final JdbcConnectionPool connectionPool;

    private final String deleteModelByIdSql;

    private final String deleteModelsSql;

    private final String getModelByIdSql;

    private final String getModelCountSql;

    private final String getModelIdsSql;

    private final String getModelsSql;

    private final String getUsernamesSql;

    private final String headModelByIdSql;

    private final String putModelSql;

    private final String tableName;
}
