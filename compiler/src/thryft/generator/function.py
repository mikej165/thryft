from thryft.generator.construct import Construct


class Function(Construct):
    def __init__(
        self,
        oneway=False,
        parameters=None,
        return_type=None,
        throws=None,
        **kwds
    ):
        Construct.__init__(self, **kwds)
        self.__oneway = oneway
        self.__parameters = parameters is not None and list(parameters) or []
        self.__throws = throws is not None and list(throws) or []
        self.__return_type = return_type

    @property
    def oneway(self):
        return self.__oneway

    @property
    def parameters(self):
        return self.__parameters

    @property
    def return_type(self):
        return self.__return_type

    @property
    def throws(self):
        return self.__throws
