from thryft.target.native_type import NativeType


class DecimalType(NativeType):
    def thrift_protocol_name(self):
        return 'STRING'
