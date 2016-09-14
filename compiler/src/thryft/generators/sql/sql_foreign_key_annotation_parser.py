from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class SqlForeignKeyAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'sql_foreign_key', (Ast.FieldNode, Ast.StructTypeNode))

    def parse_annotation(self, ast_node, name, value, **kwds):
        value_parts = value.split('.')
        if len(value_parts) != 2:
            raise ValueError("@%s must be specify table.column: '%s'" % (name, value))
        table_name, column_name = value_parts
        if len(table_name) == 0 or len(column_name) == 0:
            raise ValueError("@%s must be specify a table.column: '%s'" % (name, value))
        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=(table_name, column_name), **kwds))
