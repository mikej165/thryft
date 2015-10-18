from thryft.generators.ts._ts_container_type import _TsContainerType
from yutil import decamelize


class _TsSequenceType(_TsContainerType):
    def ts_from_json(self, value):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'ts'
        assert class_name_split[2] == 'type'

        element_from_json = self.element_type.ts_from_json('json[i]')
        qname = self.ts_qname()
        return """function(json: any): %(qname)s { var sequence: %(qname)s = []; for (var i = 0; i < json.length; i++) { sequence.push(%(element_from_json)s); } return sequence; }(%(value)s)""" % locals()

    def ts_qname(self):
        return "%s[]" % self.element_type.ts_qname()

    def ts_to_json(self, value):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'ts'
        assert class_name_split[2] == 'type'

        element_to_json = self.element_type.ts_to_json("__inArray[__i]" % locals())
        qname = self.ts_qname()
        type_name = class_name_split[1].capitalize()
        return """\
function (__inArray: %(qname)s): any { var __outArray: %(qname)s = []; for (var __i = 0; __i < __inArray.length; __i++) { __outArray.push(%(element_to_json)s); } return __outArray; }(%(value)s)""" % locals()
