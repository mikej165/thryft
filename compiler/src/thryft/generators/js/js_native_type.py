from thryft.generator.native_type import NativeType
from thryft.generators.js._js_type import _JsType
from yutil import class_qname


class JsNativeType(NativeType, _JsType):
    def js_name(self):
        raise NotImplementedError(class_qname(self) + '.js_name')

    def js_qname(self, name=None, **kwds):
        raise NotImplementedError(class_qname(self) + '.js_qname')
