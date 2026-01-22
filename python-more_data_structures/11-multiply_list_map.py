#!/usr/bin/python3
# Function that multiplies all elements of a list by a number using map
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda value: value * number, my_list))
