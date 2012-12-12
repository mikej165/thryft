from thryft.generators.java._java_construct import _JavaConstruct


class _JavaNamedConstruct(_JavaConstruct):
    def java_name(self, boxed=False):
        return getattr(self, 'name')

    def java_qname(self, boxed=False):
        from thryft.generator.document import Document
        parent_document = self.parent
        while parent_document is not None and not isinstance(parent_document, Document):
            parent_document = parent_document.parent
        if parent_document is None:
            return self.java_name(boxed=boxed)
        namespaces_by_scope = parent_document.namespaces_by_scope
        for scope in ('java', '*'):
            namespace = namespaces_by_scope.get(scope)
            if namespace is not None:
                return namespace.name + '.' + self.java_name(boxed=boxed)
        return self.java_name(boxed=boxed)
