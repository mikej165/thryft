from thryft.generator.document import Document
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlDocument(Document, _SqlNamedConstruct):
    pass
