from thryft.generator.comment import Comment
from thryft.generators.thrift._thrift_construct import _ThriftConstruct


class ThriftComment(Comment, _ThriftConstruct):
    def __repr__(self):
        return ''.join(['// ' + line for line in self.text.splitlines(True)])
