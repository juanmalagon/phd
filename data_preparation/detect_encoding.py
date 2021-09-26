#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:31:59 2020

@author: juan
"""

import os
from charset_normalizer import CharsetNormalizerMatches as CnM
from charset_normalizer import detect

os.chdir('/home/juan/Downloads/2016')
file_list = os.listdir()

my_file = open(file_list[0], encoding='latin1')
raw_text = my_file.read()

detect(raw_text)


[CnM.from_path(u).best().first() for u in file_list[:3]]


print(CnM.from_path(file_list[0]).best().first())