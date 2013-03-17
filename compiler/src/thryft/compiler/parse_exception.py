from thryft.compiler.token import Token


class ParseException(Exception):
    def __init__(self, message, token=None):
        if token is not None:
            assert isinstance(token, Token)
            message = "%s at %s" % (message, repr(token))
        Exception.__init__(self, message)
        self.__token = token

    @property
    def token(self):
        return self.__token
