from thryft.generator.service import Service
from thryft.generators.py.py_named_construct import PyNamedConstruct
from yutil import indent


class PyService(Service, PyNamedConstruct):
    def py_imports(self, caller_stack=None):
        imports = []
        for function in self.functions:
            imports.extend(function.py_imports(caller_stack=caller_stack))
        return list(set(imports))

    def __repr__(self):
        name = self.py_name()

        if len(self.functions) == 0:
            return """\
class %(name)s(object):
    pass
""" % locals()

        methods = \
            "\n\n".join(indent(' ' * 4,
                ["\n".join((
                     function.py_public_delegating_definition(),
                     function.py_protected_abstract_definition()
                 ))
                 for function in self.functions])
             )
        return """\
class %(name)s(object):
%(methods)s""" % locals()
