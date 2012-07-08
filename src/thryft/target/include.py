from thryft.target.construct import Construct


class Include(Construct):
    def __init__(self, name, parent, path):
        Construct.__init__(self, name=name, parent=parent)
        self.__path = path

    @property
    def path(self):
        return self.__path
