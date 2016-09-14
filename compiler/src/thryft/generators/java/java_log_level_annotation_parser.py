from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast
from thryft.generators.java.java_log_levels import JAVA_LOG_LEVELS


class JavaLogLevelAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'java_log_level', (Ast.ExceptionTypeNode, Ast.FieldNode, Ast.FunctionNode))

    def parse_annotation(self, ast_node, name, value, **kwds):
        value_lower = value.lower()
        if not value_lower in JAVA_LOG_LEVELS:
            raise ValueError("@%s has an invalid log level: '%s'" % (name, value))

        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value_lower, **kwds))
