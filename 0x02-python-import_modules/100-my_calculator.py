#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div
    import sys
    len_argv = len(sys.argv) - 1
    if len_argv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    match operator:
        case '-':
            print("{}".format(sub(a, b)))
        case '+':
            print("{}".format(add(a, b)))
        case '*':
            print("{}".format(mul(a, b)))
        case '/':
            print("{}".format(div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
