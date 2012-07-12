from thryft.target.base_types.bool_type import BoolType


class JavaBoolType(BoolType):
    def java_is_reference(self):
        return False

    def java_hashCode(self, value):
        return "(%(value)s ? 1 : 0)" % locals()

    def java_name(self, boxed=False):
        if boxed:
            return 'Boolean'
        else:
            return 'boolean'

    def __repr__(self):
        return self.name
