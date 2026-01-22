#!/usr/bin/python3
# Function that multiplies by 2 all values in a dictionary
def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
