from thryft.generator.compound_types.struct_type import StructType
from yutil import pad, indent


class ThriftStructType(StructType):
    def __repr__(self):
        return "struct %s {%s}" % (
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
