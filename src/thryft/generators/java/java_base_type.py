from thryft.generators.java.java_type import JavaType
from yutil import upper_camelize


class JavaBaseType(JavaType):
    def java_is_reference(self):
        return False

    def java_read_protocol(self):
        name = upper_camelize(getattr(self, 'name'))
        return "iprot.read%(name)s()" % locals()

    def java_write_protocol(self, value, depth=0):
        name = upper_camelize(getattr(self, 'name'))
        return "oprot.write%(name)s(%(value)s);" % locals()

    def __repr__(self):
        return self.java_name()
