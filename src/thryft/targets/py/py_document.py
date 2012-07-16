from thryft.target.document import Document
from thryft.targets.py.py_construct import PyConstruct
from yutil import rpad


class PyDocument(Document, PyConstruct):
    def __repr__(self):
        imports = []
        for include in self.includes:
            imports.append(str(include))
        for definition in self.definitions:
            imports.extend(definition.py_imports())
        imports = "\n".join(list(sorted(set(imports))))

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])
        return rpad(imports, "\n\n\n") + definitions + "\n"
