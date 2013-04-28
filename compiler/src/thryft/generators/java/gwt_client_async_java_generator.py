from thryft.generators.java.gwt_client_java_generator import \
    GwtClientJavaGenerator
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import indent


class GwtClientAsyncJavaGenerator(GwtClientJavaGenerator):
    class Function(JavaFunction):
        def java_declaration(self):
            javadoc = self.java_doc()

            name = self.java_name()

            parameters = [parameter.java_parameter() for parameter in self.parameters]
            if self.return_field is not None:
                return_type_name = self.return_field.type.java_declaration_name(boxed=True)
            else:
                return_type_name = 'Void'
            parameters.append("com.google.gwt.user.client.rpc.AsyncCallback<%s> callback" % return_type_name)
            parameters = ', '.join(parameters)

            return """\
%(javadoc)spublic void %(name)s(%(parameters)s);""" % locals()

    class Service(JavaService):
        def java_name(self):
            return JavaService.java_name(self) + 'GwtClientAsync'

        def __repr__(self):
            functions = "\n\n".join(indent(' ' * 4, [repr(function) for function in self.functions]))
            name = self.java_name()
            service_name = JavaService.java_name(self)
            return """\
public interface %(name)s {
%(functions)s
}""" % locals()
