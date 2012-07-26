from thryft.target.compound_types.struct_type import StructType
from thryft.targets.py.py_compound_type import PyCompoundType
from yutil import indent, lpad


class PyStructType(StructType, PyCompoundType):
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

    def _py_method_eq(self):
        expressions = []
        for field in self.fields:
            expressions.append(
                'self.' + field.py_getter_call() + \
                ' == ' + \
                'other.' + field.py_getter_call()
            )
        if len(expressions) == 0:
            expressions.append('True')
        expressions = ' and '.join(expressions)
        return {'__eq__': """\
def __eq__(self, other):
    return %(expressions)s
""" % locals()}

    def _py_method_getters(self):
        return dict((field.py_getter_name(), field.py_getter())
                    for field in self.fields)

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
        methods_dict.update(self._py_method_eq())
        methods_dict.update(self._py_method_getters())
        methods_dict.update(self._py_method_read_protocol())
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
        methods = indent(' ' * 4, "\n".join(self._py_methods()))
        name = self.py_name()
        return """\
class %(name)s(object):
%(methods)s""" % locals()
