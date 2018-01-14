"""
Automated Grading Script - compiles, builds, and runs .cpp files then
checks the output with a predefined output. DOES NOT SUPPORT TESTING YET
"""

import os
import subprocess
import glob
import argparse as arguments

# setup arguments
PARSER = arguments.ArgumentParser(description='Automated Grading Script.')
PARSER.add_argument("-dir", dest="fileDirectory", default="./Example Files",
                    help="Directory that holds all of the students' files.")
PARSER.add_argument("-grades", dest="gradeFile", default="gradeFile.txt",
                    help="File where grades will be recorded (.txt)")
PARSER.add_argument("-tests", dest="testFile",
                    help="File that contains tests to run.")
PARSER.add_argument("-comp", dest="compiler",
                    default="C:\\Users\\Keoni Garner\\Downloads\\MinGW\\bin\\g++.exe",
                    help="Path to specific compiler ")
ARGS = PARSER.parse_args()

# set arguments to objects
STUDENTDIRECTORY = ARGS.fileDirectory
GRADEFILE = open(ARGS.gradeFile, mode="w")
TESTFILE = ARGS.testFile
CPPCOMPILER = ARGS.compiler

# change working directory to directory that is specified in the arguments
os.chdir(STUDENTDIRECTORY)

# create list for all students' source files
SOURCEFILES = glob.glob("*.cpp")


# not happy with "compFile" as a variable name
for file in SOURCEFILES:
    # string manipulation and arguments at the beginning of "for" loop for clarity
    exeFile = file.split(".cpp")[0] + ".exe"
    txtFile = file.split(".cpp")[0] + "-output.txt"
    compArgs = [CPPCOMPILER, "-Wall", file, "-o", exeFile]
    
    # compile and build file as "a.exe"
    compFile = subprocess.Popen(compArgs,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # wait for file to open
    compFile.wait()

    # run executable to get output
    compFile = subprocess.Popen([os.path.join(os.curdir, exeFile)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)  # needed to receive strings

    # see above
    compFile.wait()

    # write to ".txt" file
    output = open(txtFile, "w")
    output.write(compFile.stdout.read())

    compFile = ""
    output.close


# close grade file
GRADEFILE.close()

# print progress to console along with average grade
print("Success!")
