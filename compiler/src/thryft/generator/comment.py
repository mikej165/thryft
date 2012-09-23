from thryft.generator.construct import Construct


class Comment(Construct):
    def __init__(self, parent, text):
        Construct.__init__(self, parent=parent)
        self.__text = text

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return self.text
