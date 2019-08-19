#!/usr/bin/python3

# This project is created to make HTML coding much easier and simpler
# Author: Mohammed Alsharaf
# Date: 8/18/2019

# The structuer is simple. You feed this app your .hl file and then you get out .html file

import os.path
import sys
import Worker


def main():
    if len(sys.argv) == 1:
        print("Error: no input files")
    elif str(sys.argv[0]).endswith('.hl'):
        start_working(sys.argv[0])
    else:
        print("Error: unsupported file type")


def start_working(filename):
    if os.path.isfile(filename):
        Worker.start(filename)
    else:
        print("Error: file does not exists")
        sys.exit(-1)


main()
