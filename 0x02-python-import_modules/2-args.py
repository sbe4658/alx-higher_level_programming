#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 0:
        print("0 arguments.")
    else:
        msg = "argments" if n > 1 else "argument"
        print("{:d} {:s}:".format(n - 1, msg))
        for arg in range(1, n):
            print("{:d}: {:s}".format(arg, argv[arg]))
