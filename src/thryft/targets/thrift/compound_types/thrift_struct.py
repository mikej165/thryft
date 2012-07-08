from thryft.target.compound_types.struct import Struct
from yutil import pad, indent


class ThriftStruct(Struct):
    def __repr__(self):
        return "struct %s {%s}" % (
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
