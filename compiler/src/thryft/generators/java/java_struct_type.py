from thryft.generator.struct_type import StructType
from thryft.generators.java._java_compound_type import _JavaCompoundType


class JavaStructType(StructType, _JavaCompoundType):
    def __init__(self, **kwds):
        StructType.__init__(self, **kwds)
        _JavaCompoundType.__init__(self, **kwds)

    def __repr__(self):
        return _JavaCompoundType.__repr__(self)
