from thryft.generator.generator import Generator


 # @PydevCodeAnalysisIgnore
class PyGenerator(Generator):
    from thryft.generators.py.py_binary_type import PyBinaryType as BinaryType
    from thryft.generators.py.py_bool_type import PyBoolType as BoolType
    from thryft.generators.py.py_byte_type import PyByteType as ByteType
    from thryft.generators.py.py_double_type import PyDoubleType as DoubleType
    from thryft.generators.py.py_i16_type import PyI16Type as I16Type
    from thryft.generators.py.py_i32_type import PyI32Type as I32Type
    from thryft.generators.py.py_i64_type import PyI64Type as I64Type
    from thryft.generators.py.py_string_type import PyStringType as StringType
    from thryft.generators.py.py_enum_type import PyEnumType as EnumType
    from thryft.generators.py.py_exception_type import PyExceptionType as ExceptionType
    from thryft.generators.py.py_struct_type import PyStructType as StructType
    from thryft.generators.py.py_list_type import PyListType as ListType
    from thryft.generators.py.py_map_type import PyMapType as MapType
    from thryft.generators.py.py_set_type import PySetType as SetType
    from thryft.generators.py.py_document import PyDocument as Document
    from thryft.generators.py.py_field import PyField as Field
    from thryft.generators.py.py_function import PyFunction as Function
    from thryft.generators.py.py_include import PyInclude as Include
    from thryft.generators.py.py_service import PyService as Service
