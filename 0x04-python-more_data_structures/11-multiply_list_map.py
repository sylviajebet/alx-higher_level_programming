#!/usr/bin/python3


# multiply_list_map - Function that returns list with all values multiplied by a number
def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda x: x * number, my_list)))
