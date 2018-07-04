#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import csv #for more go here https://pymotw.com/2/csv/
import json

inputFilePath = sys.argv[1]
outputFilePathRelativeToinputFilePath = sys.argv[2]
basename = os.path.basename(inputFilePath)
dirname = os.path.dirname(inputFilePath)
inputFileSplited = os.path.splitext(basename)
outputFileName = inputFileSplited[0] + '.json'
outputFilePath = outputFilePathRelativeToinputFilePath + outputFileName

# print("inputFilePath      " + inputFilePath)
# print("outputFilePath     " + outputFilePathRelativeToinputFilePath)
# print("basename            " + basename)
# print("dirname             " + dirname)
# print("inputFileSplited[0] " + inputFileSplited[0])
# print("inputFileSplited[1] " + inputFileSplited[1])
# print("outputFileName      " + outputFileName)
# print("outputFilePath      " + outputFilePath)

csvFile = open(inputFilePath, 'r')
jsonFile = open(outputFilePath, 'wt')
csvReader = csv.DictReader(csvFile)
csvFieldNames = csvReader.fieldnames
items = list(csvReader)
json.dump(items, jsonFile)
