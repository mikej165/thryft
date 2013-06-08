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

class Token(object):
    class Type(object):
        ASTERISK = None
        COMMA = None
        COMMENT = None
        COLON = None
        EOF = None
        EOL = None
        EQUALS = None
        FLOAT_LITERAL = None
        IDENTIFIER = None
        INT_LITERAL = None
        KEYWORD_BINARY = None
        KEYWORD_BOOL = None
        KEYWORD_BYTE = None
        KEYWORD_CONST = None
        KEYWORD_DOUBLE = None
        KEYWORD_ENUM = None
        KEYWORD_EXCEPTION = None
        KEYWORD_FALSE = None
        KEYWORD_I16 = None
        KEYWORD_I32 = None
        KEYWORD_I64 = None
        KEYWORD_INCLUDE = None
        KEYWORD_LIST = None
        KEYWORD_MAP = None
        KEYWORD_NAMESPACE = None
        KEYWORD_ONEWAY = None
        KEYWORD_OPTIONAL = None
        KEYWORD_REQUIRED = None
        KEYWORD_SERVICE = None
        KEYWORD_SET = None
        KEYWORD_STRING = None
        KEYWORD_STRUCT = None
        KEYWORD_THROWS = None
        KEYWORD_TYPEDEF = None
        KEYWORD_TRUE = None
        KEYWORD_VOID = None
        LEFT_ANGLE_BRACKET = None
        LEFT_BRACE = None
        LEFT_PARENTHESIS = None
        LEFT_SQUARE_BRACKET = None
        PERIOD = None
        QUOTED_STRING = None
        RIGHT_ANGLE_BRACKET = None
        RIGHT_BRACE = None
        RIGHT_PARENTHESIS = None
        RIGHT_SQUARE_BRACKET = None
        SEMICOLON = None
        UNDERSCORE = None
        WS = None

    for __attr in dir(Type):
        if __attr[0] == '_' or __attr != __attr.upper():
            continue
        value = getattr(Type, __attr)
        if value is not None:
            continue
        setattr(Type, __attr, __attr)

    def __init__(self, colno, index, input_, input_filename, lineno, offset, text, type_):
        object.__init__(self)

        assert isinstance(colno, int) and colno >= 0, colno
        self.__colno = colno

        assert isinstance(index, int) and index >= 0, index
        self.__index = index

        assert isinstance(input_, str)
        self.__input = input_

        assert isinstance(input_filename, str) and len(input_filename) > 0
        self.__input_filename = input_filename

        assert isinstance(lineno, int) and lineno >= 0, lineno
        self.__lineno = lineno

        assert isinstance(offset, int) and offset >= 0, offset
        self.__offset = offset

        assert isinstance(text, str)
        self.__text = text

        assert isinstance(type_, str) and len(type_) > 0
        self.__type = type_

    def __cmp__(self, other):
        return cmp(self.type, other)

    @property
    def colno(self):
        return self.__colno

    @property
    def index(self):
        return self.__index

    @property
    def input_filename(self):
        return self.__input_filename

    @property
    def lineno(self):
        return self.__lineno

    @property
    def offset(self):
        return self.__offset

    @property
    def text(self):
        return self.__text

    @property
    def type(self):
        return self.__type

    def __repr__(self):
        dict_ = self.to_dict()
        repr_ = []
        for key in sorted(dict_.iterkeys()):
            value = dict_[key]
            if isinstance(value, str):
                value = "'" + value + "'"
            repr_.append("%(key)s=%(value)s" % locals())
        return "%s(%s)" % (self.__class__.__name__, ', '.join(repr_))

    def __str__(self):
        return self.text

    def to_dict(self):
        dict_ = {}
        for attr in dir(self):
            if attr[0] == '_' or attr[0] != attr[0].lower() or attr == 'to_dict':
                continue
            value = getattr(self, attr)
            dict_[attr] = value
        return dict_
