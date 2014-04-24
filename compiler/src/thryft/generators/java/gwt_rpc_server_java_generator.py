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

import os.path
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.java.java_service import JavaService
from yutil import indent, lpad


class GwtRpcServerJavaGenerator(JavaGenerator):
    class Document(JavaDocument):
        def java_package(self):
            try:
                return self.namespace_by_scope(('gwt_rpc_server_java', 'java')).name
            except KeyError:
                return None

    class Function(JavaFunction):
        def __repr__(self):
            name = self.java_name()

            parameters = \
                ', '.join(parameter.java_parameter() for parameter in self.parameters)

            if self.return_field is not None:
                return_ = 'return '
                return_type_name = self.return_field.type.java_declaration_name()
            else:
                return_ = ''
                return_type_name = 'void'

            service_call = "service.%s(%s)" % (name, ', '.join(parameter.java_name() for parameter in self.parameters))

            throws = \
                lpad(
                    ' throws ',
                    ', '.join(field.type.java_declaration_name()
                               for field in self.throws)
                )

            return """\
public %(return_type_name)s %(name)s(%(parameters)s)%(throws)s {
    %(return_)s%(service_call)s;
}""" % locals()

    class Service(JavaService):
        def java_name(self):
            return JavaService.java_name(self) + 'GwtServlet'

        def __repr__(self):
            client_service_package = ''
            try:
                client_service_package = self._parent_document().namespace_by_scope(('gwt_client_java', 'java')).name + '.'
            except KeyError:
                pass
            client_service_qname = client_service_package + JavaService.java_name(self) + 'GwtClient'
            functions = \
                lpad("\n", "\n\n".join(indent(' ' * 4,
                    (repr(function) for function in self.functions)
                )))
            name = self.java_name()
            service_qname = JavaService.java_qname(self)
            return """\
@SuppressWarnings("serial")
@com.google.inject.Singleton
public final class %(name)s extends com.google.gwt.user.server.rpc.RemoteServiceServlet implements %(client_service_qname)s {
    @com.google.inject.Inject
    public %(name)s(final %(service_qname)s service) {
        this.service = service;
    }%(functions)s

    private final %(service_qname)s service;
}""" % locals()
