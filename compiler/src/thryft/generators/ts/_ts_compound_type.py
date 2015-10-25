import os.path

from thryft.generators.ts._ts_type import _TsType
from yutil import indent, lpad


class _TsCompoundType(_TsType):
    def __ts_constructor(self):
        attributes_type = \
            "{%s}" % ', '.join(field.ts_parameter()
                               for field in self.fields)
        return """\
constructor(attributes?: %(attributes_type)s) {
    super(attributes);
}""" % locals()

    def ts_from_json(self, value):
        qname = self.ts_qname()
        return "%(qname)s.fromThryftJSON(%(value)s)" % locals()

    def __ts_method_from_thryft_json(self):
        qname = self.ts_qname()
        if len(self.fields) == 0:
            return {'fromThryftJSON': """\
static fromThryftJSON(json: any): %(qname)s {
    return new %(qname)s;
}""" % locals()}

        fields_from_json = \
            lpad("\n", indent(' ' * 8, ' else '.join(
                field.ts_from_json() for field in self.fields
            )))
        return {'fromThryftJSON': """\
static fromThryftJSON(json: any): %(qname)s {
    var out: %(qname)s = new %(qname)s;
    for (var fieldName in json) {%(fields_from_json)s
    }
    return out;
}""" % locals()}

    def __ts_method_to_thryft_json(self):
        if len(self.fields) == 0:
            return {'toThryftJSON': """\
toThryftJSON(): any {
    return {};
}""" % locals()}

        fields_to_json = indent(' ' * 4, "\n".join(field.ts_to_json() for field in self.fields))
        return {'toThryftJSON': """\
toThryftJSON(): any {
    var json: {[index: string]: any} = {};
%(fields_to_json)s
    return json;
}""" % locals()}

    def __ts_methods(self):
        methods = {}
        methods.update(self.__ts_method_from_thryft_json())
        methods.update(self.__ts_method_to_thryft_json())
        return [methods[method_name] for method_name in sorted(methods.iterkeys())]

    def _ts_references_definition(self, caller_file_abspath, caller_stack):
        references = ["""/// <reference path="%s/backbone/backbone.d.ts" />""" % os.path.relpath(os.path.join(self._parent_generator().ts_document_root_dir_path, 'share', 'DefinitelyTyped'), os.path.dirname(caller_file_abspath)).replace(os.path.sep, '/')]
        for field in self.fields:
            references.extend(field.ts_references_use(caller_file_abspath=caller_file_abspath, caller_stack=caller_stack))
        return references

    def _ts_references_use(self, caller_file_abspath, caller_stack):
        return ["""/// <reference path="%s" />""" % os.path.relpath(self._parent_document().ts_path(), os.path.dirname(caller_file_abspath)).replace(os.path.sep, '/')]

    def ts_repr(self):
        accessors = indent(' ' * 4, "\n\n".join(field.ts_accessors() for field in self.fields))
        constructor = indent(' ' * 4, self.__ts_constructor())
        methods = "\n\n".join(indent(' ' * 4, self.__ts_methods()))
        name = self.ts_name()
        return """\
export class %(name)s extends Backbone.Model {
%(constructor)s

%(accessors)s

%(methods)s
}""" % locals()

    def ts_to_json(self, value):
        return "%(value)s.toThryftJSON()" % locals()
