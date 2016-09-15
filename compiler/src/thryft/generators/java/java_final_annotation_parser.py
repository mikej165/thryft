from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class JavaFinalAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'java_final', (Ast.ExceptionTypeNode, Ast.StructTypeNode))

    def parse_annotation(self, ast_node, name, value, **kwds):
        value = value.lower()
        if value == 'true':
            value = True
        elif value == 'false':
            value = False
        else:
            raise ValueError(value)
        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value, **kwds))
