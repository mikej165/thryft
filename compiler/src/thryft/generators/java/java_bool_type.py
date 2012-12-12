from thryft.generator.bool_type import BoolType
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaBoolType(BoolType, _JavaBaseType):
    def java_default_value(self):
        return 'false'

    def java_from_string(self, value):
        return """(%(value)s.equals("1") || %(value)s.equalsIgnoreCase("true"))""" % locals()

    def java_hash_code(self, value):
        return "(%(value)s ? 1 : 0)" % locals()

    def java_name(self, boxed=False):
        return boxed and 'Boolean' or 'boolean'

    def java_to_string(self, value):
        return "Boolean.toString(%(value)s)" % locals()
