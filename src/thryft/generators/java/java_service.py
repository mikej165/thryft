from thryft.generator.service import Service
from thryft.generators.java.java_construct import JavaConstruct
from yutil import indent, lpad


class JavaService(Service, JavaConstruct):
    def java_name(self):
        return self.name

    def __repr__(self):
        methods = \
            lpad("\n", "\n".join(indent(' ' * 4,
                [function.java_declaration()
                 for function in self.functions])))
        name = self.java_name()
        return """\
public interface %(name)s {%(methods)s
}""" % locals()
