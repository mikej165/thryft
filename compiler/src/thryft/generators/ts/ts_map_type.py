from thryft.generator.map_type import MapType
from thryft.generators.ts._ts_container_type import _TsContainerType


class TsMapType(MapType, _TsContainerType):
    def ts_from_json(self, value):
        key_from_json = self.key_type.ts_from_json('key')
        qname = self.ts_qname()
        value_from_json = self.value_type.ts_from_json('json[key]')
        return """function (json: any): %(qname)s { var map: any = {}; for (var key in json) { map[%(key_from_json)s] = %(value_from_json)s; } return map; }(%(value)s)""" % locals()

    def ts_qname(self):
        return "{[index: %s]: %s}" % (self.key_type.ts_qname(), self.value_type.ts_qname())

    def ts_to_json(self, value):
        key_to_json = self.key_type.ts_to_json('key')
        qname = self.ts_qname()
        return_type_qname = "{[index: string]: %s}" % self.value_type.ts_qname()
        value_to_json = self.value_type.ts_to_json('json[key]')
        return """\
function (value: %(qname)s): %(return_type_qname)s { var outObject: %(return_type_qname)s = {}; for (var key in value) { outObject[%(key_to_json)s] = %(value_to_json)s; } return outObject; }(%(value)s)""" % locals()
