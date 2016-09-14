from thryft.compiler._annotation_parser import _AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class RequiresAnnotationParser(_AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is not None:
            raise ValueError("@%(name)s does not take a value" % locals())
        ast_node.annotations.append(Ast.AnnotationNode(name=name, **kwds))

    @classmethod
    def register(cls):
        for __requires_x in ('authentication', 'guest', 'user'):
            Parser.register_annotation_parser(Ast.FunctionNode, 'requires_' + __requires_x, cls())
