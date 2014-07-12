from thryft.generator.enum_type import EnumType
from thryft.generators.dart._dart_type import _DartType
from yutil import indent


class DartEnumType(EnumType, _DartType):
    def _dart_imports_use(self, caller_stack):
        return self._parent_document().dart_imports_use(caller_stack)

    def __repr__(self):
        name = self.dart_name()
        enumerator_definitions = \
            indent(' ' * 2, "\n".join(
               "static final %s = new %s._(%s);" % (enumerator.name, name, enumerator.value)
               for enumerator in self.enumerators
            ))
        enumerator_names = \
            ', '.join(enumerator.name for enumerator in self.enumerators)
        return """\
class %(name)s {
%(enumerator_definitions)s
  int value;

  static get enumerators => [%(enumerator_names)s];

  %(name)s._(this.value);
}""" % locals()
