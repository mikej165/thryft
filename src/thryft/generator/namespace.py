from thryft.generator.construct import Construct


class Namespace(Construct):
    def __init__(self, name, parent, scope=None):
        Construct.__init__(self, name=name, parent=parent)
        self.__scope = scope

    @property
    def scope(self):
        return self.__scope
