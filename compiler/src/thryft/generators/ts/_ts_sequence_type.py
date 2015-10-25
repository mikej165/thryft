import os.path

from thryft.generators.ts._ts_container_type import _TsContainerType
from thryft.generators.ts.ts_struct_type import TsStructType
from yutil import decamelize


class _TsSequenceType(_TsContainerType):
    def ts_from_json(self, value):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'ts'
        assert class_name_split[2] == 'type'

        element_from_json = self.element_type.ts_from_json('json[i]')
        qname = self.ts_qname()
        return_value = 'sequence'
        if isinstance(self.element_type, TsStructType):
            return_value = "new Backbone.Collection<%s>(%s)" % (self.element_type.ts_qname(), return_value)
        return_value_type_qname = self.element_type.ts_qname() + '[]'
        return """function(json: any[]): %(qname)s { var sequence: %(return_value_type_qname)s = []; for (var i = 0; i < json.length; i++) { sequence.push(%(element_from_json)s); } return %(return_value)s; }(%(value)s)""" % locals()

    def ts_qname(self):
        if isinstance(self.element_type, TsStructType):
            return "Backbone.Collection<%s>" % self.element_type.ts_qname()
        else:
            return "%s[]" % self.element_type.ts_qname()

    def _ts_references_use(self, caller_file_abspath, caller_stack):
        if isinstance(self.element_type, TsStructType):
            return ["""/// <reference path="%s/backbone/backbone.d.ts" />""" % os.path.relpath(os.path.join(self._parent_generator().ts_share_dir_path, 'DefinitelyTyped'), os.path.dirname(caller_file_abspath)).replace(os.path.sep, '/')]
        else:
            return []

    def ts_to_json(self, value):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'ts'
        assert class_name_split[2] == 'type'

        if isinstance(self.element_type, TsStructType):
            value = value + '.models'
        array_qname = self.element_type.ts_qname() + '[]'
        element_to_json = self.element_type.ts_to_json("__inArray[__i]" % locals())
        type_name = class_name_split[1].capitalize()
        return """\
function (__inArray: %(array_qname)s): any[] { var __outArray: any[] = []; for (var __i = 0; __i < __inArray.length; __i++) { __outArray.push(%(element_to_json)s); } return __outArray; }(%(value)s)""" % locals()
