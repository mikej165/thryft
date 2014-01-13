from thryft.generator.typedef import Typedef
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct


class CppTypedef(Typedef, _CppNamedConstruct):
    def cpp_includes_definition(self):
        return self.type.cpp_includes_use()

    def cpp_includes_use(self):
        parent = self.parent
        while not isinstance(parent, Document):
            parent = parent.parent
        return parent.cpp_includes_use()

    def __repr__(self):
        return "typedef %s %s;" % (self.type.cpp_qname(), self.cpp_name())
