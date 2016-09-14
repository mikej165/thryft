from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ParamAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'param', Ast.FunctionNode)
