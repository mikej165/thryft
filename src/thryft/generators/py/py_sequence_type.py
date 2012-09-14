from thryft.generators.py.py_container_type import PyContainerType
from yutil import decamelize, indent


class PySequenceType(PyContainerType):
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

    def py_write_protocol(self, value, depth=0):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'py'
        assert class_name_split[2] == 'type'

        element_ttype_id = self.element_type.thrift_ttype_id()
        element_write_protocol = \
            indent(' ' * 4,
                self.element_type.py_write_protocol(
                    "_%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        type_name = class_name_split[1].capitalize()
        return """\
oprot.write%(type_name)sBegin(%(element_ttype_id)u, len(%(value)s))
for _%(depth)u in %(value)s:
%(element_write_protocol)s
oprot.write%(type_name)sEnd()""" % locals()
