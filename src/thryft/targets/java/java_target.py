from thryft.target.target import Target


 #@PydevCodeAnalysisIgnore
class JavaTarget(Target):
    from thryft.targets.java.base_types.java_bool_type import JavaBoolType as BoolType
    from thryft.targets.java.base_types.java_double_type import JavaDoubleType as DoubleType
    from thryft.targets.java.base_types.java_float_type import JavaFloatType as FloatType
    from thryft.targets.java.base_types.java_i16_type import JavaI16Type as I16Type
    from thryft.targets.java.base_types.java_i32_type import JavaI32Type as I32Type
    from thryft.targets.java.base_types.java_i64_type import JavaI64Type as I64Type
    from thryft.targets.java.base_types.java_string_type import JavaStringType as StringType
    from thryft.targets.java.compound_types.java_enum_type import JavaEnumType as EnumType
    from thryft.targets.java.compound_types.java_exception_type import JavaExceptionType as ExceptionType
    from thryft.targets.java.compound_types.java_struct_type import JavaStructType as StructType
    from thryft.targets.java.container_types.java_list_type import JavaListType as ListType
    from thryft.targets.java.container_types.java_map_type import JavaMapType as MapType
    from thryft.targets.java.container_types.java_set_type import JavaSetType as SetType
    from thryft.targets.java.java_document import JavaDocument as Document
    from thryft.targets.java.java_field import JavaField as Field
    from thryft.targets.java.java_function import JavaFunction as Function
    from thryft.targets.java.java_include import JavaInclude as Include
    from thryft.targets.java.java_service import JavaService as Service
    from thryft.targets.java.native_types.java_date_type import JavaDateType as DateType
    from thryft.targets.java.native_types.java_date_time_type import JavaDateTimeType as DateTimeType
    from thryft.targets.java.native_types.java_decimal_type import JavaDecimalType as DecimalType
