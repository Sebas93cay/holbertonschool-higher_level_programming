#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    result = 0

    for a in sys.argv[1:]:
        result += int(a)

    print(result)
