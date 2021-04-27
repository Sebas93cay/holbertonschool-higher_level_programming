#!/usr/bin/python3
add = 1
ran = [c for c in range(ord('A'), ord('Z')+1)]
ran.reverse()
for c in ran:
    print("{:c}".format(c + (add+1)*16), end='')
    add = -add
