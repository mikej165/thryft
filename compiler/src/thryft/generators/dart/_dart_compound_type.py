from thryft.generators.dart._dart_type import _DartType
from yutil import indent


class _DartCompoundType(_DartType):
    def _dart_method_getters(self):
        return dict((field.dart_name(), field.dart_getter())
                     for field in self.fields)

    def _dart_methods(self):
        methods_dict = {}
        methods_dict.update(self._dart_method_getters())
        methods_list = \
            [methods_dict[method_name]
             for method_name in sorted(methods_dict.iterkeys())]
        if len(self.fields) > 0:
            methods_list.insert(0, self._py_constructor())
        return methods_list

    def __repr__(self):
        sections = []
        sections.append(indent(' ' * 4, "\n".join(self._dart_methods())))
        sections = "\n\n".join(sections)
        name = self.py_name()
        return """\
class %(name)s {
%(sections)s
}""" % locals()
