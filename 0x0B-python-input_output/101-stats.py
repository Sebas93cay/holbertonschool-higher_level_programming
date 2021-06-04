#!/usr/bin/python3
"""
this scripts reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
Total file size: File size: <total size> where <total size> is the sum of all previous
Number of lines by status code:
format: <status code>: <number>
"""

import fileinput
import re
import signal


# def signal_handler(sig, frame):
#     print("you presed the ting")
#     exit(0)


def thePrint(total_size, codes_f, codes):
    print("File size: {}".format(total_size))
    for code in codes:
        if code in codes_f and codes_f[code] != 0:
            print("{}: {}".format(code, codes_f[code]))


if __name__ == '__main__':

    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGINT, signal.default_int_handler)

    try:
        lines_readed = 0
        codes_f = {}
        total_size = 0
        codes = ('200', '301', '400', '401', '403', '404', '405', '500')

        for line in fileinput.input():
            tokens = line.split(' ')
            if tokens[14] in codes_f:
                codes_f[tokens[14]] += 1
            else:
                codes_f[tokens[14]] = 1
            lines_readed += 1

            total_size += int(tokens[15][:-1])

            if lines_readed == 10:
                thePrint(total_size, codes_f, codes)
                lines_readed = 0
    except KeyboardInterrupt:
        thePrint(total_size, codes_f, codes)
