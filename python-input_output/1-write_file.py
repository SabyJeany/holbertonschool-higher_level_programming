#!/usr/bin/python3
"""Defines a function that writes text to a file"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
