from thryft.generator.native_types.date_type import DateType
from thryft.generators.java.java_native_type import JavaNativeType
from thryft.generators.java.native_types.java_date_time_type import \
    JavaDateTimeType


class JavaDateType(DateType, JavaNativeType):
    def __init__(self, *args, **kwds):
        DateType.__init__(self, *args, **kwds)
        self.__date_time_type = JavaDateTimeType(*args, **kwds)

    def __getattr__(self, attr):
        return getattr(self.__date_time_type, attr)

    def java_read_protocol(self):
        return "new org.joda.time.DateTime(iprot.readI64())"

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeI64(%(value)s.getMillis());" % locals()
