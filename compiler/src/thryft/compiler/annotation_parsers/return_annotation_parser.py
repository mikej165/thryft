from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ReturnAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, ('return', 'returns'), Ast.FunctionNode)

    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is None:
            raise ValueError("@%(name)s requires a value" % locals())
        if ast_node.return_field is None:
            raise ValueError("@%(name)s returns to a function with a void return" % locals())
        ast_node.return_field.doc = Ast.DocNode(text=value, **kwds)
