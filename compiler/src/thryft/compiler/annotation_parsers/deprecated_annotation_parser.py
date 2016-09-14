from thryft.compiler._annotation_parser import _AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class DeprecatedAnnotationParser(_AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is not None:
            raise ValueError("@%(name)s does not take a value" % locals())
        ast_node.annotations.append(Ast.AnnotationNode(name=name, **kwds))

    @classmethod
    def register(cls):
        for __ast_node_type in (Ast.EnumeratorNode, Ast.FieldNode):
            Parser.register_annotation_parser('deprecated', __ast_node_type, cls())
