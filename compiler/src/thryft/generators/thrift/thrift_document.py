from thryft.generator.document import Document
from thryft.generators.thrift._thrift_named_construct import _ThriftNamedConstruct


class ThriftDocument(Document, _ThriftNamedConstruct):
    def __repr__(self):
        sections = []
        for section in (
            self.comment is not None and repr(self.comment) or '',
            "\n".join([repr(include) for include in self.includes]),
            "\n".join([repr(namespace) for namespace in self.namespaces]),
        ):
            if len(section) > 0:
                sections.append(section)
        sections.extend([repr(definition) for definition in self.definitions])
        return "\n\n".join(sections)
