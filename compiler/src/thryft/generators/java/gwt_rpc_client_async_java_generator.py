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

from thryft.generators.java.gwt_rpc_client_java_generator import \
    GwtRpcClientJavaGenerator
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService


class GwtRpcClientAsyncJavaGenerator(GwtRpcClientJavaGenerator):
    class Function(JavaFunction):
        def java_declarations(self):
            javadoc = self.java_doc()

            name = self.java_name()

            parameters = [parameter.java_parameter(final=True) for parameter in self.parameters]
            if self.return_field is not None:
                return_type_name = self.return_field.type.java_boxed_qname()
            else:
                return_type_name = 'Void'
            parameters.append("final com.google.gwt.user.client.rpc.AsyncCallback<%s> callback" % return_type_name)
            parameters = ', '.join(parameters)

            return ("""\
%(javadoc)spublic void %(name)s(%(parameters)s);""" % locals(),)

    class Service(JavaService):
        def _java_message_types(self):
            return []

        def java_name(self):
            return JavaService.java_name(self) + 'GwtClientAsync'
