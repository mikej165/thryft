from thryft.target.native_type import NativeType


class DateTimeType(NativeType):
    def thrift_protocol_name(self):
        return 'I64'
