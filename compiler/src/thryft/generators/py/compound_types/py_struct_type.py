from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.py.py_compound_type import PyCompoundType
from yutil import decamelize, indent, lpad


class PyStructType(StructType, PyCompoundType):
    class _PyBuilder(object):
        def __init__(self, py_struct_type):
            object.__init__(self)
            self.__py_struct_type = py_struct_type

        def __getattr__(self, attr):
            return getattr(self.__py_struct_type, attr)

        def _py_constructor(self):
            if len(self.fields) == 0:
                return '''\
def __init__(self):
    pass
'''

            parameters = []
            for field in self.fields:
                if field.required:
                    parameters.append(field.py_parameter())
            for field in self.fields:
                if not field.required:
                    parameters.append(field.py_parameter())
            parameters = ",\n".join(indent(' ' * 4, parameters))
            initializers = \
                "\n".join(indent(' ' * 4,
                    ['self.__%s = %s' % (field.py_name(), field.py_name())
                     for field in self.fields]
                ))
            return """\
def __init__(
    self,
%(parameters)s
):
%(initializers)s
""" % locals()

        def _py_method_build(self):
            kwds = \
                ', '.join(["%s=self.__%s" % (field.py_name(), field.py_name())
                           for field in self.fields])
            name = self.py_name()
            return {'_build': """\
def build(self):
    return %(name)s(%(kwds)s)
""" % locals()}

        def _py_method_update(self):
            name = self.py_name()
            other_name = decamelize(self.py_name())
            object_updates = "\n".join(indent(' ' * 8,
                          ["self.%s(%s.%s)" % (field.py_setter_name(), other_name, field.py_getter_call())
                           for field in self.fields]
                       ))
            return {'update': """\
def update(self, %(other_name)s):
    if isinstance(%(other_name)s, %(name)s):
%(object_updates)s
    elif isinstance(%(other_name)s, dict):
        for key, value in %(other_name)s.iteritems():
            getattr(self, 'set_' + key)(value)
    else:
        raise TypeError(%(other_name)s)
    return self
""" % locals()}

        def _py_method_setters(self):
            return \
                dict((
                    field.py_setter_name(),
                    field.py_setter(return_type_name='Builder')
                )
                for field in self.fields)

        def _py_methods(self):
            methods = {}
            methods.update(self._py_method_build())
            methods.update(self._py_method_setters())
            methods.update(self._py_method_update())
            return [self._py_constructor()] + [methods[key] for key in sorted(methods.iterkeys())]

        def __repr__(self):
            name = self.py_name()
            sections = []
            sections.append("\n\n".join(indent(' ' * 4, self._py_methods())))
            sections = lpad("\n", "\n\n".join(sections))
            return """\
class Builder:%(sections)s
""" % locals()

    def _py_constructor(self):
        assert len(self.fields) > 0
        parameters = []
        for field in self.fields:
            if field.required:
                parameters.append(field.py_parameter())
        for field in self.fields:
            if not field.required:
                parameters.append(field.py_parameter())
        parameters = ",\n".join(indent(' ' * 4, parameters))
        initializers = \
            "\n\n".join(indent(' ' * 4,
                [field.py_initializer() for field in self.fields]
            ))
        return """\
def __init__(
    self,
%(parameters)s
):
%(initializers)s
""" % locals()

    def _py_method_as_dict(self):
        return {'as_dict': """\
def as_dict(self):
    return {%s}
""" % ', '.join(["'%s': %s" % (field.py_name(), 'self.' + field.py_getter_call())
                                 for field in self.fields])}

    def _py_method_eq(self):
        statements = []
        for field in self.fields:
            field_getter_call = field.py_getter_call()
            statements.append("""\
if self.%(field_getter_call)s != other.%(field_getter_call)s:
    return False""" % locals())
        statements.append('return True')
        statements = "\n".join(indent(' ' * 4, statements))
        return {'__eq__': """\
def __eq__(self, other):
%(statements)s
""" % locals()}

    def _py_method_getters(self):
        return dict((field.py_getter_name(), field.py_getter())
                    for field in self.fields)

    def _py_method_hash(self):
        if len(self.fields) == 0:
            return {}
        elif len(self.fields) == 1:
            return {'__hash__': """\
def __hash__(self):
    return hash(self.%s)
""" % self.fields[0].py_getter_name()}
        return {'__hash__': """\
def __hash__(self):
    return hash((%s,))
""" % ','.join(['self.' + field.py_getter_name()
                for field in self.fields])}

    def _py_method_ne(self):
        return {'__ne__': '''\
def __ne__(self, other):
    return not self.__eq__(other)
'''}

    def _py_method_read_protocol(self):
        field_read_protocols = \
            indent(' ' * 8, lpad('el', "el".join(
                [field.py_read_protocol()
                 for field in self.fields]
            )))
        name = self.py_name()
        return {'read': """\
@classmethod
def read(cls, iprot):
    init_kwds = {}

    iprot.readStructBegin()
    while True:
        ifield_name, ifield_type, _ifield_id = iprot.readFieldBegin()
        if ifield_type == 0: # STOP
            break
%(field_read_protocols)s
        iprot.readFieldEnd()
    iprot.readStructEnd()

    return cls(**init_kwds)
""" % locals()}

    def _py_method_replace(self):
        in_kwds = []
        out_kwds = []
        replacements = []
        for field in self.fields:
            field_getter_call = field.py_getter_call()
            field_name = field.py_name()
            in_kwds.append("%(field_name)s=None" % locals())
            out_kwds.append("%(field_name)s=%(field_name)s" % locals())
            replacements.append("""\
if %(field_name)s is None:            
    %(field_name)s = self.%(field_getter_call)s
""" % locals())
        in_kwds = ', '.join(in_kwds)
        out_kwds = ', '.join(out_kwds)
        replacements = "\n".join(indent(' ' * 4, replacements))
        return {'replace': """\
def replace(self, %(in_kwds)s):
%(replacements)s
    return self.__class__(%(out_kwds)s)
""" % locals()}

    def _py_method_repr(self):
        name = self.name

        if len(self.fields) == 0:
            return {'__repr__': """\
def __repr__(self):
    return '%(name)s()'
""" % locals()}

        field_reprs = \
            ', '.join([
                "%s=%%s" % field.name
                for field in self.fields
            ])
        field_values = \
            ', '.join([
                'self.' + field.py_getter_call()
                 for field in self.fields
            ])
        return {'__repr__': """\
def __repr__(self):
    return "%(name)s(%(field_reprs)s)" %% (%(field_values)s,)
""" % locals()}

    def _py_method_write_protocol(self):
        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                [field.py_write_protocol(depth=0)
                 for field in self.fields]
            )))
        name = self.py_name()
        return {'write': """\
def write(self, oprot):
    oprot.writeStructBegin('%(name)s')%(field_write_protocols)s

    oprot.writeFieldStop()

    oprot.writeStructEnd()
""" % locals()}

    def _py_methods(self):
        methods_dict = {}
        methods_dict.update(self._py_method_as_dict())
        methods_dict.update(self._py_method_eq())
        methods_dict.update(self._py_method_getters())
        methods_dict.update(self._py_method_hash())
        methods_dict.update(self._py_method_ne())
        methods_dict.update(self._py_method_read_protocol())
        methods_dict.update(self._py_method_replace())
        methods_dict.update(self._py_method_repr())
        methods_dict.update(self._py_method_write_protocol())
        methods_list = \
           [methods_dict[method_name]
            for method_name in sorted(methods_dict.iterkeys())]
        if len(self.fields) > 0:
            methods_list.insert(0, self._py_constructor())
        return methods_list

    def py_imports(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)
        imports = []
        for field in self.fields:
            imports.extend(field.py_imports(caller_stack=caller_stack))
        assert caller_stack[-1] is self
        caller_stack.pop(-1)
        return list(set(imports))

    def py_read_protocol(self):
        name = self.py_name()
        return "%(name)s.read(iprot)" % locals()

    def py_write_protocol(self, value, depth=0):
        return "%(value)s.write(oprot)" % locals()

    def __repr__(self):
        sections = []
        sections.append(indent(' ' * 4, repr(self._PyBuilder(self))))
        sections.append(indent(' ' * 4, "\n".join(self._py_methods())))
        sections = "\n\n".join(sections)
        name = self.py_name()
        return """\
class %(name)s(object):
%(sections)s""" % locals()
