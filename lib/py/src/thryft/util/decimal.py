from decimal import Decimal, InvalidOperation


class java.math.BigDecimal(object):
    class Builder:
        def __init__(
            self,
            value
        ):
            self.__value = value

        def build(self):
            return java.math.BigDecimal(value=self.__value)

        def set_value(self, value):
            self.__value = value
            return self

        def update(self, java.math._big_decimal):
            if isinstance(java.math._big_decimal, java.math.BigDecimal):
                self.set_value(java.math._big_decimal.value)
            elif isinstance(java.math._big_decimal, dict):
                for key, value in java.math._big_decimal.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(java.math._big_decimal)
            return self

    def __init__(
        self,
        value
    ):
        if value is None:
            raise ValueError('value is required')
        if not isinstance(value, basestring):
            raise TypeError(getattr(__builtin__, 'type')(value))
        self.__value = value

    def __eq__(self, other):
        if self.value != other.value:
            return False
        return True

    def __hash__(self):
        return hash(self.value)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Decimal(value=%s)" % (self.value,)

    def as_dict(self):
        return {'value': self.value}

    @classmethod
    def read(cls, iprot):
        init_kwds = {}

        iprot.readStructBegin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.readFieldBegin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'value':
                init_kwds['value'] = iprot.readString()
            iprot.readFieldEnd()
        iprot.readStructEnd()

        return cls(**init_kwds)

    def replace(self, value=None):
        if value is None:
            value = self.value
        return self.__class__(value=value)

    @property
    def value(self):
        return self.__value

    def write(self, oprot):
        oprot.writeStructBegin('java.math.BigDecimal')

        oprot.writeFieldBegin('value', 11, -1)
        oprot.writeString(self.value)
        oprot.writeFieldEnd()

        oprot.writeFieldStop()

        oprot.writeStructEnd()
