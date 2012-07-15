from thryft.target.native_types.date_time_type import DateTimeType
from thryft.targets.java.java_native_type import JavaNativeType


class JavaDateTimeType(DateTimeType, JavaNativeType):
    def java_name(self, boxed=False):
        return 'org.joda.time.DateTime'

    def java_read_protocol(self):
        return "new org.joda.time.DateTime(iprot.readI64())"

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeI64(%(value)s.getMillis());" % locals()
