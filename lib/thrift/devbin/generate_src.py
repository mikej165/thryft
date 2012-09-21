import os.path
from shutil import copyfile
from yutil import camelize

THRYFT_ROOT_DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..'))

try:
    import thryft
except ImportError:
    import sys
    sys.path.append(os.path.join(THRYFT_ROOT_DIR_PATH, 'compiler', 'src'))
from thryft.compiler import Compiler
from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.py.py_generator import PyGenerator

for in_dir_path, generator, out_dir_path in (
    (
        os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'thrift', 'test'),
        JavaGenerator(),
        os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'java', 'src', 'test', 'java')
    ),
):
    compiler = \
        Compiler(
            include_dir_paths=(
                in_dir_path,
                os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'thrift', 'src'),
            ),
            generator=generator
        )

    for dir_path, _, file_names in os.walk(in_dir_path):
        for file_name in file_names:
            if os.path.splitext(file_name)[1] != '.thrift':
                continue
            file_path = os.path.join(dir_path, file_name)

            for document in compiler(file_path):
                document.save(out_dir_path)
