from thryft.generator._base_type import _BaseType


class I32Type(_BaseType):
    def thrift_ttype_id(self):
        return 8
