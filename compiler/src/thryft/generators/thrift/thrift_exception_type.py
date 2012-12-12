from thryft.generator.exception_type import ExceptionType
from thryft.generators.thrift._thrift_compound_type import _ThriftCompoundType
from yutil import pad, indent, rpad


class ThriftExceptionType(ExceptionType, _ThriftCompoundType):
    def __repr__(self):
        return "%sexception %s {%s}" % (
            self.comment is not None and rpad(repr(self.comment), "\n") or '',
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
