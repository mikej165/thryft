import os.path

from thryft.generators.sql.sql_generator import SqlGenerator


class CreateTableSqlGenerator(SqlGenerator):
    class Document(SqlGenerator.Document):
        def sql_repr(self):
            repr_ = []
            for definition in self.definitions:
                if isinstance(definition, SqlGenerator.StructType):
                    repr_.append(definition.sql_create_table())
            return "\n".join(repr_)

        def _save_to_dir(self, out_dir_path):
            try:
                out_dir_path = os.path.join(out_dir_path, self.namespace_by_scope('*').name.replace('.', os.path.sep))
            except KeyError:
                pass
            return self._save_to_file(os.path.join(out_dir_path, self.name + '.sql'))
