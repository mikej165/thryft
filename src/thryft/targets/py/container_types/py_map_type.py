from thryft.target.container_types.map_type import MapType
from thryft.targets.py.py_container_type import PyContainerType


class PyMapType(MapType, PyContainerType):
    def py_element_check(self, value):
        key_type_name = self.key_type.py_name()
        value_type_name = self.value_type.py_name()
        return "(isinstance(%(value)s[0], %(key_type_name)s) and isinstance(%(value)s[1], %(value_type_name)s))" % locals()
