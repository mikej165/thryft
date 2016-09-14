from thryft.compiler.ast import Ast
from yutil import class_qname


class _AnnotationParser(object):
    def parse_annotation(self, ast_node, name, value, **kwds):
        raise NotImplementedError(class_qname(self))

    @classmethod
    def register(cls):
        raise NotImplementedError(class_qname(cls))

    @staticmethod
    def _split_param_annotation(ast_node, name, value):
        assert isinstance(ast_node, Ast.FunctionNode)

        if value is None:
            raise ValueError("@%(name)s requires a value" % locals())
        value_split = value.split(None, 1)
        if len(value_split) != 2:
            raise ValueError("@%(name)s requires a parameter name and description" % locals())
        param_name = value_split[0].rstrip(':')

        if param_name == 'return':
            if ast_node.return_field is not None:
                parameter = ast_node.return_field
            else:
                raise ValueError("unknown parameter '%s'" % param_name)
        else:
            try:
                parameter = ast_node.parameters_by_name[param_name]
            except KeyError:
                raise ValueError("unknown parameter '%s'" % param_name)

        return parameter, value_split[1]
