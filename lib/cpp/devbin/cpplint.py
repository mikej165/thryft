#!/usr/bin/env python
assert __name__ == '__main__'


from argparse import ArgumentParser
from glob import glob
import google_styleguide_cpplint
import os.path
import sys


ROOT_DIR_PATH = \
    os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '..'
        )
    )

GOOG_FILE_EXTS = {
    '.cc': '.cc',
    '.cpp': '.cc',
    '.h': '.h',
    '.hpp': '.h',
}


argument_parser = ArgumentParser()
argument_parser.add_argument(
    'file_path_patterns',
    nargs='+'
)
args = argument_parser.parse_args()

google_styleguide_cpplint._SetFilters(','.join((
    '-legal/copyright',
    '-readability/todo',
    '-runtime/explicit',
	'-runtime/int',
	'-runtime/references',
	'-whitespace/comments',
	'-whitespace/labels',
    '-whitespace/line_length'
)))




file_paths = []
for file_path_pattern in args.file_path_patterns:
    if os.path.isdir(file_path_pattern):
        for root_dir_path, _, file_names in os.walk(file_path_pattern):
            for file_name in file_names:
                file_paths.append(os.path.join(root_dir_path, file_name))
    elif os.path.isfile(file_path_pattern):
        file_paths.append(file_path_pattern)
    else:
        file_paths.extend(glob(file_path_pattern))

for file_path in file_paths:
    file_path = os.path.abspath(file_path)
    file_dir_path, file_name = os.path.split(file_path)
    file_base_name, file_ext = os.path.splitext(file_name)

    try:
        goog_file_ext = GOOG_FILE_EXTS[file_ext]
    except KeyError:
        print >> sys.stderr, 'Ignoring', file_path

    if goog_file_ext == file_ext:
        google_styleguide_cpplint.ProcessFile(os.path.relpath(file_path), 0)
    else:
        goog_file_path = os.path.join(file_dir_path, file_base_name + goog_file_ext)
        # print >>sys.stderr, 'Temporarily renaming', file_path, 'to', goog_file_path
        try:
            os.rename(file_path, goog_file_path)
            google_styleguide_cpplint.ProcessFile(os.path.relpath(goog_file_path), 0)
        finally:
            # print >>sys.stderr, 'Renaming', goog_file_path, 'back to', file_path
            os.rename(goog_file_path, file_path)

#    cppcheck_argv = ['cppcheck']
#    cppcheck_argv.append('--enable=all')
#    cppcheck_argv.extend(('-I', os.path.relpath(os.path.join(ROOT_DIR_PATH, 'include'))))
#    cppcheck_argv.append(os.path.relpath(file_path))
#    try:
#        print cppcheck_argv
#        subprocess.call(cppcheck_argv, shell=True)
#    except:
#        traceback.print_exc()
