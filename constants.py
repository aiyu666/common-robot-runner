__all__ = ['PATH', 'RES_PATH', 'LIB_PATH', 'OS']

import os, sys

PATH = os.path.dirname(os.path.abspath(__file__))
RES_PATH = PATH + '/res'
LIB_PATH = PATH + '/lib'

if sys.platform == "linux" or sys.platform == "linux2":
    OS = 'Linux'
elif sys.platform == "darwin":
    OS = 'Mac'
elif sys.platform == "win32":
    OS = 'Windows'
else:
    OS = 'Other'