from thryft.target.compound_types.exception import Exception


class JavaException(Exception):
    def java_name(self, boxed=False):
        return self.name

    def __repr__(self):
        name = self.java_name()
        return """\
@SuppressWarnings("serial")
public class %(name)s extends Exception {
}""" % locals()
