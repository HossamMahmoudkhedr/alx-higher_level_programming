#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newSet = {}
    for key in a_dictionary:
        newSet[key] = a_dictionary[key] * 2
    return newSet
