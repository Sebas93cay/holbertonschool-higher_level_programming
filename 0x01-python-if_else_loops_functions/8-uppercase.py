#!/usr/bin/python3
def uppercase(str):
    nstr = ""
    
    for i in range(len(str)):
        if (str[i].islower()):
            nstr += chr(ord(str[i]) - 32)
        else:
            nstr += str[i]

    print(nstr)

