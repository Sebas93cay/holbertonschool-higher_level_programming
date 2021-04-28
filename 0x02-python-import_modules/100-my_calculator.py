#!/usr/bin/python3
if __name__ == '__main__':

    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div

    switch_operador = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    r = switch_operador.get(argv[2])(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], r))
