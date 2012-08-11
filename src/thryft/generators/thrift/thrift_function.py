from thryft.generator.function import Function


class ThriftFunction(Function):
    def __repr__(self):
        return "%s%s %s(%s)%s" % (
            self.oneway and 'oneway ' or '',
            self.return_type is not None and self.return_type.qname or 'void',
            self.name,
            ', '.join([repr(parameter) for parameter in self.parameters]),
            len(self.throws) > 0 and \
                (' throws (' + ', '.join([repr(throws) for throws in self.throws]) + ')')
                or ''
        )
