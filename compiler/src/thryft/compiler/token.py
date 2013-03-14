class Token(object):
    class Type(object):
        ALPHAS = None
        ASTERISK = None
        COMMA = None
        COMMENT = None
        DIGITS = None
        COLON = None
        EOF = None
        EOL = None
        EQUALS = None
        KEYWORD_CONST = None
        KEYWORD_ENUM = None
        KEYWORD_EXCEPTION = None
        KEYWORD_FALSE = None
        KEYWORD_INCLUDE = None
        KEYWORD_LIST = None
        KEYWORD_MAP = None
        KEYWORD_NAMESPACE = None
        KEYWORD_ONEWAY = None
        KEYWORD_OPTIONAL = None
        KEYWORD_REQUIRED = None
        KEYWORD_SERVICE = None
        KEYWORD_SET = None
        KEYWORD_STRUCT = None
        KEYWORD_THROWS = None
        KEYWORD_TYPEDEF = None
        KEYWORD_TRUE = None
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
        return "%s(colno=%u, index=%u, input_filename=%s, lineno=%u, offset=%u, text='%s', type=%s)" % (self.__class__.__name__, self.colno, self.index, self.input_filename, self.lineno, self.offset, self.text, self.type)

    def __str__(self):
        return self.text
