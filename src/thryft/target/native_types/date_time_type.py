from thryft.target.native_type import NativeType


class DateTimeType(NativeType):
    def thrift_ttype_id(self):
        return 10

    def thrift_ttype_name(self):
        return 'I64'
