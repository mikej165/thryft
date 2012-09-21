from thryft.generator.include import Include
from thryft.generators.java.java_construct import JavaConstruct
from yutil import upper_camelize


class JavaInclude(Include, JavaConstruct):
    def __init__(self, *args, **kwds):
        Include.__init__(self, *args, **kwds)
        java_class_qname = self.path.rsplit('.', 1)[0].replace('/', '.')
        java_package, java_class_name = java_class_qname.rsplit('.', 1)
        self.__java_class_name = upper_camelize(java_class_name)
        document_java_package = self.document.java_package()
        if document_java_package is not None:
            java_package = document_java_package
        self.__java_package = java_package

    def java_package(self):
        return self.__java_package

    def java_class_name(self):
        return self.__java_class_name

    def java_class_qname(self):
        return self.__java_package + '.' + self.__java_class_name

    def __repr__(self):
        return 'import ' + self.java_class_qname() + ';'
