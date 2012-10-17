from thryft.generator.compound_types.exception_type import ExceptionType
from thryft.generators.java.java_compound_type import JavaCompoundType


class JavaExceptionType(ExceptionType, JavaCompoundType):
    def __init__(self, **kwds):
        ExceptionType.__init__(self, **kwds)
        JavaCompoundType.__init__(self, **kwds)

    def _java_extends(self):
        return 'java.lang.Exception'

    def _java_method_get_message(self):
        return {'getMessage': '''\
@Override
public String getMessage() {
    return toString();
}
'''}

    def _java_methods(self):
        methods = JavaCompoundType._java_methods(self)
        methods.update(self._java_method_get_message())
        return methods

    def __repr__(self):
        return JavaCompoundType.__repr__(self)
