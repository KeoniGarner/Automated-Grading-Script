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
PARSER.add_argument("-grades", dest="gradeFile", default="./gradeFile.txt",
                    help="File where grades will be recorded (.txt)")
PARSER.add_argument("-tests", dest="testFile", default="../testFile.txt",
                    help="File that contains tests to run.")
PARSER.add_argument("-comp", dest="compiler", default="..\\..\\..\\..\\Downloads\\MinGW\\bin\\g++.exe",
                    help="Path to specific compiler ")
ARGS = PARSER.parse_args()

# set arguments to objects
STUDENTDIRECTORY = ARGS.fileDirectory
GRADEFILE = open(ARGS.gradeFile, mode="w")
TESTFILE = ARGS.testFile
CPPCOMPILER = ARGS.compiler

def main():
    # change working directory to directory that is specified in the arguments
    os.chdir(STUDENTDIRECTORY)
    get_txt_files()

    text_files = glob.glob("*.txt")
    for out_file in text_files:
        # call to function to do the dirty work
        compare_text_files(TESTFILE, out_file)

    # close grade file
    GRADEFILE.close()


def get_txt_files():
    # create list for all students' source files
    source_files = glob.glob("*.cpp")

    for file in source_files:
        # call to function to do the dirty work
        compile_and_run_cpp_files(file)

def compile_and_run_cpp_files(cpp_file):
    # string manipulation and arguments at the beginning of "for" loop for clarity
    exe_file = cpp_file.split(".cpp")[0] + ".exe"
    txt_file = cpp_file.split(".cpp")[0] + "-output.txt"
    comp_args = [CPPCOMPILER, "-Wall", cpp_file, "-o", exe_file]

    # compile and build file
    comp_file = subprocess.Popen(comp_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # wait for file to open
    comp_file.wait()

    # run executable to get output
    comp_file = subprocess.Popen([os.path.join(os.getcwd(), exe_file)],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True)  # needed to receive strings

    # see above
    comp_file.wait()

    # write to ".txt" file
    output = open(txt_file, "w")
    output.write(comp_file.stdout.read())

    # empty variables
    output.close()
    comp_file = ""

def compare_text_files(test, actual):
    # open files to be compared
    t_file = open(test, "r")
    a_file = open(actual, "r")

    # compare the output of both files
    if t_file.read() != a_file.read():
        GRADEFILE.write(a_file.name + "-----Expected: " + t_file.read() + "-----Got: "
                        + a_file.read())
    else:
        GRADEFILE.write(a_file.name + "-----100%")

    # empty variables
    t_file.close()
    a_file.close()


main()
# print progress to console along with average grade
print("Success!")
