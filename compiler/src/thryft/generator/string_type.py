from thryft.generator._base_type import _BaseType


class StringType(_BaseType):
    def thrift_ttype_id(self):
        return 11
