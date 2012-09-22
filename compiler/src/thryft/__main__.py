from thryft.compiler import Compiler
from yutil import camelize, rpad, upper_camelize
import argparse
import logging
import os.path
import sys


MY_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR_PATH = os.path.normpath(os.path.join(MY_DIR_PATH, '..'))


def main():
    # Parse arguments
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '-debug',
        help='Parse debug trace to stdout',
        action='store_true',
    )
    argument_parser.add_argument(
        '-gen',
        help='language[:key1=val1[,key2,[key3=val3]]]',
        required=True
    )
    argument_parser.add_argument(
        '-I',
        action='append',
        dest='include_dir_paths',
        help='include directory paths'
    )
    argument_parser.add_argument(
        '-out',
        help='output directory path'
    )
    argument_parser.add_argument(
        'files',
        nargs='*'
    )
    args = argument_parser.parse_args()

    if args.debug:
        logging.basicConfig(
            format='%(asctime)s:%(module)s:%(lineno)s:%(name)s:%(levelname)s: %(message)s', #@IgnorePep8
            level=logging.DEBUG
        )

    gen = args.gen.split(':', 1)
    gen_kwds = {}
    if len(gen) == 1:
        gen = gen[0]
    elif len(gen) == 2:
        gen, gen_kwds_str = gen
        for gen_kwd in gen_kwds_str.split(','):
            gen_kwd_split = gen_kwd.split('=', 1)
            if len(gen_kwd_split) == 1:
                gen_kwds[gen_kwd_split[0]] = None
            else:
                gen_kwds[gen_kwd_split[0]] = gen_kwd_split[1]


    # Interpret arguments
    if gen == 'generator':
        if len(gen_kwds) != 1:
            raise ValueError, "--gen=generator requires a generator name"
        generator_name = gen_kwds.keys()[0]

        excluded_file_names = (
            'base_type.py',
            'compound_type.py',
            'construct.py',
            'container_type.py',
            'native_type.py',
            'type.py',
        )

        generator_template_root_dir_path = os.path.join(ROOT_DIR_PATH, 'src', 'thryft', 'generator')
        generator_template_file_paths = []
        for dir_path, _, file_names in os.walk(generator_template_root_dir_path):
            for file_name in file_names:
                if os.path.splitext(file_name)[1] != '.py':
                    continue
                elif file_name in excluded_file_names:
                    continue
                generator_template_file_paths.append(
                    os.path.relpath(
                        os.path.join(dir_path, file_name),
                        generator_template_root_dir_path
                    )
                )
        # print generator_template_file_paths

        generator_root_dir_path = os.path.join(ROOT_DIR_PATH, 'src', 'thryft', 'generators', generator_name)
        if not os.path.isdir(generator_root_dir_path):
            os.makedirs(generator_root_dir_path)
        generator_file_paths = []
        for dir_path, _, file_names in os.walk(generator_root_dir_path):
            for file_name in file_names:
                if os.path.splitext(file_name)[1] != '.py':
                    continue
                elif file_name in excluded_file_names:
                    continue
                generator_file_paths.append(
                    os.path.relpath(
                        os.path.join(dir_path, file_name),
                        generator_root_dir_path
                    )
                )
        # print generator_file_paths

        for generator_template_file_path in generator_template_file_paths:
            generator_template_subdir_path, generator_template_file_name = \
                os.path.split(generator_template_file_path)
            if generator_template_file_name == '__init__.py':
                generator_file_path = \
                    os.path.join(
                        generator_template_subdir_path,
                        generator_template_file_name
                    )
            else:
                generator_file_path = \
                    os.path.join(
                        generator_template_subdir_path,
                        generator_name + '_' + generator_template_file_name
                    )

            try:
                generator_file_paths.remove(generator_file_path)
            except ValueError:
                generator_file_paths.append(generator_file_path)

        for generator_file_path in generator_file_paths:
            generator_dir_path, generator_file_name = os.path.split(generator_file_path)
            if generator_file_name == '__init__.py':
                generator_file_contents = ''
            else:
                generator_file_base_name = os.path.splitext(generator_file_name)[0]
                generator_class_name = upper_camelize(generator_file_base_name)
                generator_parent_class_name = upper_camelize(generator_file_base_name[len(generator_name) + 1:])
                generator_parent_module_name = \
                    'thryft.generator.' + \
                    rpad(generator_dir_path.replace(os.path.sep, '.'), '.') + \
                    generator_file_base_name[len(generator_name) + 1:]
                generator_file_contents = """\
    from %(generator_parent_module_name)s import %(generator_parent_class_name)s
    
    
    class %(generator_class_name)s(%(generator_parent_class_name)s):
        pass
    """ % locals()
            generator_file_path = os.path.join(generator_root_dir_path, generator_file_path)
            if not os.path.isdir(os.path.dirname(generator_file_path)):
                os.makedirs(os.path.dirname(generator_file_path))
            with open(generator_file_path, 'wb+') as generator_file:
                generator_file.write(generator_file_contents)
                print 'wrote', generator_file_path
    else:
        generator_module_name = "thryft.generators.%(gen)s.%(gen)s_generator" % locals()
        generator_module = __import__(generator_module_name)
        for module_name in generator_module_name.split('.')[1:]:
            generator_module = getattr(generator_module, module_name)
        generator_class_name = camelize(gen) + 'Generator'
        generator_class = getattr(generator_module, generator_class_name)

        if len(args.files) == 0:
            print >> sys.stderr, 'must specify one or more .thrift files'
            sys.exit(1)

        for file_ in args.files:
            generator = generator_class(**gen_kwds)

            compiler = \
                Compiler(
                    generator=generator,
                    include_dir_paths=args.include_dir_paths
                )

            documents = compiler(file_)

            if args.out is not None and args.out != '-':
                raise NotImplementedError

            generator_repr = repr(documents[0])

            print generator_repr


if __name__ == '__main__':
    main()
