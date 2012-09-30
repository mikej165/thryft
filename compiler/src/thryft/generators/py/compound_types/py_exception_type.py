from thryft.generator.compound_types.exception_type import ExceptionType
from thryft.generators.py.py_compound_type import PyCompoundType


class PyExceptionType(ExceptionType, PyCompoundType):
    def _py_extends(self):
        return ['Exception']

    def __repr__(self):
        return PyCompoundType.__repr__(self)
