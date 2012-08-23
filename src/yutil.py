# yutil.py

# Copyright (c) 2012 Minor Gordon
# All rights reserved

# This source file is part of the yutil project.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# * Neither the name of the yutil project nor the
# names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL Minor Gordon BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from cStringIO import StringIO
from copy import copy, deepcopy
from fnmatch import fnmatch as _fnmatch
from glob import iglob
# pylint:disable=E0611
from hashlib import md5
from inspect import isclass
from os import curdir, getcwd, listdir, makedirs, pardir, walk as _walk, \
    sep as os_sep
from os.path import abspath, commonprefix, exists, isdir, isfile, join, relpath, \
    split
import os
import re
import shutil
import stat
import sys
# pylint:disable=C0111,R0912


__all__ = [
  'abspath', 'abspaths',
  'bstrip',
  'camelize',
  'class_qname',
  'commonprefix',
  'copy_file',
  'decamelize',
  'deduplist',
  'fnmatch',
  'indent',
  'ishidden',
  'istype',
  'list_files',
  'list_subdirectories',
  'lpad',
  'lower_camelize',
  'merge_dicts',
  'mirror_subdirectories',
  'ntpath', 'ntpaths',
  'pad',
  'posixpath', 'posixpaths',
  'quote',
  'quotestrlist',
  'reinterpret_cast',
  'relpath', 'relpaths',
  'rglob',
  'rpad',
  'spacify',
  'static_cast',
  'strlist',
  'touch',
  'treepaths',
  'tstrip',
  'typelist',
  'walk',
  'write_file',
]


def abspaths(paths):
    return __applypaths(paths, abspath)


def __applypaths(paths, function):
    if paths is None:
        return []
    elif isinstance(paths, list) or isinstance(paths, tuple):
        return [function(path) for path in paths]
    elif isinstance(paths, dict):
        paths_copy = {}
        for key in paths.iterkeys():
            paths_copy[key] = __applypaths(paths[key], function)
        return paths_copy
    elif isinstance(paths, basestring):
        return function(paths)
    else:
        raise TypeError('invalid paths type: ' + str(type(paths)))


def bstrip(lines, pattern=''):
    if len(lines) > 0:
        lines = copy(lines)
        line_i = len(lines) - 1
        while line_i > 0:
            if __startswith(lines[line_i], pattern):
                del lines[line_i]
                line_i -= 1
            else:
                break
    return lines


def camelize(name):
    return upper_camelize(name)


def class_qname(class_):
    if not isclass(class_):
        class_ = class_.__class__
    return class_.__module__ + '.' + class_.__name__


def commonsuffix(strings):
    return commonprefix([string[::-1] for string in strings])[::-1]


def copy_file(from_path, to_path):
    file_hashes = []
    for path in (from_path, to_path):
        try:
            file_hashes.append(md5(open(path).read()).digest())
        except IOError:
            file_hashes.append(0)

    if file_hashes[0] != file_hashes[1]:
        shutil.copyfile(from_path, to_path)
        print 'copied', from_path, 'to', to_path
        return True
    else:
        return False


def decamelize(str_):
    return re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', str_)\
            .lower()\
            .strip('_')


def deduplist(list_):
    deduped_list = []
    for element in list_:
        if element not in deduped_list:
            deduped_list.append(element)
    return deduped_list


def fnmatch(path, pattern):
    name = split(path)[1]
    if isinstance(pattern, basestring):
        if _fnmatch(name, pattern) or\
           _fnmatch(path, pattern):
            return True
    elif hasattr(pattern, 'match'): # A regex-like object
        if pattern.match(name):
            return True
    elif isinstance(pattern, tuple) or isinstance(pattern, list):
        for subpattern in strlist(pattern):
            if fnmatch(path, subpattern):
                return True

    return False


def indent(spaces, text):
    if len(spaces) > 0 and len(text) > 0:
        if isinstance(text, tuple) or isinstance(text, list):
            return [indent(spaces, line) for line in text]
        else:
            indented_lines = []
            for line in StringIO(str(text)).readlines():
                line = line.rstrip()
                if len(line) > 0:
                    indented_lines.append(spaces + line)
                else:
                    indented_lines.append(line)
            return '\n'.join(indented_lines)
    else:
        return text


def ishidden(path):
    for path_segment in path.split(os_sep):
        if len(path_segment) > 0 and\
           path_segment[0] == '.' and\
           path_segment != curdir and path_segment != pardir:
            return True
    return False


def istype(type_):
    return isinstance(type_, type) or isclass(type_)


def list_files(dir_path):
    for file_name in listdir(dir_path):
        file_path = join(dir_path, file_name)
        if isfile(file_path):
            yield file_path


def list_subdirectories(root_dir_path, include_hidden=False):
    for dir_name in listdir(root_dir_path):
        dir_path = join(root_dir_path, dir_name)
        if isdir(dir_path):
            if include_hidden or not ishidden(dir_path):
                yield dir_path


def lower_camelize(name):
    name_parts = name.split('_')
    if len(name_parts) == 1:
        return name[0].lower() + name[1:]
    else:
        return \
            ''.join([name_parts[0]] + \
                    [name_part.capitalize()
                     for name_part in name_parts[1:]])


def lpad(padding, str_):
    if str_ is not None:
        if len(str_) > 0:
            return padding + str_
        else:
            return str_
    else:
        return ''


def merge_dicts(left, right):
    a_copy = deepcopy(left)
    if len(left) > 0 or len(right) > 0:
        b_copy = deepcopy(right)
        for a_key, a_value in a_copy.iteritems():
            try:
                b_value = b_copy[a_key]
                del b_copy[a_key]
            except KeyError:
                continue

            assert a_value.__class__ == b_value.__class__
            if isinstance(b_value, list):
                a_value.extend(b_value)
                a_value = deduplist(a_value)
            elif isinstance(b_value, dict):
                merge_dicts(a_value, b_value)

        a_copy.update(b_copy)
    return a_copy


def mirror_subdirectories(source_dir_path, target_dir_path):
    if exists(source_dir_path):
        if not exists(target_dir_path):
            makedirs(target_dir_path)

        for root_dir_path, dir_names, _ in _walk(source_dir_path):
            if not ishidden(root_dir_path):
                for dir_name in dir_names:
                    source_subdir_path = join(root_dir_path, dir_name)
                    if not ishidden(source_subdir_path):
                        source_subdir_path = \
                            relpath(source_subdir_path, source_dir_path)
                        target_subdir_path = \
                            join(target_dir_path, source_subdir_path)
                        if not exists(target_subdir_path):
                            makedirs(target_subdir_path)


def ntpath(path):
    return path.replace(os_sep, '\\')


def ntpaths(paths):
    return __applypaths(paths, ntpath)


def pad(left_padding, str_, right_padding):
    if str_ is not None:
        if len(str_) > 0:
            return left_padding + str_ + right_padding
        else:
            return str_
    else:
        return ''


def posixpath(path):
    return path.replace(os_sep, '/')


def posixpaths(paths):
    return __applypaths(paths, posixpath)


def quote(str_):
    assert isinstance(str_, basestring)
    if not '"' in str_:
        return '"' + str_ + '"'
    elif not "'" in str_:
        return "'" + str_ + "'"
    else:
        raise ValueError(str_)


def quotestrlist(strlist_):
    return [quote(str_) for str_ in strlist(strlist_)]


def reinterpret_cast(object_, expected_type):
    if isinstance(object_, expected_type):
        return object_
    else:
        return expected_type(object_)


def relpaths(paths, start=None):
    if start is None:
        start = getcwd()
    return __applypaths(abspaths(paths), lambda path: relpath(path, start))


def rglob(path, debug=False):
    if debug:
        print 'rglob(', path, ')'

    if isinstance(path, tuple) or isinstance(path, list):
        for subpath in path:
            for path in rglob(subpath):
                yield path
        return
    else:
        path_parts = []
        head, tail = split(str(path))
        while len(tail) > 0:
            path_parts.append(tail)
            head, tail = split(head)
        if len(head) > 0:
            path_parts.append(head)
        path_parts.reverse()

        for path in __rglob(path_parts, 0, debug=debug):
            if debug:
                print 'rglob: yielding', path

            yield path

        if debug:
            print


def __rglob(path_parts, path_part_i, debug=False):
    if debug:
        print ' __rglob(', path_parts, ',', path_part_i, ')'

    assert len(path_parts) > 0
    assert path_part_i < len(path_parts)

    if path_parts[path_part_i] == '**':
        if path_part_i == 0:
            path = curdir
        else:
            path = join(*path_parts[:path_part_i])

        if path_part_i + 1 < len(path_parts):
            sub_path_parts = path_parts[:path_part_i] + \
                             path_parts[path_part_i + 1:]
            sub_path = join(*sub_path_parts)
            if debug:
                print ' __rglob: iglob1(', sub_path, ')'
            for sub_path in iglob(sub_path):
                yield sub_path

            for _root_dir_path, dir_paths, _file_names in\
                walk(path, abspaths=True, include_hidden=False):

                for dir_path in dir_paths:
                    sub_path_parts = \
                        path_parts[:path_part_i] + \
                        [dir_path[len(path) + 1:]] + \
                        path_parts[path_part_i + 1:]
                    sub_path = join(*sub_path_parts)
                    if debug:
                        print ' __rglob: recursing into', dir_path, sub_path
                    for sub_path in __rglob(sub_path_parts, path_part_i + 1):
                        yield sub_path
        else:
            for _, dir_paths, file_paths in \
                walk(path, abspaths=True, include_hidden=False):
                for path in file_paths + dir_paths:
                    yield path
    elif path_part_i + 1 < len(path_parts):
        path = join(*path_parts[:path_part_i + 1])
        if debug:
            print ' __rglob: iglob2(', path, ')'
        for path in iglob(path):
            if isdir(path):
                for path in __rglob(path_parts, path_part_i + 1):
                    yield path
    else:
        path = join(*path_parts[:path_part_i + 1])
        if debug:
            print ' __rglob: iglob3(', path, ')'
        for path in iglob(path):
            yield path


def rpad(str_, padding):
    if str_ is not None:
        if len(str_) > 0:
            return str_ + padding
        else:
            return str_
    else:
        return ''


def spacify(str_, spaces=' ' * 4):
    if isinstance(str_, basestring):
        return str_.replace('\t', spaces)
    elif isinstance(str_, tuple) or isinstance(str_, list):
        return [y.replace('\t', spaces) for y in str_]
    else:
        raise ValueError((type(str_)))


def __startswith(line, pattern):
    if pattern is None:
        return len(line) == 0
    if isinstance(pattern, basestring):
        if len(pattern) == 0:
            return len(line) == 0
        else:
            return line.startswith(pattern)
    elif hasattr(pattern, 'match'):
        return pattern.match(line) is not None
    elif isinstance(pattern, tuple) or isinstance(pattern, list):
        for subpattern in pattern:
            if __startswith(line, subpattern):
                return True
    else:
        raise TypeError(str(type(pattern)))


def static_cast(object_, expected_type):
    if istype(expected_type):
        if isinstance(object_, expected_type):
            return object_
        else:
            raise TypeError(type(object_))
    elif isinstance(expected_type, tuple) or isinstance(expected_type, list):
        expected_types = expected_type
        for expected_type in expected_types:
            if istype(expected_type):
                if isinstance(object_, expected_type):
                    return object_
            elif object_ == expected_type:
                return object_

        if hasattr(object_, '__class__'):
            repr_type_x = object_.__class__.__name__
        else:
            repr_type_x = repr(type(object_))

        raise TypeError(repr_type_x + ' vs. ' + repr(expected_types))
    else:
        raise TypeError(type(object_))


def strlist(list_):
    return typelist(list_, str)


def touch(file_path):
    if not exists(file_path):
        open(file_path, 'w+').close()


# Create a tree of { dir_path: { path: path } }
def treepaths(paths):
    assert isinstance(paths, list) or isinstance(paths, tuple)
    tree = {}
    for path in paths:
        str_path = str(path)
        subtree = tree
        path_segments = str_path.split(os_sep)
        for path_segment_i, _path_segment in enumerate(path_segments):
            if path_segment_i < len(path_segments) - 1:
                dir_path = os_sep.join(path_segments[:path_segment_i + 1])
                try:
                    subtree = subtree[dir_path]
                    # check if dir_path is set to a file
                    if not isinstance(subtree, dict):
                        raise ValueError(
                                  'subtree[' + dir_path + \
                                  '] already set to a file'
                              )
                except KeyError:
                    subtree[dir_path] = {}
                    subtree = subtree[dir_path]
            elif not str_path in subtree:
                subtree[str_path] = path
            else:
                raise ValueError(
                          'subtree[' + str_path + '] already set to' + \
                          subtree[str_path]
                      )

    while len(tree) == 1 and \
          isinstance(tree.values()[0], dict) and \
          len(tree.values()[0]) == 1:
        tree = tree.values()[0]

    return tree


def tstrip(lines, pattern=''):
    lines = copy(lines)
    line_i = 0
    while line_i < len(lines):
        if __startswith(lines[line_i], pattern):
            del lines[line_i]
        else:
            break

    return lines


def typelist(list_, item_type=None):
    if list_ is None:
        return []
    else:
        if isinstance(list_, tuple):
            list_ = list(list_)
        elif isinstance(list_, list):
            pass
        elif item_type is not None:
            if isinstance(list_, item_type):
                return [list_]
            else:
                return [item_type(list_)]
        else:
            raise TypeError(type(list_))

        if item_type is None:
            return list_
        else:
            for item in list_:
                if not isinstance(item, item_type):
                    new_x = []
                    for item in list_:
                        if isinstance(item, item_type):
                            new_x.append(list_)
                        else:
                            new_x.append(item_type(item))
                    return new_x
            return list_


def upper_camelize(name):
    return ''.join([name_part.capitalize() for name_part in name.split('_')])


# pylint: disable=W0621
def walk(root_dir_path, abspaths=False, include_hidden=True):
    for root_dir_path, dir_names, file_names in _walk(root_dir_path):
        if include_hidden or not ishidden(root_dir_path):
            if abspaths:
                dir_paths = []
                for dir_name in dir_names:
                    dir_path = join(root_dir_path, dir_name)
                    if include_hidden or not ishidden(dir_path):
                        dir_paths.append(dir_path)

                file_paths = []
                for file_name in file_names:
                    file_path = join(root_dir_path, file_name)
                    if include_hidden or not ishidden(file_path):
                        file_paths.append(file_path)

                yield root_dir_path, dir_paths, file_paths
            elif not include_hidden:
                dir_names = [dir_name for dir_name in dir_names
                             if not ishidden(join(root_dir_path, dir_name))]
                file_names = [file_name for file_name in file_names
                              if not ishidden(join(root_dir_path, file_name))]

                yield root_dir_path, dir_names, file_names
            else:
                yield root_dir_path, dir_names, file_names


def which(executable_file_stem):
    if sys.platform == 'win32':
        executable_file_exts = ('.bat', '.com', '.exe',)
    else:
        executable_file_exts = ('',)

    for executable_dir_path in os.environ['PATH'].split(os.path.pathsep):
        for executable_file_ext in executable_file_exts:
            executable_file_path = \
                os.path.join(
                    executable_dir_path,
                    executable_file_stem + executable_file_ext
                )

            try:
                stbuf = os.stat(executable_file_path)
            except: # pylint: disable=W0702
                continue

            if (stbuf.st_mode & stat.S_IXUSR) == stat.S_IXUSR or \
               (stbuf.st_mode & stat.S_IXGRP) == stat.S_IXGRP or \
               (stbuf.st_mode & stat.S_IXOTH) == stat.S_IXOTH:
                return executable_file_path


def write_file(path, contents, force=False, newline='\n', quiet=False):
    if isinstance(contents, basestring):
        pass
    elif isinstance(contents, tuple) or isinstance(contents, list):
        contents = newline.join(contents)
    else:
        contents = str(contents)

    if not force:
        try:
            old_file = open(path)

            file_hashes = []
            for file_ in (old_file, StringIO(contents)):
                file_hash = md5()

                for line in file_.readlines():
                    line = line.strip()
                    if len(line) == 0:
                        pass # Ignore empty lines
                    else:
                        file_hash.update(line)

                file_hashes.append(file_hash.digest())

            if file_hashes[0] == file_hashes[1]:
                return False

        except IOError: # old file does not exist
            pass

    open(path, 'wb').write(contents)
    if not quiet:
        print 'wrote', path
    return True
