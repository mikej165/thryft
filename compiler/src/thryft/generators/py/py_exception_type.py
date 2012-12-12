from thryft.generator.exception_type import ExceptionType
from thryft.generators.py._py_compound_type import _PyCompoundType


class PyExceptionType(ExceptionType, _PyCompoundType):
    def _py_extends(self):
        return ['Exception']

    def __repr__(self):
        return _PyCompoundType.__repr__(self)
