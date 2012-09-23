from thryft.generators.py.py_named_construct import PyNamedConstruct
from yutil import class_qname


class PyType(PyNamedConstruct):
    def py_check(self, value):
        raise NotImplementedError(class_qname(self) + '.py_check')

    def py_defensive_copy(self, value):
        return value

    def py_read_protocol(self):
        raise NotImplementedError(class_qname(self) + '.py_read_protocol')

    def py_read_protocol_throws(self):
        return []

    def py_write_protocol(self, value, depth=0):
        raise NotImplementedError(class_qname(self) + '.py_write_protocol')
