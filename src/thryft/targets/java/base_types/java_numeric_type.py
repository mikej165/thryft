from thryft.target.base_types.numeric_type import NumericType


class JavaNumericType(NumericType):
    __JAVA_BOXED_NAMES = {
        'byte': 'Byte',
        'double': 'Double',
        'float': 'Float',
        'i16': 'Short',
        'i32': 'Integer',
        'i64': 'Long'
    }

    __JAVA_NAMES = {
        'byte': 'byte',
        'double': 'double',
        'float': 'float',
        'i16': 'short',
        'i32': 'int',
        'i64': 'long'
    }

    def java_hashCode(self, value):
        if self.name == 'double':
            return "((int)(Double.doubleToLongBits(%(value)s) ^ (Double.doubleToLongBits(%(value)s) >>> 32)))" % locals()
        elif self.name == 'float':
            return "Float.floatToIntBits(%(value)s)" % locals()
        elif self.name == 'i32':
            return "((int)%(value)s)" % locals()
        elif self.name == 'i64':
            return "((int)(%(value)s ^ (%(value)s >>> 32)))" % locals()
        else:
            raise NotImplementedError(self.name)

    def java_is_reference(self):
        return False

    def java_name(self, boxed=False):
        if boxed:
            return self.__JAVA_BOXED_NAMES[self.name]
        else:
            return self.__JAVA_NAMES[self.name]

    def __repr__(self):
        return self.java_name()
