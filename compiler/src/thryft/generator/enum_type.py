from thryft.generator._compound_type import _CompoundType


class EnumType(_CompoundType):
    @property
    def enumerators(self):
        return self._fields

    def thrift_ttype_id(self):
        return 11

    def thrift_ttype_name(self):
        return 'STRING'
