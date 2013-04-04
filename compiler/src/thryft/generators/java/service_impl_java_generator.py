from thryft.generators.java import java_generator
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import camelize, indent
import os.path
import thryft.generator.document


class ServiceImplJavaGenerator(java_generator.JavaGenerator):
    class Document(JavaDocument):
        def _save(self, out_file_path):
            out_dir_path, out_file_name = os.path.split(out_file_path)
            out_dir_path = os.path.join(out_dir_path)
            out_file_base_name, out_file_ext = os.path.splitext(out_file_name)
            out_file_path = os.path.join(out_dir_path, camelize(out_file_base_name) + 'Impl' + out_file_ext + '.template')
            return thryft.generator.document.Document._save(self, out_file_path)

    class Function(JavaFunction):
        def __repr__(self):
            declaration = self.java_declaration(final_parameters=True).rstrip(';')
            return """\
@Override
%(declaration)s {
    // TODO Implement me!
    throw new UnsupportedOperationException();
}""" % locals()

    class Service(JavaService):
        def _java_name(self, boxed=False):
            return JavaService.java_name(self) + 'Impl'

        def _java_methods(self):
            return [repr(function) for function in self.functions]

        def __repr__(self):
            name = self._java_name()
            methods = "\n\n".join(indent(' ' * 4, self._java_methods()))
            service_qname = self.java_qname()

            return """\
public final class %(name)s implements %(service_qname)s {
%(methods)s
}""" % locals()
