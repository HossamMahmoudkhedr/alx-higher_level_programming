#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add , sub, mul, div
    a = 10
    b = 5
    add_op = add(a, b)
    sub_op = sub(a, b)
    mul_op = mul(a, b)
    div_op = div(a, b)
    print("{:d} + {:d} = {:d}".format(a ,b ,add_op))
    print("{:d} - {:d} = {:d}".format(a ,b ,sub_op))
    print("{:d} * {:d} = {:d}".format(a ,b ,mul_op))
    print("{:d} / {:d} = {:d}".format(a ,b ,div_op))
