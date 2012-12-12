from thryft.generator.exception_type import ExceptionType
from thryft.generators.java._java_compound_type import _JavaCompoundType


class JavaExceptionType(ExceptionType, _JavaCompoundType):
    def __init__(self, **kwds):
        ExceptionType.__init__(self, **kwds)
        _JavaCompoundType.__init__(self, **kwds)

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
        methods = _JavaCompoundType._java_methods(self)
        methods.update(self._java_method_get_message())
        return methods

    def __repr__(self):
        return _JavaCompoundType.__repr__(self)
