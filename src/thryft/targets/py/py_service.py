from thryft.target.service import Service
from yutil import lpad, indent


class PyService(Service):
    def py_name(self):
        return self.name

    def __repr__(self):
        name = self.py_name()

        if len(self.functions) == 0:
            return """\
class %(name)s(object):
    pass
""" % locals()

        methods = \
            "\n".join(indent(' ' * 4,
                ["\n".join((
                     function.py_public_delegating_definition(),
                     function.py_protected_abstract_definition()
                 ))
                 for function in self.functions])
             )
        return """\
class %(name)s(object):
%(methods)s""" % locals()
