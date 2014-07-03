import argparse
import os.path
import sys

MY_DIR_PATH = os.path.abspath(os.path.dirname(__file__))

try:
    import yutil
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(MY_DIR_PATH, '..', 'src')))
from yutil import upper_camelize


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--overwrite', action='store_true')
argument_parser.add_argument("language", nargs=1)
args = argument_parser.parse_args()


language = args.language[0]
language_upper_camelized = upper_camelize(language)


files = {}


files['__init__.py'] = ''


files["_%(language)s_base_type.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_type import _%(language_upper_camelized)sType


class _%(language_upper_camelized)sBaseType(_%(language_upper_camelized)sType):
    pass
""" % locals()


files["_%(language)s_compound_type.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_type import _%(language_upper_camelized)sType


class _%(language_upper_camelized)sCompoundType(_%(language_upper_camelized)sType):
    pass
""" % locals()


files["_%(language)s_construct.py" % locals()] = """\
class _%(language_upper_camelized)sConstruct(object):
    pass
""" % locals()


files["_%(language)s_container_type.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_type import _%(language_upper_camelized)sType


class _%(language_upper_camelized)sContainerType(_%(language_upper_camelized)sType):
    pass
""" % locals()


files["_%(language)s_named_construct.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_construct import _%(language_upper_camelized)sConstruct


class _%(language_upper_camelized)sNamedConstruct(_%(language_upper_camelized)sConstruct):
    pass
""" % locals()


files["_%(language)s_numeric_type.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_base_type import _%(language_upper_camelized)sBaseType


class _%(language_upper_camelized)sNumericType(_%(language_upper_camelized)sBaseType):
    pass
""" % locals()


files["_%(language)s_sequence_type.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_container_type import _%(language_upper_camelized)sContainerType


class _%(language_upper_camelized)sSequenceType(_%(language_upper_camelized)sContainerType):
    pass
""" % locals()


files["_%(language)s_type.py" % locals()] = """\
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class _%(language_upper_camelized)sType(_%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_binary_type.py" % locals()] = """\
from thryft.generators.%(language)s.%(language)s_string_type import %(language_upper_camelized)sStringType


class %(language_upper_camelized)sBinaryType(%(language_upper_camelized)sStringType):
    pass
""" % locals()


files["%(language)s_bool_type.py" % locals()] = """\
from thryft.generator.bool_type import BoolType
from thryft.generators.%(language)s._%(language)s_base_type import _%(language_upper_camelized)sBaseType


class %(language_upper_camelized)sBoolType(BoolType, _%(language_upper_camelized)sBaseType):
    pass
""" % locals()


files["%(language)s_byte_type.py" % locals()] = """\
from thryft.generator.byte_type import ByteType
from thryft.generators.%(language)s._%(language)s_numeric_type import _%(language_upper_camelized)sNumericType


class %(language_upper_camelized)sByteType(ByteType, _%(language_upper_camelized)sNumericType):
    pass
""" % locals()


files["%(language)s_const.py" % locals()] = """\
from thryft.generator.const import Const
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sConst(Const, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_document.py" % locals()] = """\
from thryft.generator.document import Document
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sDocument(Document, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_double_type.py" % locals()] = """\
from thryft.generator.double_type import DoubleType
from thryft.generators.%(language)s._%(language)s_numeric_type import _%(language_upper_camelized)sNumericType


class %(language_upper_camelized)sDoubleType(DoubleType, _%(language_upper_camelized)sNumericType):
    pass
""" % locals()


files["%(language)s_enum_type.py" % locals()] = """\
from thryft.generator.enum_type import EnumType
from thryft.generators.%(language)s._%(language)s_type import _%(language_upper_camelized)sType


class %(language_upper_camelized)sEnumType(EnumType, _%(language_upper_camelized)sType):
    pass
""" % locals()


files["%(language)s_exception_type.py" % locals()] = """\
from thryft.generator.exception_type import ExceptionType
from thryft.generators.%(language)s._%(language)s_compound_type import _%(language_upper_camelized)sCompoundType


class %(language_upper_camelized)sExceptionType(ExceptionType, _%(language_upper_camelized)sCompoundType):
    pass
""" % locals()


files["%(language)s_field.py" % locals()] = """\
from thryft.generator.field import Field
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sField(Field, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_function.py" % locals()] = """\
from thryft.generator.function import Function
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sFunction(Function, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_generator.py" % locals()] = """\
from thryft.generator.generator import Generator


class %(language_upper_camelized)sGenerator(Generator):
    from thryft.generators.%(language)s.%(language)s_binary_type import %(language_upper_camelized)sBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_bool_type import %(language_upper_camelized)sBoolType as BoolType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_byte_type import %(language_upper_camelized)sByteType as ByteType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_const import %(language_upper_camelized)sConst as Const  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_document import %(language_upper_camelized)sDocument as Document  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_double_type import %(language_upper_camelized)sDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_enum_type import %(language_upper_camelized)sEnumType as EnumType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_exception_type import %(language_upper_camelized)sExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_field import %(language_upper_camelized)sField as Field  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_function import %(language_upper_camelized)sFunction as Function  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_i16_type import %(language_upper_camelized)sI16Type as I16Type  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_i32_type import %(language_upper_camelized)sI32Type as I32Type  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_i64_type import %(language_upper_camelized)sI64Type as I64Type  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_include import %(language_upper_camelized)sInclude as Include  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_list_type import %(language_upper_camelized)sListType as ListType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_map_type import %(language_upper_camelized)sMapType as MapType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_native_type import %(language_upper_camelized)sNativeType as NativeType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_service import %(language_upper_camelized)sService as Service  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_set_type import %(language_upper_camelized)sSetType as SetType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_string_type import %(language_upper_camelized)sStringType as StringType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_struct_type import %(language_upper_camelized)sStructType as StructType  # @UnusedImport
    from thryft.generators.%(language)s.%(language)s_typedef import %(language_upper_camelized)sTypedef as Typedef  # @UnusedImport
""" % locals()


files["%(language)s_i16_type.py" % locals()] = """\
from thryft.generator.i16_type import I16Type
from thryft.generators.%(language)s._%(language)s_numeric_type import _%(language_upper_camelized)sNumericType


class %(language_upper_camelized)sI16Type(I16Type, _%(language_upper_camelized)sNumericType):
    pass
""" % locals()


files["%(language)s_i32_type.py" % locals()] = """\
from thryft.generator.i32_type import I32Type
from thryft.generators.%(language)s._%(language)s_numeric_type import _%(language_upper_camelized)sNumericType


class %(language_upper_camelized)sI32Type(I32Type, _%(language_upper_camelized)sNumericType):
    pass
""" % locals()


files["%(language)s_i64_type.py" % locals()] = """\
from thryft.generator.i64_type import I64Type
from thryft.generators.%(language)s._%(language)s_numeric_type import _%(language_upper_camelized)sNumericType


class %(language_upper_camelized)sI64Type(I64Type, _%(language_upper_camelized)sNumericType):
    pass
""" % locals()


files["%(language)s_include.py" % locals()] = """\
from thryft.generator.include import Include
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sInclude(Include, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_list_type.py" % locals()] = """\
from thryft.generator.list_type import ListType
from thryft.generators.%(language)s._%(language)s_sequence_type import _%(language_upper_camelized)sSequenceType


class %(language_upper_camelized)sListType(ListType, _%(language_upper_camelized)sSequenceType):
    pass
""" % locals()


files["%(language)s_map_type.py" % locals()] = """\
from thryft.generator.map_type import MapType
from thryft.generators.%(language)s._%(language)s_container_type import _%(language_upper_camelized)sContainerType


class %(language_upper_camelized)sMapType(MapType, _%(language_upper_camelized)sContainerType):
    pass
""" % locals()


files["%(language)s_native_type.py" % locals()] = """\
from thryft.generator.service import NativeType
from thryft.generators.%(language)s._%(language)s_type import _%(language_upper_camelized)sType


class %(language_upper_camelized)sNativeType(NativeType, _%(language_upper_camelized)sType):
    pass
""" % locals()


files["%(language)s_service.py" % locals()] = """\
from thryft.generator.service import Service
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sService(Service, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


files["%(language)s_set_type.py" % locals()] = """\
from thryft.generator.set_type import SetType
from thryft.generators.%(language)s._%(language)s_sequence_type import _%(language_upper_camelized)sSequenceType


class %(language_upper_camelized)sSetType(SetType, _%(language_upper_camelized)sSequenceType):
    pass
""" % locals()


files["%(language)s_string_type.py" % locals()] = """\
from thryft.generator.string_type import StringType
from thryft.generators.%(language)s._%(language)s_base_type import _%(language_upper_camelized)sBaseType


class %(language_upper_camelized)sStringType(StringType, _%(language_upper_camelized)sBaseType):
    pass
""" % locals()


files["%(language)s_struct_type.py" % locals()] = """\
from thryft.generator.struct_type import StructType
from thryft.generators.%(language)s._%(language)s_compound_type import _%(language_upper_camelized)sCompoundType


class %(language_upper_camelized)sStructType(StructType, _%(language_upper_camelized)sCompoundType):
    pass
""" % locals()


files["%(language)s_typedef.py" % locals()] = """\
from thryft.generator.typedef import Typedef
from thryft.generators.%(language)s._%(language)s_named_construct import _%(language_upper_camelized)sNamedConstruct


class %(language_upper_camelized)sTypedef(Typedef, _%(language_upper_camelized)sNamedConstruct):
    pass
""" % locals()


out_dir_path = os.path.abspath(os.path.join(MY_DIR_PATH, '..', 'src', 'thryft', 'generators', language))
if not os.path.isdir(out_dir_path):
    os.makedirs(out_dir_path)

for file_name, file_contents in files.iteritems():
    file_path = os.path.join(out_dir_path, file_name)
    if os.path.exists(file_path) and not args.overwrite:
        continue
    with open(file_path, 'w+b') as file_:
        file_.write(file_contents)
        print 'wrote', file_path

