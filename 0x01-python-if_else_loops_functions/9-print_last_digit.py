#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    lastDigit = number % 10
    print("{:d}".format(lastDigit), end="")
    return lastDigit


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)