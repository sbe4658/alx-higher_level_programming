#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    n = 0
    for arg in range(1, ac):
        n += int(argv[arg])
    print(n)
