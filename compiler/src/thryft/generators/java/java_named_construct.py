from thryft.generators.java.java_construct import JavaConstruct


class JavaNamedConstruct(JavaConstruct):
    def java_name(self):
        return getattr(self, 'name')
