from thryft.generator.set_type import SetType
from thryft.generators.py._py_sequence_type import _PySequenceType


class PySetType(SetType, _PySequenceType):
    def py_check(self, value):
        element_check = self.element_type.py_check('_')
        return "(isinstance(%(value)s, frozenset) and len(list(ifilterfalse(lambda _: %(element_check)s, %(value)s))) == 0)" % locals()

    def py_read_protocol(self):
        element_read_protocol = self.element_type.py_read_protocol()
        return """frozenset([%(element_read_protocol)s for _ in xrange(iprot.readSetBegin()[1])] + (iprot.readSetEnd() is None and []))""" % locals()
