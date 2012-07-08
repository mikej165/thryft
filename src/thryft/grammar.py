from collections import OrderedDict
from decimal import Decimal
from pyparsing import alphas, alphanums, CaselessLiteral, Combine, \
    cppStyleComment, cStyleComment, delimitedList, Forward, Group, Keyword, Literal, \
    nums, Optional, pythonStyleComment, quotedString, Word, ZeroOrMore
import sys
import traceback


class Grammar(object):
    '''
    Thrift grammar.

    Adapted from http://thrift.apache.org/docs/idl/.
    '''

    def __init__(self):
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

        # Basic definitions
        # literal = quotedString
        identifier = Word(alphas, alphanums)
        list_separator = Literal(',') | Literal(';')

        # Constant Values
        int_constant = \
            Combine(CaselessLiteral('0x') + Word(nums + 'abcdefABCDEF')).\
                setParseAction(wrap_parse_action(lambda tokens: [int(tokens[0], 16)])) | \
            Word(nums + '+-', nums).\
                setParseAction(wrap_parse_action(lambda tokens: [int(tokens[0])]))
        double_constant = \
            Combine(Word(nums + '+-', nums) + '.' + Word(nums) + Optional(CaselessLiteral('E') + Word(nums + '+-', nums))).\
                setParseAction(wrap_parse_action(lambda tokens: [Decimal(tokens[0])]))
        const_list = Forward()
        const_map = Forward()
        const_value = \
            double_constant ^ \
            int_constant ^ \
            quotedString ^ \
            identifier ^ \
            const_list ^ \
            const_map
        const_list << \
            (Literal('[').suppress() + \
                Group(delimitedList(const_value, list_separator)) + \
            Literal(']').suppress())
        const_map << \
            (Literal('{').suppress() + \
                Optional(delimitedList(
                    Group(const_value + Literal(':').suppress() + const_value),
                    list_separator
                )) + \
            Literal('}').suppress())
        const_map.setParseAction(
            wrap_parse_action(lambda tokens: [OrderedDict(tuple(item)
                                              for item in tokens)])
        )

        # Types
        field_type = Forward()
        self.base_type = \
            Keyword('binary') ^ \
            Keyword('bool') ^ \
            Keyword('byte') ^ \
            Keyword('double') ^ \
            Keyword('i16') ^ \
            Keyword('i32') ^ \
            Keyword('i64') ^ \
            Keyword('slist') ^ \
            Keyword('string')
        self.map_type = \
            Keyword('map') + Literal('<').suppress() + \
                field_type + \
                Literal(',').suppress() + \
                field_type + \
            Literal('>').suppress()
        self.list_type = \
            Keyword('list') + Literal('<').suppress() + \
                field_type + \
            Literal('>').suppress()
        self.set_type = \
            Keyword('set') + Literal('<').suppress() + \
                field_type + \
            Literal('>').suppress()
        container_type = self.list_type ^ self.map_type ^ self.set_type
        field_type << (self.base_type ^ container_type ^ identifier)

        # Thrift Include
        self.include = Keyword('include') + quotedString

        # Namespace
        namespace_scope = Keyword('*') ^ Keyword('java') ^ Keyword('py')
        self.namespace = Keyword('namespace') + namespace_scope + identifier

        # Field
        self.field = \
            Optional(int_constant + Literal(':').suppress()) + \
            Optional(
                (Keyword('required') ^ Keyword('optional')).\
                    setParseAction(
                        wrap_parse_action(lambda tokens: [tokens[0] == 'required'])
                    )
            ) + \
            field_type + identifier + \
            Optional(Literal('=').suppress() + const_value)

        # Functions
        self.function_declarator = \
            Optional(Keyword('oneway')) + \
            (Keyword('void') ^ field_type) + \
            identifier
        self.function = \
            self.function_declarator + Literal('(').suppress() + \
                Optional(Group(delimitedList(self.field))) + \
            Literal(')').suppress() + \
            Optional(
                Keyword('throws').suppress() + Literal('(').suppress() + \
                    Group(delimitedList(self.field, list_separator)) + \
                Literal(')').suppress()
            )

        # Header
        header = self.include ^ self.namespace

        # Definition
        # Const
        self.const = \
            Keyword('const') + field_type + identifier + \
                Literal('=').suppress() + const_value + \
                Optional(list_separator).suppress()
        # Typedef
        self.typedef = \
            Keyword('typedef') + (self.base_type ^ container_type) + identifier
        # Enum
        self.enum_declarator = Keyword('enum') + identifier
        self.enum = \
            self.enum_declarator + Literal('{').suppress() + \
                Optional(Group(delimitedList(
                    Group(identifier + \
                        Optional(Literal('=').suppress() + int_constant)),
                    list_separator
                ))) + \
            Literal('}').suppress()
        # Senum
        self.senum_declarator = Keyword('senum') + identifier
        self.senum = \
            self.senum_declarator + Literal('{').suppress() + \
                Optional(delimitedList(quotedString, list_separator)) + \
            Literal('}').suppress()
        # Struct
        self.struct_declarator = Keyword('struct') + identifier
        self.struct = \
            self.struct_declarator + Literal('{').suppress() + \
                Group(ZeroOrMore(
                    self.field + Optional(list_separator).suppress()
                )) + \
                Literal('}').suppress()
        # Exception
        self.exception_declarator = Keyword('exception') + identifier
        self.exception = \
            self.exception_declarator + Literal('{').suppress() + \
                Group(ZeroOrMore(
                    self.field + Optional(list_separator).suppress()
                )) + \
            Literal('}').suppress()
        # Service
        self.service_declarator = \
            Keyword('service') + identifier + \
                Optional(Keyword('extends') + identifier)
        self.service = \
            self.service_declarator + Literal('{').suppress() + \
                Group(ZeroOrMore(
                    self.function + Optional(list_separator).suppress()
                )) + \
            Literal('}').suppress()
        definition = \
            self.const ^ \
            self.typedef ^ \
            self.enum ^ \
            self.senum ^ \
            self.struct ^ \
            self.exception ^ \
            self.service

        # Document
        self.document = \
            Group(ZeroOrMore(header)) + Group(ZeroOrMore(definition))
        self.document.ignore(cStyleComment)
        self.document.ignore(cppStyleComment)
        self.document.ignore(pythonStyleComment)
