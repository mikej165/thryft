from thryft.generator.generator import Generator


 #@PydevCodeAnalysisIgnore
class JavaGenerator(Generator):
    from thryft.generators.java.base_types.java_bool_type import JavaBoolType as BoolType
    from thryft.generators.java.base_types.java_byte_type import JavaByteType as ByteType
    from thryft.generators.java.base_types.java_double_type import JavaDoubleType as DoubleType
    from thryft.generators.java.base_types.java_i16_type import JavaI16Type as I16Type
    from thryft.generators.java.base_types.java_i32_type import JavaI32Type as I32Type
    from thryft.generators.java.base_types.java_i64_type import JavaI64Type as I64Type
    from thryft.generators.java.base_types.java_string_type import JavaStringType as StringType
    from thryft.generators.java.compound_types.java_enum_type import JavaEnumType as EnumType
    from thryft.generators.java.compound_types.java_exception_type import JavaExceptionType as ExceptionType
    from thryft.generators.java.compound_types.java_struct_type import JavaStructType as StructType
    from thryft.generators.java.container_types.java_list_type import JavaListType as ListType
    from thryft.generators.java.container_types.java_map_type import JavaMapType as MapType
    from thryft.generators.java.container_types.java_set_type import JavaSetType as SetType
    from thryft.generators.java.java_document import JavaDocument as Document
    from thryft.generators.java.java_field import JavaField as Field
    from thryft.generators.java.java_function import JavaFunction as Function
    from thryft.generators.java.java_include import JavaInclude as Include
    from thryft.generators.java.java_service import JavaService as Service
    from thryft.generators.java.native_types.java_date_type import JavaDateType as DateType
    from thryft.generators.java.native_types.java_date_time_type import JavaDateTimeType as DateTimeType
    from thryft.generators.java.native_types.java_decimal_type import JavaDecimalType as DecimalType
