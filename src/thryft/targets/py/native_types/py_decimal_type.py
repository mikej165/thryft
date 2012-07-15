from thryft.target.native_types.decimal_type import DecimalType
from thryft.targets.py.py_native_type import PyNativeType


class PyDecimalType(DecimalType, PyNativeType):
    def py_from_json_object(self, json_object_variable_name):
        return "Decimal(%(json_object_variable_name)s)" % locals()

    def py_imports(self):
        return ['from decimal import Decimal']

    def py_name(self):
        return 'java.math.BigDecimal'
