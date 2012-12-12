from thryft.generator._base_type import _BaseType


class BoolType(_BaseType):
    def thrift_ttype_id(self):
        return 2
