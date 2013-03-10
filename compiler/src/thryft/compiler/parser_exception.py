from thryft.compiler.token import Token


class ParserException(Exception):
    def __init__(self, token):
        Exception.__init__(self, repr(token))
        if not isinstance(token, Token):
            raise TypeError(type(token))
        self.__token = token

    @property
    def token(self):
        return self.__token
