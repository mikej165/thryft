from thryft.generator._compound_type import _CompoundType


class StructType(_CompoundType):
    @property
    def fields(self):
        return self._fields

    def thrift_ttype_id(self):
        return 12

    def thrift_ttype_name(self):
        return 'STRUCT'
