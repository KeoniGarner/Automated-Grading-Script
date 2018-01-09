"""
Automated Grading Script - compiles,
"""

import os
import subprocess
import glob
import argparse as arguments

# setup arguments
parser = arguments.ArgumentParser(description='Automated Grading Script.')
parser.add_argument("-dir", dest="fileDirectory", default="./",
    help="Directory that holds all of the students' files.")
parser.add_argument("-grades", dest="gradeFile", default="gradeFile.txt",
    help="File where grades will be recorded (.txt)")
parser.add_argument("-tests", dest="testFile",
    help="File that contains tests to run.")
args = parser.parse_args()

# set arguments to objects
studentDirectory = args.fileDirectory
gFile = open(args.gradeFile, mode="w")
tFile = args.testFile

# change working directory to directory that is specified in the arguments
os.chdir(studentDirectory)

# create list for all student files
studentFiles = glob.glob("*.cpp")

for file in studentFiles:
    # compile, build, and run file
    # if file output == example output
        # write file + "     100%" + newline? to gFile
    # else
        # write file + "       0%" + newline? to gFile

# close grade file
gFile.close()

# print progress to console along with average grade
print("Success!")