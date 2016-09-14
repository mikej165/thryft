from thryft.compiler.ast import Ast


class AnnotationParser(object):
    def __init__(self, annotation_names, ast_node_types):
        if not isinstance(annotation_names, tuple):
            annotation_names = (annotation_names,)
        for annotation_name in annotation_names:
            assert isinstance(annotation_name, str)
        self.__annotation_names = annotation_names

        if not isinstance(ast_node_types, tuple):
            ast_node_types = (ast_node_types,)
        for ast_node_type in ast_node_types:
            assert issubclass(ast_node_type, Ast.Node)
        self.__ast_node_types = ast_node_types

    @property
    def annotation_names(self):
        return self.__annotation_names

    @property
    def ast_node_types(self):
        return self.__ast_node_types

    def parse_annotation(self, ast_node, name, value, **kwds):
        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value, **kwds))

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
