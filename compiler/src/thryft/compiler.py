from pyparsing import ParseException
from thryft.grammar import Grammar
from thryft.generator.type import Type
from yutil import upper_camelize
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

        native_type_qnames = []
        for _1, _2, file_names in \
            os.walk(os.path.join(lib_thrift_src_dir_path, 'thryft', 'generator', 'native_types')):
            for file_name in file_names:
                file_base_name, file_ext = os.path.splitext(file_name)
                if file_ext != '.thrift':
                    continue
                native_type_qnames.append(
                    file_base_name + '.' + upper_camelize(file_base_name)
                )
        self.__native_type_qnames = native_type_qnames

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

    def compile(self, thrift_file_paths): #@ReservedAssignment
        if not isinstance(thrift_file_paths, (list, tuple)):
            thrift_file_paths = (thrift_file_paths,)

        documents = []
        for thrift_file_path in thrift_file_paths:
            document = self.__generator.Document(path=thrift_file_path)
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

    def __parse_compound_type_declarator(self, keyword, tokens):
        compound_type = \
            getattr(self.__generator, keyword.capitalize() + 'Type')(
                name=tokens[1],
                parent=self.__scope_stack[-1]
            )

        self.__scope_stack.append(compound_type)
        # Insert the compound type into the type_map here to allow recursive
        # definitions
        if keyword != 'struct' or \
           not compound_type.qname in self.__native_type_qnames:
            self.__type_map[compound_type.qname] = compound_type

        return [compound_type]

    def __parse_compound_type(self, keyword, tokens):
        compound_type = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            for field in tokens[1]:
                compound_type.fields.append(field)

        if keyword != 'struct' or \
           not compound_type.qname in self.__native_type_qnames:
            return [compound_type]
        else:
            return []

    def _parse_const(self, tokens):
        const = \
            self.__generator.Const(
                name=tokens[2],
                parent=self.__scope_stack[-1],
                type=self.__resolve_type(tokens[1]),
                value=tokens[3]
            )
        return [const]

    def _parse_document(self, tokens):
        document = self.__scope_stack[-1]
        document.definitions.extend(tokens[1])
        document.headers.extend(tokens[0])
        return [document]

    def _parse_enum_declarator(self, tokens):
        return self.__parse_compound_type_declarator('enum', tokens)

    def _parse_enum(self, tokens):
        enum = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            type_ = self.__resolve_type('i32')
            for token_i, token in enumerate(tokens[1]):
                if len(token) > 1:
                    value = token[1]
                else:
                    value = None
                enum.fields.append(
                    self.__generator.Field(
                        id=token_i,
                        name=token[0],
                        parent=enum,
                        type=type_,
                        value=value
                    )
                )

        self.__type_map[enum.qname] = enum

        return [enum]

    def _parse_exception_declarator(self, tokens):
        return self.__parse_compound_type_declarator('exception', tokens)

    def _parse_exception(self, tokens):
        return self.__parse_compound_type('exception', tokens)

    def _parse_field(self, tokens):
        tokens_copy = list(tokens)
        if isinstance(tokens_copy[0], int) and \
           not isinstance(tokens_copy[0], bool):
            id = tokens_copy.pop(0) #@ReservedAssignment
        else:
            id = None #@ReservedAssignment
        if isinstance(tokens_copy[0], bool):
            required = tokens_copy.pop(0)
        else:
            required = True
        type = self.__resolve_type(tokens_copy.pop(0)) #@ReservedAssignment
        name = tokens_copy.pop(0)
        if len(tokens_copy) > 0:
            value = tokens_copy.pop(0)
        else:
            value = None

        parent = self.__scope_stack[-1]

        field = \
            self.__generator.Field(
                id=id,
                name=name,
                parent=parent,
                required=required,
                type=type,
                value=value
            )

        return [field]

    def _parse_function_declarator(self, tokens):
        tokens_copy = list(tokens)
        if tokens_copy[0] == 'oneway':
            tokens_copy.pop(0)
            oneway = True
        else:
            oneway = False

        return_type_name = tokens_copy.pop(0)
        if return_type_name == 'void':
            return_type = None
        else:
            return_type = self.__resolve_type(return_type_name)

        name = tokens_copy.pop(0)

        parent = self.__scope_stack[-1]

        function = \
            self.__generator.Function(
                name=name,
                oneway=oneway,
                parent=parent,
                return_type=return_type
            )

        self.__scope_stack.append(function)

        return [function]

    def _parse_function(self, tokens):
        tokens_copy = list(tokens)
        function = tokens_copy.pop(0)
        self.__scope_stack.pop(-1)

        while len(tokens_copy) > 0:
            if tokens_copy[0] == 'throws':
                tokens_copy.pop(0)
                function.throws.extend(tokens_copy.pop(0))
            else:
                function.parameters.extend(tokens_copy.pop(0))

        return [function]

    def _parse_include(self, tokens):
        include = \
            self.__generator.Include(
                name=tokens[1],
                parent=self.__scope_stack[-1],
                path=tokens[1]
            )

        for include_dir_path in self.__include_dir_paths:
            include_file_path = os.path.join(include_dir_path, include.path)
            if os.path.exists(include_file_path):
                include_file_path = os.path.abspath(include_file_path)
                self.compile((include_file_path,))
                if not include.path.startswith('thryft/generator/native_types/'):
                    return [include]
                else:
                    return []
        raise RuntimeError("include path not found: %s" % include.path)

    def _parse_list_type(self, tokens):
        return self.__parse_sequence_type('list', tokens)

    def _parse_map_type(self, tokens):
        key_type = self.__resolve_type(tokens[1])
        value_type = self.__resolve_type(tokens[2])
        map_type = \
            self.__generator.MapType(
                key_type=key_type,
                name="map<%s, %s>" % (key_type.qname, value_type.qname),
                parent=self.__scope_stack[-1],
                value_type=value_type
            )
        return [map_type]

    def _parse_namespace(self, tokens):
        namespace = \
            self.__generator.Namespace(
                name=tokens[2],
                parent=self.__scope_stack[-1],
                scope=tokens[1]
            )
        return [namespace]

    def __parse_sequence_type(self, keyword, tokens):
        assert tokens[0] == keyword
        element_type = self.__resolve_type(tokens[1])
        sequence_type = \
            getattr(self.__generator, keyword.capitalize() + 'Type')(
                element_type=element_type,
                name="%s<%s>" % (keyword, element_type.qname),
                parent=self.__scope_stack[-1]
            )
        return [sequence_type]

    def _parse_service_declarator(self, tokens):
        service = \
            self.__generator.Service(
                extends=len(tokens) > 2 and tokens[3] or None,
                name=tokens[1],
                parent=self.__scope_stack[-1]
            )

        self.__scope_stack.append(service)

        return [service]

    def _parse_service(self, tokens):
        service = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            service.functions.extend(tokens[1])

        return [service]

    def _parse_set_type(self, tokens):
        return self.__parse_sequence_type('set', tokens)

    def _parse_struct_declarator(self, tokens):
        return self.__parse_compound_type_declarator('struct', tokens)

    def _parse_struct(self, tokens):
        return self.__parse_compound_type('struct', tokens)

    def _parse_typedef(self, tokens):
        typedef = \
            self.__generator.Typedef(
                name=tokens[2],
                parent=self.__scope_stack[-1],
                type=self.__resolve_type(tokens[1])
            )

        self.__type_map[typedef.qname] = typedef.type

        return [typedef]

    def __resolve_type(self, type_):
        if isinstance(type_, Type):
            return type_
        type_name = type_
        try:
            return self.__type_map[type_name]
        except KeyError:
            if type_name in self.__grammar.base_type_names:
                return getattr(self.__generator, type_name.capitalize() + 'Type')(name=type_name)
            elif type_name in self.__native_type_qnames:
                type_name = type_name.rsplit('.', 1)[1]
                return getattr(self.__generator, type_name)(name=type_name)
            elif not '.' in type_name:
                document = self.__scope_stack[0]
                type_qname = document.name + '.' + type_name
                return self.__type_map[type_qname]
            else:
                raise

    @staticmethod
    def _wrap_parse_action(parse_action):
        def wrapped_parse_action(tokens):
            try:
                out_tokens = parse_action(tokens)
                logging.debug(
                    "parsed %s with %s -> %s",
                    tokens,
                    parse_action,
                    out_tokens
                )
                return out_tokens
            except:
                logging.error(
                    "error parsing %s with %s",
                    tokens,
                    parse_action,
                    exc_info=True
                )
                raise
        return lambda tokens: wrapped_parse_action(tokens)
