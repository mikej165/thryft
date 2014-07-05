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
        try:
            annotation = self.annotations['sql_foreign_key']
        except KeyError:
            return None
        name = self.sql_name()
        foreign_table_name, foreign_column_name = annotation
        return "FOREIGN KEY (%(name)s) REFERENCES %(foreign_table_name)s (%(foreign_column_name)s) ON DELETE CASCADE ON UPDATE CASCADE" % locals()

    def sql_is_unique(self):
        return self.annotations.has_key('sql_unique')

    def sql_name(self):
        return self.name
