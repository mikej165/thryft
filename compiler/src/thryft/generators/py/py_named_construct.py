from thryft.generators.py.py_construct import PyConstruct


class PyNamedConstruct(PyConstruct):
    def py_name(self):
        return getattr(self, 'name')

    def py_qname(self):
        if self.parent is None:
            return self.name
        from thryft.generators.py.py_document import PyDocument
        parent_document = self.parent
        while not isinstance(parent_document, PyDocument):
            parent_document = parent_document.parent
        parent_document_namespaces_by_scope = parent_document.namespaces_by_scope
        for scope in ('py', '*'):
            namespace = parent_document_namespaces_by_scope.get(scope)
            if namespace is not None:
                return '.'.join((namespace.name, parent_document.name, self.py_name()))
        return '.'.join((parent_document.name, self.py_name()))
