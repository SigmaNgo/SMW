#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys

print("current working directory " + os.getcwd())
for file in os.listdir(os.getcwd()):
    if file.endswith(".doc") or file.endswith(".docx") or file.endswith(".odt"):
        print("transformming " + file)
        os.system("python transformToCsv.py '" + file + "' " + sys.argv[1])
    else:
        print("! wrong extension, skipping " + file)
