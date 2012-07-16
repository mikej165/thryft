from thryft.target.target import Target


 #@PydevCodeAnalysisIgnore
class PyTarget(Target):
    from thryft.targets.py.base_types.py_bool_type import PyBoolType as BoolType
    from thryft.targets.py.base_types.py_double_type import PyDoubleType as DoubleType
    from thryft.targets.py.base_types.py_i16_type import PyI16Type as I16Type
    from thryft.targets.py.base_types.py_i32_type import PyI32Type as I32Type
    from thryft.targets.py.base_types.py_i64_type import PyI64Type as I64Type
    from thryft.targets.py.base_types.py_string_type import PyStringType as StringType
    from thryft.targets.py.compound_types.py_enum_type import PyEnumType as EnumType
    from thryft.targets.py.compound_types.py_exception_type import PyExceptionType as ExceptionType
    from thryft.targets.py.compound_types.py_struct_type import PyStructType as StructType
    from thryft.targets.py.native_types.py_date_type import PyDateType as DateType
    from thryft.targets.py.native_types.py_date_time_type import PyDateTimeType as DateTimeType
    from thryft.targets.py.native_types.py_decimal_type import PyDecimalType as DecimalType
    from thryft.targets.py.container_types.py_list_type import PyListType as ListType
    from thryft.targets.py.container_types.py_map_type import PyMapType as MapType
    from thryft.targets.py.container_types.py_set_type import PySetType as SetType
    from thryft.targets.py.py_document import PyDocument as Document
    from thryft.targets.py.py_field import PyField as Field
    from thryft.targets.py.py_function import PyFunction as Function
    from thryft.targets.py.py_include import PyInclude as Include
    from thryft.targets.py.py_service import PyService as Service
