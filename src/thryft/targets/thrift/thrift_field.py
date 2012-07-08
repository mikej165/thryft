from thryft.target.field import Field


class ThriftField(Field):
    def __repr__(self):
        repr_ = []
        if self.id is not None:
            repr_.append(str(self.id) + ':')
        repr_.append(self.type.qname)
        repr_.append(self.name)
        if self.value is not None:
            repr_.extend(('=', str(self.value)))
        return ' '.join(repr_)
