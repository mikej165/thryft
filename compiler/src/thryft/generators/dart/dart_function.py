from thryft.generator.function import Function
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct
from thryft.generators.dart.dart_struct_type import DartStructType
from yutil import upper_camelize


class DartFunction(Function, _DartNamedConstruct):
    class _DartRequestType(DartStructType):
        def __init__(self, parent_function):
            DartStructType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Request',
                parent=parent_function.parent
            )

            for parameter in parent_function.parameters:
                self.fields.append(
                    parameter.__class__(
                        annotations=parameter.annotations,
                        doc=parameter.doc,
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required,
                    )
                )

    class _DartResponseType(DartStructType):
        def __init__(self, parent_function):
            DartStructType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Response',
                parent=parent_function.parent
            )
            if parent_function.return_field is not None:
                self.fields.append(parent_function.return_field)

    def _dart_imports_definition(self, caller_stack):
        imports = []
        for parameter in self.parameters:
            imports.extend(parameter.dart_imports_use(caller_stack=caller_stack))
        if self.return_field is not None:
            imports.extend(self.return_field.type.dart_imports_use(caller_stack=caller_stack))
        return imports

    def _dart_imports_use(self, caller_stack):
        raise NotImplementedError

    def dart_request_type(self, **kwds):
        return self._DartRequestType(parent_function=self, **kwds)

    def dart_response_type(self, **kwds):
        return self._DartResponseType(parent_function=self, **kwds)
