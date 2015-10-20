from thryft.generator.function import Function
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct
from yutil import decamelize, indent, lower_camelize, lpad, pad


class TsFunction(Function, _TsNamedConstruct):
    def ts_name(self):
        return lower_camelize(self.name)

    def _ts_references_definition(self, **kwds):
        references = []
        for parameter in self.parameters:
            references.extend(parameter.ts_references_use(**kwds))
        if self.return_field is not None:
            references.extend(self.return_field.ts_references_use(**kwds))
        return references

    def ts_repr(self):
        for parameter in self.parameters:
            assert parameter.name != 'error', self.parent.name
            assert parameter.name != 'success', self.parent.name

        name = self.name
        ts_name = self.ts_name()

        parameters = [parameter.ts_parameter()
                      for parameter in self.parameters]

        async_call_setup = []
        sync_call_setup = []
        if len(self.parameters) > 0:
            parameters_to_json = []
            for parameter in self.parameters:
                parameter_json_name = parameter.name
                parameter_ts_name = parameter.ts_name()
                if parameter.id is not None:
                    parameter_json_name = str(parameter.id) + ':' + parameter_json_name
                parameter_to_json = """__jsonrpc_params["%(parameter_json_name)s"] = """ % locals() + parameter.type.ts_to_json("kwds.%(parameter_ts_name)s" % locals()) + ';'
                if not parameter.required:
                    parameter_to_json = indent(' ' * 4, parameter_to_json)
                    parameter_to_json = """\
if (typeof kwds.%(parameter_ts_name)s !== "undefined") {
%(parameter_to_json)s
}"""
                parameters_to_json.append(parameter_to_json)
            parameters_to_json = "\n".join(parameters_to_json)
            jsonrpc_params_setup = """\
var __jsonrpc_params: {[index: string]: any} = {};
%(parameters_to_json)s
""" % locals()
            async_call_setup.append(jsonrpc_params_setup)
            sync_call_setup.append(jsonrpc_params_setup)
            jsonrpc_params = '__jsonrpc_params'
        else:
            jsonrpc_params = '{}'

        async_parameters = list(parameters)
        async_parameters.append('error: (jqXHR: JQueryXHR, textStatus: string, errorThrown: string) => any')
        if self.return_field is not None:
            return_field_parameter = self.return_field.ts_parameter()
            async_parameters.append('success: (%(return_field_parameter)s) => void' % locals())
            return_value = self.return_field.type.ts_from_json('__response.result')
            sync_return_type_qname = self.return_field.type.ts_qname()
            sync_call_setup.append("var returnValue: %(sync_return_type_qname)s = null;" % locals())
            sync_return = "\n\n    return returnValue;"
            sync_return_value_assignment = indent(' ' * 12, """\
if (typeof __response.result !== "undefined") {
    returnValue = %(return_value)s;
} else {
    throw new Error(__response.error);
}""" % locals())
        else:
            async_parameters.append('success: () => void')
            return_value = ''
            sync_return = ''
            sync_return_type_qname = 'void'
            sync_return_value_assignment = indent(' ' * 12, """\
if (typeof __response.result === "undefined") {
    throw new Error(__response.error);
}""" % locals())
        async_call_setup = pad("\n", indent(' ' * 4, "\n".join(async_call_setup)), "\n")
        async_parameters = "kwds: {%s}" % ', '.join(async_parameters)
        sync_call_setup = pad("\n", indent(' ' * 4, "\n".join(sync_call_setup)), "\n")
        sync_parameters = "kwds: {%s}" % ', '.join(parameters) if len(parameters) > 0 else ''

        jsonrpc_url = '\'/api/jsonrpc/'
        if self.parent.name.endswith('Service'):
            jsonrpc_url += '_'.join(decamelize(self.parent.name).split('_')[:-1])
        else:
            jsonrpc_url += decamelize(self.parent.name)
        jsonrpc_url += '\''

        return """\
%(ts_name)sAsync(%(async_parameters)s): void {%(async_call_setup)s
    $.ajax({
        async:true,
        data:JSON.stringify({
            jsonrpc:'2.0',
            method:'%(name)s',
            params:%(jsonrpc_params)s,
            id:'1234'
        }),
        dataType:'json',
        error:function(jqXHR, textStatus, errorThrown) {
            kwds.error(jqXHR, textStatus, errorThrown);
        },
        mimeType:'application/json',
        type:'POST',
        success:function(__response) {
            if (typeof __response.result !== "undefined") {
                kwds.success(%(return_value)s);
            } else {
                kwds.error(null, __response.error.message, null);
            }
        },
        url:%(jsonrpc_url)s,
    });
}

%(ts_name)sSync(%(sync_parameters)s): %(sync_return_type_qname)s {%(sync_call_setup)s
    $.ajax({
        async:false,
        data:JSON.stringify({
            jsonrpc:'2.0',
            method:'%(name)s',
            params:%(jsonrpc_params)s,
            id:'1234'
        }),
        dataType:'json',
        error:function(jqXHR, textStatus, errorThrown) {
            throw new Error(errorThrown);
        },
        mimeType:'application/json',
        type:'POST',
        success:function(__response) {
%(sync_return_value_assignment)s
        },
        url:%(jsonrpc_url)s,
    });%(sync_return)s
}""" % locals()
