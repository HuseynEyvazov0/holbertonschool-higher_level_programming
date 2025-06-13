#!/usr/bin/python3
b = "best"
c = "Best School 98 Battery street"

def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
