from thryft.generator.typedef import Typedef
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct


class CppTypedef(Typedef, _CppNamedConstruct):
    def cpp_includes_definition(self):
        return self.type.cpp_includes_use()

    def cpp_includes_use(self):
        return self._parent_document().cpp_includes_use()

    def cpp_name(self):
        return self.name

    def cpp_repr(self):
        return "typedef %s %s;" % (self.type.cpp_qname(), self.cpp_name())
