from thryft.target.compound_types.exception_type import ExceptionType
from thryft.targets.py.py_compound_type import PyCompoundType


class PyExceptionType(ExceptionType, PyCompoundType):
    def __repr__(self):
        name = self.py_name()
        return """\
class %(name)s(Exception):
    pass
""" % locals()
