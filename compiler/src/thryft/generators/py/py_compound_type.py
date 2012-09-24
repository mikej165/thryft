from thryft.generators.py.py_type import PyType


class PyCompoundType(PyType):
    def py_check(self, value):
        qname = self.py_qname()
        return "isinstance(%(value)s, %(qname)s)" % locals()
