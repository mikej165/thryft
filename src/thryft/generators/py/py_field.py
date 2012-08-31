from thryft.generator.field import Field
from thryft.generators.py.py_construct import PyConstruct
from yutil import quote, indent


class PyField(Field, PyConstruct):
    def py_getter(self):
        name = self.py_name()
        return """\
@property
def %(name)s(self):
    return self.__%(name)s
""" % locals()

    def py_getter_call(self):
        return self.py_getter_name()

    def py_getter_name(self):
        return self.py_name()

    def py_imports(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self.type.py_imports(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        imports.append('import __builtin__')

        return list(set(imports))

    def py_initializer(self):
        name = self.py_name()

        type_check = self.type.py_check(name)
        type_check = """\
if not %(type_check)s:
    raise TypeError(getattr(__builtin__, 'type')(%(name)s))""" % locals()

        if self.required:
            checks = """\
if %(name)s is None:
    raise ValueError('%(name)s is required')
%(type_check)s""" % locals()
        else:
            type_check = indent(' ' * 4, type_check)
            checks = """\
if %(name)s is not None:
%(type_check)s""" % locals()

        return """\
%(checks)s
self.__%(name)s = %(name)s
""" % locals()

    def py_parameter(self):
        if not self.required:
            if self.value is not None:
                return self.py_name() + '=' + str(self.py_value())
            else:
                return self.py_name() + '=None'
        else:
            return self.py_name()

    def py_read_protocol(self):
        name = self.name
        read_protocol = self.type.py_read_protocol()
        read_protocol = "init_kwds['%(name)s'] = %(read_protocol)s" % locals()
        if not self.required:
            read_protocol_throws = self.type.py_read_protocol_throws()
            if len(read_protocol_throws) > 0:
                read_protocol_throws = ', '.join(read_protocol_throws)
                read_protocol = indent(' ' * 4, read_protocol)
                read_protocol = """\
try:
%(read_protocol)s
except (%(read_protocol_throws)s,):
    pass
""" % locals()
        read_protocol = indent(' ' * 4, read_protocol)
        return """\
if ifield_name == '%(name)s':
%(read_protocol)s
""" % locals()

    def py_write_protocol(self, depth=0):
        id_ = self.id
        if id_ is None:
            id_ = -1
        name = self.name
        getter_call = self.py_getter_call()
        ttype_id = self.type.thrift_ttype_id()
        write_protocol = \
            self.type.py_write_protocol(
                'self.' + getter_call,
                depth=depth
            )
        write_protocol = """\
oprot.writeFieldBegin('%(name)s', %(ttype_id)u, %(id_)d)
%(write_protocol)s
oprot.writeFieldEnd()
""" % locals()
        if not self.required:
            write_protocol = indent(' ' * 4, write_protocol)
            write_protocol = """\
if self.%(getter_call)s is not None:
%(write_protocol)s
""" % locals()
        return write_protocol

    def py_value(self):
        if self.value is None:
            return None
        if isinstance(self.value, str):
            return quote(self.value)
        else:
            return self.value

    def __repr__(self):
        return self.py_parameter()
