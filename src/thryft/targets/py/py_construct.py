class PyConstruct(object):
    def py_imports(self):
        return []

    def py_name(self):
        return getattr(self, 'name')
