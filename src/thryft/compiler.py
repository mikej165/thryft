from thryft.grammar import Grammar
from thryft.target.type import Type
from yutil import camelize
import argparse
import sys
import traceback


class Compiler(object):
    def __init__(self, target):
        object.__init__(self)

        self.__grammar = grammar = Grammar()
        self.__target = target
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

    def __call__(self, file_paths):
        for file_path in file_paths:
            document = self.__target.Document(path=file_path)
            self.__scope_stack.append(document)

            self.__grammar.document.parseFile(file_path, parseAll=True)

            self.__scope_stack.pop(-1)

    @classmethod
    def main(cls):
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument(
            '--gen',
            dest='target',
            help='generator/target name',
            required=True
        )
        argument_parser.add_argument(
            'files',
            nargs='+',
            type=argparse.FileType
        )
        args = argument_parser.parse_args()

        target_module_name = 'thryft.targets.' + args.target + '_target'
        target_module = __import__(target_module_name)
        for module_name in target_module_name.split('.')[1:]:
            target_module = getattr(module_name, target_module)
        target_class_name = camelize(args.target) + 'Target'
        target_class = getattr(target_module, target_class_name)
        target = target_class()

        cls(target)(args.files)

    def __parse_compound_type_declarator(self, keyword, tokens):
        compound_type = \
            getattr(self.__target, keyword.capitalize())(
                name=tokens[1],
                parent=self.__scope_stack[-1]
            )

        self.__scope_stack.append(compound_type)

        return [compound_type]

    def __parse_compound_type(self, keyword, tokens):
        compound_type = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            for field in tokens[1]:
                compound_type.fields.append(field)

        self.__type_map[compound_type.qname] = compound_type

        return [compound_type]

    def _parse_const(self, tokens):
        const = \
            self.__target.Const(
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
                    self.__target.Field(
                        id=token_i,
                        name=token[0],
                        parent=enum,
                        type=type_,
                        value=value
                    )
                )

        return [enum]

    def _parse_exception_declarator(self, tokens):
        return self.__parse_compound_type_declarator('exception', tokens)

    def _parse_exception(self, tokens):
        return self.__parse_compound_type('exception', tokens)

    def _parse_field(self, tokens):
        tokens_copy = list(tokens)
        if isinstance(tokens_copy[0], int):
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
            self.__target.Field(
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
            self.__target.Function(
                name=name,
                oneway=oneway,
                parent=parent,
                return_type=return_type
            )

        self.__scope_stack.append(function)

        return [function]

    def _parse_function(self, tokens):
        function = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            function.parameters.extend(tokens[1])

        if len(tokens) > 2:
            function.throws.extend(tokens[2])

        return [function]

    def _parse_include(self, tokens):
        include = \
            self.__target.Include(
                name=tokens[1],
                parent=self.__scope_stack[-1],
                path=tokens[1]
            )
        return [include]

    def _parse_list_type(self, tokens):
        return self.__parse_sequence_type('list', tokens)

    def _parse_map_type(self, tokens):
        key_type = self.__resolve_type(tokens[1])
        value_type = self.__resolve_type(tokens[2])
        map_type = \
            self.__target.MapType(
                key_type=key_type,
                name="map<%s, %s>" % (key_type.qname, value_type.qname),
                parent=self.__scope_stack[-1],
                value_type=value_type
            )
        return [map_type]

    def _parse_namespace(self, tokens):
        namespace = \
            self.__target.Namespace(
                name=tokens[2],
                parent=self.__scope_stack[-1],
                scope=tokens[1]
            )
        return [namespace]

    def _parse_senum_declarator(self, tokens):
        return self.__parse_compound_type_declarator('senum', tokens)

    def _parse_senum(self, tokens):
        senum = tokens[0]
        self.__scope_stack.pop(-1)

        if len(tokens) > 1:
            type_ = self.__resolve_type('string')
            for token_i, token in enumerate(tokens[1]):
                senum.fields.append(
                    self.__target.Field(
                        id=token_i,
                        name=token,
                        parent=senum,
                        type=type_
                    )
                )

        return [senum]

    def __parse_sequence_type(self, keyword, tokens):
        assert tokens[0] == keyword
        element_type = self.__resolve_type(tokens[1])
        sequence_type = \
            getattr(self.__target, keyword.capitalize() + 'Type')(
                element_type=element_type,
                name="%s<%s>" % (keyword, element_type.qname),
                parent=self.__scope_stack[-1]
            )
        return [sequence_type]

    def _parse_service_declarator(self, tokens):
        service = \
            self.__target.Service(
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
            self.__target.Typedef(
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
            if type_name in ('binary', 'bool', 'string'):
                return getattr(self.__target, type_name.capitalize() + 'Type')(name=type_name)
            elif type_name in ('byte', 'i16', 'i32', 'i64', 'double'):
                return self.__target.NumericType(type_name)
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
                print >> sys.stderr, 'Parsing', tokens, \
                    'with', parse_action,
                out_tokens = parse_action(tokens)
                print >> sys.stderr, '->', out_tokens
                return out_tokens
            except:
                print >> sys.stderr, 'Error parsing', tokens, \
                    'with', parse_action
                traceback.print_exc()
                raise
        return lambda tokens: wrapped_parse_action(tokens)
