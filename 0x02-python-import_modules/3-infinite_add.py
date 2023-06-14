#!/usr/bin/python3

import sys

def add_arg(argv):
    total_sum = 0
    length = len(argv)
    if length > 1:
        for i in range(1, length):
            total_sum += int(argv[i])
    print("{:d}".format(total_sum))

if __name__ == "__main__":
    add_arg(sys.argv)
