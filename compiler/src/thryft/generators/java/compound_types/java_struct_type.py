from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.java_compound_type import JavaCompoundType


class JavaStructType(StructType, JavaCompoundType):
    def __init__(self, java_static_class=False, **kwds):
        StructType.__init__(self, **kwds)
        JavaCompoundType.__init__(self, java_static_class=java_static_class)

    def __repr__(self):
        return JavaCompoundType.__repr__(self)
