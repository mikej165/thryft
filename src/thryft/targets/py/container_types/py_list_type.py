from thryft.target.container_types.list_type import ListType
from thryft.targets.py.py_container_type import PyContainerType
from yutil import indent


class PyListType(ListType, PyContainerType):
    def py_read_protocol(self):
        element_read_protocol = self.element_type.py_read_protocol()
        return """[%(element_read_protocol)s for _ in xrange(iprot.readListBegin()[1])]""" % locals()

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
