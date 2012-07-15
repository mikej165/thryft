from thryft.target.compound_types.exception_type import ExceptionType
from thryft.targets.java.java_compound_type import JavaCompoundType


class JavaExceptionType(ExceptionType, JavaCompoundType):
    def __repr__(self):
        name = self.java_name()
        return """\
@SuppressWarnings("serial")
public class %(name)s extends Exception {
}""" % locals()
