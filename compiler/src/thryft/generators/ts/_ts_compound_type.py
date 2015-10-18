import os.path

from thryft.generators.ts._ts_type import _TsType
from yutil import indent


class _TsCompoundType(_TsType):
    def _ts_references_definition(self, caller_file_abspath, caller_stack):
        references = ["""/// <reference path="%s/backbone/backbone.d.ts" />""" % os.path.relpath(os.path.join(self._parent_generator().ts_document_root_dir_path, 'share', 'DefinitelyTyped'), os.path.dirname(caller_file_abspath)).replace(os.path.sep, '/')]
        for field in self.fields:
            references.extend(field.ts_references_use(caller_file_abspath=caller_file_abspath, caller_stack=caller_stack))
        return references

    def _ts_references_use(self, caller_file_abspath, caller_stack):
        return ["""/// <reference path="%s" />""" % os.path.relpath(self._parent_document().ts_path(), os.path.dirname(caller_file_abspath)).replace(os.path.sep, '/')]

    def ts_repr(self):
        accessors = indent(' ' * 4, "\n\n".join(field.ts_accessors() for field in self.fields))
        name = self.ts_name()
        return """\
export class %(name)s extends Backbone.Model{
%(accessors)s
}""" % locals()
