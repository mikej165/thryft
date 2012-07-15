from thryft.target.native_types.date_type import DateType
from thryft.targets.java.java_native_type import JavaNativeType


class JavaDateType(DateType, JavaNativeType):
    def java_name(self, boxed=False):
        return 'org.joda.time.DateTime'
