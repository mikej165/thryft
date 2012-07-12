from thryft.target.document import Document
from yutil import rpad


class PyDocument(Document):
    def __repr__(self):
        imports = []
        for definition in self.definitions:
            if hasattr(definition, 'py_imports'):
                imports.extend(definition.py_imports())
        imports = "\n".join(imports)

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])
        return rpad(imports, "\n\n\n") + definitions + "\n"
