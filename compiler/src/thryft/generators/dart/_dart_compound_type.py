from thryft.generators.dart._dart_type import _DartType
from yutil import indent, lpad, pad


class _DartCompoundType(_DartType):
    def _dart_constructor_from_json(self):
        name = self.dart_name()
        return """\
%(name)s.fromJson(String json) : this.fromMap(JSON.decode(json));""" % locals()

    def _dart_constructor_from_map(self):
        field_initializers = []
        for field in self.fields:
            field_dart_name = field.dart_name()
            field_name = field.name
            field_from_core_type = field.type.dart_from_core_type('map["%(field_name)s"]' % locals())
            field_initializer = """\
if (map["%(field_name)s"] != null) {
  this.%(field_dart_name)s = %(field_from_core_type)s;
}""" % locals()
            if field.required:
                field_initializer += """\
 else {
  throw new Exception("missing %(field_name)s");
}""" % locals()
            field_initializers.append(field_initializer)
        field_initializers = \
            lpad("\n", "\n".join(indent(' ' * 2, field_initializers)))
        name = self.dart_name()
        return """\
%(name)s.fromMap(Map<String, Object> map) {%(field_initializers)s
}""" % locals()

    def _dart_constructor_total(self):
        name = self.dart_name()
        parameters = pad('{', ', '.join(field.dart_parameter() for field in self.fields), '}')
        initializers = \
            lpad(' : ', ', '.join(
                field.dart_initializer()
                for field in self.fields
            ))
        return """\
%(name)s(%(parameters)s)%(initializers)s;""" % locals()

    def dart_from_core_type(self, value):
        name = self.dart_name()
        return "new %(name)s.fromMap(%(value)s)" % locals()

    def _dart_imports_definition(self, caller_stack):
        imports = []
        imports.append("import 'dart:convert' show JSON;")
        for field in self.fields:
            imports.extend(field.dart_imports_use(caller_stack))
        return imports

    def _dart_imports_use(self, caller_stack):
        return self._parent_document().dart_imports_use(caller_stack)

    def _dart_member_declarations(self):
        return [field.dart_member_declaration()
                for field in self.fields]

    def _dart_method_to_json(self):
        return {'toJson': """\
String toJson() {
  return JSON.encode(this.toMap());
}"""}

    def _dart_method_to_map(self):
        field_puts = []
        for field in self.fields:
            field_name = field.name
            field_dart_name = field.dart_name()
            field_put = """map["%(field_name)s"] = this.%(field_dart_name)s;""" % locals()
            if not field.required:
                field_put = """\
if (this.%(field_dart_name)s != null) {
  %(field_put)s
}""" % locals()
            field_puts.append(field_put)
        field_puts = \
            lpad("\n", "\n".join(indent(' ' * 2, field_puts)))
        return {'toMap':  """\
Map<String, Object> toMap() {
  Map<String, Object> map = new Map<String, Object>();%(field_puts)s
  return map;
}""" % locals()}

    def _dart_methods(self):
        methods_dict = {}
        methods_dict.update(self._dart_method_to_json())
        methods_dict.update(self._dart_method_to_map())
        methods_list = []
        if len(self.fields) > 0:
            methods_list.append(self._dart_constructor_total())
        methods_list.append(self._dart_constructor_from_json())
        methods_list.append(self._dart_constructor_from_map())
        methods_list.extend(
            methods_dict[method_name]
            for method_name in sorted(methods_dict.iterkeys())
        )
        return methods_list

    def dart_to_core_type(self, value):
        return value + '.toMap()'

    def __repr__(self):
        name = self.dart_name()
        sections = []
        sections.append(indent(' ' * 2, "\n".join(self._dart_member_declarations())))
        sections.append(indent(' ' * 2, "\n\n".join(self._dart_methods())))
        sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
        return """\
class %(name)s {%(sections)s
}""" % locals()
