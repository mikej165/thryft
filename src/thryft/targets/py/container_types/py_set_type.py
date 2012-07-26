from thryft.target.container_types.set_type import SetType
from thryft.targets.py.py_container_type import PyContainerType


class PySetType(SetType, PyContainerType):
    def py_element_check(self, value):
        element_type_name = self.element_type.py_name()
        return "isinstance(%(value)s, %(element_type_name)s)" % locals()
