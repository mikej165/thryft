from thryft.generator.document import Document
from thryft.generators.java.java_named_construct import JavaNamedConstruct
from yutil import rpad, camelize
import os.path


class JavaDocument(Document, JavaNamedConstruct):
    def java_package(self):
        namespaces_by_scope = self.namespaces_by_scope
        for scope in ('java', '*'):
            try:
                return namespaces_by_scope[scope].name
            except KeyError:
                pass
        return None

    def java_package_declaration(self):
        package = self.java_package()
        if package is not None:
            return 'package ' + package + ';'

    def __repr__(self):
        headers = []
        package_declaration = self.java_package_declaration()
        if package_declaration is not None:
            headers.append(package_declaration)
        for include in self.includes:
            if len(headers) == 1 and headers[0].startswith('package'):
                headers.append('')
            headers.append(repr(include))
        headers = "\n".join(headers)

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])

        return rpad(headers, "\n\n") + definitions + "\n"

    def _save(self, out_file_path):
        out_dir_path, out_file_name = os.path.split(out_file_path)
        out_file_base_name, out_file_ext = os.path.splitext(out_file_name)
        assert out_file_ext == '.java'
        if out_file_base_name.lower() == out_file_base_name:
            out_file_base_name = camelize(out_file_base_name)
        out_file_path = \
            os.path.join(out_dir_path, out_file_base_name + '.java')
        return Document._save(self, out_file_path)
