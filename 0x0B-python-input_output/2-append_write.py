#!/usr/bin/python3
""" appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ return the length of the added text """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
