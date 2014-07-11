from thryft.generator.struct_type import StructType
from thryft.generators.dart._dart_compound_type import _DartCompoundType


class DartStructType(StructType, _DartCompoundType):
    def __repr__(self):
        return _DartCompoundType.__repr__(self)