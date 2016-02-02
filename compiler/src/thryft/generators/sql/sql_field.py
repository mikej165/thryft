from thryft.generator.field import Field
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlField(Field, _SqlNamedConstruct):
    def sql_column_definition(self):
        name = self.sql_name()
        type_name = self.type.sql_name()
        if type_name is None:
            return None
        ret = name + ' ' + type_name
        if self.required:
            ret += ' NOT NULL'
        if self.sql_is_unique():
            ret += ' UNIQUE'
        return ret

    def sql_foreign_key_definition(self):
        for annotation in self.annotations:
            if annotation.name == 'sql_foreign_key':
                return \
                    self.sql_foreign_key_definition_static(
                        column_name=self.sql_name(),
                        foreign_table_name=annotation.value[0],
                        foreign_column_name=annotation.value[1]
                    )

    @staticmethod
    def sql_foreign_key_definition_static(column_name, foreign_table_name, foreign_column_name):
        return "FOREIGN KEY (%(column_name)s) REFERENCES %(foreign_table_name)s (%(foreign_column_name)s) ON DELETE CASCADE ON UPDATE CASCADE" % locals()

    def sql_is_unique(self):
        for annotation in self.annotations:
            if annotation.name == 'sql_unique':
                return True
        return False

    def sql_name(self):
        name = self.name
        if self.id is not None:
            name = name + '_' + str(self.id)
        return name
