from thryft.generator.service import Service
from thryft.generators.java.java_named_construct import JavaNamedConstruct
from yutil import indent, lpad


class JavaService(Service, JavaNamedConstruct):
    def java_extends(self):
        return self.extends

    def java_name(self):
        return self.name

    def __repr__(self):
        extends = self.java_extends()
        if extends is None:
            extends = ''
        else:
            extends = ' extends ' + extends
        methods = \
            lpad("\n", "\n".join(indent(' ' * 4,
                [function.java_declaration()
                 for function in self.functions])))
        name = self.java_name()
        return """\
public interface %(name)s%(extends)s {%(methods)s
}""" % locals()
