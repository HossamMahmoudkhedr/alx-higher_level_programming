#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible = []
    length = len(my_list)
    for i in range(length):
        if my_list[i] % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    return divisible
