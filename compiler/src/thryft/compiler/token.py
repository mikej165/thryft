class Token(object):
    class Type(object):
        ALPHAS = None
        ASTERISK = None
        COMMA = None
        COMMENT = None
        DIGITS = None
        DOUBLE_QUOTE = None
        COLON = None
        EOF = None
        EOL = None
        EQUALS = None
        LEFT_ANGLE_BRACKET = None
        LEFT_BRACE = None
        LEFT_PARENTHESIS = None
        LEFT_SQUARE_BRACKET = None
        PERIOD = None
        RIGHT_ANGLE_BRACKET = None
        RIGHT_BRACE = None
        RIGHT_PARENTHESIS = None
        RIGHT_SQUARE_BRACKET = None
        SEMICOLON = None
        SINGLE_QUOTE = None
        UNDERSCORE = None

    for __attr in dir(Type):
        if __attr[0] == '_' or __attr != __attr.upper():
            continue
        value = getattr(Type, __attr)
        if value is not None:
            continue
        setattr(Type, __attr, __attr)

    def __init__(self, colno, input_, input_filename, lineno, offset, text, type_):
        object.__init__(self)

        if not isinstance(colno, int):
            raise TypeError(type(colno))
        if colno < 0:
            raise ValueError(colno)
        self.__colno = colno

        if not isinstance(input_, str):
            raise TypeError(type(input_))
        self.__input = input_

        if not isinstance(input_filename, str):
            raise TypeError(type(input_filename))
        if len(input_filename) == 0:
            raise ValueError(input_filename)
        self.__input_filename = input_filename

        if not isinstance(lineno, int):
            raise TypeError(type(lineno))
        if lineno < 0:
            raise ValueError(lineno)
        self.__lineno = lineno

        if not isinstance(offset, int):
            raise TypeError(type(offset))
        if offset < 0:
            raise ValueError(offset)
        self.__offset = offset

        if not isinstance(text, str):
            raise TypeError(type(text))
        self.__text = text

        if not isinstance(type_, str):
            raise TypeError(type(type_))
        self.__type = type_

    def __cmp__(self, other):
        return self.type is other.type

    @property
    def colno(self):
        return self.__colno

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
        return "%s(colno=%u, input_filename=%s, lineno=%u, offset=%u, text='%s', type=%s)" % (self.__class__.__name__, self.colno, self.input_filename, self.lineno, self.offset, self.text, self.type)

