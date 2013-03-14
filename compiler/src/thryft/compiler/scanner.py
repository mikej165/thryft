from spark import GenericScanner
from thryft.compiler.scan_exception import ScanException
from thryft.compiler.token import Token
import os.path


class Scanner(GenericScanner):
    def error(self, text, offset):
        colno, lineno = self.__find_offset(offset)
        raise ScanException(colno=colno, filename=self.__input_filename, lineno=lineno, offset=offset, text=text)

    def tokenize(self, input_):
        if isinstance(input_, file):
            self.__input = input_.read()
            self.__input_filename = input_.name
        elif isinstance(input_, str):
            if os.path.exists(input_):
                with open(input_, 'rb') as input_file:
                    self.__input = input_file.read()
                    self.__input_filename = input_
            else:
                self.__input = input_
                self.__input_filename = '<string>'
        else:
            raise TypeError(type(input_))

        self.__input_lines = self.__input.splitlines()

        self.__output_tokens = []

        GenericScanner.tokenize(self, self.__input)

        self.__output_tokens.append(
            Token(
                colno=0,
                index=len(self.__output_tokens),
                input_=self.__input,
                input_filename=self.__input_filename,
                lineno=len(self.__input_lines),
                offset=len(self.__input),
                text='',
                type_=Token.Type.EOF
            )
        )

        return self.__output_tokens

    def __find_offset(self, offset):
        colno = offset
        for lineno, line in enumerate(self.__input_lines):
            if len(line) < colno:
                colno -= len(line)
            else:
                return colno, lineno + 1
        return colno, lineno + 1

    def t_alphanum_keywords(self, offset, text):
        r'i16|i32|i64'
        self.__t(offset, text, getattr(Token.Type, 'KEYWORD_' + text.upper()))

    def t_alphas(self, offset, text):
        r'[a-zA-Z]+'
        try:
            if text == text.lower():
                self.__t(offset, text, getattr(Token.Type, 'KEYWORD_' + text.upper()))
                return
        except AttributeError:
            pass
        self.__t(offset, text, Token.Type.ALPHAS)

    def t_asterisk(self, offset, text):
        r'\*'
        self.__t(offset, text, Token.Type.ASTERISK)

    def t_colon(self, offset, text):
        r':'
        self.__t(offset, text, Token.Type.COLON)

    def t_comma(self, offset, text):
        r','
        self.__t(offset, text, Token.Type.COMMA)

    def t_c_style_comment(self, offset, text):
        r'/\*(?:(.|[\r\n])*)\*/'
        self.__t(offset, text, Token.Type.COMMENT)

    def t_cpp_style_comment(self, offset, text):
        r'\/\/(\\\n|.)*'
        self.__t(offset, text, Token.Type.COMMENT)

    def t_default(self, offset, text):
        r'.+'
        raise NotImplementedError(offset, text)

    def t_digits(self, offset, text):
        r'\d+'
        self.__t(offset, text, Token.Type.DIGITS)

    def t_equals(self, offset, text):
        r'='
        self.__t(offset, text, Token.Type.EQUALS)

    def t_eol(self, offset, text):
        r'\n'
        pass
        # self.__t(offset, text, Token.Type.EOL)

    def t_left_angle_bracket(self, offset, text):
        r'\<'
        self.__t(offset, text, Token.Type.LEFT_ANGLE_BRACKET)

    def t_left_brace(self, offset, text):
        r'\{'
        self.__t(offset, text, Token.Type.LEFT_BRACE)

    def t_left_parenthesis(self, offset, text):
        r'\('
        self.__t(offset, text, Token.Type.LEFT_PARENTHESIS)

    def t_left_square_bracket(self, offset, text):
        r'\['
        self.__t(offset, text, Token.Type.LEFT_SQUARE_BRACKET)

    def t_period(self, offset, text):
        r'\.'
        self.__t(offset, text, Token.Type.PERIOD)

    def t_py_style_comment(self, offset, text):
        r'#.*'
        self.__t(offset, text, Token.Type.COMMENT)

    def t_quoted_string(self, offset, text):
        r'"(?:[^"\n\r\\]|(?:"")|(?:\\x[0-9a-fA-F]+)|(?:\\.))*"'
        self.__t(offset, text, Token.Type.QUOTED_STRING)

    def t_right_angle_bracket(self, offset, text):
        r'\>'
        self.__t(offset, text, Token.Type.RIGHT_ANGLE_BRACKET)

    def t_right_brace(self, offset, text):
        r'\}'
        self.__t(offset, text, Token.Type.RIGHT_BRACE)

    def t_right_parenthesis(self, offset, text):
        r'\)'
        self.__t(offset, text, Token.Type.RIGHT_PARENTHESIS)

    def t_right_square_bracket(self, offset, text):
        r'\]'
        self.__t(offset, text, Token.Type.RIGHT_SQUARE_BRACKET)

    def t_semicolon(self, offset, text):
        r';'
        self.__t(offset, text, Token.Type.SEMICOLON)

    def t_underscore(self, offset, text):
        r'_'
        self.__t(offset, text, Token.Type.UNDERSCORE)

    def t_whitespace(self, offset, text):
        r'[ \r\t]+'
        pass

    def __t(self, offset, text, type_):
        assert offset >= 0
        colno, lineno = self.__find_offset(offset)
        token = \
            Token(
                colno=colno,
                index=len(self.__output_tokens),
                input_=self.__input,
                input_filename=self.__input_filename,
                lineno=lineno,
                offset=offset,
                text=text,
                type_=type_
            )
        self.__output_tokens.append(token)
