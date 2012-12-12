from thryft.generator.function import Function
from thryft.generators.thrift._thrift_named_construct import _ThriftNamedConstruct
from yutil import rpad


class ThriftFunction(Function, _ThriftNamedConstruct):
    def __repr__(self):
        return "%s%s%s %s(%s)%s" % (
            self.comment is not None and rpad(repr(self.comment), "\n") or '',
            self.oneway and 'oneway ' or '',
            self.return_type is not None and self.return_type.thrift_qname() or 'void',
            self.name,
            ', '.join([repr(parameter) for parameter in self.parameters]),
            len(self.throws) > 0 and \
                (' throws (' + ', '.join([repr(throws) for throws in self.throws]) + ')')
                or ''
        )
