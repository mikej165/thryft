from thryft.compiler._annotation_parser import _AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class ParamAnnotationParser(_AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        parameter, value = self._split_param_annotation(ast_node=ast_node, name=name, value=value)
        parameter.doc = Ast.DocNode(text=value, **kwds)

    @classmethod
    def register(cls):
        Parser.register_annotation_parser(Ast.FunctionNode, 'param', cls())
