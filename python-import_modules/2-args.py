#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    print(f"{argc} argument{'s' if argc != 1 else ''}{'.' if argc == 0 else ':'}")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
