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
from pyparsing import ParseException
from thryft.generator.comment import Comment
from thryft.generator.document import Document
from thryft.generator._type import _Type
from thryft.grammar import Grammar
import imp
import logging
import os.path
import sys


class Compiler(object):
    def __init__(self, generator, include_dir_paths=None):
        object.__init__(self)

        self.__grammar = grammar = Grammar()

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
                '..', '..', '..',
                'lib', 'thrift', 'src'
            ))
        if not lib_thrift_src_dir_path in include_dir_paths:
            include_dir_paths.append(lib_thrift_src_dir_path)
        self.__include_dir_paths = include_dir_paths

        self.__generator = generator

        self.__scope_stack = []
        self.__type_map = {}

        for attr in dir(self):
            if not attr.startswith('_parse_'):
                continue
            parser_element = getattr(grammar, attr[len('_parse_'):])
            parse_action = getattr(self, attr)
            parser_element.setParseAction(
                self._wrap_parse_action(parse_action)
            )

    def __call__(self, thrift_file_paths):
        return self.compile(thrift_file_paths)

    def compile(self, thrift_file_paths):  # @ReservedAssignment
        if not isinstance(thrift_file_paths, (list, tuple)):
            thrift_file_paths = (thrift_file_paths,)

        documents = []
        for thrift_file_path in thrift_file_paths:
            document = self.__construct('Document', path=thrift_file_path)
            self.__scope_stack.append(document)

            try:
                self.__grammar.document.parseFile(thrift_file_path, parseAll=True)
            except ParseException, e:
                print >> sys.stderr, 'Error parsing', thrift_file_path + ':'
                print >> sys.stderr, e.line
                print >> sys.stderr, ' ' * (e.column - 1) + '^'
                print >> sys.stderr, e
                raise

            assert self.__scope_stack[-1] is document
            self.__scope_stack.pop(-1)
            documents.append(document)

        return documents

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

    def __merge_comments(self, tokens):
        comments = []
        while isinstance(tokens[0], Comment):
            comment = tokens.pop(0)
            if len(comments) > 0:
                assert comment.__class__ is comments[0].__class__
                assert comment.parent is comments[0].parent
            comments.append(comment)
        if len(comments) > 0:
            return self.__construct(
                       'Comment',
                       parent=comments[0].parent,
                       text="\n".join(comment.text
                                       for comment in comments),
                   )

    def _parse_comment(self, tokens):
        text = tokens[0]
        if text.startswith('/*'):
            text = text[2:-2]
            lines = []
            for line in text.splitlines():
                if line.lstrip().startswith(' * '):
                    line = line.lstrip().lstrip(' * ')
                line = line.rstrip()
                if len(line) > 0:
                    lines.append(line)
            text = "\n".join(lines)
        elif text.startswith('//'):
            text = text[2:].strip()
        elif text.startswith('#'):
            text = text[2:].strip()
        else:
            raise NotImplementedError(text)

        comment = \
            self.__construct(
                'Comment',
                text=text
            )
        return [comment]

    def __parse_compound_type(self, keyword, tokens):
        compound_type = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            for field in tokens[1]:
                if keyword == 'enum':
                    compound_type.enumerators.append(field)
                else:
                    compound_type.fields.append(field)

        return [compound_type]

    def __parse_compound_type_declarator(self, keyword, tokens):
        comment = self.__merge_comments(tokens)

        compound_type = \
            self.__construct(
                keyword.capitalize() + 'Type',
                comment=comment,
                name=tokens[1]
            )

        self.__scope_stack.append(compound_type)

        # Insert the compound type into the type_map here to allow recursive
        # definitions
        self.__type_map[compound_type.thrift_qname()] = compound_type

        return [compound_type]

    def _parse_const(self, tokens):
        comment = self.__merge_comments(tokens)

        print tokens

        const = \
            self.__construct(
                'Const',
                comment=comment,
                name=tokens[2],
                type=self.__resolve_type(tokens[1]),
                value=tokens[3]
            )
        return [const]

    def _parse_document(self, tokens):
        comment = self.__merge_comments(tokens)
        document = self.__scope_stack[-1]
        document._set_comment(comment)
        document.definitions.extend(tokens[1])
        document.headers.extend(tokens[0])
        return [document]

    def _parse_enum(self, tokens):
        enum = self.__parse_compound_type('enum', tokens)[0]
        enumerators = list(enum.enumerators)
        del enum.enumerators[::]
        for enumerator_i, enumerator in enumerate(enumerators):
            enum.enumerators.append(
                enumerator.__class__(
                    id=enumerator_i,
                    name=enumerator.name,
                    parent=enumerator.parent,
                    type=enumerator.type,
                    value=enumerator.value
                )
            )
        return [enum]

    def _parse_enum_declarator(self, tokens):
        return self.__parse_compound_type_declarator('enum', tokens)

    def _parse_enumerator(self, tokens):
        comment = self.__merge_comments(tokens)

        if len(tokens) > 1:
            value = tokens[1]
        else:
            value = None
        enumerator = \
            self.__construct(
                'Field',
                comment=comment,
                name=tokens[0],
                type=self.__resolve_type('i32'),
                value=value
            )
        return [enumerator]

    def _parse_exception(self, tokens):
        return self.__parse_compound_type('exception', tokens)

    def _parse_exception_declarator(self, tokens):
        return self.__parse_compound_type_declarator('exception', tokens)

    def _parse_field(self, tokens):
        comment = self.__merge_comments(tokens)

        if isinstance(tokens[0], int) and \
           not isinstance(tokens[0], bool):
            id = tokens.pop(0)  # @ReservedAssignment
        else:
            id = None  # @ReservedAssignment
        if isinstance(tokens[0], bool):
            required = tokens.pop(0)
        else:
            required = True
        type = self.__resolve_type(tokens.pop(0))  # @ReservedAssignment
        name = tokens.pop(0)
        if len(tokens) > 0:
            value = tokens.pop(0)
        else:
            value = None

        field = \
            self.__construct(
                'Field',
                comment=comment,
                id=id,
                name=name,
                required=required,
                type=type,
                value=value
            )

        return [field]

    def _parse_function(self, tokens):
        function = tokens.pop(0)
        self.__scope_stack.pop(-1)

        while len(tokens) > 0:
            if tokens[0] == 'throws':
                tokens.pop(0)
                function.throws.extend(tokens.pop(0))
            else:
                function.parameters.extend(tokens.pop(0))

        return [function]

    def _parse_function_declarator(self, tokens):
        comment = self.__merge_comments(tokens)

        if tokens[0] == 'oneway':
            tokens.pop(0)
            oneway = True
        else:
            oneway = False

        return_type_name = tokens.pop(0)
        if return_type_name == 'void':
            return_type = None
        else:
            return_type = self.__resolve_type(return_type_name)

        function = \
            self.__construct(
                'Function',
                comment=comment,
                name=tokens[0],
                oneway=oneway,
                return_type=return_type
            )

        self.__scope_stack.append(function)

        return [function]

    def _parse_include(self, tokens):
        include_dir_paths = list(self.__include_dir_paths)
        for scope in reversed(self.__scope_stack):
            if isinstance(scope, Document):
                include_dir_paths.append(os.path.dirname(scope.path))
                break

        include_file_relpath = tokens[1]
        for include_dir_path in include_dir_paths:
            include_file_path = os.path.join(include_dir_path, include_file_relpath)
            if os.path.exists(include_file_path):
                include_file_path = os.path.abspath(include_file_path)
                document = self.compile((include_file_path,))[0]
                include = \
                    self.__construct(
                        'Include',
                        document=document,
                        path=include_file_relpath
                    )
                return [include]
        raise RuntimeError("include path not found: %s" % include_file_relpath)

    def _parse_list_type(self, tokens):
        return self.__parse_sequence_type('list', tokens)

    def _parse_map_type(self, tokens):
        key_type = self.__resolve_type(tokens[1])
        value_type = self.__resolve_type(tokens[2])
        map_type = \
            self.__construct(
                'MapType',
                key_type=key_type,
                name="map<%s, %s>" % (key_type.thrift_qname(), value_type.thrift_qname()),
                value_type=value_type
            )
        return [map_type]

    def _parse_namespace(self, tokens):
        namespace = \
            self.__construct(
                'Namespace',
                name=tokens[2],
                scope=tokens[1]
            )
        return [namespace]

    def __parse_sequence_type(self, keyword, tokens):
        assert tokens[0] == keyword
        element_type = self.__resolve_type(tokens[1])
        sequence_type = \
            self.__construct(
                keyword.capitalize() + 'Type',
                element_type=element_type,
                name="%s<%s>" % (keyword, element_type.thrift_qname())
            )
        return [sequence_type]

    def _parse_service(self, tokens):
        service = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            service.functions.extend(tokens[1])

        return [service]

    def _parse_service_declarator(self, tokens):
        comment = self.__merge_comments(tokens)

        service = \
            self.__construct(
                'Service',
                comment=comment,
                extends=len(tokens) > 2 and tokens[3] or None,
                name=tokens[1]
            )

        self.__scope_stack.append(service)

        return [service]

    def _parse_set_type(self, tokens):
        return self.__parse_sequence_type('set', tokens)

    def _parse_struct(self, tokens):
        return self.__parse_compound_type('struct', tokens)

    def _parse_struct_declarator(self, tokens):
        return self.__parse_compound_type_declarator('struct', tokens)

    def _parse_typedef(self, tokens):
        comment = self.__merge_comments(tokens)

        typedef = \
            self.__construct(
                'Typedef',
                comment=comment,
                name=tokens[2],
                type=self.__resolve_type(tokens[1])
            )

        self.__type_map[typedef.thrift_qname()] = typedef.type

        return [typedef]

    def __resolve_type(self, type_):
        if isinstance(type_, _Type):
            return type_
        type_name = type_
        try:
            return self.__type_map[type_name]
        except KeyError:
            if type_name in self.__grammar.base_type_names:
                return getattr(self.__generator, type_name.capitalize() + 'Type')(name=type_name)
            elif not '.' in type_name:
                document = self.__scope_stack[0]
                type_qname = document.name + '.' + type_name
                return self.__type_map[type_qname]
            else:
                raise

    @staticmethod
    def _wrap_parse_action(parse_action):
        def wrapped_parse_action(in_tokens):
            in_tokens_copy = list(in_tokens)
            try:
                out_tokens = parse_action(in_tokens_copy)
                logging.debug(
                    "parsed %s with %s -> %s",
                    in_tokens,
                    parse_action,
                    out_tokens
                )
                return out_tokens
            except:
                logging.error(
                    "error parsing %s with %s",
                    in_tokens,
                    parse_action,
                    exc_info=True
                )
                raise
        return lambda in_tokens: wrapped_parse_action(in_tokens)
