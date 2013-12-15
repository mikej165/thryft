from thryft.generator.native_type import NativeType
from thryft.generators.java._java_type import _JavaType
from yutil import class_qname


class JavaNativeType(NativeType, _JavaType):
    def java_name(self):
        return self.java_qname()

    def java_qname(self, name=None, **kwds):
        raise NotImplementedError(class_qname(self) + '.java_qname')
