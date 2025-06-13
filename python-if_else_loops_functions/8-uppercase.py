#!/usr/bin/python3
b = "best"
c = "Best School 98 Battery street"
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) >= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
