from thryft.generators.java.java_named_construct import JavaNamedConstruct
from yutil import class_qname


class JavaType(JavaNamedConstruct):
    def java_declaration_name(self, boxed=False):
        return self.java_qname(boxed=boxed)

    def java_default_value(self):
        raise NotImplementedError(class_qname(self) + '.java_default_value')

    def java_hash_code(self, value):
        raise NotImplementedError(class_qname(self) + '.java_hash_code')

    def java_is_reference(self):
        raise NotImplementedError(class_qname(self) + '.java_is_reference')

    def java_name(self, boxed=False):
        return JavaNamedConstruct.java_name(self)

    def java_read_protocol(self):
        raise NotImplementedError(class_qname(self) + '.java_read_protocol')

    def java_read_protocol_throws(self):
        return []

    def java_to_string(self, value):
        raise NotImplementedError(class_qname(self) + '.java_to_string')

    def java_to_summary_string(self, value):
        return self.java_to_string(value)

    def java_ttype(self):
        raise NotImplementedError(class_qname(self) + '.java_ttype')

    def java_write_protocol(self, value, depth=0):
        raise NotImplementedError(class_qname(self) + '.java_write_protocol')
