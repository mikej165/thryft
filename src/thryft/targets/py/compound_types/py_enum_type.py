from thryft.target.compound_types.enum_type import EnumType
from thryft.targets.py.py_compound_type import PyCompoundType
from yutil import indent


class PyEnumType(EnumType, PyCompoundType):
    def __repr__(self):
        name = self.py_name()
        if len(self.fields) == 0:
            return """\
class %(name)s(object):
    pass"""

        for enumerator in self.fields:
            if enumerator.value is not None:
                enumerators = \
                    "\n".join(indent(' ' * 4,
                        ["%s = %u" % (enumerator.name, enumerator.value)
                         for enumerator in self.fields]
                    ))
                return """\
class %(name)s(object):
%(enumerators)s""" % locals()

        enumerators = \
            "\n".join(indent(' ' * 4,
                ["%s = %u" % (enumerator.name, enumerator.id)
                  for enumerator in self.fields]
            ))
        return """\
class %(name)s(object):
%(enumerators)s""" % locals()
