#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 1:
        print("{} argument:".format(num_args))
    elif num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        print("{} arguments:".format(num_args))
    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
