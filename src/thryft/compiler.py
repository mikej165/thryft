from thryft.grammar import Grammar
from yutil import camelize
import argparse
import sys
import traceback


class Compiler(object):
    def __init__(self, target):
        def wrap_parse_action(parse_action):
            def wrapped_parse_action(tokens):
                try:
                    # print tokens
                    return parse_action(tokens)
                except:
                    print >> sys.stderr, 'Error parsing', tokens
                    traceback.print_exc()
                    raise
            return lambda tokens: wrapped_parse_action(tokens)

        self.__grammar = grammar = Grammar()
        self.__target = target
        self.__scope_stack = []
        self.__type_map = {}

        grammar.field.setParseAction(wrap_parse_action(self.__parse_field))

    def __call__(self, documents):
        for document in documents:
            while len(self.__scope_stack) > 0:
                self.__scope_stack.pop()
            self.__grammar.document.parseFile(document, parseAll=True)

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

    def __parse_field(self, tokens):
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
        assert len(tokens_copy) == 0

        return [self.__target.Field(
                   id=id,
                   name=name,
                   parent=None,
                   required=required,
                   type=type,
                   value=value
                )]

    def __resolve_type(self, type_name):
        try:
            return self.__type_map[type_name]
        except KeyError:
            if type_name in ('binary', 'bool', 'string'):
                return getattr(self.__target, type_name.capitalize() + 'Type')(type_name)
            elif type_name in ('byte', 'i16', 'i32', 'i64', 'double'):
                return self.__target.NumericType(type_name)
            else:
                raise



