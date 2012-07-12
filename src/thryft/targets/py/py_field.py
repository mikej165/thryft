from thryft.target.container_types.list_type import ListType
from thryft.target.field import Field
from yutil import quote


class PyField(Field):
    def py_getter(self):
        name = self.py_name()
        return """\
@property
def %(name)s(self):
    return self.__%(name)s
""" % locals()

    def py_name(self):
        return self.name

    def py_initializer(self):
        lhs = 'self.__' + self.py_name()
        rhs = self.py_name()
        if isinstance(self.type, ListType):
            rhs = "%(rhs)s is not None and tuple(%(rhs)s) or None" % locals()
        return "%(lhs)s = %(rhs)s" % locals()

    def py_parameter(self):
        if not self.required:
            if self.value is not None:
                return self.py_name() + '=' + str(self.py_value())
            else:
                return self.py_name() + '=None'
        else:
            return self.py_name()

    def py_value(self):
        if self.value is None:
            return None
        if isinstance(self.value, str):
            return quote(self.value)
        else:
            return self.value

    def __repr__(self):
        return self.py_parameter()
