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

from inspect import isclass
from thryft.compiler.ast import Ast
from thryft.compiler.compile_exception import CompileException
from thryft.compiler.parser import Parser
from thryft.compiler.scanner import Scanner
from thryft.generator.document import Document
import imp
import logging
import os.path


class Compiler(object):
    class __AstVisitor(object):
        def __init__(self, compiler, generator, include_dir_paths):
            object.__init__(self)
            self.__compiler = compiler
            self.__generator = generator
            self.__include_dir_paths = include_dir_paths
            self.__scope_stack = []
            self.__type_cache = {}

        def __construct(self, class_name, parent=None, **kwds):
            if parent is None and len(self.__scope_stack) > 0:
                parent = self.__scope_stack[-1]
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
                                default_construct_class = getattr(self.__generator, class_name)
                                for attr in dir(overrides_module):
                                    value = getattr(overrides_module, attr)
                                    if isclass(value) and issubclass(value, default_construct_class):
                                        return getattr(overrides_module, attr)(**kwds)
                        break

            return getattr(self.__generator, class_name)(**kwds)

        def visit_base_type_node(self, base_type_node):
            try:
                return self.__type_cache[base_type_node.name]
            except:
                base_type = getattr(self.__generator, base_type_node.name.capitalize() + 'Type')(name=base_type_node.name)
                self.__type_cache[base_type_node.name] = base_type
                return base_type

        def __visit_compound_type_node(self, construct_class_name, compound_type_node):
            compound_type = \
                self.__construct(
                    construct_class_name,
                    name=compound_type_node.name
                )
            self.__scope_stack.append(compound_type)

            # Insert the compound type into the type_map here to allow recursive
            # definitions
            self.__type_cache[compound_type.thrift_qname()] = compound_type

            if construct_class_name == 'EnumType':
                for enumerator_i, enumerator_node in enumerate(compound_type_node.enumerators):
                    compound_type.enumerators.append(
                        self.__construct(
                            'Field',
                            id=enumerator_i,
                            name=enumerator_node.name,
                            type=Ast.BaseTypeNode('i32').accept(self),
                            value=enumerator_node.value
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
                    name=const_node.name,
                    type=const_node.type.accept(self),
                    value=const_node.value
                )

        def visit_document_node(self, document_node):
            document = self.__construct('Document', path=document_node.path)
            self.__scope_stack.append(document)

            for header in document_node.headers:
                document.headers.append(header.accept(self))
            for definition in document_node.definitions:
                document.definitions.append(definition.accept(self))

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
                    id=field_node.id,
                    name=field_node.name,
                    required=field_node.required,
                    type=field_node.type.accept(self),
                    value=field_node.value
                )

        def visit_function_node(self, function_node):
            if function_node.return_type.name == 'void':
                return_type = None
            else:
                return_type = function_node.return_type.accept(self)

            function = \
                self.__construct(
                    'Function',
                    name=function_node.name,
                    oneway=function_node.oneway,
                    return_type=return_type
                )
            self.__scope_stack.append(function)

            for parameter_node in function_node.parameters:
                function.parameters.append(parameter_node.accept(self))
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
                    document = self.__compiler.compile((include_file_path,))[0]
                    include = \
                        self.__construct(
                            'Include',
                            document=document,
                            path=include_file_relpath
                        )
                    return include
            raise RuntimeError("include path not found: %s" % include_file_relpath)

        def visit_list_type_node(self, list_type_node):
            return self.__visit_sequence_type_node('ListType', list_type_node)

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
            service = self.__construct('Service', name=service_node.name)
            self.__scope_stack.append(service)

            for function_node in service_node.functions:
                service.functions.append(function_node.accept(self))

            self.__scope_stack.pop(-1)

            return service

        def visit_set_type_node(self, set_type_node):
            return self.__visit_sequence_type_node('SetType', set_type_node)

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

        self.__scanner = Scanner()
        self.__parser = Parser()

    def __call__(self, thrift_file_paths, generator=None):
        return self.compile(thrift_file_paths)

    def compile(self, thrift_file_paths, generator=None):
        if not isinstance(thrift_file_paths, (list, tuple)):
            thrift_file_paths = (thrift_file_paths,)

        documents = []
        for thrift_file_path in thrift_file_paths:
            tokens = self.__scanner.tokenize(thrift_file_path)
            document_node = self.__parser.parse(tokens)
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
        return documents
