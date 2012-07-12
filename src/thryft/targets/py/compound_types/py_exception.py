from thryft.target.compound_types.exception import Exception


class PyException(Exception):
    def py_name(self):
        return self.name

    def __repr__(self):
        name = self.py_name()
        return """\
class %(name)s(Exception):
    pass
""" % locals()
