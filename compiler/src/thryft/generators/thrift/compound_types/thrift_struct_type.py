from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.thrift.thrift_compound_type import ThriftCompoundType
from yutil import pad, indent, rpad


class ThriftStructType(StructType, ThriftCompoundType):
    def __repr__(self):
        return "%sstruct %s {%s}" % (
            self.comment is not None and rpad(repr(self.comment), "\n") or '',
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
