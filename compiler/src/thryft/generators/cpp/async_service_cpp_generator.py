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

from thryft.generator.document import Document
from thryft.generators.cpp import cpp_generator
from thryft.generators.cpp.cpp_document import CppDocument
from thryft.generators.cpp.cpp_field import CppField
from thryft.generators.cpp.cpp_function import CppFunction
from thryft.generators.cpp.cpp_service import CppService
from thryft.generators.cpp.cpp_struct_type import CppStructType
from yutil import indent, lpad, pad, upper_camelize
import os.path


class AsyncServiceCppGenerator(cpp_generator.CppGenerator):
    class Document(CppDocument):
        def save(self, out_path):
            return Document.save(self, file_ext='.hpp', language='cpp', out_path=out_path)

        def _save(self, out_file_path):
            out_dir_path, out_file_name = os.path.split(out_file_path)
            out_file_base_name, out_file_ext = os.path.splitext(out_file_name)
            out_file_path = os.path.join(out_dir_path, out_file_base_name + '_async' + '.hpp')
            return CppDocument._save(self, out_file_path)

    class Function(CppFunction):
        class _CppRequestType(CppStructType):
            def __init__(self, parent_function, cpp_suppress_warnings=None, parameters=None):
                CppStructType.__init__(
                    self,
                    name=upper_camelize(parent_function.name) + 'Request',
                    parent=parent_function.parent
                )
                self.__parent_function_name = parent_function.name

                if parameters is None:
                    parameters = parent_function.parameters
                for parameter in parameters:
                    self.fields.append(
                        CppField(
                            annotations=parameter.annotations,
                            doc=parameter.doc,
                            name=parameter.name,
                            type=parameter.type,
                            parent=self,
                            required=parameter.required,
                        )
                    )

            def _cpp_extends(self):
                return 'Request'

            def cpp_forward_declaration(self):
                return 'class ' + self.cpp_name() + ';'

            def _cpp_method_accept(self):
                return {'accept': """\
void accept(RequestHandler& handler) const {
  handler.handle(*this);
}"""}

            def _cpp_methods(self):
                methods = CppStructType._cpp_methods(self)
                methods.update(self._cpp_method_accept())
                return methods

            def cpp_read_if(self):
                return """\
if (strcmp(function_name, "%s") == 0) {
  return new %s(iprot, as_type);
}""" % (self.__parent_function_name, self.cpp_name())

            def cpp_handle_declaration(self):
                return "virtual void handle(const %s&) = 0;" % self.cpp_name()

        class _CppResponseType(CppStructType):
            def __init__(self, parent_function, cpp_suppress_warnings=None):
                CppStructType.__init__(
                    self,
                    name=upper_camelize(parent_function.name) + 'Response',
                    parent=parent_function.parent
                )
                if parent_function.return_field is not None:
                    self.fields.append(parent_function.return_field)

            def _cpp_extends(self):
                return 'Response'

        def cpp_request_type(self, **kwds):
            return self._CppRequestType(parent_function=self, **kwds)

        def cpp_response_type(self, **kwds):
            return self._CppResponseType(parent_function=self, **kwds)

    class Service(CppService):
        def __repr__(self):
            name = self.cpp_name()

            sections = []

            if len(self.functions) > 0:
                message_types = []
                read_requests = []
                handle_request_declarations = []
                request_forward_declarations = []
                for function in self.functions:
                    request_type = function.cpp_request_type()
                    read_requests.append(request_type.cpp_read_if())
                    request_forward_declarations.append(request_type.cpp_forward_declaration())
                    handle_request_declarations.append(request_type.cpp_handle_declaration())
                    message_types.append(repr(request_type))

                    response_type = function.cpp_response_type()
                    message_types.append(repr(response_type))
                message_types = "\n\n".join(message_types)
                read_requests = indent(' ' * 2, ' else '.join(read_requests))
                request_forward_declarations = "\n".join(request_forward_declarations)
                handle_request_declarations = indent(' ' * 2, "\n".join(handle_request_declarations))

                sections.append("public:\n" + indent(' ' * 2, """\
class RequestHandler;

class Message : public ::thryft::Struct {
};

class Request : public Message {
public:
  virtual void accept(RequestHandler& visitor) const = 0;
};

%(request_forward_declarations)s

class RequestHandler {
public:
%(handle_request_declarations)s
};

class Response : public Message {
};

%(message_types)s

static Request* read_request(const char* function_name, ::thryft::protocol::Protocol& iprot, ::thryft::protocol::Type::Enum as_type) {
  if (function_name == NULL) {
    return NULL;
  }

%(read_requests)s

  return NULL;
}
""" % locals()))

            sections = pad("\n", "\n\n".join(sections), "\n")

            return """\
class %(name)sAsync {%(sections)s
public:
  virtual ~%(name)sAsync() {
  }
};""" % locals()
