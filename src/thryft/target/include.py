from thryft.target.construct import Construct
import os.path


class Include(Construct):
    def __init__(self, name, parent, path):
        Construct.__init__(self, name=name, parent=parent)
        self.__path = path

    @property
    def is_native(self):
        dir_path = os.path.split(self.path)[0]
        if len(dir_path) > 0:
            dir_name = os.path.split(dir_path)[1]
            if dir_name == 'native':
                return True
        return False

    @property
    def path(self):
        return self.__path
