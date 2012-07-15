from thryft.target.native_types.date_time_type import DateTimeType
from thryft.targets.java.java_native_type import JavaNativeType


class JavaDateTimeType(DateTimeType, JavaNativeType):
    def java_name(self, boxed=False):
        return 'org.joda.time.DateTime'
