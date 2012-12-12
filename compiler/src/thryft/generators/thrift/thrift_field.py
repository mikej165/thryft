from thryft.generator.field import Field
from thryft.generators.thrift._thrift_named_construct import _ThriftNamedConstruct
from yutil import rpad


class ThriftField(Field, _ThriftNamedConstruct):
    def __repr__(self):
        repr_ = []
        if self.id is not None:
            repr_.append(str(self.id) + ':')
        if self.required:
            repr_.append('required')
        else:
            repr_.append('optional')
        repr_.append(self.type.thrift_qname())
        repr_.append(self.name)
        if self.value is not None:
            repr_.extend(('=', str(self.value)))
        return (self.comment is not None and rpad(repr(self.comment), "\n") or '') + \
               ' '.join(repr_)
