from thryft.generators.java.service_template_java_generator import \
    ServiceTemplateJavaGenerator
from thryft_test import _generator_test


class ServiceTemplateJavaGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=ServiceTemplateJavaGenerator,
            repr_method_name='java_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return ServiceTemplateJavaGeneratorTest.suite()
