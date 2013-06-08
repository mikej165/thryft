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

from thryft.compiler.scan_exception import ScanException
from thryft.compiler.token import Token
from yutil import class_qname
import logging
import os.path
import re


class Scanner(object):
    __PATTERNS = [
        [re.compile(r'(/\*[^*]*\*+(?:[^/*][^*]*\*+)*/)', re.DOTALL | re.MULTILINE), Token.Type.COMMENT],
        [r'\*', Token.Type.ASTERISK],
        [r':', Token.Type.COLON],
        [r',', Token.Type.COMMA],
        [r'\/\/(\\\n|.)*', Token.Type.COMMENT],
        [r'=', Token.Type.EQUALS],
        [r'\n', Token.Type.EOL],
        [r'[-+]?[0-9]+\.[0-9]+([eE][-+]?[0-9]+)?', Token.Type.FLOAT_LITERAL],
    ]
    __PATTERNS.extend([
        [r'[a-zA-Z][a-zA-Z0-9_]*', Token.Type.IDENTIFIER],
        [r'[-+]?[0-9]+', Token.Type.INT_LITERAL],
        [r'\<', Token.Type.LEFT_ANGLE_BRACKET],
        [r'\{', Token.Type.LEFT_BRACE],
        [r'\(', Token.Type.LEFT_PARENTHESIS],
        [r'\[', Token.Type.LEFT_SQUARE_BRACKET],
        [r'\.', Token.Type.PERIOD],
        [r'#.*', Token.Type.COMMENT],
        [r'"(?:[^"\n\r\\]|(?:"")|(?:\\x[0-9a-fA-F]+)|(?:\\.))*"' , Token.Type.QUOTED_STRING],
        [r'\>', Token.Type.RIGHT_ANGLE_BRACKET],
        [r'\}' , Token.Type.RIGHT_BRACE],
        [r'\)', Token.Type.RIGHT_PARENTHESIS],
        [r'\]', Token.Type.RIGHT_SQUARE_BRACKET],
        [r';', Token.Type.SEMICOLON],
        [r'_', Token.Type.UNDERSCORE],
        [r'[ \r\t]+', Token.Type.WS],
    ])
    for __pattern_i in xrange(len(__PATTERNS)):
        __pattern = __PATTERNS[__pattern_i]
        if isinstance(__pattern[0], str):
            __pattern[0] = re.compile('(' + __pattern[0] + ')')
        __PATTERNS[__pattern_i] = tuple(__pattern)
    __PATTERNS = tuple(__PATTERNS)

    def tokenize(self, input_):
        if isinstance(input_, file):
            input_ = input_.read()
            input_filename = input_.name
        elif isinstance(input_, str):
            if os.path.exists(input_):
                with open(input_, 'rb') as input_file:
                    input_ = input_file.read()
                    input_filename = input_file.name
            else:
                input_ = input_
                input_filename = '<string>'
        else:
            raise TypeError(type(input_))

        input_lines = input_.splitlines()

        logger = logging.getLogger(class_qname(self))
        logger.debug("tokenizing " + input_filename)

        output = []

        offset = 0
        input_len = len(input_)
        patterns = self.__PATTERNS
        while offset < input_len:
            for pattern in patterns:
                match = pattern[0].match(input_, offset)
                if match is None:
                    continue

                colno = match.start(1)
                for lineno, line in enumerate(input_lines):
                    if len(line) < colno:
                        colno -= len(line)
                    else:
                        break

                token_offset = match.start(1)
                token_text = match.group(1)
                token_type = pattern[1]
                if token_type == Token.Type.IDENTIFIER:
                    if token_text.islower():
                        try:
                            token_type = getattr(Token.Type, 'KEYWORD_' + token_text.upper())
                        except AttributeError:
                            pass
                token = \
                    Token(
                        colno=colno,
                        index=len(output),
                        input_=input_,
                        input_filename=input_filename,
                        lineno=lineno,
                        offset=token_offset,
                        text=token_text,
                        type_=token_type
                    )
                logger.debug(repr(token))
                output.append(token)

                offset = match.end()

                break

            if match is None:
                colno = offset
                for lineno, line in enumerate(input_lines):
                    if len(line) < colno:
                        colno -= len(line)
                    else:
                        break
                raise ScanException(colno=colno, filename=input_filename, lineno=lineno, offset=offset, text=input_)

        output.append(
            Token(
                colno=0,
                index=len(output),
                input_=input_,
                input_filename=input_filename,
                lineno=len(input_lines),
                offset=len(input_),
                text='',
                type_=Token.Type.EOF
            )
        )

        return output
