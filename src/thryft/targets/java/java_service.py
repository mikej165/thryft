from thryft.target.service import Service
from yutil import indent, lpad


class JavaService(Service):
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
