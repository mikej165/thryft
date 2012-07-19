from thryft.targets.py.py_type import PyType


class PyCompoundType(PyType):
    def py_check(self, value):
        name = self.py_name()
        return "isinstance(%(value)s, %(name)s)" % locals()
