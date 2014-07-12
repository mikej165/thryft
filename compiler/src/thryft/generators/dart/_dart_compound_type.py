from thryft.generators.dart._dart_type import _DartType
from yutil import indent, lpad


class _DartCompoundType(_DartType):
    def _dart_constructor(self):
        name = self.dart_name()
        field_qualified_names = \
            ', '.join('this.' + field.dart_name()
                      for field in self.fields)
        return """\
%(name)s(%(field_qualified_names)s);""" % locals()

    def _dart_imports_definition(self, caller_stack):
        imports = []
        for field in self.fields:
            imports.extend(field.dart_imports_use(caller_stack))
        return imports

    def _dart_imports_use(self, caller_stack):
        return self._parent_document().dart_imports_use(caller_stack)

    def _dart_member_declarations(self):
        return [field.dart_member_declaration()
                for field in self.fields]

    def _dart_methods(self):
        methods_dict = {}
        methods_list = \
            [methods_dict[method_name]
             for method_name in sorted(methods_dict.iterkeys())]
        if len(self.fields) > 0:
            methods_list.insert(0, self._dart_constructor())
        return methods_list

    def __repr__(self):
        name = self.dart_name()
        sections = []
        sections.append(indent(' ' * 2, "\n".join(self._dart_member_declarations())))
        sections.append(indent(' ' * 2, "\n".join(self._dart_methods())))
        sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
        return """\
class %(name)s {%(sections)s
}""" % locals()
