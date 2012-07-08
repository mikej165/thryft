from thryft.target.construct import Construct


class Service(Construct):
    def __init__(self, name, parent, extends=None, functions=None):
        Construct.__init__(self, name=name, parent=parent)
        self.__extends = extends
        self.__functions = functions is not None and list(functions) or []

    @property
    def extends(self):
        return self.__extends

    @property
    def functions(self):
        return self.__functions

    @property
    def qname(self):
        return self.parent.name + '.' + self.name
