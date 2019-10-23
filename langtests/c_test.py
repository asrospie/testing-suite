import os
from os.path import isfile, join
import sys

'''
    getFiles
    returns a list of files in a given directory
    path: a string of the path to the directory
    return []: the list of files
'''
def getFiles(path: str) -> []:
    return [f for f in os.listdir(path) if isfile(join(path, f))]

'''
    getArgs
    breaks each line in a file into arguments to be used later
    path: the path to the file
    return []: the list of arguments in a file
'''
def getArgs(path: str) -> []:
    inputs = []
    try:     
        with open(path, 'r+') as f:
            # for every line, add a list 
            for line in f:
                args = []

                # for every word in line, add to list of arguments
                for word in line.split():
                    args.append(word)
                
                # append arguments to the inputs
                inputs.append(args)
    except Exception as e:
        print("Error loading from files")
    finally:
        f.close()
    return inputs

'''
    checkTests
    checks to make sure there is a file for each test in the inputs.txt
    inputs: the file arguments
    expected: the list of expected files
    returns bool: True if tests are valid, else False
'''
def checkTests(inputs: [], expected: []) -> bool:
    # go through each index of inputs
    for i in range(0, len(inputs)):

        # check to see if each file name in inputs has an expected file
        if (inputs[i][0] + ".txt") not in expected:
            print("Mismatch between expected and inputs")
            return False
    return True

'''
    runCTests
    runs all of the tests
    inputs: the inputs for each test case
    returns int: the number of failed tests
'''
def runCTests(process: str) -> int:
    failed = 0
    test = 1
    inputs = getArgs("inputs.in")
    expected = getFiles("test-suite/")
    if not checkTests(inputs, expected):
        return -1

    # loop through all of the arguments in inputs
    # this runs each test case
    for args in inputs:
        command = "./" + process + " "
        # builds the command to run the test case
        for j in range(1, len(args)):
            command = command + args[j] + " "
        
        # piping the result to a file that can be diffed
        command = command + "> " + args[0] + ".test"
        os.system(command)

        # diff the created file with its expected equivalent
        os.system("diff " + args[0] + ".test test-suite/" + args[0] + ".txt > diff.test")

        # if nothing in diff, test passed, clean up
        if os.stat("diff.test").st_size == 0:
            print("Test " + str(test) + " PASSED")
            os.system("rm diff.test " + args[0] + ".test")

        # test failed so leave the test files
        # and display the diff
        else:
            print("----------------------------")
            print(args[0] + " test FAILED")
            os.system("cat diff.test; rm diff.test")
            print("----------------------------\n")
            failed += 1
        test += 1
    return failed