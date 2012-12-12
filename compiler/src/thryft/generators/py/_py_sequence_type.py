from thryft.generators.py._py_container_type import _PyContainerType
from yutil import decamelize, indent


class _PySequenceType(_PyContainerType):
    def _py_imports_definition(self, caller_stack):
        return self.element_type.py_imports_definition(caller_stack=caller_stack) + \
               ['from itertools import ifilterfalse']

    def _py_imports_use(self, caller_stack):
        return self.element_type.py_imports_use(caller_stack=caller_stack) + \
               ['from itertools import ifilterfalse']

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
