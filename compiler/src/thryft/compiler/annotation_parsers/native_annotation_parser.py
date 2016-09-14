from thryft.compiler.ast import Ast
from thryft.compiler.valueless_annotation_parser import ValuelessAnnotationParser


class NativeAnnotationParser(ValuelessAnnotationParser):
    def __init__(self):
        ValuelessAnnotationParser.__init__(self, 'native', (Ast.StructTypeNode, Ast.TypedefNode))
