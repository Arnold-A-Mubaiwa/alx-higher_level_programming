#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    if op != '+' or op != '-' or op != '*' or op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = 0
    a = int(argv[1])
    b = int(argv[3])
    if op is '+':
        result += add(a, b)
    elif op is '-':
        result += sub(a, b)
    elif op is '/':
        result += div(a, b)
    elif op is '*':
        result += mul(a, b)
    print("{} {} {} = {}".format(a, op, b, result))
