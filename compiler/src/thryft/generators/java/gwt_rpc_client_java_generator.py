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
from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.java.java_service import JavaService
from yutil import indent


class GwtRpcClientJavaGenerator(JavaGenerator):
    class Document(JavaDocument):
        def java_package(self):
            try:
                return self.namespace_by_scope(('gwt_rpc_client_java', 'java')).name
            except KeyError:
                return None

    class Service(JavaService):
        def java_name(self):
            return JavaService.java_name(self) + 'GwtClient'

        def __repr__(self):
            functions = \
                "\n\n".join(indent(' ' * 4,
                    (repr(function) for function in self.functions)
                ))
            name = self.java_name()
            service_name = JavaService.java_name(self)
            return """\
@com.google.gwt.user.client.rpc.RemoteServiceRelativePath("%(service_name)s")
public interface %(name)s extends com.google.gwt.user.client.rpc.RemoteService {
%(functions)s
}""" % locals()
