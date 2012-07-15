from thryft.target.service import Service
from thryft.targets.py.py_construct import PyConstruct
from yutil import indent


class PyService(Service, PyConstruct):
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
