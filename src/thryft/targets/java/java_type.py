from thryft.targets.java.java_construct import JavaConstruct
from yutil import class_qname


class JavaType(JavaConstruct):
    def java_hash_code(self, value):
        raise NotImplementedError(class_qname(self))

    def java_is_reference(self):
        raise NotImplementedError(class_qname(self))
