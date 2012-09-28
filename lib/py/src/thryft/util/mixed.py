class Mixed(object):
    class Builder:
        def __init__(self):
            pass

        def build(self):
            return Mixed()

        def update(self, mixed):
            if isinstance(mixed, Mixed):

            elif isinstance(mixed, dict):
                for key, value in mixed.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(mixed)
            return self

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
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

    def replace(self, ):

        return self.__class__()

    def write(self, oprot):
        oprot.writeStructBegin('Mixed')

        oprot.writeFieldStop()

        oprot.writeStructEnd()
