from thryft.generator.base_type import BaseType


class BoolType(BaseType):
    def thrift_ttype_id(self):
        return 2
