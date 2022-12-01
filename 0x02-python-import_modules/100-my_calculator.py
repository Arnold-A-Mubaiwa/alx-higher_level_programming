#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    result = 0
    if len(argv) == 4:
        if operator == '+':
            result = add(a, b)
            print("{} {} {} = {} \n0".format(a, operator, b, result))
        elif operator == '-':
            result = sub(a, b)
            print("{} {} {} = {} \n0".format(a, operator, b, result))
        elif operator == '*':
            result = mul(a, b)
            print("{} {} {} = {} \n0".format(a, operator, b, result))
        elif operator == '/':
            result = div(a, b)
            print("{} {} {} = {} \n0".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /\n1")
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> \n1")
