from thryft.generator.comment import Comment
from thryft.generators.thrift.thrift_construct import ThriftConstruct


class ThriftComment(Comment, ThriftConstruct):
    def __repr__(self):
        return ''.join(['// ' + line for line in self.text.splitlines(True)])
