from thryft.targets.py.py_type import PyType
from yutil import upper_camelize


class PyBaseType(PyType):
    def py_read_protocol(self):
        name = upper_camelize(getattr(self, 'name'))
        return "iprot.read%(name)s()" % locals()

    def py_read_protocol_throws(self):
        return ['TypeError', 'ValueError']

    def py_write_protocol(self, value, depth=0):
        name = upper_camelize(getattr(self, 'name'))
        return "oprot.write%(name)s(%(value)s)" % locals()
