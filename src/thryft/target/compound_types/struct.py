from thryft.target.compound_type import CompoundType


class Struct(CompoundType):
    @property
    def is_native(self):
        for namespace in self.parent.namespaces:
            if namespace == '*' and namespace.rsplit('.', 1) == 'native':
                return True
        return False
