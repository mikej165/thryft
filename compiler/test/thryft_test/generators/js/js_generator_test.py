from thryft.generators.js.js_generator import JsGenerator
from thryft_test import _generator_test


class JsGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(self, generator_class=JsGenerator, *args, **kwds)


def load_tests(*args, **kwds):
    return JsGeneratorTest.suite()
