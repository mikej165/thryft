from thryft.target.native_types.date_time_type import DateTimeType
from thryft.targets.py.py_native_type import PyNativeType


class PyDateTimeType(DateTimeType, PyNativeType):
    def py_from_json_object(self, json_object_variable_name):
        return "datetime.strptime('', %(json_object_variable_name)s)" % locals()

    def py_imports(self):
        return ['from datetime import datetime']

    def py_name(self):
        return 'org.joda.time.DateTime'
