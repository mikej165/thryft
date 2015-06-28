# -----------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

from thryft.generators.py.json_rpc_client_py_generator import JsonRpcClientPyGenerator
from thryft.generators.py.py_generator import PyGenerator
from yutil import indent, lpad


class CliClientPyGenerator(JsonRpcClientPyGenerator):
    class BoolType(JsonRpcClientPyGenerator.BoolType):  # @UndefinedVariable
        def py_argparse_action(self):
            return 'store_true'

    class Field(JsonRpcClientPyGenerator.Field):  # @UndefinedVariable
        def py_argparse_action(self):
            try:
                return self.type.py_argparse_action()
            except AttributeError:
                return 'store'

        def py_argparse_name(self):
            return self.py_name()

        def py_argparse_parse(self):
            input_variable = '__args.' + self.py_argparse_name()
            output_variable = self.py_argparse_name()
            try:
                return self.type.py_argparse_parse(input_variable=input_variable, output_variable=output_variable)
            except AttributeError:
                return output_variable + ' = ' + input_variable

        def py_argparse_type(self):
            try:
                return self.type.py_argparse_name()
            except AttributeError:
                return 'str'

    class I32Type(JsonRpcClientPyGenerator.I32Type):
        def py_argparse_name(self):
            return 'int'

    class Function(JsonRpcClientPyGenerator.Function):
        def py_add_arguments(self):
            name = self.py_name()
            add_arguments = []
            parse_args = []
            for parameter in self.parameters:
                parameter_action = parameter.py_argparse_action()
                parameter_name = parameter.py_argparse_name()
                parameter_required = ', required=True' if parameter.required else ''
                parameter_type = ", type=%s" % parameter.py_argparse_type() if parameter_action == 'store' else ''
                add_arguments.append("%(name)s_argument_parser.add_argument('--%(parameter_name)s', action='%(parameter_action)s'%(parameter_required)s%(parameter_type)s)" % locals())
                parse_args.append(parameter.py_argparse_parse())
            add_arguments = lpad("\n", "\n".join(add_arguments))
            call_kwds = ', '.join("%s=%s" % (parameter.py_name(), parameter.py_name()) for parameter in self.parameters)
            parse_args = lpad("\n", "\n".join(indent(' ' * 4, parse_args)))
            return """\
def %(name)s(__args):%(parse_args)s
    return cls().%(name)s(%(call_kwds)s)
%(name)s_argument_parser = argument_subparsers.add_parser('%(name)s')%(add_arguments)s
%(name)s_argument_parser.set_defaults(func=%(name)s)
""" % locals()

    class Service(JsonRpcClientPyGenerator.Service):
        def py_imports_definition(self, caller_stack=None):
            return JsonRpcClientPyGenerator.Service.py_imports_definition(self, caller_stack=caller_stack) + ['import argparse']

        def __py_method_main(self):
            assert len(self.functions) > 0

            function_add_arguments = \
                "\n".join(indent(' ' * 4, (
                    function.py_add_arguments()
                    for function in self.functions
                )))
            return """\
@classmethod
def main(cls):
    argument_parser = argparse.ArgumentParser()
    argument_subparsers = argument_parser.add_subparsers()

%(function_add_arguments)s

    args = argument_parser.parse_args()
    print args.func(args)
""" % locals()

        def _py_methods(self):
            return JsonRpcClientPyGenerator.Service._py_methods(self) + [self.__py_method_main()]

        def py_name(self):
            return PyGenerator.Service.py_name(self) + 'CliClient'  # @UndefinedVariable

        def py_repr(self):
            name = self.py_name()
            return JsonRpcClientPyGenerator.Service.py_repr(self) + """
assert __name__ == '__main__'
%(name)s.main()

""" % locals()

    class SetType(JsonRpcClientPyGenerator.SetType):  # @UndefinedVariable
        def py_argparse_action(self):
            return 'store'

        def py_argparse_name(self):
            return 'str'

    class StringType(JsonRpcClientPyGenerator.StringType):  # @UndefinedVariable
        def py_argparse_name(self):
            return 'str'

    class StructType(JsonRpcClientPyGenerator.StructType):  # @UndefinedVariable
        def py_argparse_name(self):
            return 'str'
