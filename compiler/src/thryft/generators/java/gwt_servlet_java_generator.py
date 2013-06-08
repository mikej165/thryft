from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.java.java_service import JavaService
from yutil import indent, lpad


class GwtServletJavaGenerator(JavaGenerator):
    class Document(JavaDocument):
        def java_package(self):
            for scope in ('gwt_server_java', 'java', '*'):
                try:
                    return self.namespaces_by_scope[scope].name
                except KeyError:
                    pass
            return None

        def save(self, out_path):
            return JavaDocument.save(self, file_ext='.java', language='gwt_server_java', out_path=out_path)

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
            for scope in ('gwt_client_java', 'java', '*'):
                try:
                    client_service_package = self.parent.namespaces_by_scope[scope].name + '.'
                    break
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
