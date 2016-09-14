from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class RequiresSetAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, tuple('requires_' + suffix for suffix in ('permissions', 'roles')), Ast.FunctionNode)

    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is None or len(value) == 0:
            raise ValueError("@%(name)s requires a value" % locals())
        if ',' in value:
            values = value.split(',')
        else:
            values = value.split()
        values = frozenset(value.strip() for value in values)
        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=values, **kwds))
