from thryft.protocol._output_protocol import _OutputProtocol


class _StackedOutputProtocol(_OutputProtocol):
    def __init__(self):
        _OutputProtocol.__init__(self)
        self._output_protocol_stack = []

    def writeBool(self, value):
        return self._output_protocol_stack[-1].writeBool(value)

    def writeFieldBegin(self, name, *args, **kwds):
        return self._output_protocol_stack[-1].writeFieldBegin(name, *args, **kwds)

    def writeFieldEnd(self):
        return self._output_protocol_stack[-1].writeFieldEnd()

    def writeFieldStop(self):
        return self._output_protocol_stack[-1].writeFieldStop()

    def writeI32(self, value):
        return self._output_protocol_stack[-1].writeI32(value)

    def writeI64(self, value):
        return self._output_protocol_stack[-1].writeI16(value)

    def writeListBegin(self, *args, **kwds):
        return self._output_protocol_stack[-1].writeListBegin(*args, **kwds)

    def writeListEnd(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].writeListEnd()

    def writeMapBegin(self, *args, **kwds):
        return self._output_protocol_stack[-1].writeMapBegin(*args, **kwds)

    def writeMapEnd(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].writeListEnd()

    def writeNull(self):
        return self._output_protocol_stack[-1].writeNull()

    def writeSetBegin(self, *args, **kwds):
        return self._output_protocol_stack[-1].writeSetBegin(*args, **kwds)

    def writeSetEnd(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].writeSetEnd()

    def writeString(self, value):
        return self._output_protocol_stack[-1].writeString(value)

    def writeStructBegin(self, *args, **kwds):
        return self._output_protocol_stack[-1].writeStructBegin(*args, **kwds)

    def writeStructEnd(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].writeStructEnd()
