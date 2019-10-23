import os
from os.path import exists, isfile, join
import sys

def main():
    length = len(sys.argv)
    if length < 2 or length > 2:
        print("setup.py <path to directory>")
        return

    path = sys.argv[1]
    if (not os.path.exists(path) and os.path.isfile(path)):
        print("Invalid path.")
        return

    if not path[len(path) - 1] == '/':
        path = path + "/"

    os.system("touch %sinputs.in" % (path))
    os.system("mkdir %stest-suite/" % (path))
    os.system("cp suite.py %ssuite.py" % (path))
    os.system("cp -r langtests/ %slangtests/" % (path))

main()