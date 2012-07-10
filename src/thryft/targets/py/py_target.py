from thryft.target.target import Target


class PyTarget(Target):
    from thryft.target.namespace import Namespace #@UnusedImport
    from thryft.targets.py.base_types.py_bool_type import PyBoolType as BoolType #@UnusedImport
    from thryft.targets.py.base_types.py_numeric_type import PyNumericType as NumericType #@UnusedImport
    from thryft.targets.py.base_types.py_string_type import PyStringType as StringType #@UnusedImport
    from thryft.targets.py.compound_types.py_enum import PyEnum as Enum #@UnusedImport
    from thryft.targets.py.compound_types.py_exception import PyException as Exception #@UnusedImport
    from thryft.targets.py.compound_types.py_struct import PyStruct as Struct #@UnusedImport
    from thryft.targets.py.py_const import PyConst as Const #@UnusedImport
    from thryft.targets.py.container_types.py_list_type import PyListType as ListType #@UnusedImport
    from thryft.targets.py.container_types.py_map_type import PyMapType as MapType #@UnusedImport
    from thryft.targets.py.container_types.py_set_type import PySetType as SetType  #@UnusedImport
    from thryft.targets.py.py_document import PyDocument as Document #@UnusedImport
    from thryft.targets.py.py_field import PyField as Field #@UnusedImport
    from thryft.targets.py.py_function import PyFunction as Function #@UnusedImport
    from thryft.targets.py.py_include import PyInclude as Include #@UnusedImport
    from thryft.targets.py.py_service import PyService as Service #@UnusedImport
