import os.path
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from date_time import JavaDateTime, PyDateTime


class JavaDate(JavaDateTime):
    pass


class PyDate(PyDateTime):
    pass
