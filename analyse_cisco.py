#!/usr/bin/python
from setuptools import find_packages
packages=find_packages()

import os, sys, re

#from dumper import dump
import datetime
import xlsxwriter

from lib.analysis import Analysis

##### GLOBAL CONFIG ############

files_dir = 'files'

input_files_re = '_output.txt$'
device_re = '_(\d+\.\d+\.\d+\.\d+)' + input_files_re
hostname_re = '(.+)' + device_re


## NOTE -  '\r\n'  or  '\n for delimiter'
delimiter = '^\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\r\n$'

config_file = files_dir + '/analysis_config_cisco.xlsx'
device_list_file = 'input/T-all.txt'

output_report_name = 'Automatic Analysis - ' + files_dir


analyser = Analysis(config_file, output_report_name)
analyser.analyze(files_dir, input_files_re, device_re, hostname_re, delimiter, config_file, device_list_file)


