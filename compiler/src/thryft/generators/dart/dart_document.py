import os.path
from thryft.generator.document import Document
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct
from yutil import rpad


class DartDocument(Document, _DartNamedConstruct):
    def __repr__(self):
        imports = []
        for definition in self.definitions:
            imports.extend(definition.dart_imports_definition())
        imports = "\n".join(list(sorted(set(imports))))

        definitions = \
            "\n\n".join(repr(definition)
                        for definition in self.definitions)
        return rpad(imports, "\n\n\n") + rpad(definitions, "\n")

    def _save_to_dir(self, out_dir_path):
        try:
            out_dir_path = os.path.join(out_dir_path, self.namespace_by_scope('dart').name.replace('.', os.path.sep))
        except KeyError:
            pass
        return self._save_to_file(os.path.join(out_dir_path, self.name + '.dart'))
