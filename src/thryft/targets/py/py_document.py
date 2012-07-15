from thryft.target.document import Document
from thryft.targets.py.py_construct import PyConstruct
from yutil import rpad


class PyDocument(Document, PyConstruct):
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
