import argparse


__all__ = ['Compiler']


class Compiler(object):
    @classmethod
    def main(cls):
        argument_parser = argparse.ArgumentParser()
        args = argument_parser.parse_args()

