from thryft.generator.document import Document
from thryft.generators.java.java_construct import JavaConstruct
from yutil import rpad, camelize
import os.path


class JavaDocument(Document, JavaConstruct):
    def java_package(self):
        namespaces_by_scope = self.namespaces_by_scope
        for scope in ('java', '*'):
            try:
                return namespaces_by_scope[scope].name
            except KeyError:
                pass
        return None

    def __repr__(self):
        headers = []
        package = self.java_package()
        if package is not None:
            headers.append('package ' + package + ';')
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
        out_file_path = \
            os.path.join(out_dir_path, camelize(out_file_base_name) + '.java')
        return Document._save(self, out_file_path)
