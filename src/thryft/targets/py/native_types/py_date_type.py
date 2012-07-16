from thryft.target.native_types.date_type import DateType
from thryft.targets.py.py_native_type import PyNativeType


class PyDateType(DateType, PyNativeType):
    def py_from_json_object(self, json_object_variable_name):
        return "datetime.strptime('', %(json_object_variable_name)s).date()" % locals()

    def py_imports(self):
        return ['from datetime import datetime']

    def py_name(self):
        return 'datetime'

    def py_read_protocol(self):
        return "datetime.fromtimestamp(iprot.readI64() / 1000)"

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeI64(timegm(datetime.timetuple()))"
