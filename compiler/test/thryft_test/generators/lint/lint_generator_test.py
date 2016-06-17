from thryft.generators.lint.lint_generator import LintGenerator
from thryft_test import _generator_test


class LintGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=LintGenerator,
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return LintGeneratorTest.suite()
