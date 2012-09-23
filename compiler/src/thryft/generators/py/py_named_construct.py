from thryft.generators.py.py_construct import PyConstruct


class PyNamedConstruct(PyConstruct):
    def py_name(self):
        return getattr(self, 'name')
