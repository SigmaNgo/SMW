#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys

print("current working directory " + os.getcwd())
for file in os.listdir(os.getcwd()):
    print("--------------------------------------")
    if file.endswith(".csv"):
        print("joining " + file)
        os.system("cat '" + file + "' >> " + sys.argv[1])
    else:
        print("! wrong extension, skipping " + file)
