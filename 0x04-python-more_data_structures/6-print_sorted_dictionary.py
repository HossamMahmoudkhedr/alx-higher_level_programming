#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for element in sorted_dictionary:
        print(f"{element}: {a_dictionary[element]}")
