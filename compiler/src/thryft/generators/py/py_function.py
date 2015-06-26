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

from thryft.generator.function import Function
from thryft.generators.py._py_named_construct import _PyNamedConstruct
from thryft.generators.py.py_struct_type import PyStructType
from yutil import indent, pad, upper_camelize


class PyFunction(Function, _PyNamedConstruct):
    class _PyMessageType(PyStructType):
        pass

    class _PyRequestType(_PyMessageType):
        def __init__(self, parent_function):
            PyFunction._PyMessageType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Request',
                parent=parent_function.parent
            )
            for parameter in parent_function.parameters:
                self.fields.append(
                    parameter.__class__(
                        annotations=parameter.annotations,
                        doc=parameter.doc,
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required,
                    )
                )

    class _PyResponseType(_PyMessageType):
        def __init__(self, parent_function):
            PyFunction._PyMessageType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Response',
                parent=parent_function.parent
            )
            if parent_function.return_field is not None:
                self.fields.append(parent_function.return_field)

    def py_doc(self):
        doc_sections = []
        if self.doc is not None:
            doc_sections.append(self.doc)

        if len(self.parameters) > 0 or self.return_field is not None:
            parameter_doc_lines = []
            for parameter in self.parameters:
                parameter_doc_lines.append(parameter.py_sphinx_doc())
            if self.return_field is not None:
                parameter_doc_lines.append(":rtype: %s" % self.return_field.type.py_description())
            doc_sections.append("\n".join(parameter_doc_lines))

        if len(doc_sections) > 0:
            return "\n\n".join(doc_sections)
        else:
            return None

    def _py_imports_definition(self, caller_stack):
        imports = []
        for parameter in self.parameters:
            imports.extend(parameter.py_imports_use(caller_stack=caller_stack))
        if self.return_field is not None:
            imports.extend(self.return_field.py_imports_use(caller_stack=caller_stack))
        imports.append('import __builtin__')
        return imports

    def _py_imports_use(self, caller_stack):
        raise NotImplementedError

    def py_parameters(self):
        parameters = []
        for parameter in self.parameters:
            if parameter.required:
                parameters.append(parameter.py_parameter())
        for parameter in self.parameters:
            if not parameter.required:
                parameters.append(parameter.py_parameter())
        return parameters

    def py_protected_abstract_definition(self):
        name = self.py_name()
        parameters = ', '.join(['self'] + self.py_parameters())
        return """\
def _%(name)s(%(parameters)s):
    raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._%(name)s')
""" % locals()

    def py_public_delegating_definition(self):
        doc = self.py_doc()
        if doc is not None:
            doc = indent(' ' * 4, """
'''
%(doc)s
'''

""" % locals())
        else:
            doc = ''

        name = self.py_name()

        parameters = ', '.join(['self'] + self.py_parameters())

        parameter_checks = \
            pad("\n", "\n".join(indent(' ' * 4,
                (parameter.py_check()
                 for parameter in self.parameters)
            )), "\n")

        call = ', '.join("%s=%s" % (parameter.py_name(), parameter.py_name())
                          for parameter in self.parameters)

        if self.return_field is not None:
            return_value = name + '_return_value'
            while True:
                renamed_return_value = False
                for parameter in self.parameters:
                    if parameter.name == return_value:
                        return_value += '_'
                        renamed_return_value = True
                        break
                if not renamed_return_value:
                    break
            return_prefix = return_value + ' = '
            return_suffix = []
            return_type_check = self.return_field.type.py_check(return_value)
            return_suffix.append("""\
if not %(return_type_check)s:
    raise TypeError(getattr(__builtin__, 'type')(%(return_value)s))""" % locals())
            return_suffix.append('return ' + return_value)
            return_suffix = "\n\n" + "\n\n".join(indent(' ' * 4, return_suffix))
        else:
            return_prefix = return_suffix = ''

        return """\
def %(name)s(%(parameters)s):%(doc)s%(parameter_checks)s
    %(return_prefix)sself._%(name)s(%(call)s)%(return_suffix)s
""" % locals()

    def py_message_types(self):
        message_types = [self.py_request_type()]
        if not self.oneway:
            message_types.append(self.py_response_type())
        return message_types

    def py_request_type(self):
        return self._PyRequestType(parent_function=self)

    def py_response_type(self):
        return self._PyResponseType(parent_function=self)
