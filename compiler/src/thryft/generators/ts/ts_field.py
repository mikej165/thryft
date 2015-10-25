from thryft.generator.field import Field
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct
from yutil import indent


class TsField(Field, _TsNamedConstruct):
    def ts_accessors(self):
        name = self.ts_name()
        type_qname = self.type.ts_qname()
        return """\
get %(name)s(): %(type_qname)s {
    return this.get('%(name)s');
}

set %(name)s(value: %(type_qname)s) {
    this.set('%(name)s', value);
}""" % locals()

    def ts_from_json(self):
        from_json = self.type.ts_from_json('json[fieldName]')
        name = self.name
        ts_name = self.ts_name()
        field_name_tests = ["fieldName == \"%(name)s\"" % locals()]
        if self.id is not None:
            id_ = self.id
            field_name_tests.append("fieldName == \"%(id_)d:%(name)s\"" % locals())
        field_name_tests = ' || '.join(field_name_tests)
        return """\
if (%(field_name_tests)s) {
    out.attributes.%(ts_name)s = %(from_json)s;
}""" % locals()

    def ts_name_constant(self):
        return '%s: "%s"' % (self.name.upper(), self.name)

    def ts_parameter(self):
        name = self.ts_name()
        optional = '?' if not self.required else ''
        type_qname = self.type.ts_qname()
        return """%(name)s%(optional)s: %(type_qname)s""" % locals()

    def _ts_references_use(self, **kwds):
        return self.type.ts_references_use(**kwds)

    def ts_to_json(self):
        ts_name = self.ts_name()
        json_name = self.name
        if self.id is not None:
            json_name = str(self.id) + ':' + json_name
        to_json = """json["%(json_name)s"] = """ % locals() + self.type.ts_to_json("this.%(ts_name)s" % locals()) + ';'
        if not self.required:
            to_json = indent(' ' * 4, to_json)
            to_json = """\
if (this.has("%(ts_name)s")) {
%(to_json)s
}""" % locals()
        return to_json
