from thryft.generator.struct_type import StructType
from thryft.generators.sql._sql_compound_type import _SqlCompoundType
from thryft.generators.sql.sql_field import SqlField
from yutil import decamelize, lpad


class SqlStructType(StructType, _SqlCompoundType):
    def sql_create_table(self):
        column_definitions = []
        foreign_key_definitions = []
        for annotation_i, annotation in enumerate(self.annotations):
            if annotation.name == 'sql_column':
                column_definitions.append(annotation.value)
            elif annotation.name == 'sql_foreign_key':
                if annotation_i == 0:
                    raise ValueError('sql_foreign_key annotation on a struct must follow a sql_column annotation')
                elif self.annotations[annotation_i - 1].name != 'sql_column':
                    raise ValueError("sql_foreign_key annotation on a struct must follow a sql_column annotation, not " + self.annotations[annotation_i - 1].name)
                foreign_key_definitions.append(SqlField.sql_foreign_key_definition_static(
                    column_name=self.annotations[annotation_i - 1].value.split(' ', 1)[0],
                    foreign_table_name=annotation.value[0],
                    foreign_column_name=annotation.value[1]
                ))
        for field in self.fields:
            column_definition = field.sql_column_definition()
            if column_definition is not None:
                column_definitions.append(column_definition)
        for field in self.fields:
            foreign_key_definition = field.sql_foreign_key_definition()
            if foreign_key_definition is not None:
                foreign_key_definitions.append(foreign_key_definition)
        column_definitions.extend(foreign_key_definitions)
        column_definitions = lpad(",\n    ", ",\n    ".join(column_definitions))
        name = decamelize(self.name)
        return """\
CREATE TABLE IF NOT EXISTS %(name)s(
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL%(column_definitions)s
)""" % locals()

    def sql_name(self):
        return None
