from thryft.generator.base_type import BaseType


class StringType(BaseType):
    def thrift_ttype_id(self):
        return 11