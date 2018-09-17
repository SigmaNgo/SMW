#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys

print("current working directory " + os.getcwd())

file = open(sys.argv[1], 'w')
file.write("startDate,id,description,type,address,result,fine,endDate\n")
file.close()

for file in os.listdir(os.getcwd()):
    print("--------------------------------------")
    if file.endswith(".csv") and file != sys.argv[1]:
        print("joining " + file)
        os.system("cat '" + file + "' >> " + sys.argv[1])
    else:
        print("! skipping " + file)
