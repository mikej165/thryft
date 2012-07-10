from thryft.target.base_types.bool_type import BoolType


class JavaBoolType(BoolType):
    def java_is_reference(self):
        return False

    def java_name(self, boxed=False):
        if boxed:
            return 'Boolean'
        else:
            return 'boolean'

    def __repr__(self):
        return self.name
