from thryft.generators.ts.ts_generator import TsGenerator
from thryft_test import _generator_test


class TsGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=TsGenerator,
            generator_kwds={'ts_out_dir_path': '.', 'ts_share_dir_path': '.'},
            repr_method_name='ts_repr',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return TsGeneratorTest.suite()
