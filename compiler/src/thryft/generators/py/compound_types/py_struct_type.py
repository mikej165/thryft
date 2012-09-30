from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.py.py_compound_type import PyCompoundType


class PyStructType(StructType, PyCompoundType):
    def __repr__(self):
        return PyCompoundType.__repr__(self)
