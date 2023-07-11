#!/usr/bin/python3
"""  writes a string to a file and returns the number of characters """


def write_file(filename="", text=""):
    """ Returns the number of characters written """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    with open(filename, encoding="utf-8") as myFile:
        charCount = 0
        while True:
            line = myFile.readline() 
            if not line :
                return charCount
            for char in line:
                if char:
                    charCount += 1
