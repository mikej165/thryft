from thryft.target.native_type import NativeType


class DateType(NativeType):
    def thrift_protocol_name(self):
        return 'I64'
