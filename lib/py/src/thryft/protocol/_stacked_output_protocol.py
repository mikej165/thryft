from thryft.protocol._output_protocol import _OutputProtocol


class _StackedOutputProtocol(_OutputProtocol):
    def __init__(self):
        _OutputProtocol.__init__(self)
        self._output_protocol_stack = []

    def write_bool(self, value):
        return self._output_protocol_stack[-1].write_bool(value)

    def write_byte(self, value):
        return self._output_protocol_stack[-1].write_byte(value)

    def write_date_time(self, value):
        return self._output_protocol_stack[-1].write_date_time(value)

    def write_decimal(self, value):
        return self._output_protocol_stack[-1].write_decimal(value)

    def write_email_address(self, value):
        return self._output_protocol_stack[-1].write_email_address(value)

    def write_field_begin(self, name, *args, **kwds):
        return self._output_protocol_stack[-1].write_field_begin(name, *args, **kwds)

    def write_field_end(self):
        return self._output_protocol_stack[-1].write_field_end()

    def write_field_stop(self):
        return self._output_protocol_stack[-1].write_field_stop()

    def write_i16(self, value):
        return self._output_protocol_stack[-1].write_i16(value)

    def write_i32(self, value):
        return self._output_protocol_stack[-1].write_i32(value)

    def write_i64(self, value):
        return self._output_protocol_stack[-1].write_i16(value)

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

    def write_mixed(self, value):
        return self._output_protocol_stack[-1].write_mixed(value)

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
