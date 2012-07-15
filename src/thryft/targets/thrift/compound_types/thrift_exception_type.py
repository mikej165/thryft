from thryft.target.compound_types.exception_type import ExceptionType
from yutil import pad, indent


class ThriftExceptionType(ExceptionType):
    def __repr__(self):
        return "exception %s {%s}" % (
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
