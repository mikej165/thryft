from thryft.generator._construct import _Construct


class Comment(_Construct):
    def __init__(self, parent, text):
        _Construct.__init__(self, parent=parent)
        self.__text = text

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return self.text
