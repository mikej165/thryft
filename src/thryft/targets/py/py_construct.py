class PyConstruct(object):
    def py_imports(self, caller_stack=None):
        return []

    def py_name(self):
        return getattr(self, 'name')
