#!/usr/bin/python3
def islower(c):
    asciiNumber = ord(c)
    if asciiNumber >= 97 and asciiNumber <= 122:
        return True
    
    return False
