#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    defined = dir(hidden_4)
    for name in defined:
        if name[:2] != "__":
            print("{:s}".format(name))
