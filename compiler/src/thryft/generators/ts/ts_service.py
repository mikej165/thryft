import os.path

from thryft.generator.service import Service
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct
from yutil import indent, lpad


class TsService(Service, _TsNamedConstruct):
    def _ts_references_definition(self, caller_file_abspath, caller_stack):
        references = ["""/// <reference path="%s/jquery/jquery.d.ts" />""" % os.path.relpath(os.path.join(self._parent_generator().ts_share_dir_path, 'DefinitelyTyped'), os.path.dirname(caller_file_abspath)).replace(os.path.sep, '/')]
        for function in self.functions:
            references.extend(function.ts_references_definition(caller_file_abspath=caller_file_abspath, caller_stack=caller_stack))
        return references

    def ts_repr(self):
        methods = \
            lpad("\n", "\n\n".join(indent(' ' * 4,
                (function.ts_repr()
                 for function in self.functions)
            )))
        name = self.ts_name()
        return """\
export class %(name)s {%(methods)s
}""" % locals()
