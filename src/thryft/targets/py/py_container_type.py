from thryft.targets.py.py_type import PyType
from yutil import class_qname


class PyContainerType(PyType):
    def py_element_check(self, value):
        raise NotImplementedError(class_qname(self))
