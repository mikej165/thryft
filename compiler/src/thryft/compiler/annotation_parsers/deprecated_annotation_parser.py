from thryft.compiler.ast import Ast
from thryft.compiler.valueless_annotation_parser import ValuelessAnnotationParser


class DeprecatedAnnotationParser(ValuelessAnnotationParser):
    def __init__(self):
        ValuelessAnnotationParser.__init__(self, 'deprecated', (Ast.EnumeratorNode, Ast.FieldNode))
