from thryft.target.compound_type import CompoundType


class Struct(CompoundType):
    @property
    def native(self):
        for namespace in self.parent.namespaces:
            if namespace.scope == '*' and \
               namespace.name.rsplit('.', 1)[1] == 'native':
                return True
        return False
