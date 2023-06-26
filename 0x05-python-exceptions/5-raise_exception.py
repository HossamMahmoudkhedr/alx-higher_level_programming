#!/usr/bin/python3
def raise_exception():
    try:
        value = 2 / 'h'
        print(value)
    except TypeError:
        raise
