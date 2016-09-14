from thryft.compiler.annotation_parser import AnnotationParser
from thryft.compiler.ast import Ast


class ElasticSearchDocumentTypeAnnotationParser(AnnotationParser):
    def __init__(self):
        AnnotationParser.__init__(self, 'elastic_search_document_type', Ast.StructTypeNode)

    def parse_annotation(self, ast_node, name, value, **kwds):
        assert isinstance(ast_node, Ast.StructTypeNode)
        ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value, **kwds))
