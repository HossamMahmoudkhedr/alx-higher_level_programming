#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


"""
text must be a string, 
otherwise raise a TypeError exception with the message 'text must be a string'

There should be no space at the beginning or at the end of each printed line
"""
def text_indentation(text):
    """prints a text new lines

    Args:
        text: the text to be printed
    
    Return:
        no return
    
    Raise:
        raise a TypeError if the text is not a string
    """
    isSpecial = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in range(len(text)):
        if text[i] == '.' or text[i] == ',' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            isSpecial = True
        elif text[i] == ' ' and isSpecial:
            isSpecial = False
            continue
        else:
            print(text[i], end="")
            isSpecial = False
