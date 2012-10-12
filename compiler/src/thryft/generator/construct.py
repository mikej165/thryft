class Construct(object):
    def __init__(self, parent, comment=None, **kwds):
        object.__init__(self)
        self._comment = comment
        self.__parent = parent

    @property
    def comment(self):
        return self._comment

    @property
    def parent(self):
        return self.__parent

    def __repr__(self):
        raise NotImplementedError('.'.join((
                  self.__class__.__module__,
                  self.__class__.__name__,
                  '__repr__'
              )))
