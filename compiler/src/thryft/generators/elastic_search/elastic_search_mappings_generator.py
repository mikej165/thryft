from collections import OrderedDict
import json

from thryft.compiler.parser import Parser
from thryft.generator.generator import Generator
from thryft.generators.elastic_search.elastic_search_document_type_annotation_parser import ElasticSearchDocumentTypeAnnotationParser
from thryft.generators.elastic_search.elastic_search_mapping_annotation_parser import ElasticSearchMappingAnnotationParser
from thryft.generators.elastic_search.elastic_search_mappings_base_annotation_parser import ElasticSearchMappingsBaseAnnotationParser
from yutil import decamelize


class ElasticSearchMappingsGenerator(Generator):
    class BoolType(Generator.BoolType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'type': 'boolean'}

    class Document(Generator.Document):  # @UndefinedVariable
        def elastic_search_mappings_json(self):
            if len(self.definitions) != 1:
                return ''
            elif not isinstance(self.definitions[0], Generator.StructType):  # @UndefinedVariable
                return ''

            out = OrderedDict()
            if self._parent_generator()._template is not None:
                out['template'] = self._parent_generator()._template
            if self._parent_generator()._settings is not None:
                out['settings'] = self._parent_generator()._settings
            out['mappings'] = self.definitions[0].elastic_search_mappings_dict()
            return json.dumps(out, indent=2).replace("\r\n", "\n")

        def _save_to_file(self, out_file_path):
            return self._save_to_file_helper(self.elastic_search_mappings_json(), out_file_path)

    class EnumType(Generator.EnumType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'index': 'not_analyzed', 'type': 'string'}

    class Field(Generator.Field):  # @UndefinedVariable
        def elastic_search_name(self):
            name = self.name
            if self.id is not None:
                name = "%d:%s" % (self.id, name)
            return name

        def elastic_search_mapping_dict(self):
            out = {}
            out.update(self.type.elastic_search_mapping_dict())
            for annotation in self.annotations:
                if annotation.name == 'elastic_search_mapping':
                    out.update(annotation.value)
            if out.get('index') == 'not_analyzed':
                out.pop('analyzer', None)
            return out

    class DoubleType(Generator.DoubleType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'type': 'double'}

    class I32Type(Generator.I32Type):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'type': 'integer'}

    class I64Type(Generator.I64Type):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'type': 'long'}

    class ListType(Generator.ListType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return self.element_type.elastic_search_mapping_dict()

    class MapType(Generator.MapType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'type': 'nested', 'dynamic': True}

    class StringType(Generator.StringType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return {'type': 'string'}

    class SetType(Generator.SetType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            return self.element_type.elastic_search_mapping_dict()

    class StructType(Generator.StructType):  # @UndefinedVariable
        def elastic_search_mapping_dict(self):
            field_mappings = OrderedDict()
            for field in self.fields:
                field_mappings[field.elastic_search_name()] = field.elastic_search_mapping_dict()
            return {'type': 'nested', 'properties': field_mappings}

        def elastic_search_mappings_dict(self):
            document_type = None
            for annotation in self.annotations:
                if annotation.name == 'elastic_search_document_type':
                    document_type = annotation.value
                    break
            if document_type is None:
                document_type = decamelize(self.name)

            properties = OrderedDict()
            for field in self.fields:
                properties[field.elastic_search_name()] = field.elastic_search_mapping_dict()

            mappings = {}
            mappings[document_type] = \
                {
                    '_all': {'enabled': False},
                    'dynamic': 'strict',
                }
            for annotation in self.annotations:
                if annotation.name == 'elastic_search_mappings_base':
                    mappings[document_type].update(annotation.value)
            if 'properties' in mappings[document_type]:
                updated_properties = OrderedDict()
                updated_properties.update(mappings[document_type]['properties'])
                updated_properties.update(properties)
                properties = updated_properties
            mappings[document_type]['properties'] = properties

            return mappings

    def __init__(self, settings=None, template=None):
        Generator.__init__(self)
        if settings is not None and not isinstance(settings, dict):
            raise TypeError('settings must be a dict')
        self._settings = settings
        if template is not None and not isinstance(template, str):
            raise TypeError('template must be a str')
        self._template = template


Parser.register_annotation_parser(ElasticSearchDocumentTypeAnnotationParser())
Parser.register_annotation_parser(ElasticSearchMappingAnnotationParser())
Parser.register_annotation_parser(ElasticSearchMappingsBaseAnnotationParser())
