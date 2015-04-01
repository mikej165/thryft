from thryft.generators.cpp._cpp_base_type import _CppBaseType
from thryft.generators.cpp.cpp_document import CppDocument
from thryft.generators.cpp.cpp_generator import CppGenerator
from thryft.generators.cpp.cpp_function import CppFunction
from thryft.generators.cpp.cpp_service import CppService
from thryft.generators.cpp.cpp_typedef import CppTypedef
from yutil import indent, lpad


class LoggingServiceCppGenerator(CppGenerator):
    class Document(CppDocument):
        def cpp_name(self):
            return 'logging_' + CppDocument.cpp_name(self)

        def cpp_namespace(self):
            try:
                return self.namespace_by_scope(('logging_cpp', 'cpp', '*')).name
            except KeyError:
                return

    class Function(CppFunction):
        def logging_cpp_repr(self):
            declaration = self.cpp_declaration(override=True)
            delegate_call = \
                "impl_->%s(%s)" % (
                    self.cpp_name(),
                    ', '.join(
                        parameter.cpp_name()
                        for parameter in self.parameters
                    )
                )
            if self.return_field is not None:
                delegate_call = 'return ' + delegate_call
            log_parameters = []
            for parameter in self.parameters:
                log_parameter = parameter.cpp_name()
                if not parameter.required:
                    log_parameter = '*' + log_parameter
                parameter_type = parameter.type
                while isinstance(parameter_type, CppTypedef):
                    parameter_type = parameter_type.type
                if not isinstance(parameter_type, _CppBaseType):
                    log_parameter = "to_string(%s)" % log_parameter
                if not parameter.required:
                    log_parameter = "(%s.present() ? %s : \"\")" % (parameter.cpp_name(), log_parameter)
                log_parameters.append(log_parameter)
            log_parameters = lpad(' << ', ' << \", \" << '.join(log_parameters))
            name = self.cpp_name()
            service_name = self.parent.name
            return """\
%(declaration)s {
  VLOG(VerboseLevel) << "%(service_name)s::%(name)s("%(log_parameters)s << ")";
  %(delegate_call)s;
}""" % locals()

    class Service(CppService):
        def _logging_cpp_includes_definition(self):
            return ('<easylogging++.h>',)

        def cpp_includes_definition(self):
            try:
                namespace = self._parent_document().namespace_by_scope(('cpp', '*')).name
            except KeyError:
                namespace = None
            include = []
            if namespace is not None:
                include.extend(namespace.split('.'))
            include.append(self._parent_document().name + '.hpp')
            includes = ['"' + '/'.join(include) + '"']
            includes.append('<thryft/protocol/json_output_protocol.hpp>')
            includes.extend(self._logging_cpp_includes_definition())
            return includes

        def cpp_name(self):
            return 'Logging' + CppService.cpp_name(self)

        def cpp_qname(self):
            return

        def cpp_repr(self):
            return self.logging_cpp_repr()

        def logging_cpp_repr(self):
            methods = \
                indent(' ' * 2,
                    "\n\n".join(function.logging_cpp_repr()
                                for function in self.functions))
            name = self.cpp_name()
            service_name = CppService.cpp_name(self)
            service_qname = CppService.cpp_qname(self)
            return """\
template <class %(service_name)sT, int VerboseLevel>
class %(name)s final : public %(service_qname)s {
public:
  %(name)s(::std::shared_ptr<%(service_name)sT> impl)
    : impl_(impl) {
  }

  virtual ~%(name)s() {
  }

public:
%(methods)s

private:
  static inline ::std::string to_string(const ::thryft::Base& object) {
    ::thryft::protocol::JsonOutputProtocol oprot;
    object.write(oprot);
    return oprot.to_string();
  }

  static inline ::std::string to_string(const ::thryft::native::Variant& variant) {
    return variant.operator std::string();
  }

private:
  ::std::shared_ptr<%(service_name)sT> impl_;
};""" % locals()

