class ScannerException(Exception):
    def __init__(self, colno, filename, lineno, offset, text):
        Exception.__init__(self, "error scanning %(filename)s:%(lineno)u:%(colno)u: %(text)s" % locals())
        self.__colno = colno
        self.__filename = filename
        self.__lineno = lineno
        self.__offset = offset
        self.__text = text
