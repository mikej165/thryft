from thryft.target.document import Document
from thryft.target.include import Include
from thryft.target.namespace import Namespace
from yutil import rpad


class JavaDocument(Document):
    def __repr__(self):
        headers = []
        for header in self.headers:
            if isinstance(header, Namespace):
                namespace = header
                if namespace.name.rsplit('.', 1)[-1] == 'native':
                    return ''
                if namespace.scope == '*' or namespace.scope == 'java':
                    headers.append('package ' + namespace.name + ';')
        for header in self.headers:
            if isinstance(header, Include):
                include = header
                if include.java_is_native():
                    continue
                if len(headers) == 1 and headers[0].startswith('package'):
                    headers.append('')
                headers.append(repr(include))
        headers = "\n".join(headers)

        definitions = \
            "\n\n".join([repr(definition)
                         for definition in self.definitions])

        return rpad(headers, "\n\n") + definitions + "\n"
