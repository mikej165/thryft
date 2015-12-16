#-----------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

import logging
import os.path

from thryft.compiler.ast import Ast
from thryft.compiler.compile_exception import CompileException
from thryft.compiler.parser import Parser
from thryft.compiler.scanner import Scanner
from thryft.generator._type import _Type
from thryft.generator.document import Document
from thryft.generator.typedef import Typedef
from yutil import lower_camelize, class_qname


class Compiler(object):
    class __AstVisitor(object):
        def __init__(self, compiler, document_root_dir_path, generator, include_dir_paths):
            object.__init__(self)
            self.__compiler = compiler
            self.__document_root_dir_path = document_root_dir_path
            self.__generator = generator
            self.__include_dir_paths = include_dir_paths
            self.__scope_stack = []
            self.__type_by_thrift_qname_cache = {}
            self.__used_include_abspaths = {}
            self.__visited_includes = []

        def __construct(self, class_name, annotation_nodes=None, **kwds):
            if len(self.__scope_stack) > 0:
                parent = self.__scope_stack[-1]
            else:
                parent = self.__generator
            kwds['parent'] = parent
            construct_class = getattr(self.__generator, class_name)
            if annotation_nodes is not None and len(annotation_nodes) > 0:
                annotation_class = getattr(construct_class, 'Annotation')
                kwds['annotations'] = \
                    tuple(
                        annotation_class(
                            name=annotation_node.name,
                            value=annotation_node.value
                        )
                        for annotation_node in annotation_nodes
                    )
            return construct_class(**kwds)

        def __get_type(self, type_thrift_qname, resolve=True):
            # e.g., struct_include_file.Struct
            try:
                return self.__type_by_thrift_qname_cache[type_thrift_qname]
            except KeyError:
                if not resolve:
                    raise
                for include in self.__visited_includes:
                    for definition in include.document.definitions:
                        if isinstance(definition, _Type) or isinstance(definition, Typedef):
                            definition_thrift_qname = definition.thrift_qname()
                            if definition_thrift_qname == type_thrift_qname:
                                self.__type_by_thrift_qname_cache[definition_thrift_qname] = definition
                                self.__used_include_abspaths[include.abspath] = True
                                return definition
                raise KeyError(type_thrift_qname)

        def __put_type(self, type_thrift_qname, type_):
            if type_thrift_qname in self.__type_by_thrift_qname_cache:
                raise CompileException("duplicate type %s" % type_thrift_qname)
            self.__type_by_thrift_qname_cache[type_thrift_qname] = type_

        def visit_base_type_node(self, base_type_node):
            try:
                return self.__get_type(base_type_node.name, resolve=False)
            except KeyError:
                base_type = getattr(self.__generator, base_type_node.name.capitalize() + 'Type')(name=base_type_node.name)
                self.__put_type(base_type_node.name, base_type)
                return base_type

        def visit_bool_literal_node(self, bool_literal_node):
            return bool_literal_node.value

        def __visit_compound_type_node(self, construct_class_name, compound_type_node):
            compound_type = \
                self.__construct(
                    construct_class_name,
                    annotations=compound_type_node.annotations,
                    doc=self.__visit_doc_node(compound_type_node.doc),
                    name=compound_type_node.name
                )
            self.__scope_stack.append(compound_type)

            # Insert the compound type into the type_map here to allow recursive
            # definitions
            self.__put_type(compound_type.thrift_qname(), compound_type)

            if construct_class_name == 'EnumType':
                enum_type_node = compound_type_node
                have_enumerator_with_value = False
                enumerator_node_names = []
                for enumerator_i, enumerator_node in enumerate(enum_type_node.enumerators):
                    if enumerator_node.name in enumerator_node_names:
                        raise CompileException("%s has a duplicate enumerator name, %s" % (enum_type_node.name, enumerator_node.name), ast_node=enumerator_node)
                    enumerator_node_names.append(enumerator_node.name)

                    if enumerator_node.value is not None:
                        have_enumerator_with_value = True
                        assert isinstance(enumerator_node.value, Ast.IntLiteralNode), type(enumerator_node.value)
                        value = enumerator_node.value.value
                    else:
                        if have_enumerator_with_value:
                            raise CompileException("%s has mix of enumerators with and without values, must be one or the other" % enum_type_node.name, ast_node=enum_type_node)
                        value = enumerator_i

                    compound_type.enumerators.append(
                        self.__construct(
                            'Field',
                            annotation_nodes=enumerator_node.annotations,
                            doc=self.__visit_doc_node(enumerator_node.doc),
                            id=enumerator_i,
                            name=enumerator_node.name,
                            type=Ast.BaseTypeNode('i32').accept(self),
                            value=value
                        )
                    )
            else:
                field_names = []
                id_count = 0
                for field_node in compound_type_node.fields:
                    field_name = field_node.name
                    if field_name in field_names:
                        raise CompileException("compound type %s has a duplicate field %s" % (compound_type_node.name, field_name), ast_node=field_node)
                    field_name_lower_camelized = lower_camelize(field_name)
                    if field_name_lower_camelized in field_names:
                        raise CompileException("compound type %s has a duplicate field %s" % (compound_type_node.name, field_name), ast_node=field_node)
                    field_names.append(field_name)
                    field_names.append(field_name_lower_camelized)

                    field = field_node.accept(self)
                    if field.required:
                        if len(compound_type.fields) > 0:
                            if not compound_type.fields[-1].required:
                                raise CompileException("compound type %s has a required field %s after an optional field %s" % (compound_type_node.name, field.name, compound_type.fields[-1].name), ast_node=compound_type_node)
                    if field.id is not None:
                        id_count += 1
                        for existing_field in compound_type.fields:
                            if existing_field.id == field.id:
                                raise CompileException("compound type %s has duplicate field id %d (%s and %s fields)" % (compound_type_node.name, field.id, field.name, existing_field.name), ast_node=compound_type_node)
                    compound_type.fields.append(field)
                if len(compound_type.fields) > 0:
                    if id_count != 0 and id_count != len(compound_type_node.fields):
                        raise CompileException("compound type %s has some fields with ids and some fields without" % compound_type_node.name, ast_node=compound_type_node)

            self.__scope_stack.pop(-1)

            return compound_type

        def visit_const_node(self, const_node):
            return \
                self.__construct(
                    'Const',
                    annotation_nodes=const_node.annotations,
                    doc=self.__visit_doc_node(const_node.doc),
                    name=const_node.name,
                    type=const_node.type.accept(self),
                    value=const_node.value.accept(self)
                )

        def __visit_doc_node(self, doc_node):
            if doc_node is not None:
                return doc_node.text
            else:
                return None

        def visit_document_node(self, document_node):
            document = \
                self.__construct(
                    'Document',
                    document_root_dir_path=self.__document_root_dir_path,
                    path=document_node.path
                )
            self.__scope_stack.append(document)

            for header_node in document_node.headers:
                document.headers.append(header_node.accept(self))
            for definition_node in document_node.definitions:
                document.definitions.append(definition_node.accept(self))

            self.__scope_stack.pop(-1)

            logger = logging.getLogger(class_qname(Compiler))
            for include in self.__visited_includes:
                if not include.abspath in self.__used_include_abspaths:
                    logger.warn("unused include %s in document %s", include.relpath, document.path)
            return document

        def visit_enum_type_node(self, enum_node):
            return self.__visit_compound_type_node('EnumType', enum_node)

        def visit_exception_type_node(self, exception_type_node):
            return self.__visit_compound_type_node('ExceptionType', exception_type_node)

        def visit_field_node(self, field_node):
            if field_node.value is not None:
                value = field_node.value.accept(self)
            else:
                value = None
            return \
                self.__construct(
                    'Field',
                    annotation_nodes=field_node.annotations,
                    doc=self.__visit_doc_node(field_node.doc),
                    id=field_node.id,
                    name=field_node.name,
                    required=field_node.required,
                    type=field_node.type.accept(self),
                    value=value
                )

        def visit_float_literal_node(self, float_literal_node):
            return float_literal_node.value

        def visit_function_node(self, function_node):
            function = \
                self.__construct(
                    'Function',
                    annotation_nodes=function_node.annotations,
                    doc=self.__visit_doc_node(function_node.doc),
                    name=function_node.name,
                    oneway=function_node.oneway
                )
            self.__scope_stack.append(function)

            for parameter_node in function_node.parameters:
                parameter = parameter_node.accept(self)
                if parameter.required:
                    if len(function.parameters) > 0:
                        if not function.parameters[-1].required:
                            raise CompileException("function %s has a required parameter %s after an optional parameter %s" % (function.name, parameter.name, function.parameters[-1].name))
                function.parameters.append(parameter)
            if function_node.return_field is not None:
                function.return_field = function_node.return_field.accept(self)
            for throws_node in function_node.throws:
                function.throws.append(throws_node.accept(self))

            self.__scope_stack.pop(-1)
            return function

        def visit_include_node(self, include_node):
            include_dir_paths = list(self.__include_dir_paths)
            for scope in reversed(self.__scope_stack):
                if isinstance(scope, Document):
                    include_dir_paths.append(os.path.dirname(scope.path))
                    break

            include_file_relpath = include_node.path.replace('/', os.path.sep)
            for include_dir_path in include_dir_paths:
                include_file_path = os.path.join(include_dir_path, include_file_relpath)
                if os.path.exists(include_file_path):
                    include_file_path = os.path.abspath(include_file_path)
                    included_document = \
                        self.__compiler.compile(
                            thrift_file_paths=(include_file_path,),
                            generator=self.__generator
                        )[0]
                    include = \
                        self.__construct(
                            'Include',
                            abspath=include_file_path,
                            annotation_nodes=include_node.annotations,
                            doc=self.__visit_doc_node(include_node.doc),
                            document=included_document,
                            relpath=include_file_relpath
                        )
                    self.__visited_includes.append(include)
                    return include
            raise CompileException("include path not found: %s" % include_file_relpath, ast_node=include_node)

        def visit_int_literal_node(self, int_literal_node):
            return int_literal_node.value

        def visit_list_literal_node(self, list_literal_node):
            return tuple(element_value.accept(self) for element_value in list_literal_node.value)

        def visit_list_type_node(self, list_type_node):
            return self.__visit_sequence_type_node('ListType', list_type_node)

        def visit_map_literal_node(self, map_literal_node):
            return tuple((key_value.accept(self), value_value.accept(self)) for key_value, value_value in map_literal_node.value)

        def visit_map_type_node(self, map_type_node):
            try:
                return self.__get_type(map_type_node.name, resolve=False)
            except KeyError:
                map_type = self.__construct('MapType', key_type=map_type_node.key_type.accept(self), value_type=map_type_node.value_type.accept(self))
                self.__put_type(map_type_node.name, map_type)
                return map_type

        def visit_namespace_node(self, namespace_node):
            return \
                self.__construct(
                    'Namespace',
                    annotation_nodes=namespace_node.annotations,
                    doc=self.__visit_doc_node(namespace_node.doc),
                    name=namespace_node.name,
                    scope=namespace_node.scope
                )

        def __visit_sequence_type_node(self, construct_class_name, sequence_type_node):
            try:
                return self.__get_type(sequence_type_node.name, resolve=False)
            except KeyError:
                sequence_type = self.__construct(construct_class_name, element_type=sequence_type_node.element_type.accept(self))
                self.__put_type(sequence_type_node.name, sequence_type)
                return sequence_type

        def visit_service_node(self, service_node):
            service = \
                self.__construct(
                    'Service',
                    annotation_nodes=service_node.annotations,
                    doc=self.__visit_doc_node(service_node.doc),
                    name=service_node.name
                )
            self.__scope_stack.append(service)

            for function_node in service_node.functions:
                service.functions.append(function_node.accept(self))

            self.__scope_stack.pop(-1)

            return service

        def visit_set_type_node(self, set_type_node):
            return self.__visit_sequence_type_node('SetType', set_type_node)

        def visit_string_literal_node(self, string_literal_node):
            return string_literal_node.value

        def visit_struct_type_node(self, struct_type_node):
            return \
                self.__visit_compound_type_node(
                    'StructType',
                    struct_type_node,
                )

        def visit_type_node(self, type_node):
            try:
                try:
                    return self.__get_type(type_node.qname)
                except KeyError:
                    if type_node.qname == type_node.name:
                        document = self.__scope_stack[0]
                        return self.__get_type(document.name + '.' + type_node.qname)
                    else:
                        raise
            except KeyError:
                raise CompileException("unrecognized type '%s'" % type_node.qname, ast_node=type_node)

        def visit_typedef_node(self, typedef_node):
            typedef = \
                self.__construct(
                    'Typedef',
                    annotation_nodes=typedef_node.annotations,
                    doc=self.__visit_doc_node(typedef_node.doc),
                    name=typedef_node.name,
                    type=typedef_node.type.accept(self)
                )

            self.__put_type(typedef.thrift_qname(), typedef.type)

            return typedef

    def __init__(self, include_dir_paths=None):
        object.__init__(self)

        if include_dir_paths is None:
            include_dir_paths = []
        elif isinstance(include_dir_paths, (list, tuple)):
            include_dir_paths = list(include_dir_paths)
        else:
            include_dir_paths = [include_dir_paths]
        if len(include_dir_paths) == 0:
            include_dir_paths.append(os.getcwd())
        my_dir_path = os.path.dirname(os.path.realpath(__file__))
        lib_thrift_src_dir_path = \
            os.path.abspath(os.path.join(
                my_dir_path,
                '..', '..', '..', '..',
                'lib', 'thrift', 'src'
            ))
        if lib_thrift_src_dir_path not in include_dir_paths:
            include_dir_paths.append(lib_thrift_src_dir_path)
        self.__include_dir_paths = []
        for include_dir_path in include_dir_paths:
            if include_dir_path not in self.__include_dir_paths:
                self.__include_dir_paths.append(include_dir_path)
        self.__include_dir_paths = tuple(self.__include_dir_paths)

        self.__parsed_thrift_files_by_path = {}
        self.__scanner = Scanner()
        self.__parser = Parser()

    def __call__(self, *args, **kwds):
        return self.compile(*args, **kwds)

    def compile(self, generator, thrift_file_paths, document_root_dir_path=None):
        if generator is None:
            raise ValueError('generator must not be None')

        if not isinstance(thrift_file_paths, (list, tuple)):
            thrift_file_paths = (thrift_file_paths,)
        if len(thrift_file_paths) == 0:
            return tuple()

        documents = []
        for thrift_file_path in thrift_file_paths:
            thrift_file_path = os.path.abspath(thrift_file_path)
            document_node = self.__parsed_thrift_files_by_path.get(thrift_file_path)
            if document_node is None:
                tokens = self.__scanner.tokenize(thrift_file_path)
                document_node = self.__parser.parse(tokens)
                self.__parsed_thrift_files_by_path[thrift_file_path] = document_node
            ast_visitor = \
                self.__AstVisitor(
                    compiler=self,
                    document_root_dir_path=document_root_dir_path,
                    generator=generator,
                    include_dir_paths=self.__include_dir_paths
                )
            document = document_node.accept(ast_visitor)
            documents.append(document)
        return tuple(documents)

    @property
    def include_dir_paths(self):
        return self.__include_dir_paths
