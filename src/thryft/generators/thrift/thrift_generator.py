from thryft.generator.generator import Generator
from thryft.generators.thrift.thrift_base_type import ThriftBaseType


 #@PydevCodeAnalysisIgnore
class ThriftGenerator(Generator):
    from thryft.generators.thrift.compound_types.thrift_enum_type import ThriftEnumType as EnumType
    from thryft.generators.thrift.compound_types.thrift_exception_type import ThriftExceptionType as ExceptionType
    from thryft.generators.thrift.compound_types.thrift_struct_type import ThriftStructType as StructType
    from thryft.generators.thrift.thrift_const import ThriftConst as Const
    from thryft.generators.thrift.container_types.thrift_list_type import ThriftListType as ListType
    from thryft.generators.thrift.container_types.thrift_map_type import ThriftMapType as MapType
    from thryft.generators.thrift.container_types.thrift_set_type import ThriftSetType as SetType
    from thryft.generators.thrift.thrift_document import ThriftDocument as Document
    from thryft.generators.thrift.thrift_field import ThriftField as Field
    from thryft.generators.thrift.thrift_function import ThriftFunction as Function
    from thryft.generators.thrift.thrift_include import ThriftInclude as Include
    from thryft.generators.thrift.thrift_namespace import ThriftNamespace as Namespace
    from thryft.generators.thrift.thrift_service import ThriftService as Service
    from thryft.generators.thrift.thrift_typedef import ThriftTypedef as Typedef

for __base_type_name in ('binary', 'double', 'float', 'i16', 'i32', 'i64', 'string'):
    __base_class_name = __base_type_name.capitalize() + 'Type'
    setattr(
        ThriftGenerator,
        __base_class_name,
        type(
            __base_class_name,
            (getattr(Generator, __base_class_name), ThriftBaseType),
            {}
        )
    )
