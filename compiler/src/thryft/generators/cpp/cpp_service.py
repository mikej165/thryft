# -----------------------------------------------------------------------------
# Copyright (c) 2016, Minor Gordon
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

from thryft.generator.service import Service
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct
from yutil import indent, lpad


class CppService(Service, _CppNamedConstruct):
    def cpp_includes_definition(self):
        includes = []
        includes.extend(self._parent_generator().cpp_service_includes_definition)
        for function in self.functions:
            includes.extend(function.cpp_includes_definition())
            includes.extend(function.cpp_request_type().cpp_includes_definition())
            includes.extend(function.cpp_response_type().cpp_includes_definition())
        return includes

    def cpp_includes_use(self):
        return self._parent_document().cpp_includes_use()

    def cpp_extends(self):
        return self.extends

    def cpp_name(self, boxed=False):
        return self.name

    def cpp_qname(self, boxed=False):
        return _CppNamedConstruct.cpp_qname(self, name=self.name)

    def cpp_repr(self):
        name = self.cpp_name()

        parent_class_qname = self._parent_generator().cpp_service_parent_class_qname + "<%s>" % name
        extends = self.cpp_extends()
        if extends is not None:
            extends = ' : public ' + extends + ', public ' + parent_class_qname
        else:
            extends = ' : public ' + parent_class_qname

        sections = []

        if len(self.functions) > 0:
            message_types = []
            read_requests = []
            handle_request_declarations = []
            request_forward_declarations = []
            sync_request_handlers = []
            for function in self.functions:
                request_type = function.cpp_request_type()
                read_requests.append(request_type.cpp_read_if())
                request_forward_declarations.append(request_type.cpp_forward_declaration())
                handle_request_declarations.append(request_type.cpp_handle_declaration())
                message_types.append(request_type.cpp_repr())
                response_type = function.cpp_response_type()
                message_types.append(response_type.cpp_repr())
                sync_request_handlers.append(request_type.cpp_sync_handler())
            message_types = indent(' ' * 2, "\n\n".join(message_types))
            read_requests = indent(' ' * 4, ' else '.join(read_requests))
            request_forward_declarations = indent(' ' * 2, "\n".join(request_forward_declarations))
            handle_request_declarations = indent(' ' * 4, "\n".join(handle_request_declarations))
            service_parent_class_qname = self._parent_generator().cpp_service_parent_class_qname
            sync_request_handlers = indent(' ' * 4, "\n\n".join(sync_request_handlers))

            sections.append("public:\n" + indent(' ' * 2, """\
class Messages {
public:
  typedef %(parent_class_qname)s::Messages::Request Request;
  typedef %(parent_class_qname)s::Messages::Response Response;
%(request_forward_declarations)s

  class RequestHandler : public %(service_parent_class_qname)s<%(name)s>::Messages::RequestHandler {
  public:
    void handle(Request& request) override {
      request.accept(*this);
    }

%(handle_request_declarations)s
  };

%(message_types)s

  static ::std::unique_ptr< %(service_parent_class_qname)s<%(name)s>::Messages::Request > read_request(const char* function_name, ::thryft::protocol::InputProtocol& iprot, const ::thryft::protocol::Type& as_type) {
    if (!function_name || function_name[0] == 0) {
      return ::std::unique_ptr< %(service_parent_class_qname)s<%(name)s>::Messages::Request >();
    }

%(read_requests)s

    return ::std::unique_ptr< %(service_parent_class_qname)s<%(name)s>::Messages::Request >();
  }

  class SyncRequestHandler : public RequestHandler {
  public:
    SyncRequestHandler(::std::shared_ptr<%(name)s> impl)
      : impl_(impl) {
    }

  public:
    // RequestHandler
%(sync_request_handlers)s

  private:
    ::std::shared_ptr<%(name)s> impl_;
  };
};""" % locals()))

        sections.append(
                indent(' ' * 2,
                    "\n\n".join(function.cpp_pure_virtual_declaration()
                                for function in self.functions)))

        sections.append(
"""\
  #define %s_DECLARATIONS\\
%s""" % (
                self._parent_document().cpp_guard()[1:-5],
                indent(' ' * 2,
                    "\\\n\\\n".join(function.cpp_declaration(line_ending="\\\n", override=True) + ';'
                                for function in self.functions))))

        sections = lpad("\n\n", "\n\n".join(sections))

        return """\
class %(name)s%(extends)s {
public:
  virtual ~%(name)s() {
  }%(sections)s
};""" % locals()
