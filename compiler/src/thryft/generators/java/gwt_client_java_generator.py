from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.java.java_service import JavaService
from yutil import indent


class GwtClientJavaGenerator(JavaGenerator):
    class Document(JavaDocument):
        def java_package(self):
            for scope in ('gwt_client_java', 'java', '*'):
                try:
                    return self.namespaces_by_scope[scope].name
                except KeyError:
                    pass
            return None

        def save(self, out_path):
            return JavaDocument.save(self, file_ext='.java', language='gwt_client_java', out_path=out_path)

    class Service(JavaService):
        def java_name(self):
            return JavaService.java_name(self) + 'GwtClient'

        def __repr__(self):
            functions = "\n\n".join(indent(' ' * 4, [repr(function) for function in self.functions]))
            name = self.java_name()
            service_name = JavaService.java_name(self)
            return """\
@com.google.gwt.user.client.rpc.RemoteServiceRelativePath("%(service_name)s")
public interface %(name)s extends com.google.gwt.user.client.rpc.RemoteService {
%(functions)s
}""" % locals()
