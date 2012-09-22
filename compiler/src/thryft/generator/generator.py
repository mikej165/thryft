 #@PydevCodeAnalysisIgnore
class Generator(object):
    from thryft.generator.base_types.bool_type import BoolType
    from thryft.generator.base_types.byte_type import ByteType
    from thryft.generator.base_types.double_type import DoubleType
    from thryft.generator.base_types.i16_type import I16Type
    from thryft.generator.base_types.i32_type import I32Type
    from thryft.generator.base_types.i64_type import I64Type
    from thryft.generator.base_types.string_type import StringType
    from thryft.generator.comment import Comment
    from thryft.generator.compound_types.enum_type import EnumType
    from thryft.generator.compound_types.exception_type import ExceptionType
    from thryft.generator.compound_types.struct_type import StructType
    from thryft.generator.const import Const
    from thryft.generator.container_types.list_type import ListType
    from thryft.generator.container_types.map_type import MapType
    from thryft.generator.container_types.set_type import SetType
    from thryft.generator.document import Document
    from thryft.generator.field import Field
    from thryft.generator.function import Function
    from thryft.generator.include import Include
    from thryft.generator.namespace import Namespace
    from thryft.generator.native_types.date_type import DateType
    from thryft.generator.native_types.date_time_type import DateTimeType
    from thryft.generator.native_types.decimal_type import DecimalType
    from thryft.generator.service import Service
    from thryft.generator.typedef import Typedef
