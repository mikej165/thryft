from thryft.targets.java.java_construct import JavaConstruct
from yutil import class_qname


class JavaType(JavaConstruct):
    def java_hash_code(self, value):
        raise NotImplementedError(class_qname(self) + '.java_write_protocol')

    def java_is_reference(self):
        raise NotImplementedError(class_qname(self) + '.java_is_reference')

    def java_read_protocol(self, value, depth=0):
        raise NotImplementedError(class_qname(self) + '.java_read_protocol')

    def java_read_protocol_throws(self):
        return []

    def java_ttype(self):
        raise NotImplementedError(class_qname(self) + '.java_ttype')

    def java_write_protocol(self, value, depth=0):
        raise NotImplementedError(class_qname(self) + '.java_write_protocol')
