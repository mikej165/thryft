from thryft.target.container_types.list_type import ListType
from thryft.targets.py.py_container_type import PyContainerType
from yutil import indent


class PyListType(ListType, PyContainerType):
    def py_check(self, value):
        element_check = self.element_type.py_check('_')
        return "(isinstance(%(value)s, tuple) and len(list(ifilterfalse(lambda _: %(element_check)s, %(value)s))) == 0)" % locals()

    def py_imports(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self.element_type.py_imports(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return imports + ['from itertools import ifilterfalse']

    def py_read_protocol(self):
        element_read_protocol = self.element_type.py_read_protocol()
        return """tuple([%(element_read_protocol)s for _ in xrange(iprot.readListBegin()[1])] + (iprot.readListEnd() is None and []))""" % locals()

    def py_write_protocol(self, value, depth=0):
        element_ttype_id = self.element_type.thrift_ttype_id()
        element_type_name = self.element_type.py_name()
        element_write_protocol = \
            indent(' ' * 4,
                self.element_type.py_write_protocol(
                    "_%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        return """\
oprot.writeListBegin(%(element_ttype_id)u, len(%(value)s))
for _%(depth)u in %(value)s:
%(element_write_protocol)s
oprot.writeListEnd()""" % locals()
