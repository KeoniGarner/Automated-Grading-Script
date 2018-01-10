"""
Automated Grading Script - compiles, builds, and runs .cpp files then
checks the output with a predefined output. DOES NOT SUPPORT TESTING YET
"""

import os
import subprocess
import glob
import argparse as arguments

# setup arguments
parser = arguments.ArgumentParser(description='Automated Grading Script.')
parser.add_argument("-dir", dest="fileDirectory", default="./Example Files",
    help="Directory that holds all of the students' files.")
parser.add_argument("-grades", dest="gradeFile", default="gradeFile.txt",
    help="File where grades will be recorded (.txt)")
parser.add_argument("-tests", dest="testFile",
    help="File that contains tests to run.")
parser.add_argument("-comp", dest="compiler", 
    default="C:\\Users\\Keoni Garner\\Downloads\\MinGW\\bin\\g++.exe",
    help="Path to specific compiler ")
args = parser.parse_args()

# set arguments to objects
studentDirectory = args.fileDirectory
gFile = open(args.gradeFile, mode="w")
tFile = args.testFile
cppCompiler = args.compiler

# change working directory to directory that is specified in the arguments
os.chdir(studentDirectory)

# create list for all students' source files
sourceFiles = glob.glob("*.cpp")

for file in sourceFiles:
    # compile and build file as "a.exe"
    compFile = subprocess.Popen([cppCompiler, file], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # run "a.exe" to get output and write to file.
    compFile = subprocess.Popen(["./a.exe"], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
        universal_newlines = True) # needed to receive strings

    output = open((file + "-output.txt"), "w")
    output.write(compFile.stdout.read())

    compFile = ""
    os.remove("a.exe")
    output.close
    


# close grade file
gFile.close()

# print progress to console along with average grade
print("Success!")