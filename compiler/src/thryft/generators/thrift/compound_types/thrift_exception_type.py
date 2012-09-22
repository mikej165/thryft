from thryft.generator.compound_types.exception_type import ExceptionType
from yutil import pad, indent, rpad


class ThriftExceptionType(ExceptionType):
    def __repr__(self):
        return "%sexception %s {%s}" % (
            self.comment is not None and rpad(repr(self.comment), "\n") or '',
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
