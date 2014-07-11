from thryft.protocol._output_protocol import _OutputProtocol


class _StackedOutputProtocol(_OutputProtocol):
    def __init__(self):
        _OutputProtocol.__init__(self)
        self._output_protocol_stack = []

    def write_bool(self, value):
        return self._output_protocol_stack[-1].write_bool(value)

    def writeByte(self, value):
        return self._output_protocol_stack[-1].writeByte(value)

    def writeDateTime(self, value):
        return self._output_protocol_stack[-1].writeDateTime(value)

    def writeDecimal(self, value):
        return self._output_protocol_stack[-1].writeDecimal(value)

    def writeEmailAddress(self, value):
        return self._output_protocol_stack[-1].writeEmailAddress(value)

    def write_field_begin(self, name, *args, **kwds):
        return self._output_protocol_stack[-1].write_field_begin(name, *args, **kwds)

    def write_field_end(self):
        return self._output_protocol_stack[-1].write_field_end()

    def write_field_stop(self):
        return self._output_protocol_stack[-1].write_field_stop()

    def writeI16(self, value):
        return self._output_protocol_stack[-1].writeI16(value)

    def write_i32(self, value):
        return self._output_protocol_stack[-1].write_i32(value)

    def write_i64(self, value):
        return self._output_protocol_stack[-1].writeI16(value)

    def write_list_begin(self, *args, **kwds):
        return self._output_protocol_stack[-1].write_list_begin(*args, **kwds)

    def write_list_end(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].write_list_end()

    def write_map_begin(self, *args, **kwds):
        return self._output_protocol_stack[-1].write_map_begin(*args, **kwds)

    def write_map_end(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].write_list_end()

    def writeMixed(self, value):
        return self._output_protocol_stack[-1].writeMixed(value)

    def write_null(self):
        return self._output_protocol_stack[-1].write_null()

    def write_set_begin(self, *args, **kwds):
        return self._output_protocol_stack[-1].write_set_begin(*args, **kwds)

    def write_set_end(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].write_set_end()

    def write_string(self, value):
        return self._output_protocol_stack[-1].write_string(value)

    def write_struct_begin(self, *args, **kwds):
        return self._output_protocol_stack[-1].write_struct_begin(*args, **kwds)

    def write_struct_end(self):
        self._output_protocol_stack.pop(-1)
        return self._output_protocol_stack[-1].write_struct_end()

    def writeUrl(self, value):
        return self._output_protocol_stack[-1].writeUrl(value)
