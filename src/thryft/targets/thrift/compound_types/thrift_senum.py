from thryft.target.compound_types.senum import Senum
from yutil import pad, indent


class ThriftSenum(Senum):
    def __repr__(self):
        return "senum %s {%s}" % (
            self.name,
            pad("\n", ",\n".join(indent(' ' * 4,
                [enumerator.name
                 for enumerator in self.fields]
            )), "\n")
        )
