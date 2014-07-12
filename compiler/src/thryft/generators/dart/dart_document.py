import os.path
from thryft.generator.document import Document
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct
from yutil import rpad, upper_camelize


class DartDocument(Document, _DartNamedConstruct):
    def __init__(self, package_name, **kwds):
        Document.__init__(self, **kwds)
        self.__package_name = package_name

    def dart_name(self):
        return upper_camelize(self.name)

    def _dart_imports_definition(self, caller_stack):
        imports = []
        for definition in self.definitions:
            imports.extend(definition.dart_imports_definition(caller_stack))
        imports = list(sorted(set(imports)))
        return imports

    def _dart_imports_use(self, caller_stack):
        return ["import 'package:%s/%s';" % (
                    self.__package_name,
                    rpad(self.namespace_by_scope('dart').name.replace('.', '/'), '/') + self.dart_name() + '.dart')]

    def __repr__(self):
        imports = "\n".join(self.dart_imports_definition())
        definitions = "\n\n".join(repr(definition)
                        for definition in self.definitions)
        if len(definitions) == 0:
            return ''

        sections = []
        sections.append("library " + rpad(self.namespace_by_scope('dart').name, '.') + self.dart_name() + ';')
        if len(imports) > 0:
            sections.append(imports)
        sections.append(definitions)

        return "\n\n".join(sections) + "\n"

    def _save_to_dir(self, out_dir_path):
        try:
            out_dir_path = os.path.join(out_dir_path, self.namespace_by_scope('dart').name.replace('.', os.path.sep))
        except KeyError:
            pass
        return self._save_to_file(os.path.join(out_dir_path, self.dart_name() + '.dart'))
