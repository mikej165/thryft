from thryft.target.native_types.date_type import DateType
from thryft.targets.py.py_native_type import PyNativeType


class PyDateType(DateType, PyNativeType):
    def py_from_json_object(self, json_object_variable_name):
        return "datetime.strptime('', %(json_object_variable_name)s).date()" % locals()

    def py_imports(self):
        return ['from datetime import datetime']

    def py_name(self):
        return 'org.joda.time.DateTime'
