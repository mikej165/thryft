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
    nums, Optional, QuotedString, pythonStyleComment, Word, ZeroOrMore
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

    def __init__(self):
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
        self.comment = cppStyleComment ^ cStyleComment ^ pythonStyleComment
        string_literal = QuotedString('\'') ^ QuotedString('"')
        identifier = Word(alphas, alphanums + '._')
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
            string_literal ^ \
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
        self.base_type = Keyword(self.base_type_names[0])
        for base_type_name in self.base_type_names[1:]:
            self.base_type ^= Keyword(base_type_name)
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
        self.include = Keyword('include') + string_literal

        # Namespace
        namespace_scope = Keyword('*') ^ Keyword('java') ^ Keyword('py')
        self.namespace = Keyword('namespace') + namespace_scope + identifier

        # Field
        self.field = \
            ZeroOrMore(self.comment) + \
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
            ZeroOrMore(self.comment) + \
            Optional(Keyword('oneway')) + \
            (Keyword('void') ^ field_type) + \
            identifier
        self.function = \
            self.function_declarator + Literal('(').suppress() + \
                Optional(Group(delimitedList(self.field))) + \
            Literal(')').suppress() + \
            Optional(
                Keyword('throws') + Literal('(').suppress() + \
                    Group(delimitedList(self.field, list_separator)) + \
                Literal(')').suppress()
            )

        # Header
        header = self.include ^ self.namespace

        # Definition
        # Const
        self.const = \
            ZeroOrMore(self.comment) + \
            Keyword('const') + field_type + identifier + \
                Literal('=').suppress() + const_value + \
                Optional(list_separator).suppress()
        # Typedef
        self.typedef = \
            ZeroOrMore(self.comment) + \
            Keyword('typedef') + (self.base_type ^ container_type) + identifier
        # Enum
        self.enum_declarator = \
            ZeroOrMore(self.comment) + \
            Keyword('enum') + identifier
        self.enumerator = \
            ZeroOrMore(self.comment) + \
                identifier + \
                    Optional(Literal('=').suppress() + int_constant)
        self.enum = \
            self.enum_declarator + Literal('{').suppress() + \
                Group(ZeroOrMore(
                    self.enumerator + Optional(list_separator).suppress()
                )) + \
            Literal('}').suppress()
        # Struct
        self.struct_declarator = \
            ZeroOrMore(self.comment) + \
            Keyword('struct') + identifier
        self.struct = \
            self.struct_declarator + Literal('{').suppress() + \
                Group(ZeroOrMore(
                    self.field + Optional(list_separator).suppress()
                )) + \
                Literal('}').suppress()
        # Exception
        self.exception_declarator = \
            ZeroOrMore(self.comment) + \
            Keyword('exception') + identifier
        self.exception = \
            self.exception_declarator + Literal('{').suppress() + \
                Group(ZeroOrMore(
                    self.field + Optional(list_separator).suppress()
                )) + \
            Literal('}').suppress()
        # Service
        self.service_declarator = \
            ZeroOrMore(self.comment) + \
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
            self.struct ^ \
            self.exception ^ \
            self.service

        # Document
        self.document = \
            ZeroOrMore(self.comment) + \
            Group(ZeroOrMore(header)) + \
            Group(ZeroOrMore(definition))
