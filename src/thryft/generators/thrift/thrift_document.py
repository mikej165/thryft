from thryft.generator.document import Document
from thryft.generator.include import Include
from thryft.generator.namespace import Namespace
from yutil import rpad


class ThriftDocument(Document):
    def __repr__(self):
        includes = [header for header in self.headers
                    if isinstance(header, Include)]
        namespaces = [header for header in self.headers
                      if isinstance(header, Namespace)]

        return rpad("\n".join([repr(include) for include in includes]), "\n") + \
               rpad("\n".join([repr(namespace) for namespace in namespaces]), "\n") + \
               "\n\n".join([repr(definition) for definition in self.definitions])
