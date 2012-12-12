from thryft.generator.struct_type import StructType
from thryft.generators.py._py_compound_type import _PyCompoundType


class PyStructType(StructType, _PyCompoundType):
    def __repr__(self):
        return _PyCompoundType.__repr__(self)
