from thryft.target.compound_types.exception import Exception
from yutil import pad, indent


class ThriftException(Exception):
    def __repr__(self):
        return "exception %s {%s}" % (
            self.name,
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(field) + ';' for field in self.fields],
            )), "\n")
        )
