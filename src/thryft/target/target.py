 #@PydevCodeAnalysisIgnore
class Target(object):
    from thryft.target.base_types.binary_type import BinaryType
    from thryft.target.base_types.bool_type import BoolType
    from thryft.target.base_types.double_type import DoubleType
    from thryft.target.base_types.float_type import FloatType
    from thryft.target.base_types.i32_type import I32Type
    from thryft.target.base_types.i64_type import I64Type
    from thryft.target.base_types.string_type import StringType
    from thryft.target.compound_types.enum_type import EnumType
    from thryft.target.compound_types.exception_type import ExceptionType
    from thryft.target.compound_types.senum_type import SenumType
    from thryft.target.compound_types.struct_type import StructType
    from thryft.target.const import Const
    from thryft.target.container_types.list_type import ListType
    from thryft.target.container_types.map_type import MapType
    from thryft.target.container_types.set_type import SetType
    from thryft.target.document import Document
    from thryft.target.field import Field
    from thryft.target.function import Function
    from thryft.target.include import Include
    from thryft.target.namespace import Namespace
    from thryft.target.native_types.date_type import DateType
    from thryft.target.native_types.date_time_type import DateTimeType
    from thryft.target.native_types.decimal_type import DecimalType
    from thryft.target.service import Service
    from thryft.target.typedef import Typedef
