import json
import logging

from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class JsViewMetadataAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'js_view_metadata', Ast.FieldNode)

    def parse_annotation(self, ast_node, name, value, **kwds):
        assert isinstance(ast_node, Ast.FieldNode)

        try:
            value = json.loads(value)
        except ValueError, e:
            raise ValueError("@%s contains invalid JSON: '%s', exception: %s" % (name, value, e))
        if not isinstance(value, dict):
            raise ValueError("expected @%s to contain a JSON object, found '%s'" % (name, value))

        for subname, subvalue in value.iteritems():
            if subname not in ('displayFormat', 'editControl'):
                logging.warn("unknown %(name)s property '%s'" % locals())

        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value, **kwds))
