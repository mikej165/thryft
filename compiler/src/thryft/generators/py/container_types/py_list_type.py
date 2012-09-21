from thryft.generator.container_types.list_type import ListType
from thryft.generators.py.py_sequence_type import PySequenceType


class PyListType(ListType, PySequenceType):
    def py_check(self, value):
        element_check = self.element_type.py_check('_')
        return "(isinstance(%(value)s, tuple) and len(list(ifilterfalse(lambda _: %(element_check)s, %(value)s))) == 0)" % locals()

    def py_read_protocol(self):
        element_read_protocol = self.element_type.py_read_protocol()
        return """tuple([%(element_read_protocol)s for _ in xrange(iprot.readListBegin()[1])] + (iprot.readListEnd() is None and []))""" % locals()