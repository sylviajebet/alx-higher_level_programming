#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    big = my_list[0]
    for i in my_list:
        if i > big:
            big = i
    return (big)
