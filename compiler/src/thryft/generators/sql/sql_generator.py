from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser
from thryft.generator.generator import Generator


class SqlGenerator(Generator):
    from thryft.generators.sql.sql_binary_type import SqlBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.sql.sql_bool_type import SqlBoolType as BoolType  # @UnusedImport
    from thryft.generators.sql.sql_byte_type import SqlByteType as ByteType  # @UnusedImport
    from thryft.generators.sql.sql_const import SqlConst as Const  # @UnusedImport
    from thryft.generators.sql.sql_document import SqlDocument as Document  # @UnusedImport
    from thryft.generators.sql.sql_double_type import SqlDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.sql.sql_enum_type import SqlEnumType as EnumType  # @UnusedImport
    from thryft.generators.sql.sql_exception_type import SqlExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.sql.sql_field import SqlField as Field  # @UnusedImport
    from thryft.generators.sql.sql_function import SqlFunction as Function  # @UnusedImport
    from thryft.generators.sql.sql_i16_type import SqlI16Type as I16Type  # @UnusedImport
    from thryft.generators.sql.sql_i32_type import SqlI32Type as I32Type  # @UnusedImport
    from thryft.generators.sql.sql_i64_type import SqlI64Type as I64Type  # @UnusedImport
    from thryft.generators.sql.sql_include import SqlInclude as Include  # @UnusedImport
    from thryft.generators.sql.sql_list_type import SqlListType as ListType  # @UnusedImport
    from thryft.generators.sql.sql_map_type import SqlMapType as MapType  # @UnusedImport
    from thryft.generators.sql.sql_service import SqlService as Service  # @UnusedImport
    from thryft.generators.sql.sql_set_type import SqlSetType as SetType  # @UnusedImport
    from thryft.generators.sql.sql_string_type import SqlStringType as StringType  # @UnusedImport
    from thryft.generators.sql.sql_struct_type import SqlStructType as StructType  # @UnusedImport
    from thryft.generators.sql.sql_typedef import SqlTypedef as Typedef  # @UnusedImport


def __parse_sql_foreign_key_annotation(ast_node, name, value, **kwds):
    value_parts = value.split('.')
    if len(value_parts) != 2:
        raise ValueError("@%s must be specify table.column: '%s'" % (name, value))
    table_name, column_name = value_parts
    if len(table_name) == 0 or len(column_name) == 0:
        raise ValueError("@%s must be specify a table.column: '%s'" % (name, value))

    annotation = Ast.AnnotationNode(name=name, value=(table_name, column_name), **kwds)

    ast_node.annotations.append(annotation)
Parser.register_annotation(Ast.FieldNode, 'sql_foreign_key', __parse_sql_foreign_key_annotation)

def __parse_sql_unique_annotation(ast_node, name, value, **kwds):
    if value is not None:
        raise ValueError("@%(name)s does not take a value" % locals())
    ast_node.annotations.append(Ast.AnnotationNode(name=name, **kwds))
Parser.register_annotation(Ast.FieldNode, 'sql_unique', __parse_sql_unique_annotation)
