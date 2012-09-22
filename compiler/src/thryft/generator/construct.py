class Construct(object):
    def __init__(self, name, parent, comment=None):
        self._comment = comment
        self.__name = name
        self.__parent = parent

    @property
    def comment(self):
        return self._comment

    @property
    def name(self):
        return self.__name

    @property
    def parent(self):
        return self.__parent

    @property
    def qname(self):
        return self.name

    def __repr__(self):
        raise NotImplementedError('.'.join((
                  self.__class__.__module__,
                  self.__class__.__name__,
                  '__repr__'
              )))
