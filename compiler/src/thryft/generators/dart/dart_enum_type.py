from thryft.generator.enum_type import EnumType
from thryft.generators.dart._dart_type import _DartType
from yutil import indent


class DartEnumType(EnumType, _DartType):
    def dart_from_core_type(self, value):
        name = self.dart_name()
        return "new %(name)s.fromName(%(value)s)" % locals()

    def _dart_imports_use(self, caller_stack):
        return self._parent_document().dart_imports_use(caller_stack)

    def dart_to_core_type(self, value):
        return value + '.name'

    def __repr__(self):
        assert len(self.enumerators) > 0
        name = self.dart_name()
        enumerator_definitions = \
            indent(' ' * 2, "\n".join(
               "static final %s = new %s._(\"%s\", %s);" % (
                   enumerator.name, name, enumerator.name, enumerator.value
               )
               for enumerator in self.enumerators
            ))
        enumerator_name_cases = \
            "\n".join(indent(' ' * 4, (
                "case \"%s\": return %s;" % (
                enumerator.name, enumerator.name
                )
                for enumerator in self.enumerators
            )))
        enumerator_names = \
            ', '.join(enumerator.name for enumerator in self.enumerators)
        return """\
class %(name)s {
%(enumerator_definitions)s
  final String name;
  final int value;

  static get enumerators => [%(enumerator_names)s];

  %(name)s._(this.name, this.value);

  factory %(name)s.fromName(String name) {
    switch (name) {
%(enumerator_name_cases)s
    }
  }
}""" % locals()
