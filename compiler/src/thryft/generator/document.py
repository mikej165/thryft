from collections import OrderedDict
from thryft.generator.include import Include
from thryft.generator._named_construct import _NamedConstruct
from thryft.generator.namespace import Namespace
from yutil import decamelize
import os.path


class Document(_NamedConstruct):
    def __init__(self, path, definitions=None, headers=None, **kwds):
        self.__path = os.path.abspath(path)
        _NamedConstruct.__init__(
            self,
            name=os.path.splitext(os.path.split(self.__path)[1])[0],
            **kwds
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
    def namespaces_by_scope(self):
        return OrderedDict([(namespace.scope, namespace)
                            for namespace in self.namespaces])

    @property
    def path(self):
        return self.__path

    def save(self, out_path, language=None):
        if os.path.isdir(out_path):
            out_dir_path = out_path

            if language is None:
                assert self.__class__.__name__.endswith('Document')
                class_name_decamelized = decamelize(self.__class__.__name__)
                class_name_split = class_name_decamelized.split('_')
                if len(class_name_split) > 1:
                    language = class_name_split[-2]
                else:
                    raise ValueError('unknown language: ' + self.__class__.__name__)

            namespaces_by_scope = self.namespaces_by_scope
            for language in (language, '*'):
                language_namespace = namespaces_by_scope.get(language)
                if language_namespace is not None:
                    out_dir_path = \
                        os.path.join(
                            out_dir_path,
                            language_namespace.name.replace('.', os.path.sep)
                        )
                    break

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

    def _set_comment(self, comment):
        self._comment = comment
