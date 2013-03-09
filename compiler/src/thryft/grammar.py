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

from collections import OrderedDict
from decimal import Decimal
from pyparsing import alphas, alphanums, CaselessLiteral, Combine, \
    cppStyleComment, cStyleComment, delimitedList, Forward, Group, Keyword, Literal, \
    nums, Optional, QuotedString, pythonStyleComment, Word, ZeroOrMore, \
    ParserElement, lineEnd, lineno, col, Suppress, Empty, Regex, OneOrMore, White, \
    stringEnd
import sys
import traceback


class Grammar(object):
    '''
    Thrift grammar.

    Adapted from http://thrift.apache.org/docs/idl/.
    '''

    base_type_names = (
        'binary',
        'bool',
        'byte',
        'double',
        'float',
        'i16',
        'i32',
        'i64',
        'string'
    )

    def __init__(self, debug=False):
        def wrap_parse_action(parse_action):
            def wrapped_parse_action(tokens):
                try:
                    return parse_action(tokens)
                except:
                    print >> sys.stderr, 'Error parsing', tokens
                    traceback.print_exc()
                    raise
            return lambda tokens: wrapped_parse_action(tokens)

        # Basic definitions
        self.comment = (cppStyleComment ^ cStyleComment ^ pythonStyleComment).setName('comment')
        ws = Suppress(White()).setName('ws')
        optional_ws = Suppress(White() | Empty()).setName('optional_ws')
        construct_start = Empty()  # (ZeroOrMore(self.comment) + optional_ws).setName('construct_start')
        construct_end = ws | stringEnd  # (Suppress(ZeroOrMore(White(" \r\t"))) + ZeroOrMore(self.comment) + Suppress(ZeroOrMore(White(" \r\t"))) + lineEnd.suppress()).setName('construct_end')
        identifier = Word(alphas, alphanums + '._').setName('identifier')
        list_separator = (Literal(',') | Literal(';')).setName('list_separator')
        string_literal = (QuotedString('\'') ^ QuotedString('"')).setName('string_literal')

        # Constant Values
        int_constant = \
            (Combine(CaselessLiteral('0x') + Word(nums + 'abcdefABCDEF')).\
                setParseAction(wrap_parse_action(lambda tokens: [int(tokens[0], 16)])) | \
            Word(nums + '+-', nums).\
                setParseAction(wrap_parse_action(lambda tokens: [int(tokens[0])]))).setName('int_constant')
        double_constant = \
            Combine(Word(nums + '+-', nums) + '.' + Word(nums) + Optional(CaselessLiteral('E') + Word(nums + '+-', nums))).\
                setName('double_constant').setParseAction(wrap_parse_action(lambda tokens: [Decimal(tokens[0])]))
        const_list = Forward().setName('const_list')
        const_map = Forward().setName('const_map')
        const_value = \
            double_constant ^ \
            int_constant ^ \
            string_literal ^ \
            identifier ^ \
            const_list ^ \
            const_map
        const_list << \
            (Literal('[').suppress() + optional_ws + \
                Group(delimitedList(const_value, optional_ws + list_separator + optional_ws)) + \
            Literal(']').suppress())
        const_map << \
            (Literal('{').suppress() + optional_ws + \
                Optional(delimitedList(
                    Group(const_value + optional_ws + Literal(':').suppress() + optional_ws + const_value),
                    optional_ws + list_separator
                )) + \
            Literal('}').suppress())
        const_map.setParseAction(
            wrap_parse_action(lambda tokens: [OrderedDict(tuple(item)
                                              for item in tokens)])
        )

        # Types
        field_type = Forward().setName('field_type')
        self.base_type = Keyword(self.base_type_names[0])
        for base_type_name in self.base_type_names[1:]:
            self.base_type ^= Keyword(base_type_name)
        self.base_type.setName('base_type')
        self.map_type = \
            (Keyword('map') + optional_ws + Literal('<').suppress() + optional_ws + \
                field_type + optional_ws + \
                Literal(',').suppress() + optional_ws + \
                field_type + optional_ws + \
            Literal('>').suppress()).setName('map_type')
        self.list_type = \
            (Keyword('list') + optional_ws + Literal('<').suppress() + optional_ws + \
                field_type + optional_ws + \
             Literal('>').suppress()).setName('list_type')
        self.set_type = \
            (Keyword('set') + optional_ws + Literal('<').suppress() + optional_ws + \
                field_type + optional_ws + \
             Literal('>').suppress()).setName('set_type')
        container_type = self.list_type ^ self.map_type ^ self.set_type
        field_type << (self.base_type ^ container_type ^ identifier)

        # Thrift Include
        self.include = (construct_start + Keyword('include') + ws + string_literal + construct_end).setName('include')

        # Namespace
        namespace_scope = (Keyword('*') ^ Keyword('java') ^ Keyword('py')).setName('namespace_scope')
        self.namespace = (construct_start + Keyword('namespace') + ws + namespace_scope + ws + identifier + construct_end).setName('namespace')

        # Field
        self.field = \
            (Optional(int_constant + optional_ws + Literal(':').suppress() + optional_ws) + \
             Optional(
                 (Keyword('required') ^ Keyword('optional')).\
                     setParseAction(
                         wrap_parse_action(lambda tokens: [tokens[0] == 'required'])
                     ) + ws
             ) + \
             field_type + ws + identifier + optional_ws + \
             Optional(Literal('=').suppress() + optional_ws + const_value)).setName('field')
        self.compound_type_field = (self.field + optional_ws + Optional(list_separator).suppress() + construct_end).setName('compound_type_field')

        # Functions
        self.function_declarator = \
            (construct_start + \
             Optional(Keyword('oneway') + ws) + \
             (Keyword('void') ^ field_type) + ws + \
             identifier).setName('function_declarator')
        self.function = \
            (self.function_declarator + optional_ws + Literal('(').suppress() + optional_ws + \
                 Optional(Group(delimitedList(self.field, optional_ws + Literal(',') + optional_ws))) + optional_ws + \
             Literal(')').suppress() + optional_ws + \
             Optional(
                 Keyword('throws') + ws + Literal('(').suppress() + optional_ws + \
                     Group(delimitedList(self.field, optional_ws + list_separator + optional_ws)) + optional_ws + \
                 Literal(')').suppress() + optional_ws
             ) + Optional(list_separator).suppress() + construct_end).setName('function')

        # Header
        header = self.include ^ self.namespace
        header.setName('header')

        # Definition
        # Const
        self.const = \
            (construct_start + \
             Keyword('const') + ws + \
                 field_type + ws + \
                 identifier + optional_ws + \
                 Literal('=').suppress() + optional_ws + const_value + optional_ws + \
                 Optional(list_separator).suppress() + construct_end).setName('const')
        # Typedef
        self.typedef = \
            (construct_start + \
                 Keyword('typedef') + ws + \
                     (self.base_type ^ container_type) + ws + \
                     identifier + \
                 construct_end).setName('typedef')
        # Enum
        self.enum_declarator = \
            (construct_start + \
             Keyword('enum') + ws + identifier).setName('enum_declarator')
        self.enumerator = \
            (construct_start + \
                 identifier + optional_ws + \
                     Optional(Literal('=').suppress() + optional_ws + int_constant + optional_ws) + \
                     Optional(list_separator).suppress() + \
                 construct_end).setName('enumerator')
        self.enum = \
            (self.enum_declarator + optional_ws + Literal('{').suppress() + ws + \
                 Group(ZeroOrMore(
                     self.enumerator
                 )) + \
             Literal('}').suppress() + construct_end).setName('enum')
        # Struct
        self.struct_declarator = (construct_start + Keyword('struct') + ws + identifier).setName('struct_declarator')
        struct_body = \
            optional_ws + \
            Literal('{').suppress() + optional_ws + \
                 Group(ZeroOrMore(
                     self.compound_type_field
                 )) + optional_ws + \
                 Literal('}').suppress() + construct_end
        self.struct = \
            (self.struct_declarator + struct_body).setName('struct')
        # Exception
        self.exception_declarator = (construct_start + Keyword('exception') + ws + identifier).setName('exception_declarator')
        self.exception = (self.exception_declarator + struct_body).setName('exception')
        # Service
        self.service_declarator = \
            (# construct_start + \
             Keyword('service').suppress() + ws + identifier + \
                Optional(optional_ws + Keyword('extends') + ws + identifier)).setName('service_declarator')
#        self.service = \
#            (self.service_declarator + optional_ws + Literal('{').suppress() + optional_ws + \
#                 Group(ZeroOrMore(
#                     self.function
#                 )) + optional_ws + \
#             Literal('}').suppress() + construct_end).setName('service')
        self.service = \
            (self.service_declarator + ws + Literal('{').suppress() + optional_ws + \
                Group(ZeroOrMore(optional_ws + self.function + optional_ws)) + \
             Literal('}').suppress()).setName('service')
        definition = \
            self.const ^ \
            self.typedef ^ \
            self.enum ^ \
            self.struct ^ \
            self.exception ^ \
            self.service
        definition.setName('definition')

        # Document
        self.document = \
            optional_ws + \
            ZeroOrMore(header) + \
            optional_ws + \
            OneOrMore(definition) + \
            optional_ws
        self.document.leaveWhitespace()  # Recursive
        self.document.setName('document')

        constructs = []
        for varsdict in (locals(), self.__dict__):
            constructs.extend(construct
                              for construct in varsdict.itervalues()
                              if isinstance(construct, ParserElement))

        if debug:
            def debugStart(instring, loc, expr):
                print ("Match " + str(expr) + " at loc " + str(loc) + "(%d,%d)" % (lineno(loc, instring), col(loc, instring)))
                pass

            def debugSuccess(instring, startloc, endloc, expr, toks):
                if len(toks.asList()) == 0:
                    return
                print ("Matched " + str(expr) + " -> " + str(toks.asList()))
                # print 'Matched ', str(toks.asList())

            def debugException(instring, loc, expr, exc):
                if exc is None:
                    return
                print ("Exception raised:" + str(exc))

            # Add debug actions to all of the parser elements defined above
            for construct in constructs:
                construct.setDebug(True)
                construct.setDebugActions(debugStart, debugSuccess, debugException)
