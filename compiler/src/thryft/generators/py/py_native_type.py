from thryft.generator.native_type import NativeType
from thryft.generators.py._py_type import _PyType
from yutil import class_qname


class PyNativeType(NativeType, _PyType):
    def py_name(self):
        raise NotImplementedError(class_qname(self) + '.py_name')

    def py_qname(self, name=None, **kwds):
        raise NotImplementedError(class_qname(self) + '.py_qname')
