from thryft.target.compound_types.enum_type import EnumType
from thryft.targets.py.py_compound_type import PyCompoundType
from yutil import indent, lpad, pad


class PyEnumType(EnumType, PyCompoundType):
    def py_check(self, value):
        return "isinstance(%(value)s, int)" % locals()

    def py_read_protocol(self):
        name = self.py_name()
        return "%(name)s.value_of(iprot.readString().strip().upper())" % locals()

    def py_write_protocol(self, value, depth=0):
        name = self.py_name()
        return "oprot.writeString([attr for attr in dir(%(name)s) if getattr(%(name)s, attr) == %(value)s][0])" % locals()

    def __repr__(self):
        name = self.py_name()

        enumerators = []
        value_of_statements = []
        if len(self.fields) > 0:
            enumerator_values = []
            for enumerator in self.fields:
                if enumerator.value is not None:
                    for enumerator in self.fields:
                        assert enumerator.value is not None
                        enumerator_values.append(enumerator.value)
            if len(enumerator_values) == 0:
                enumerator_values = [enumerator.id for enumerator in self.fields]

            for enumerator, enumerator_value in zip(self.fields, enumerator_values):
                enumerator_name = enumerator.name
                enumerators.append("%(enumerator_name)s = %(enumerator_value)u" % locals())
                value_of_statements.append("""\
if name == '%(enumerator_name)s' or name == '%(enumerator_value)u':
    return %(name)s.%(enumerator_name)s
""" % locals())
        enumerators = \
            pad("\n", "\n".join(indent(' ' * 4, enumerators)), "\n")
        value_of_statements = \
            lpad("\n", indent(' ' * 8, 'el'.join(value_of_statements)))
        return """\
class %(name)s(object):%(enumerators)s
    @classmethod
    def value_of(cls, name):%(value_of_statements)s
        raise ValueError(name)""" % locals()
