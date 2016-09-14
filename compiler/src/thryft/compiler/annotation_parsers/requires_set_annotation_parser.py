from thryft.compiler._annotation_parser import _AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class RequiresSetAnnotationParser(_AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is None or len(value) == 0:
            raise ValueError("@%(name)s requires a value" % locals())
        if ',' in value:
            values = value.split(',')
        else:
            values = value.split()
        values = frozenset(value.strip() for value in values)
        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=values, **kwds))

    @classmethod
    def register(cls):
        for __requires_x in ('permissions', 'roles'):
            Parser.register_annotation_parser(Ast.FunctionNode, 'requires_' + __requires_x, cls())
