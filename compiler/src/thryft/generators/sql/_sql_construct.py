from yutil import class_qname


class _SqlConstruct(object):
    def sql_repr(self):
        raise NotImplementedError(class_qname(self) + '.sql_repr')
