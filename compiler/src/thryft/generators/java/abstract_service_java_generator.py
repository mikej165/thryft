#-------------------------------------------------------------------------------
# Copyright (c) 2013, Minor Gordon
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

from thryft.generators.java import java_generator
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import indent, lpad, upper_camelize


class AbstractServiceJavaGenerator(java_generator.JavaGenerator):
    def __init__(self, include_current_user=False, **kwds):
        java_generator.JavaGenerator.__init__(self, **kwds)
        self._include_current_user = include_current_user

    class Document(java_generator.JavaGenerator.Document):
        def java_package(self):
            try:
                return self.namespace_by_scope(('abstract_service_java', 'java')).name
            except KeyError:
                return None

    class Function(JavaFunction):
        def java_repr(self):
            annotations = lpad("\n", "\n".join(self.java_annotations()))
            name = self.java_name()
            public_parameters = \
                ', '.join(parameter.java_parameter(final=True) for parameter in self.parameters)
            public_parameter_names = ', '.join(parameter.java_name() for parameter in self.parameters)
            parameter_validations = []
            for parameter in self.parameters:
                parameter_validation = parameter.java_validation()
                if parameter_validation != parameter.java_name():
                    parameter_validations.append(parameter_validation + ';')
            if len(parameter_validations) > 0:
                parameter_validations = \
                    "\n".join(indent(' ' * 4, parameter_validations))
                validate_method_name = '_validate' + upper_camelize(self.name) + 'Parameters'
                validate_method = lpad("\n\n", """\
protected void %(validate_method_name)s(%(public_parameters)s) {
%(parameter_validations)s
}""" % locals())
                validate_method_call = lpad("\n", indent(' ' * 4, "%s(%s);" % (validate_method_name, public_parameter_names)))
            else:
                validate_method = validate_method_call = ''
            protected_parameters = [parameter.java_parameter(final=True)
                                    for parameter in self.parameters]
            protected_parameter_names = [parameter.java_name()
                                         for parameter in self.parameters]
            if self.parent.parent.parent._include_current_user:
                protected_parameters.insert(0, 'org.apache.shiro.subject.Subject currentUser')
                protected_parameter_names.insert(0, 'org.apache.shiro.SecurityUtils.getSubject()')
            protected_delegation = \
                "_%s(%s)" % (name, ', '.join(protected_parameter_names))
            protected_parameters = ', '.join(protected_parameters)
            if self.return_field is not None:
                protected_delegation = 'return ' + self.return_field.java_validation(value=protected_delegation)
                return_type_name = self.return_field.type.java_declaration_name()
            else:
                return_type_name = 'void'
            throws = \
                lpad(
                    ' throws ',
                    ', '.join(field.type.java_declaration_name()
                               for field in self.throws)
                )

            return """\
@Override%(annotations)s
public final %(return_type_name)s %(name)s(%(public_parameters)s)%(throws)s {%(validate_method_call)s
    %(protected_delegation)s;
}%(validate_method)s

protected abstract %(return_type_name)s _%(name)s(%(protected_parameters)s)%(throws)s;
""" % locals()

    class Service(JavaService):
        def java_name(self, boxed=False):
            return 'Abstract' + JavaService.java_name(self)

        def _java_methods(self):
            return [function.java_repr() for function in self.functions]

        def java_repr(self):
            name = self.java_name()
            methods = "\n\n".join(indent(' ' * 4, self._java_methods()))
            service_qname = JavaService.java_qname(self)

            return """\
public abstract class %(name)s implements %(service_qname)s {
%(methods)s
}""" % locals()
