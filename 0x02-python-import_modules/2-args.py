#!/usr/bin/python3
def print_arg(argv):
    length = len(argv) - 1
    if length == 1:
        print("{:d} argument:".format(length))
    elif length == 0:
        print("{:d} arguments.".format(length))
    else:
        print("{:d} arguments:".format(length))
    
    if length >= 0:
        for i in range(1,length):
            print("{:d}: {:s}".format(i, argv[i]))
if __name__ == "__main__":
    import sys
    print_arg(sys.argv)