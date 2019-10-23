import os
from os.path import exists, isfile, join
import sys
from langtests.c_test import runCTests

langFlags = {
    "-c": "Run tests for the C language, requires additional argument for executable",
    "-j": "Run tests for the Java language, requires additional argument for java file"
}

helpFlags = {
    "-r": "Removes all test-suite files",
    "-h": "Displays all flags and purposes"
}

def printDictionary(d: {}):
    for key, value in d.items():
        print("%s : %s" % (key, value))

def printValidFlags():
    print("---VALID FLAGS---")
    printDictionary(langFlags)
    printDictionary(helpFlags)
    print("-----------------")

def help(flag: str):
    if flag == "-h":
        printValidFlags()
    elif flag == "-r":
        os.system("rm -r inputs.in test-suite/ langtests/ *.test")

def test(flag: str, process: str):
    failed = 0
    # if flag is c, run c tests
    if flag == "-c":
        failed = runCTests(process)

    if not failed:
        print("---ALL TESTS PASSED---")
    else:
        print("---" + str(failed) + " TEST(S) HAVE FAILED---")

def main():
    # check if there is more than one argument
    length = len(sys.argv)
    if length == 1:
        print("suite.py <flag> <process>")
        return

    # check if flag is valid
    flag = sys.argv[1]
    if not (flag in helpFlags or flag in langFlags):
        print("%s is not a valid flag" % (flag))
        printValidFlags()              
        return

    # check if there are too many arguments
    if length > 3:
        print("Too many arguments")
        return

    # check if the flag is the help flag
    if length == 2 and flag in helpFlags:
        help(flag)
        return
    elif flag in helpFlags and length > 2:
        print("Help flags have no arguments.")
        return
        
    # check to make sure langFlag has enough arguments
    if flag in langFlags and length != 3:
        print("Not enough arguments for language flag.")
        return
    elif flag in langFlags and length == 3:
        test(flag, sys.argv[2])
        return

    return
main()