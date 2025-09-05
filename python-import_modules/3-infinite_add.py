#!/usr/bin/python3
import sys

if __name__ == "__main__":
    tot = 0
    for arg in sys.argv[1:]:
        tot = tot + int(arg)
    print(tot)
