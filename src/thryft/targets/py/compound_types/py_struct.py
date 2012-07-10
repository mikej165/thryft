from thryft.target.compound_types.struct import Struct
from yutil import indent


class PyStruct(Struct):
    def py_constructor(self):
        parameters = []
        for field in self.fields:
            if field.required:
                parameters.append(field.py_parameter())
        for field in self.fields:
            if not field.required:
                parameters.append(field.py_parameter())
        parameters = ', '.join(parameters)
        initializers = \
            "\n".join(indent(' ' * 4,
                [field.py_initializer() for field in self.fields]
            ))
        return """\
def __init__(self, %(parameters)s):
%(initializers)s
""" % locals()

    def py_getters(self):
        return [field.py_getter() for field in self.fields]

    def py_name(self):
        return self.name

    def __repr__(self):
        name = self.py_name()

        if len(self.fields) == 0:
            return """\
class %(name)s(object):
    pass
""" % locals()

        constructor = indent(' ' * 4, self.py_constructor())
        getters = "\n\n".join(indent(' ' * 4, self.py_getters()))
        return """\
class %(name)s(object):
%(constructor)s

%(getters)s""" % locals()
