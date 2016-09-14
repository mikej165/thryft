from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ThrowAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, ('throw', 'throws'), Ast.FunctionNode)

    def parse_annotation(self, ast_node, name, value, **kwds):
        if value is None:
            raise ValueError("@%(name)s requires a value" % locals())
        value_split = value.split(None, 1)
        if len(value_split) != 2:
            raise ValueError("@%(name)s requires an exception type name and a description" % locals())
        exception_type_name, value = value_split
        exception_type_name = exception_type_name.rstrip(':')
        try:
            throw = ast_node.throws_by_exception_type_name[exception_type_name]
        except KeyError:
            raise ValueError("'%s' refers to unknown exception type '%s'" % (value, exception_type_name))
        throw.doc = Ast.DocNode(text=value, **kwds)
