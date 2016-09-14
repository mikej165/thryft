import json

from thryft.compiler._annotation_parser import _AnnotationParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class ValidationAnnotationParser(_AnnotationParser):
    def parse_annotation(self, ast_node, name, value, **kwds):
        if isinstance(ast_node, Ast.FunctionNode):
            parameter, value = self._split_param_annotation(ast_node=ast_node, name=name, value=value)

        try:
            value = json.loads(value)
        except ValueError, e:
            raise ValueError("@%s contains invalid JSON: '%s', exception: %s" % (name, value, e))
        if not isinstance(value, dict):
            raise ValueError("expected @%s to contain a JSON object, found '%s'" % (name, value))

        for lengthPropertyName in ('maxLength', 'minLength'):
            lengthPropertyValue = value.get(lengthPropertyName)
            if lengthPropertyValue is None:
                continue
            try:
                lengthPropertyValue = int(lengthPropertyValue)
            except ValueError:
                raise ValueError("@%(name)s %(lengthPropertyName)s must be an integer" % locals())
            if lengthPropertyValue < 0:
                raise ValueError("@%(name)s %(lengthPropertyName)s must be >= 0" % locals())

        annotation = Ast.AnnotationNode(name=name, value=value, **kwds)

        if isinstance(ast_node, Ast.FunctionNode):
            parameter.annotations.append(annotation)
        else:
            ast_node.annotations.append(annotation)

    @classmethod
    def register(cls):
        for __ast_node_type in (Ast.FieldNode, Ast.FunctionNode, Ast.TypedefNode):
            Parser.register_annotation_parser(__ast_node_type, 'validation', cls())
