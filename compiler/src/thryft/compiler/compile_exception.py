class CompileException(Exception):
    def __init__(self, message, ast_node=None):
        if ast_node is not None:
            message = "%s at %s" % (message, repr(ast_node.start_token))
        Exception.__init__(self, message)
        self.__ast_node = ast_node

    @property
    def ast_node(self):
        return self.__ast_node
