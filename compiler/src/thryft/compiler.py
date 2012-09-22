from pyparsing import ParseException
from thryft.generator.type import Type
from thryft.grammar import Grammar
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

    def __merge_comments(self, tokens):
        comments = []
        while isinstance(tokens[0], self.__generator.Comment):
            comment = tokens.pop(0)
            if len(comments) > 0:
                assert comment.__class__ is comments[0].__class__
                assert comment.parent is comments[0].parent
            comments.append(comment)
        if len(comments) > 0:
            return self.__generator.Comment(
                       parent=comments[0].parent,
                       text="\n".join([comment.text
                                       for comment in comments]),
                   )

    def _parse_comment(self, tokens):
        text = tokens[0]
        if text.startswith('/*'):
            text = text[2:-2]
            lines = []
            for line in text.splitlines():
                if line.lstrip().startswith('*'):
                    line = line.lstrip().lstrip('*')
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
            self.__generator.Comment(
                parent=self.__scope_stack[-1],
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

        if keyword != 'struct' or \
           not compound_type.qname in self.__native_type_qnames:
            return [compound_type]
        else:
            return []

    def __parse_compound_type_declarator(self, keyword, tokens):
        comment = self.__merge_comments(tokens)

        compound_type = \
            getattr(self.__generator, keyword.capitalize() + 'Type')(
                comment=comment,
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

    def _parse_const(self, tokens):
        comment = self.__merge_comments(tokens)

        print tokens

        const = \
            self.__generator.Const(
                comment=comment,
                name=tokens[2],
                parent=self.__scope_stack[-1],
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
            self.__generator.Field(
                comment=comment,
                name=tokens[0],
                parent=self.__scope_stack[-1],
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
            id = tokens.pop(0) #@ReservedAssignment
        else:
            id = None #@ReservedAssignment
        if isinstance(tokens[0], bool):
            required = tokens.pop(0)
        else:
            required = True
        type = self.__resolve_type(tokens.pop(0)) #@ReservedAssignment
        name = tokens.pop(0)
        if len(tokens) > 0:
            value = tokens.pop(0)
        else:
            value = None

        parent = self.__scope_stack[-1]

        field = \
            self.__generator.Field(
                comment=comment,
                id=id,
                name=name,
                parent=parent,
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

        name = tokens.pop(0)

        parent = self.__scope_stack[-1]

        function = \
            self.__generator.Function(
                comment=comment,
                name=name,
                oneway=oneway,
                parent=parent,
                return_type=return_type
            )

        self.__scope_stack.append(function)

        return [function]

    def _parse_include(self, tokens):
        include_dir_paths = list(self.__include_dir_paths)
        for scope in reversed(self.__scope_stack):
            if isinstance(scope, self.__generator.Document):
                include_dir_paths.append(os.path.dirname(scope.path))
                break

        include_file_relpath = tokens[1]
        for include_dir_path in include_dir_paths:
            include_file_path = os.path.join(include_dir_path, include_file_relpath)
            if os.path.exists(include_file_path):
                include_file_path = os.path.abspath(include_file_path)
                document = self.compile((include_file_path,))[0]
                if not include_file_relpath.startswith('thryft/generator/native_types/'):
                    include = \
                        self.__generator.Include(
                            document=document,
                            name=include_file_relpath,
                            parent=self.__scope_stack[-1],
                            path=include_file_relpath
                        )
                    return [include]
                else:
                    return []
        raise RuntimeError("include path not found: %s" % include_file_relpath)

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

    def _parse_service(self, tokens):
        service = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            service.functions.extend(tokens[1])

        return [service]

    def _parse_service_declarator(self, tokens):
        comment = self.__merge_comments(tokens)

        service = \
            self.__generator.Service(
                comment=comment,
                extends=len(tokens) > 2 and tokens[3] or None,
                name=tokens[1],
                parent=self.__scope_stack[-1]
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
            self.__generator.Typedef(
                comment=comment,
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
