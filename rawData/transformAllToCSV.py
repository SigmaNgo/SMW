#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys

print("current working directory " + os.getcwd())
for file in os.listdir(os.getcwd()):
    print("--------------------------------------")
    if file.endswith(".docx") or file.endswith(".odt"):
        print("transforming to CSV " + file)
        os.system("python transformToCsv.py '" + file + "' " + sys.argv[1])
    else:
        print("! wrong extension, skipping " + file)
os.system('say "your program has finished"') #for mac only :)
