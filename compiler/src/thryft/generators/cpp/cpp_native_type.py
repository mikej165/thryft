from thryft.generator.native_type import NativeType
from thryft.generators.cpp._cpp_type import _CppType
from yutil import class_qname


class CppNativeType(NativeType, _CppType):
    def cpp_qname(self, name=None, **kwds):
        raise NotImplementedError(class_qname(self) + '.cpp_qname')
