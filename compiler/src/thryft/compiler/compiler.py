#-------------------------------------------------------------------------------
# Copyright (c) 2013, Minor Gordon
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
#-------------------------------------------------------------------------------

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
#-------------------------------------------------------------------------------

from inspect import isclass
from thryft.compiler.ast import Ast
from thryft.compiler.compile_exception import CompileException
from thryft.compiler.parser import Parser
from thryft.compiler.scanner import Scanner
from thryft.generator._type import _Type
from thryft.generator.document import Document
from thryft.generator.generator import Generator
from thryft.generator.typedef import Typedef
import imp
import logging
import os.path


class Compiler(object):
    class __AstVisitor(object):
        __ROOT_GENERATOR = Generator()

        def __init__(self, compiler, generator, include_dir_paths):
            object.__init__(self)
            self.__compiler = compiler
            self.__generator = generator
            self.__include_dir_paths = include_dir_paths
            self.__scope_stack = []
            self.__type_cache = {}

        def __construct(self, class_name, **kwds):
            if len(self.__scope_stack) > 0:
                parent = self.__scope_stack[-1]
            else:
                parent = self.__generator
            kwds['parent'] = parent

            name = kwds.get('name')
            if name is not None:
                for scope in reversed(self.__scope_stack):
                    if isinstance(scope, Document):
                        document = scope
                        overrides_module_file_path = os.path.splitext(document.path)[0] + '.py'
                        if os.path.isfile(overrides_module_file_path):
                            overrides_module_dir_path, overrides_module_file_name = \
                                os.path.split(overrides_module_file_path)
                            overrides_module_name = \
                                os.path.splitext(overrides_module_file_name)[0]
                            try:
                                overrides_module = \
                                    imp.load_module(
                                        overrides_module_name,
                                        *imp.find_module(
                                            overrides_module_name,
                                            [overrides_module_dir_path]
                                        )
                                    )
                            except ImportError:
                                logging.error(
                                    "error importing overrides module %s",
                                    overrides_module_file_path,
                                    exc_info=True
                                )
                                overrides_module = None

                            if overrides_module is not None:
                                # Find an override implementation corresponding to our generator
                                # For example, find JavaDateTime by looking in the module for a
                                # class that inherits JavaStructType, assuming class_name is
                                # StructType.
                                # The first_bases algorithm below covers the case where we want
                                # JavaDateTime but the generator gave us something that itself
                                # inherits from JavaStructType e.g., SubJavaStructType.
                                # In this case there is no SubJavaDateTime(SubJavaStructType), so
                                # we need to consider SubJavaStructType's parent (JavaStructType)
                                # and look for a subclass of that.
                                root_construct_class = getattr(self.__ROOT_GENERATOR, class_name)
                                generator_construct_class = getattr(self.__generator, class_name)
                                parent_construct_classes = [generator_construct_class]
                                def __get_first_bases(class_, first_bases):
                                    if len(class_.__bases__) == 0:
                                        return
                                    first_base = class_.__bases__[0]
                                    if first_base is object or first_base is root_construct_class:
                                        return
                                    if first_base.__name__[0] != '_':
                                        first_bases.append(first_base)
                                    __get_first_bases(first_base, first_bases)
                                __get_first_bases(generator_construct_class, parent_construct_classes)

                                for parent_construct_class in parent_construct_classes:
                                    for attr in dir(overrides_module):
                                        value = getattr(overrides_module, attr)
                                        if isclass(value) and \
                                           issubclass(value, parent_construct_class) and \
                                           value != parent_construct_class:
                                            return getattr(overrides_module, attr)(**kwds)
                                # logging.warn("could not find override class for %s in %s" % (default_construct_class.__name__, overrides_module_name))
                        break

            return getattr(self.__generator, class_name)(**kwds)

        def visit_annotation_node(self, annotation_node):
            return annotation_node.value

        def __visit_annotation_nodes(self, annotation_nodes):
            if annotation_nodes is None:
                return {}
            return dict((annotation_node.name, annotation_node.accept(self))
                         for annotation_node in annotation_nodes)

        def visit_base_type_node(self, base_type_node):
            try:
                return self.__type_cache[base_type_node.name]
            except:
                base_type = getattr(self.__generator, base_type_node.name.capitalize() + 'Type')(name=base_type_node.name)
                self.__type_cache[base_type_node.name] = base_type
                return base_type

        def visit_bool_literal_node(self, bool_literal_node):
            return bool_literal_node.value

        def __visit_compound_type_node(self, construct_class_name, compound_type_node):
            compound_type = \
                self.__construct(
                    construct_class_name,
                    annotations=self.__visit_annotation_nodes(compound_type_node.annotations),
                    doc=self.__visit_doc_node(compound_type_node.doc),
                    name=compound_type_node.name
                )
            self.__scope_stack.append(compound_type)

            # Insert the compound type into the type_map here to allow recursive
            # definitions
            self.__type_cache[compound_type.thrift_qname()] = compound_type

            if construct_class_name == 'EnumType':
                have_enumerator_with_value = False
                for enumerator_node in compound_type_node.enumerators:
                    if enumerator_node.value is not None:
                        have_enumerator_with_value = True
                    elif have_enumerator_with_value:
                        raise CompileException("%s has mix of enumerators with and without values, must be one or the other" % compound_type_node.name, ast_node=compound_type_node)
                for enumerator_i, enumerator_node in enumerate(compound_type_node.enumerators):
                    if enumerator_node.value is None:
                        value = enumerator_i
                    else:
                        assert isinstance(enumerator_node.value, Ast.IntLiteralNode), type(enumerator_node.value)
                        value = enumerator_node.value.value
                    compound_type.enumerators.append(
                        self.__construct(
                            'Field',
                            annotations=self.__visit_annotation_nodes(enumerator_node.annotations),
                            doc=self.__visit_doc_node(enumerator_node.doc),
                            id=enumerator_i,
                            name=enumerator_node.name,
                            type=Ast.BaseTypeNode('i32').accept(self),
                            value=value
                        )
                    )
            else:
                for field in compound_type_node.fields:
                    compound_type.fields.append(field.accept(self))

            self.__scope_stack.pop(-1)

            return compound_type

        def visit_const_node(self, const_node):
            return \
                self.__construct(
                    'Const',
                    annotations=self.__visit_annotation_nodes(const_node.annotations),
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
            document = self.__construct('Document', path=document_node.path)
            self.__scope_stack.append(document)

            for header_node in document_node.headers:
                document.headers.append(header_node.accept(self))
            for definition_node in document_node.definitions:
                document.definitions.append(definition_node.accept(self))

            self.__scope_stack.pop(-1)

            return document

        def visit_enum_type_node(self, enum_node):
            return self.__visit_compound_type_node('EnumType', enum_node)

        def visit_exception_type_node(self, exception_type_node):
            return self.__visit_compound_type_node('ExceptionType', exception_type_node)

        def visit_field_node(self, field_node):
            return \
                self.__construct(
                    'Field',
                    annotations=self.__visit_annotation_nodes(field_node.annotations),
                    doc=self.__visit_doc_node(field_node.doc),
                    id=field_node.id,
                    name=field_node.name,
                    required=field_node.required,
                    type=field_node.type.accept(self),
                    value=field_node.value
                )

        def visit_float_literal_node(self, float_literal_node):
            return float_literal_node.value

        def visit_function_node(self, function_node):
            function = \
                self.__construct(
                    'Function',
                    annotations=self.__visit_annotation_nodes(function_node.annotations),
                    doc=self.__visit_doc_node(function_node.doc),
                    name=function_node.name,
                    oneway=function_node.oneway
                )
            self.__scope_stack.append(function)

            for parameter_node in function_node.parameters:
                function.parameters.append(parameter_node.accept(self))
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
                    included_document = self.__compiler.compile((include_file_path,), generator=self.__generator)[0]
                    include = \
                        self.__construct(
                            'Include',
                            annotations=self.__visit_annotation_nodes(include_node.annotations),
                            doc=self.__visit_doc_node(include_node.doc),
                            document=included_document,
                            path=include_file_relpath
                        )
                    for definition in included_document.definitions:
                        if isinstance(definition, _Type):
                            self.__type_cache[definition.thrift_qname()] = definition
                        elif isinstance(definition, Typedef):
                            self.__type_cache[definition.thrift_qname()] = definition.type
                    return include
            raise CompileException("include path not found: %s" % include_file_relpath, ast_node=include_node)

        def visit_int_literal_node(self, int_literal_node):
            return int_literal_node.value

        def visit_list_literal_node(self, list_literal_node):
            return tuple(element_value.accept(self) for element_value in list_literal_node.value)

        def visit_list_type_node(self, list_type_node):
            return self.__visit_sequence_type_node('ListType', list_type_node)

        def visit_map_literal_node(self, map_literal_node):
            return dict((key_value.accept(self), value_value.accept(self)) for key_value, value_value in map_literal_node.value.iteritems())

        def visit_map_type_node(self, map_type_node):
            try:
                return self.__type_cache[map_type_node.name]
            except:
                map_type = self.__construct('MapType', key_type=map_type_node.key_type.accept(self), value_type=map_type_node.value_type.accept(self))
                self.__type_cache[map_type_node.name] = map_type
                return map_type

        def visit_namespace_node(self, namespace_node):
            return \
                self.__construct(
                    'Namespace',
                    annotations=self.__visit_annotation_nodes(namespace_node.annotations),
                    doc=self.__visit_doc_node(namespace_node.doc),
                    name=namespace_node.name,
                    scope=namespace_node.scope
                )

        def __visit_sequence_type_node(self, construct_class_name, sequence_type_node):
            try:
                return self.__type_cache[sequence_type_node.name]
            except:
                sequence_type = self.__construct(construct_class_name, element_type=sequence_type_node.element_type.accept(self))
                self.__type_cache[sequence_type_node.name] = sequence_type
                return sequence_type

        def visit_service_node(self, service_node):
            service = \
                self.__construct(
                    'Service',
                    annotations=self.__visit_annotation_nodes(service_node.annotations),
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
            return self.__visit_compound_type_node('StructType', struct_type_node)

        def visit_type_node(self, type_node):
            try:
                try:
                    return self.__type_cache[type_node.qname]
                except KeyError:
                    if type_node.qname == type_node.name:
                        document = self.__scope_stack[0]
                        return self.__type_cache[document.name + '.' + type_node.qname]
                    else:
                        raise
            except KeyError:
                raise CompileException("unrecognized type '%s'" % type_node.qname, ast_node=type_node)

        def visit_typedef_node(self, typedef_node):
            typedef = \
                self.__construct(
                    'Typedef',
                    annotations=self.__visit_annotation_nodes(typedef_node.annotations),
                    doc=self.__visit_doc_node(typedef_node.doc),
                    name=typedef_node.name,
                    type=typedef_node.type.accept(self)
                )

            self.__type_cache[typedef.thrift_qname()] = typedef.type

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
        if not lib_thrift_src_dir_path in include_dir_paths:
            include_dir_paths.append(lib_thrift_src_dir_path)
        self.__include_dir_paths = []
        for include_dir_path in include_dir_paths:
            if not include_dir_path in self.__include_dir_paths:
                self.__include_dir_paths.append(include_dir_path)
        self.__include_dir_paths = tuple(self.__include_dir_paths)

        self.__parsed_thrift_files_by_path = {}
        self.__scanner = Scanner()
        self.__parser = Parser()

    def __call__(self, thrift_file_paths, generator=None):
        return self.compile(thrift_file_paths, generator=generator)

    def compile(self, thrift_file_paths, generator=None):
        if not isinstance(thrift_file_paths, (list, tuple)):
            thrift_file_paths = (thrift_file_paths,)

        documents = []
        for thrift_file_path in thrift_file_paths:
            thrift_file_path = os.path.abspath(thrift_file_path)
            document_node = self.__parsed_thrift_files_by_path.get(thrift_file_path)
            if document_node is None:
                tokens = self.__scanner.tokenize(thrift_file_path)
                document_node = self.__parser.parse(tokens)
                self.__parsed_thrift_files_by_path[thrift_file_path] = document_node
            if generator is not None:
                ast_visitor = \
                    self.__AstVisitor(
                        compiler=self,
                        generator=generator,
                        include_dir_paths=self.__include_dir_paths
                    )
                document = document_node.accept(ast_visitor)
                documents.append(document)
            else:
                documents.append(document_node)
        return tuple(documents)

    @property
    def include_dir_paths(self):
        return self.__include_dir_paths
