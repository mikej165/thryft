from thryft.generator.compound_types.exception_type import ExceptionType
from thryft.generators.java.java_compound_type import JavaCompoundType


class JavaExceptionType(ExceptionType, JavaCompoundType):
    def __init__(self, java_static_class=False, **kwds):
        ExceptionType.__init__(self, **kwds)
        JavaCompoundType.__init__(self, java_static_class=java_static_class)

    def _java_extends(self):
        return 'java.lang.Exception'

    def __repr__(self):
        return JavaCompoundType.__repr__(self)
