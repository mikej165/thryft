from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ValuelessAnnotationParser(AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is not None:
            raise ValueError("@%(name)s does not take a value" % locals())
        ast_node.annotations.append(Ast.AnnotationNode(name=name, **kwds))
