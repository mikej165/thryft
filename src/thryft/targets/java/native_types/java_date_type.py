from thryft.target.native_types.date_type import DateType
from thryft.targets.java.java_native_type import JavaNativeType


class JavaDateType(DateType, JavaNativeType):
    def java_name(self, boxed=False):
        return 'org.joda.time.DateTime'

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeI64(%(value)s.getMillis());" % locals()
