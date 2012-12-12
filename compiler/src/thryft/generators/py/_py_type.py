from thryft.generators.py._py_named_construct import _PyNamedConstruct
from yutil import class_qname


class _PyType(_PyNamedConstruct):
    def py_check(self, value):
        raise NotImplementedError(class_qname(self) + '.py_check')

    def py_defensive_copy(self, value):
        return value

    def py_read_protocol(self):
        raise NotImplementedError(class_qname(self) + '.py_read_protocol')

    def py_read_protocol_throws(self):
        return []

    def py_repr(self, value):
        return 'repr(' + value + ')'

    def py_write_protocol(self, value, depth=0):
        raise NotImplementedError(class_qname(self) + '.py_write_protocol')

