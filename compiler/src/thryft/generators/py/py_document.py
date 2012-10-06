from thryft.generator.document import Document
from thryft.generators.py.py_named_construct import PyNamedConstruct
from yutil import rpad
import os.path


class PyDocument(Document, PyNamedConstruct):
    def __repr__(self):
        imports = []
# Don't import anything that isn't required
#        for include in self.includes:
#            imports.append(str(include))
        for definition in self.definitions:
            imports.extend(definition.py_imports_definition())
        imports = "\n".join(list(sorted(set(imports))))

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])
        return rpad(imports, "\n\n\n") + definitions + "\n"

    def save(self, out_path):
        out_file_path = Document.save(self, out_path)
        if not os.path.isdir(out_path):
            return out_file_path

        root_out_dir_path = out_path
        leaf_out_dir_path = os.path.split(out_file_path)[0]

        py_module_dir_path = leaf_out_dir_path
        while py_module_dir_path != root_out_dir_path:
            init_py_file_path = os.path.join(py_module_dir_path, '__init__.py')
            if not os.path.isfile(init_py_file_path):
                with open(init_py_file_path, 'wb+') as _init_py_file:
                    print 'wrote', init_py_file_path
            py_module_dir_path = os.path.split(py_module_dir_path)[0]

        return out_file_path
