class Mixed(object):
    class Builder:
        def build(self):
            return Mixed()

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'Mixed()'

    def __str__(self):
        return 'Mixed()'

    def as_dict(self):
        return {}

    @classmethod
    def read(cls, iprot):
        init_kwds = {}

        iprot.readStructBegin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.readFieldBegin()
            if ifield_type == 0: # STOP
                break

            iprot.readFieldEnd()
        iprot.readStructEnd()

        return cls(**init_kwds)

    def write(self, oprot):
        oprot.writeStructBegin('Mixed')

        oprot.writeFieldStop()

        oprot.writeStructEnd()
