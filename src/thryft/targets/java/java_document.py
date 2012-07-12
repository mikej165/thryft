from thryft.target.document import Document
from yutil import rpad


class JavaDocument(Document):
    def __repr__(self):
        headers = []
        for namespace in self.namespaces:
            if namespace.scope == '*' or namespace.scope == 'java':
                headers.append('package ' + namespace.name + ';')
        for include in self.includes:
            if include.native:
                continue
            if len(headers) == 1 and headers[0].startswith('package'):
                headers.append('')
            headers.append(repr(include))
        headers = "\n".join(headers)

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])

        return rpad(headers, "\n\n") + definitions + "\n"
