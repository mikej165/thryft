#-------------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
#-------------------------------------------------------------------------------

from thryft.generators.py._py_type import _PyType
from yutil import decamelize, indent, lpad


class _PyCompoundType(_PyType):
    class _PyBuilder(object):
        def __init__(self, py_struct_type):
            object.__init__(self)
            self.__py_struct_type = py_struct_type

        def __getattr__(self, attr):
            return getattr(self.__py_struct_type, attr)

        def _py_constructor(self):
            if len(self.fields) == 0:
                return None

            parameters = []
            for field in self.fields:
                if field.required:
                    parameters.append(field.py_name() + '=None')
                else:
                    parameters.append(field.py_parameter())
            parameters = ",\n".join(indent(' ' * 4, parameters))
            initializers = \
                "\n".join(indent(' ' * 4,
                    ('self.__%s = %s' % (field.py_name(), field.py_name())
                     for field in self.fields)
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
                ', '.join("%s=self.__%s" % (field.py_name(), field.py_name())
                           for field in self.fields)
            name = self.py_name()
            return {'_build': """\
def build(self):
    return %(name)s(%(kwds)s)
""" % locals()}

        def _py_method_update(self):
            if len(self.fields) == 0:
                return {}

            name = self.py_name()
            other_name = decamelize(self.py_name())
            object_updates = \
                "\n".join(indent(' ' * 8,
                    ("self.%s(%s.%s)" % (field.py_setter_name(), other_name, field.py_getter_call())
                     for field in self.fields)
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
            constructor = self._py_constructor()
            methods = {}
            methods.update(self._py_method_build())
            methods.update(self._py_method_setters())
            methods.update(self._py_method_update())
            return ([constructor] if constructor is not None else []) + \
                    [methods[key] for key in sorted(methods.iterkeys())]

        def py_repr(self):
            name = self.py_name()
            sections = []
            sections.append("\n\n".join(indent(' ' * 4, self._py_methods())))
            sections = lpad("\n", "\n\n".join(sections))
            return """\
class Builder:%(sections)s
""" % locals()

    def py_check(self, value):
        qname = self.py_qname()
        return "isinstance(%(value)s, %(qname)s)" % locals()

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
                (field.py_initializer()
                 for field in self.fields)
            ))
        return """\
def __init__(
    self,
%(parameters)s
):
%(initializers)s
""" % locals()

    def _py_extends(self):
        return ['object']

    def _py_imports_definition(self, caller_stack):
        imports = []
        for field in self.fields:
            imports.extend(field.py_imports_use(caller_stack=caller_stack))
        return imports

    def _py_imports_use(self, caller_stack):
        return ['import ' + self.py_qname().rsplit('.', 1)[0]]

    def _py_method_as_dict(self):
        return {'as_dict': """\
def as_dict(self):
    return {%s}
""" % ', '.join("'%s': %s" % (field.py_name(), 'self.' + field.py_getter_call())
                                 for field in self.fields)}

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
""" % ','.join('self.' + field.py_getter_name()
                for field in self.fields)}

    def _py_method_ne(self):
        return {'__ne__': '''\
def __ne__(self, other):
    return not self.__eq__(other)
'''}

    def _py_method_read_protocol(self):
        if len(self.fields) == 0:
            return {'read': """\
@classmethod
def read(cls, iprot):
    iprot.read_struct_begin()
    iprot.read_struct_end()
    return cls()
""" % locals()}

        field_read_protocols = \
            indent(' ' * 8, lpad('el', "el".join(
                field.py_read_protocol()
                for field in self.fields
            )))
        name = self.py_name()
        return {'read': """\
@classmethod
def read(cls, iprot):
    init_kwds = {}

    iprot.read_struct_begin()
    while True:
        ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
        if ifield_type == 0: # STOP
            break
%(field_read_protocols)s
        iprot.read_field_end()
    iprot.read_struct_end()

    return cls(**init_kwds)
""" % locals()}

    def _py_method_replace(self):
        if len(self.fields) == 0:
            return {}

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

    def _py_method_repr(self, method_name='__repr__'):
        name = self.name

        if len(self.fields) == 0:
            return {method_name: """\
def %(method_name)s(self):
    return '%(name)s()'
""" % locals()}

        field_reprs = []
        for field in self.fields:
            field_name = field.name
            field_getter_call = field.py_getter_call()
            field_repr = field.type.py_runtime_repr('self.' + field.py_getter_call())
            field_repr = "field_reprs.append('%(field_name)s=' + %(field_repr)s)" % locals()
            if not field.required:
                field_repr = """\
if self.%(field_getter_call)s is not None:
    %(field_repr)s
""" % locals()
            field_reprs.append(field_repr)
        field_reprs = "\n".join(indent(' ' * 4, field_reprs))
        return {method_name: """\
def %(method_name)s(self):
    field_reprs = []
%(field_reprs)s
    return '%(name)s(' + ', '.join(field_reprs) + ')'
""" % locals()}

    def _py_method_str(self):
        return self._py_method_repr('__str__')

    def _py_method_write_protocol(self):
        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                (field.py_write_protocol(depth=0)
                 for field in self.fields)
            )))
        name = self.py_name()
        return {'write': """\
def write(self, oprot):
    oprot.write_struct_begin('%(name)s')%(field_write_protocols)s

    oprot.write_field_stop()

    oprot.write_struct_end()

    return self
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
        methods_dict.update(self._py_method_str())
        methods_dict.update(self._py_method_write_protocol())
        methods_list = \
           [methods_dict[method_name]
            for method_name in sorted(methods_dict.iterkeys())]
        if len(self.fields) > 0:
            methods_list.insert(0, self._py_constructor())
        return methods_list

    def py_read_protocol(self):
        qname = self.py_qname()
        return "%(qname)s.read(iprot)" % locals()

    def py_repr(self):
        extends = ', '.join(self._py_extends())
        sections = []
        sections.append(indent(' ' * 4, self._PyBuilder(self).py_repr()))
        sections.append(indent(' ' * 4, "\n".join(self._py_methods())))
        sections = "\n\n".join(sections)
        name = self.py_name()
        return """\
class %(name)s(%(extends)s):
%(sections)s""" % locals()

    def py_write_protocol(self, value, depth=0):
        return "%(value)s.write(oprot)" % locals()
