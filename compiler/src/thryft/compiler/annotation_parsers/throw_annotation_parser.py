from thryft.compiler._annotation_parser import _AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class ThrowAnnotationParser(_AnnotationParser):
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

    @classmethod
    def register(cls):
        for __name in ('throw', 'throws'):
            Parser.register_annotation_parser(Ast.FunctionNode, __name, cls())
