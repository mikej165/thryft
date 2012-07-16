from thryft.target.base_type import BaseType


class DoubleType(BaseType):
    def thrift_ttype_id(self):
        return 4
