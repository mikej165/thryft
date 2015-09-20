from thryft.generators.elastic_search.elastic_search_mappings_generator import ElasticSearchMappingsGenerator
from thryft_test import _generator_test


class ElasticSearchMappingsGeneratorTest(_generator_test._GeneratorTest):
    def __init__(self, *args, **kwds):
        _generator_test._GeneratorTest.__init__(
            self,
            generator_class=ElasticSearchMappingsGenerator,
            generator_kwds={'index_name': 'thryft'},
            repr_method_name='elastic_search_mappings_json',
            *args, **kwds
        )


def load_tests(*args, **kwds):
    return ElasticSearchMappingsGeneratorTest.suite()
