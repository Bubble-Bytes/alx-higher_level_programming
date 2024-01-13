#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import *
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    operator = sys.argv[2]

    if operator not in ['+','/','-','+']:
        print('Unknown operator. Available operators: +, -, * and / \n')
        exit(1)

    a = int(sys.arg[1])
    b = int(sys.arg[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
