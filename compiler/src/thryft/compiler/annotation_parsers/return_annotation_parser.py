from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class ReturnAnnotationParser(AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is None:
            raise ValueError("@%(name)s requires a value" % locals())
        if ast_node.return_field is None:
            raise ValueError("@%(name)s returns to a function with a void return" % locals())
        ast_node.return_field.doc = Ast.DocNode(text=value, **kwds)

    @classmethod
    def register(cls):
        for __name in ('return', 'returns'):
            Parser.register_annotation_parser(Ast.FunctionNode, __name, cls())
