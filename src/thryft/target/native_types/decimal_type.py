from thryft.target.native_type import NativeType


class DecimalType(NativeType):
    def thrift_ttype_id(self):
        return 11

    def thrift_ttype_name(self):
        return 'STRING'
