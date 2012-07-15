from thryft.target.document import Document
from thryft.targets.java.java_construct import JavaConstruct
from yutil import rpad


class JavaDocument(Document, JavaConstruct):
    def __repr__(self):
        headers = []
        for namespace in self.namespaces:
            if namespace.scope == '*' or namespace.scope == 'java':
                headers.append('package ' + namespace.name + ';')
        for include in self.includes:
            if len(headers) == 1 and headers[0].startswith('package'):
                headers.append('')
            headers.append(repr(include))
        headers = "\n".join(headers)

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])

        return rpad(headers, "\n\n") + definitions + "\n"
