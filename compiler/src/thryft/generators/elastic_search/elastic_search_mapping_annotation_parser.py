import json

from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ElasticSearchMappingAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'elastic_search_mapping', Ast.FieldNode)

    def parse_annotation(self, ast_node, name, value, **kwds):
        assert isinstance(ast_node, Ast.FieldNode)

        try:
            value = json.loads(value)
        except ValueError, e:
            raise ValueError("@%s contains invalid JSON: '%s', exception: %s" % (name, value, e))
        if not isinstance(value, dict):
            raise ValueError("expected @%s to contain a JSON object, found '%s'" % (name, value))

        annotation = Ast.AnnotationNode(name=name, value=value, **kwds)

        ast_node.annotations.append(annotation)
