#-------------------------------------------------------------------------------
# Cojsright (c) 2013, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above cojsright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above cojsright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
#-------------------------------------------------------------------------------

from thryft.generator.generator import Generator


 # @JsdevCodeAnalysisIgnore
class JsGenerator(Generator):
    from thryft.generators.js.js_binary_type import JsBinaryType as BinaryType
    from thryft.generators.js.js_bool_type import JsBoolType as BoolType
    from thryft.generators.js.js_byte_type import JsByteType as ByteType
    from thryft.generators.js.js_double_type import JsDoubleType as DoubleType
    from thryft.generators.js.js_i16_type import JsI16Type as I16Type
    from thryft.generators.js.js_i32_type import JsI32Type as I32Type
    from thryft.generators.js.js_i64_type import JsI64Type as I64Type
    from thryft.generators.js.js_string_type import JsStringType as StringType
    from thryft.generators.js.js_enum_type import JsEnumType as EnumType
    from thryft.generators.js.js_exception_type import JsExceptionType as ExceptionType
    from thryft.generators.js.js_struct_type import JsStructType as StructType
    from thryft.generators.js.js_list_type import JsListType as ListType
    from thryft.generators.js.js_map_type import JsMapType as MapType
    from thryft.generators.js.js_set_type import JsSetType as SetType
    from thryft.generators.js.js_document import JsDocument as Document
    from thryft.generators.js.js_field import JsField as Field
    from thryft.generators.js.js_function import JsFunction as Function
    from thryft.generators.js.js_include import JsInclude as Include
    from thryft.generators.js.js_service import JsService as Service
