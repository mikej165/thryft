from time import mktime
import thryft.protocol._abstract_output_protocol
from thryft.protocol._stacked_output_protocol import _StackedOutputProtocol


def _upper_camelize(name):
    return ''.join([name_part.capitalize() for name_part in name.split('_')])


class JavaOutputProtocol(_StackedOutputProtocol):
    class _OutputProtocol(thryft.protocol._abstract_output_protocol._AbstractOutputProtocol):
        def __init__(self, output_protocol_stack, output_str_list):
            thryft.protocol._output_protocol._OutputProtocol.__init__(self)
            self.__output_protocol_stack = output_protocol_stack
            self._output_str_list = output_str_list

        def writeBool(self, value):
            self._writeValue("true" if value else "false")
            return self

        def writeDateTime(self, value):
            self._writeValue("new java.util.Date(%sl)" % (long(mktime(value.timetuple())) * 1000l))
            return self

        def writeFieldStop(self):
            return self

        def writeI32(self, value):
            self._writeValue(str(value))
            return self

        def writeI64(self, value):
            self._writeValue(str(value))
            return self

        def writeListBegin(self, *args, **kwds):
            self._output_str_list.append('com.google.common.collect.ImmutableList.of(')
            self.__output_protocol_stack.append(JavaOutputProtocol._ListOutputProtocol(self.__output_protocol_stack, self._output_str_list))
            return self

        def writeListEnd(self):
            self._output_str_list.pop()
            self._output_str_list.append(')')
            return self

        def writeMapBegin(self, *args, **kwds):
            self._output_str_list.append('com.google.common.collect.ImmutableMap.of(')
            self.__output_protocol_stack.append(JavaOutputProtocol._MapOutputProtocol(self.__output_protocol_stack, self._output_str_list))
            return self

        def writeMapEnd(self):
            self._output_str_list.pop()
            self._output_str_list.append(')')
            return self

        def writeNull(self):
            raise NotImplementedError
            return self

        def writeString(self, value):
            self._writeValue("\"" + value.encode('string-escape').replace('"', '\\"') + "\"")
            return self

        def writeStructBegin(self, name):
            self._output_str_list.append("%(name)s.builder()." % locals())
            self.__output_protocol_stack.append(JavaOutputProtocol._StructOutputProtocol(self.__output_protocol_stack, self._output_str_list))
            return self

        def writeStructEnd(self):
            self._output_str_list.append('build()')
            return self

        def _writeValue(self, value):
            raise NotImplementedError

    class _ListOutputProtocol(_OutputProtocol):
        def _writeValue(self, value):
            self._output_str_list.append(value)
            self._output_str_list.append(', ')

    class _MapOutputProtocol(_OutputProtocol):
        def __init__(self, *args, **kwds):
            JavaOutputProtocol._OutputProtocol.__init__(self, *args, **kwds)
            self.__next_key = None

        def _writeValue(self, value):
            if self.__next_key is None:
                self.__output_str_list.append(value)
            else:
                self.__output_str_list.append(value)
                self.__next_key = None
            self.__output_str_list.append(', ')
            return self

    class _RootOutputProtocol(_OutputProtocol):
        def __init__(self, *args, **kwds):
            JavaOutputProtocol._OutputProtocol.__init__(self, *args, **kwds)
            self.__value = None

        @property
        def value(self):
            return self.__value

        def _writeValue(self, value):
            self.__value = value
            return self

    class _StructOutputProtocol(_OutputProtocol):
        def __init__(self, *args, **kwds):
            JavaOutputProtocol._OutputProtocol.__init__(self, *args, **kwds)
            self.__next_field_name = None

        def writeFieldBegin(self, name, *args, **kwds):
            self.__next_field_name = name
            return self

        def writeFieldEnd(self):
            self.__next_field_name = None
            return self

        def _writeValue(self, value):
            self._output_str_list.append("set%s(%s)." % (_upper_camelize(self.__next_field_name), value))
            return self

    def __init__(self):
        _StackedOutputProtocol.__init__(self)
        self.__output_str_list = []
        self._output_protocol_stack.append(JavaOutputProtocol._RootOutputProtocol(self._output_protocol_stack, self.__output_str_list))

    def __str__(self):
        return ''.join(self.__output_str_list)
