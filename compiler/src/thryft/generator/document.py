from thryft.generator.construct import Construct
from thryft.generator.include import Include
from thryft.generator.namespace import Namespace
from yutil import decamelize
import os.path


class Document(Construct):
    def __init__(self, path, definitions=None, headers=None):
        self.__path = os.path.abspath(path)
        Construct.__init__(
            self,
            name=os.path.splitext(os.path.split(self.__path)[1])[0],
            parent=None
        )
        self.__definitions = \
            definitions is not None and list(definitions) or []
        self.__headers = headers is not None and list(headers) or []

    @property
    def definitions(self):
        return self.__definitions

    @property
    def headers(self):
        return self.__headers

    @property
    def includes(self):
        return [header for header in self.headers
                if isinstance(header, Include)]

    @property
    def namespaces(self):
        return [header for header in self.headers
                if isinstance(header, Namespace)]

    @property
    def path(self):
        return self.__path

    def save(self, out_path):
        if os.path.isdir(out_path):
            out_dir_path = out_path

            assert self.__class__.__name__.endswith('Document')
            language = decamelize(self.__class__.__name__[:-len('Document')]).split('_')[-1]

            language_namespace = None
            for namespace in self.namespaces:
                if namespace.scope == language:
                    language_namespace = namespace
                    break
            if language_namespace is None:
                for namespace in self.namespaces:
                    if namespace.scope == '*':
                        language_namespace = namespace
                        break
            if language_namespace is not None:
                out_dir_path = \
                    os.path.join(
                        out_dir_path,
                        language_namespace.name.replace('.', os.path.sep)
                    )

            return self._save(os.path.join(out_dir_path, self.name + '.' + language))
        else:
            return self._save(out_path)

    def _save(self, out_file_path):
        out_dir_path = os.path.split(out_file_path)[0]
        if not os.path.isdir(out_dir_path):
            os.makedirs(out_dir_path)

        repr_ = repr(self)
        if len(repr_) == 0:
            return

        with open(out_file_path, 'w+b') as out_file:
            out_file.write(repr_)
            print 'wrote', out_file_path

        return out_file_path
