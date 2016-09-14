import json

from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ValidationAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'validation', (Ast.FieldNode, Ast.FunctionNode, Ast.TypedefNode))

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
