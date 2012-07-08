from thryft.target.service import Service
from yutil import pad, indent


class ThriftService(Service):
    def __repr__(self):
        return "service %s%s {%s}" % (
            self.name,
            self.extends is not None and (' ' + self.extends) or '',
            pad("\n", "\n".join(indent(' ' * 4,
                [repr(function) + ';' for function in self.functions],
            )), "\n")
        )
