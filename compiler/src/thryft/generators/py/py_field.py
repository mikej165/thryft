# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------

from thryft.generator.field import Field
from thryft.generators.py._py_named_construct import _PyNamedConstruct
from yutil import quote, indent


class PyField(Field, _PyNamedConstruct):
    def py_check(self):
        name = self.py_name()

        check = []

        type_check = self.type.py_check(name)
        type_description = self.type.py_description()
        check.append("""\
if not %(type_check)s:
    raise TypeError("expected %(name)s to be a %(type_description)s but it is a %%s" %% getattr(__builtin__, 'type')(%(name)s))""" % locals())

        validation = {}
        for annotation in self.annotations:
            if annotation.name == 'validation':
                validation = annotation.value.copy()
                break
        min_length = validation.get('minLength')
        if min_length is not None:
            check.append("""\
if len(%(name)s) < %(min_length)d:
    raise ValueError("expected len(%(name)s) to be >= %(min_length)d, was %%d" %% len(%(name)s))""" % locals())
        max_length = validation.get('maxLength')
        if max_length is not None:
            check.append("""\
if len(%(name)s) > %(max_length)d:
    raise ValueError("expected len(%(name)s) to be <= %(min_length)d, was %%d" %% len(%(name)s))""" % locals())

        check = "\n".join(check)

        if self.required:
            return """\
if %(name)s is None:
    raise ValueError('%(name)s is required')
%(check)s""" % locals()
        else:
            check = indent(' ' * 4, check)
            return """\
if %(name)s is not None:
%(check)s""" % locals()

    def py_decorated_setter(self):
        decorated_setter_name = self.py_decorated_setter_name()
        doc = self.py_sphinx_doc()
        name = self.py_name()
        setter_name = self.py_setter_name()
        suppress_warnings = '  # @ReservedAssignment' if self._py_is_reserved_name(name) else ''
        return """\
@%(name)s.setter
def %(decorated_setter_name)s(self, %(name)s):%(suppress_warnings)s
    '''
    %(doc)s
    '''

    self.%(setter_name)s(%(name)s)
""" % locals()

    def py_decorated_setter_name(self):
        return self.py_name()

    def py_getter(self):
        name = self.py_name()
        defensive_copy = self.type.py_defensive_copy('self.__' + name)
        type_description = self.type.py_description()
        suppress_warnings = '  # @ReservedAssignment' if self._py_is_reserved_name(name) else ''

        return """\
@property
def %(name)s(self):%(suppress_warnings)s
    '''
    :rtype: %(type_description)s
    '''

    return %(defensive_copy)s
""" % locals()

    def py_getter_call(self):
        return self.py_getter_name()

    def py_getter_name(self):
        return self.py_name()

    def _py_imports_check(self, caller_stack):
        return self.type.py_imports_check(caller_stack=caller_stack) + ['import __builtin__']

    def _py_imports_use(self, caller_stack):
        return self.type.py_imports_use(caller_stack=caller_stack)

    def py_initializer(self):
        check = self.py_check()
        name = self.py_name()
        defensive_copy = self.type.py_defensive_copy(name)
        return """\
%(check)s
self.__%(name)s = %(defensive_copy)s
""" % locals()

    def py_parameter(self, default_value=None, required=None):
        if required is None:
            required = self.required
        suppress_warnings = '  # @ReservedAssignment' if self._py_is_reserved_name(self.py_name()) else ''
        if self.value is not None:
            return self.py_name() + '=' + str(self.py_value()) + ',' + suppress_warnings
        elif default_value is not None:
            return self.py_name() + '=' + str(default_value) + ',' + suppress_warnings
        elif required:
            return self.py_name() + ',' + suppress_warnings
        else:
            return self.py_name() + '=None,' + suppress_warnings

    def py_read_protocol(self):
        id_check = (' and ifield_id == ' + str(self.id)) if self.id is not None else ''
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
if ifield_name == '%(name)s'%(id_check)s:
%(read_protocol)s
""" % locals()

    def py_repr(self):
        return self.py_parameter()

    def py_setter(self, return_type_name='void'):
        doc = self.py_sphinx_doc()
        setter_name = self.py_setter_name()
        name = self.py_name()
        suppress_warnings = '  # @ReservedAssignment' if self._py_is_reserved_name(name) else ''
        return """\
def %(setter_name)s(self, %(name)s):%(suppress_warnings)s
    '''
    %(doc)s
    '''

    self.__%(name)s = %(name)s
    return self
""" % locals()

    def py_setter_name(self):
        return 'set_' + self.py_name()

    def py_sphinx_doc(self):
        return ":type %s: %s%s" % (self.py_name(), self.type.py_description(), ' or None' if not self.required else '')

    def py_write_protocol(self, depth=0, value=None):
        if value is None:
            value = 'self.' + self.py_getter_call()
        id_ = self.id
        name = self.name
        ttype_id = self.type.thrift_ttype_id()
        write_protocol = \
            self.type.py_write_protocol(
                value,
                depth=depth
            )
        write_protocol = """\
oprot.write_field_begin(name='%(name)s', type=%(ttype_id)u, id=%(id_)s)
%(write_protocol)s
oprot.write_field_end()
""" % locals()
        if not self.required:
            write_protocol = indent(' ' * 4, write_protocol)
            write_protocol = """\
if %(value)s is not None:
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
