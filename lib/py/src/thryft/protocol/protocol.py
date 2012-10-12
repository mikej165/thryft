class Protocol(object):
    def writeMixed(self, object_):
        if isinstance(object_, float):
            self.writeDouble(object_)
        elif isinstance(object_, frozenset):
            self.writeSetBegin(len(object_))
            for item in object_:
                self.writeMixed(item)
            self.writeSetEnd()
        elif isinstance(object_, int):
            self.writeI32(object_)
        elif isinstance(object_, list):
            self.writeListBegin(len(object_))
            for item in object_:
                self.writeMixed(item)
            self.writeListEnd()
        elif isinstance(object_, long):
            self.writeI64(object_)
        elif isinstance(object_, str):
            self.writeString(object_)
        elif hasattr(object_, 'write'):
            object_.write(self)
        else:
            raise TypeError(type(object_))
