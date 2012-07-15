from thryft.target.target import Target
from thryft.targets.thrift.thrift_base_type import ThriftBaseType


 #@PydevCodeAnalysisIgnore
class ThriftTarget(Target):
    from thryft.targets.thrift.compound_types.thrift_enum_type import ThriftEnumType as EnumType
    from thryft.targets.thrift.compound_types.thrift_exception_type import ThriftExceptionType as ExceptionType
    from thryft.targets.thrift.compound_types.thrift_senum_type import ThriftSenumType as SenumType
    from thryft.targets.thrift.compound_types.thrift_struct_type import ThriftStructType as StructType
    from thryft.targets.thrift.thrift_const import ThriftConst as Const
    from thryft.targets.thrift.container_types.thrift_list_type import ThriftListType as ListType
    from thryft.targets.thrift.container_types.thrift_map_type import ThriftMapType as MapType
    from thryft.targets.thrift.container_types.thrift_set_type import ThriftSetType as SetType
    from thryft.targets.thrift.thrift_document import ThriftDocument as Document
    from thryft.targets.thrift.thrift_field import ThriftField as Field
    from thryft.targets.thrift.thrift_function import ThriftFunction as Function
    from thryft.targets.thrift.thrift_include import ThriftInclude as Include
    from thryft.targets.thrift.thrift_namespace import ThriftNamespace as Namespace
    from thryft.targets.thrift.thrift_service import ThriftService as Service
    from thryft.targets.thrift.thrift_typedef import ThriftTypedef as Typedef

for __base_type_name in ('binary', 'double', 'float', 'i16', 'i32', 'i64', 'string'):
    __base_class_name = __base_type_name.capitalize() + 'Type'
    setattr(
        ThriftTarget,
        __base_class_name,
        type(
            __base_class_name,
            (getattr(Target, __base_class_name), ThriftBaseType),
            {}
        )
    )
