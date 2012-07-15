from thryft.target.base_types.bool_type import BoolType
from thryft.targets.java.java_base_type import JavaBaseType


class JavaBoolType(BoolType, JavaBaseType):
    def java_hash_code(self, value):
        return "(%(value)s ? 1 : 0)" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Boolean' or 'boolean'
