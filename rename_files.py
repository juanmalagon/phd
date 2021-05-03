# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import unidecode


os.chdir('/home/juan/Downloads/2016')
file_list = os.listdir()

file_list_fixed = [unidecode.unidecode(name) for name in file_list]

zipped = zip(file_list, file_list_fixed)

for x,y in zipped:
    os.rename(x,y)