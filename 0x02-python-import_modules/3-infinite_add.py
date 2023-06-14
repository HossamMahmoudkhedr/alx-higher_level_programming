#!/usr/bin/python3
def add_arg(argv):
    sum = 0
    length = len(argv)
    if length > 1:
        for i in range(1,argv):
            sum += argv[i]
    print("{:d}".format(sum))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
