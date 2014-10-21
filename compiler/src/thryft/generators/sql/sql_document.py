from thryft.generator.document import Document
from thryft.generators.sql._sql_named_construct import _SqlNamedConstruct


class SqlDocument(Document, _SqlNamedConstruct):
    def _save_to_file(self, out_file_path):
        return self._save_to_file_helper(self.sql_repr(), out_file_path)
