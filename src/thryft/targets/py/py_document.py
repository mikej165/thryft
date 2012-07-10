from thryft.target.document import Document
from yutil import rpad


class PyDocument(Document):
    def __repr__(self):
#        includes = "\n".join([repr(include)
#                              for include in self.includes
#                              if not include.is_native])
        includes = ''
        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])
        return rpad(includes, "\n\n\n") + definitions + "\n"
