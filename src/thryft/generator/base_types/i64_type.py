from thryft.generator.base_type import BaseType


class I64Type(BaseType):
    def thrift_ttype_id(self):
        return 10
