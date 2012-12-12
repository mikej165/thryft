from thryft.generator._base_type import _BaseType


class ByteType(_BaseType):
    def thrift_ttype_id(self):
        return 3
