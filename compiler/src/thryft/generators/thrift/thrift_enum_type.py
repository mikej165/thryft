from thryft.generator.enum_type import EnumType
from thryft.generators.thrift._thrift_compound_type import _ThriftCompoundType
from yutil import pad, indent, rpad


class ThriftEnumType(EnumType, _ThriftCompoundType):
    def __repr__(self):
        return "%senum %s {%s}" % (
            self.comment is not None and rpad(self.comment.text, "\n") or '',
            self.name,
            pad("\n", indent(' ' * 4, ",\n".join([
                "%s%s%s" % (
                    enumerator.comment is not None and rpad(repr(enumerator.comment), "\n") or '',
                    enumerator.name,
                    enumerator.value is not None and " = %s" % enumerator.value or '',
                )
                for enumerator in self.enumerators]
            )), "\n")
        )
