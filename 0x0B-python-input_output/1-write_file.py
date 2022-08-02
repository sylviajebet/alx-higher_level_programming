#!/usr/bin/python3
"""
function that writes a string to a text file and returns no of characters
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
