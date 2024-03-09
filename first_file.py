# How to list all files of a directory in python in python.

from os import listdir
from os.path import isfile , join

files_list = [f for f in listdir('/home') if isfile(join('/home',f))]
