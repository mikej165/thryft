from thryft.target.compound_types.enum import Enum
from yutil import indent


class PyEnum(Enum):
    def java_name(self):
        return self.name

    def __repr__(self):
        name = self.java_name()
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
