class JavaConstruct(object):
    def java_name(self, boxed=False):
        return getattr(self, 'name')
