from thryft.generator.function import Function
from thryft.generators.java.compound_types.java_struct_type import \
    JavaStructType
from thryft.generators.java.java_field import JavaField
from thryft.generators.java.java_named_construct import JavaNamedConstruct
from yutil import lower_camelize, lpad, indent


class JavaFunction(Function, JavaNamedConstruct):
    class _JavaRequestType(JavaStructType):
        def __init__(self, parent_function, java_suppress_warnings=None, parameters=None):
            JavaStructType.__init__(
                self,
                java_class_modifiers='public final static',
                java_suppress_warnings=java_suppress_warnings,
                name=parent_function.java_name() + 'Request',
                parent=parent_function.parent
            )

            if parameters is None:
                parameters = parent_function.parameters
            for parameter in parameters:
                self.fields.append(
                    JavaField(
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required
                    )
                )

    class _JavaResponseType(JavaStructType):
        def __init__(self, parent_function, java_suppress_warnings=None):
            JavaStructType.__init__(
                self,
                java_class_modifiers='public final static',
                java_suppress_warnings=java_suppress_warnings,
                name=parent_function.java_name() + 'Response',
                parent=parent_function.parent
            )
            if parent_function.return_type is not None:
                self.fields.append(
                    JavaField(
                        name='return_value',
                        parent=self,
                        required=True,
                        type=parent_function.return_type
                    )
                )

        def _java_constructor_protocol(self):
            name = self.java_name()
            if len(self.fields) > 0:
                field = self.fields[0]
                field_initializer = lpad("\n", indent(' ' * 4, field.java_protocol_initializer()))
            else:
                field_initializer = ''
            return """\
public %(name)s(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {%(field_initializer)s
}""" % locals()

    def java_declaration(self):
        name = self.java_name()
        parameters = \
            ', '.join([repr(parameter)
                       for parameter in self.parameters])
        return_type_name = \
            self.return_type is not None and \
                self.return_type.java_declaration_name() or \
                'void'
        throws = \
            lpad(
                ' throws ',
                ', '.join([field.type.java_declaration_name()
                           for field in self.throws])
            )
        return """\
public %(return_type_name)s %(name)s(%(parameters)s)%(throws)s;""" % locals()

    def java_name(self):
        return lower_camelize(self.name)

    def java_request_type(self, **kwds):
        return self._JavaRequestType(parent_function=self, **kwds)

    def java_response_type(self, **kwds):
        return self._JavaResponseType(parent_function=self, **kwds)

    def __repr__(self):
        return self.java_declaration()
