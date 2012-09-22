from thryft.generator.function import Function
from thryft.generators.java.java_construct import JavaConstruct
from yutil import lower_camelize, lpad


class JavaFunction(Function, JavaConstruct):
    def java_declaration(self):
        name = self.java_name()
        parameters = \
            ', '.join([repr(parameter)
                       for parameter in self.parameters])
        return_type = \
            self.return_type is not None and \
                self.return_type.java_name() or \
                'void'
        throws = \
            lpad(
                ' throws ',
                ', '.join([field.type.java_name()
                           for field in self.throws])
            )
        return """\
public %(return_type)s %(name)s(%(parameters)s)%(throws)s;""" % locals()

    def java_name(self):
        return lower_camelize(self.name)

    def __repr__(self):
        return self.java_declaration()
