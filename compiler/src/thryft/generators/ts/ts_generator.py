import os.path

from thryft.generator.generator import Generator


class TsGenerator(Generator):
    from thryft.generators.ts.ts_binary_type import TsBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.ts.ts_bool_type import TsBoolType as BoolType  # @UnusedImport
    from thryft.generators.ts.ts_byte_type import TsByteType as ByteType  # @UnusedImport
    from thryft.generators.ts.ts_const import TsConst as Const  # @UnusedImport
    from thryft.generators.ts.ts_document import TsDocument as Document  # @UnusedImport
    from thryft.generators.ts.ts_double_type import TsDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.ts.ts_enum_type import TsEnumType as EnumType  # @UnusedImport
    from thryft.generators.ts.ts_exception_type import TsExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.ts.ts_field import TsField as Field  # @UnusedImport
    from thryft.generators.ts.ts_function import TsFunction as Function  # @UnusedImport
    from thryft.generators.ts.ts_i16_type import TsI16Type as I16Type  # @UnusedImport
    from thryft.generators.ts.ts_i32_type import TsI32Type as I32Type  # @UnusedImport
    from thryft.generators.ts.ts_i64_type import TsI64Type as I64Type  # @UnusedImport
    from thryft.generators.ts.ts_include import TsInclude as Include  # @UnusedImport
    from thryft.generators.ts.ts_list_type import TsListType as ListType  # @UnusedImport
    from thryft.generators.ts.ts_map_type import TsMapType as MapType  # @UnusedImport
    from thryft.generators.ts.ts_service import TsService as Service  # @UnusedImport
    from thryft.generators.ts.ts_set_type import TsSetType as SetType  # @UnusedImport
    from thryft.generators.ts.ts_string_type import TsStringType as StringType  # @UnusedImport
    from thryft.generators.ts.ts_struct_type import TsStructType as StructType  # @UnusedImport
    from thryft.generators.ts.ts_typedef import TsTypedef as Typedef  # @UnusedImport

    def __init__(self, ts_document_root_dir_path, **kwds):
        Generator.__init__(self, **kwds)
        self.__ts_document_root_dir_path = os.path.abspath(ts_document_root_dir_path)

    @property
    def ts_document_root_dir_path(self):
        return self.__ts_document_root_dir_path
