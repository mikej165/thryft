from collections import OrderedDict
from decimal import Decimal
from pyparsing import alphas, alphanums, CaselessLiteral, Combine, \
    cppStyleComment, cStyleComment, delimitedList, Forward, Group, Literal, nums, \
    Optional, pythonStyleComment, quotedString, Word, ZeroOrMore
import sys
import traceback


__all__ = ['Grammar']


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
            Combine(CaselessLiteral('0x') + Word(nums + 'abcdefABCDEF')).setParseAction(wrap_parse_action(lambda tokens: [int(tokens[0], 16)])) | \
            Word(nums + '+-', nums).setParseAction(wrap_parse_action(lambda tokens: [int(tokens[0])]))
        self.double_constant = double_constant = \
            Combine(Word(nums + '+-', nums) + '.' + Word(nums) + Optional(CaselessLiteral('E') + Word(nums + '+-', nums))).\
                setParseAction(wrap_parse_action(lambda tokens: [Decimal(tokens[0])]))
        const_list = const_list = Forward()
        const_map = const_map = Forward()
        const_value = double_constant ^ int_constant ^ quotedString ^ identifier ^ const_list ^ const_map
        const_list << (Literal('[').suppress() + Group(delimitedList(const_value, list_separator)) + Literal(']').suppress())
        const_map << (Literal('{').suppress() + Optional(delimitedList(Group(const_value + Literal(':').suppress() + const_value), list_separator)) + Literal('}').suppress())
        const_map.setParseAction(wrap_parse_action(lambda tokens: [OrderedDict(tuple(item) for item in tokens)]))

        # Types
        field_type = Forward()
        self.base_type = base_type = Literal('bool') ^ 'byte' ^ 'i16' ^ 'i32' ^ 'i64' ^ 'double' ^ 'string' ^ 'binary' ^ 'slist'
        self.map_type = map_type = Literal('map').suppress() + Literal('<').suppress() + field_type + Literal(',').suppress() + field_type + Literal('>').suppress()
        self.list_type = list_type = Literal('list').suppress() + Literal('<').suppress() + field_type + Literal('>').suppress()
        self.set_type = set_type = Literal('set').suppress() + Literal('<').suppress() + field_type + Literal('>').suppress()
        container_type = map_type ^ list_type ^ set_type
        definition_type = base_type ^ container_type
        field_type << (base_type ^ container_type ^ identifier)

        # Thrift Include
        self.include = include = Literal('include').suppress() + quotedString

        # Namespace
        namespace_scope = Literal('*') ^ 'java' ^ 'py'
        self.namespace = namespace = Literal('namespace').suppress() + namespace_scope + identifier

        # Field
        field_id = int_constant + Literal(':').suppress()
        field_req = (Literal('required') ^ Literal('optional')).setParseAction(wrap_parse_action(lambda tokens: [tokens[0] == 'required']))
        self.field = field = Optional(field_id) + Optional(field_req) + field_type + identifier + Optional(Literal('=').suppress() + const_value)

        # Functions
        function_type = Literal('void') ^ field_type
        throws = Literal('throws').suppress() + Literal('(').suppress() + Group(delimitedList(field, list_separator)) + Literal(')').suppress()
        self.function = function = Optional(Literal('oneway')) + function_type + identifier + Literal('(').suppress() + Optional(Group(delimitedList(field))) + Literal(')').suppress() + Optional(throws)

        # Header
        header = include ^ namespace

        # Definition
        self.const = const = Literal('const').suppress() + field_type + identifier + Literal('=').suppress() + const_value + Optional(list_separator).suppress()
        self.typedef = typedef = Literal('typedef').suppress() + definition_type + identifier
        self.enum = enum = Literal('enum').suppress() + identifier + Literal('{').suppress() + Optional(delimitedList(identifier + Optional(Literal('=').suppress() + int_constant), list_separator)) + Literal('}').suppress()
        self.senum = senum = Literal('senum').suppress() + identifier + Literal('{').suppress() + Optional(delimitedList(quotedString, list_separator)) + Literal('}').suppress()
        self.struct = struct = Literal('struct').suppress() + identifier + Literal('{').suppress() + Group(ZeroOrMore(field + Optional(list_separator).suppress())) + Literal('}').suppress()
        self.exception = exception = Literal('exception').suppress() + identifier + Literal('{').suppress() + Group(ZeroOrMore(field + Optional(list_separator).suppress())) + Literal('}').suppress()
        self.service = service = Literal('service').suppress() + identifier + Optional(Literal('extends') + identifier) + Literal('{').suppress() + Group(ZeroOrMore(function + Optional(list_separator).suppress())) + Literal('}').suppress()
        definition = const ^ typedef ^ enum ^ senum ^ struct ^ exception ^ service

        # Document
        self.document = document = ZeroOrMore(header) + ZeroOrMore(definition)
        document.ignore(cStyleComment)
        document.ignore(cppStyleComment)
        document.ignore(pythonStyleComment)
