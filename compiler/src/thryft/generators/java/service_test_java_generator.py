import thryft.generator.document
from thryft.generators.java import java_generator
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import indent, camelize, upper_camelize
import os.path


class ServiceTestJavaGenerator(java_generator.JavaGenerator):
    class Document(JavaDocument):
        def java_imports(self):
            return ['import org.junit.Test;']

        def _save(self, out_file_path):
            out_dir_path, out_file_name = os.path.split(out_file_path)
            out_dir_path = os.path.join(out_dir_path)
            out_file_base_name, out_file_ext = os.path.splitext(out_file_name)
            out_file_path = os.path.join(out_dir_path, camelize(out_file_base_name) + 'Test' + out_file_ext + '.template')
            return thryft.generator.document.Document._save(self, out_file_path)

    class Function(JavaFunction):
        def java_name(self):
            return 'test' + upper_camelize(self.name)

        def __repr__(self):
            name = self.java_name()
            return """\
@Test
public void %(name)s() {
}""" % locals()

    class Service(JavaService):
        def _java_name(self, boxed=False):
            return JavaService.java_name(self) + 'Test'

        def _java_constructor(self):
            name = self._java_name()
            service_qname = JavaService.java_qname(self)
            return """\
public %(name)s(final %(service_qname)s service) {
    this.service = service;
}""" % locals()

        def _java_member_declarations(self):
            service_qname = JavaService.java_qname(self)
            return [
                "private final %(service_qname)s service;" % locals()
            ]

        def _java_methods(self):
            return [repr(function) for function in self.functions]

        def __repr__(self):
            name = self._java_name()

            sections = []
            sections.append("\n\n".join([self._java_constructor()] + self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
public final class %(name)s {
%(sections)s
}""" % locals()
