from thryft.generator.compound_types.enum_type import EnumType
from thryft.generators.py.py_type import PyType
from yutil import indent, lpad, pad


class PyEnumType(EnumType, PyType):
    def py_check(self, value):
        qname = self.py_qname()
        return "isinstance(%(value)s, %(qname)s)" % locals()

    def _py_imports_use(self, caller_stack):
        return ['import ' + self.py_qname().rsplit('.', 1)[0]]

    def py_read_protocol(self):
        qname = self.py_qname()
        return "%(qname)s.value_of(iprot.readString().strip().upper())" % locals()

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.writeString([attr for attr in dir(%(qname)s) if getattr(%(qname)s, attr) == %(value)s][0])" % locals()

    def __repr__(self):
        name = self.py_name()

        enumerators = []
        enumerator_placeholders = []
        value_of_statements = []
        if len(self.enumerators) > 0:
            enumerator_values = []
            for enumerator in self.enumerators:
                if enumerator.value is not None:
                    for enumerator in self.enumerators:
                        assert enumerator.value is not None
                        enumerator_values.append(enumerator.value)
            if len(enumerator_values) == 0:
                enumerator_values = [enumerator.id for enumerator in self.enumerators]

            for enumerator, enumerator_value in zip(self.enumerators, enumerator_values):
                enumerator_name = enumerator.name
                enumerator_placeholders.append("%(enumerator_name)s = None" % locals())
                enumerators.append("%(name)s.%(enumerator_name)s = %(name)s('%(enumerator_name)s', %(enumerator_value)u)" % locals())
                value_of_statements.append("""\
if name == '%(enumerator_name)s' or name == '%(enumerator_value)u':
    return getattr(%(name)s, '%(enumerator_name)s')
""" % locals())
        enumerators = \
            lpad("\n\n", "\n".join(enumerators))
        enumerator_placeholders = \
            pad("\n", "\n".join(indent(' ' * 4,
                enumerator_placeholders
            )), "\n")
        value_of_statements = \
            lpad("\n", indent(' ' * 8, 'el'.join(value_of_statements)))
        return """\
class %(name)s(object):%(enumerator_placeholders)s
    def __init__(self, name, value):
        object.__init__(self)
        self.__name = name
        self.__value = value

    def __int__(self):
        return self.__value

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name

    @classmethod
    def value_of(cls, name):%(value_of_statements)s
        raise ValueError(name)%(enumerators)s""" % locals()
