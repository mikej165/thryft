from thryft.generator.comment import Comment


class ThriftComment(Comment):
    def __repr__(self):
        return ''.join(['// ' + line for line in self.text.splitlines(True)])
