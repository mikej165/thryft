from thryft.generator.container_types.set_type import SetType
from thryft.generators.py.py_sequence_type import PySequenceType


class PySetType(SetType, PySequenceType):
    def py_check(self, value):
        element_check = self.element_type.py_check('_')
        return "(isinstance(%(value)s, tuple) and len(frozenset(%(value)s)) == len(%(value)s) and len(list(ifilterfalse(lambda _: %(element_check)s, %(value)s))) == 0)" % locals()

    def py_read_protocol(self):
        element_read_protocol = self.element_type.py_read_protocol()
        return """tuple(frozenset([%(element_read_protocol)s for _ in xrange(iprot.readSetBegin()[1])] + (iprot.readSetEnd() is None and [])))""" % locals()
