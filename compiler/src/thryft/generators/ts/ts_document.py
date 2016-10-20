import os.path

from thryft.generator.document import Document
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct
from yutil import indent


class TsDocument(Document, _TsNamedConstruct):
    def __init__(self, **kwds):
        Document.__init__(self, **kwds)
        self.__ts_path = None

    def _save_to_dir(self, out_dir_path):
        assert out_dir_path == self._parent_generator().ts_out_dir_path
        return self._save_to_file(self.ts_path())

    def _save_to_file(self, out_file_path):
        assert out_file_path == self.ts_path(), "%s vs. %s" % (out_file_path, self.ts_path())
        return self._save_to_file_helper(self.ts_repr(), out_file_path)

    def ts_path(self):
        if self.__ts_path is None:
            self.__ts_path = \
                os.path.join(
                    self._parent_generator().ts_out_dir_path,
                    self.namespace_by_scope(('ts', '*')).name.replace('.', os.path.sep),
                    self.name + '.ts'
                )
        return self.__ts_path

    def _ts_references_definition(self, **kwds):
        references = []
        for definition in self.definitions:
            references.extend(definition.ts_references_definition(**kwds))
        return references

    def ts_repr(self):
        definitions = \
            "\n\n".join(definition.ts_repr()
                         for definition in self.definitions)
        if len(definitions) == 0:
            return ''

        sections = []

        references = "\n".join(sorted(list(set(self.ts_references_definition(self.ts_path())))))
        if len(references) > 0:
            sections.append(references)

        try:
            module_qname = self.namespace_by_scope(('ts', '*')).name
            definitions = indent(' ' * 4, definitions)
            definitions = """\
module %(module_qname)s {
%(definitions)s
}""" % locals()
        except KeyError:
            definitions = definitions
        sections.append(definitions)
        return "\n".join(sections) + "\n"
