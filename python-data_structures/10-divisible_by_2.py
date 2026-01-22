#!/usr/bin/python3
# write a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    return [n % 2 == 0 for n in my_list]
