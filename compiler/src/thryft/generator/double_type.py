from thryft.generator._base_type import _BaseType


class DoubleType(_BaseType):
    def thrift_ttype_id(self):
        return 4
