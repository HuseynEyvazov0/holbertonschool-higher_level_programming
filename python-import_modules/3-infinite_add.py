#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    arg = 0

    for i in range(1, argc):
        arg += int(argv[i])
    print(arg)
