#!/usr/bin/python3
"""Module function to convert a JSON string to a Python object"""
import json


def from_json_string(my_str):
    '''
    Function that returns an object represented by a JSON string

    Args: my_str (string): JSON string

    Return: object (Python data structure)
    '''
    return json.loads(my_str)
