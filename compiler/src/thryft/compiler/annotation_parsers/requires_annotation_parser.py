from thryft.compiler.ast import Ast
from thryft.compiler.valueless_annotation_parser import ValuelessAnnotationParser


class RequiresAnnotationParser(ValuelessAnnotationParser):
    def __init__(self):
        ValuelessAnnotationParser.__init__(self, tuple('requires_' + suffix for suffix in ('authentication', 'guest', 'user')), Ast.FunctionNode)
