#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import textract
import re
import csv #for more go here https://pymotw.com/2/csv/
import inspect

pattern = re.compile('(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})[\s]+(INT-\d{4,7}\/\d{2})[\s]+(.*)[\s]+(.*)[\s]+(.*)[\s]+(.*)[\s]+(\d*)[\s]+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')

inputFilePatch = sys.argv[1]
outputFilePatchRelativeToinputFilePatch = sys.argv[2]
basename = os.path.basename(inputFilePatch)
dirname = os.path.dirname(inputFilePatch)
inputFileSplited = os.path.splitext(basename)
outputFileName = inputFileSplited[0] + '.csv'
outputFilePath = outputFilePatchRelativeToinputFilePatch + outputFileName

#print("inputFilePatch      " + inputFilePatch)
#print("outputFilePatch     " + outputFilePatchRelativeToinputFilePatch)
#print("basename            " + basename)
#print("dirname             " + dirname)
#print("inputFileSplited[0] " + inputFileSplited[0])
#print("inputFileSplited[1] " + inputFileSplited[1])
#print("outputFileName      " + outputFileName)
#print("outputFilePath      " + outputFilePath)

f = open(outputFilePath, 'wt')
try:
    writer = csv.writer(f)
    textToBeExamined = textract.process(inputFilePatch, 'utf8').replace("|", "\n") #the replace is needed because (for unknown reason) .doc files has this characted while .docx does not
    print(len(re.findall(pattern, textToBeExamined)))
    for result in re.findall(pattern, textToBeExamined):
        writer.writerow(result)

finally:
    f.close()
