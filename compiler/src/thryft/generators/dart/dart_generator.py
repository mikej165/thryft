from thryft.generator.generator import Generator


class DartGenerator(Generator):
    from thryft.generators.dart.dart_binary_type import DartBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.dart.dart_bool_type import DartBoolType as BoolType  # @UnusedImport
    from thryft.generators.dart.dart_byte_type import DartByteType as ByteType  # @UnusedImport
    from thryft.generators.dart.dart_const import DartConst as Const  # @UnusedImport
    from thryft.generators.dart.dart_document import DartDocument as Document  # @UnusedImport
    from thryft.generators.dart.dart_double_type import DartDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.dart.dart_enum_type import DartEnumType as EnumType  # @UnusedImport
    from thryft.generators.dart.dart_exception_type import DartExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.dart.dart_field import DartField as Field  # @UnusedImport
    from thryft.generators.dart.dart_function import DartFunction as Function  # @UnusedImport
    from thryft.generators.dart.dart_i16_type import DartI16Type as I16Type  # @UnusedImport
    from thryft.generators.dart.dart_i32_type import DartI32Type as I32Type  # @UnusedImport
    from thryft.generators.dart.dart_i64_type import DartI64Type as I64Type  # @UnusedImport
    from thryft.generators.dart.dart_include import DartInclude as Include  # @UnusedImport
    from thryft.generators.dart.dart_list_type import DartListType as ListType  # @UnusedImport
    from thryft.generators.dart.dart_map_type import DartMapType as MapType  # @UnusedImport
    from thryft.generators.dart.dart_native_type import DartNativeType as NativeType  # @UnusedImport
    from thryft.generators.dart.dart_service import DartService as Service  # @UnusedImport
    from thryft.generators.dart.dart_set_type import DartSetType as SetType  # @UnusedImport
    from thryft.generators.dart.dart_string_type import DartStringType as StringType  # @UnusedImport
    from thryft.generators.dart.dart_struct_type import DartStructType as StructType  # @UnusedImport
    from thryft.generators.dart.dart_typedef import DartTypedef as Typedef  # @UnusedImport
