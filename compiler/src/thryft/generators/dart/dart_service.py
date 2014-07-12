from thryft.generator.service import Service
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct


class DartService(Service, _DartNamedConstruct):
    def _dart_imports_definition(self, caller_stack):
        imports = []
        imports.append("import 'dart:convert' show JSON;")
        for function in self.functions:
            imports.extend(function.dart_imports_definition(caller_stack=caller_stack))
        return imports

    def __repr__(self):
        message_types = []
        for function in self.functions:
            message_types.append(function.dart_request_type())
            message_types.append(function.dart_response_type())
        return "\n\n".join(repr(message_type)
                           for message_type in message_types)
