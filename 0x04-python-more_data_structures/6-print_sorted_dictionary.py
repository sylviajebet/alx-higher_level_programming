#!/usr/bin/python3


#function that prints a dictionary by ordered keys
def print_sorted_dictionary(my_dict):
    for keys in sorted(my_dict.keys()):
        print('{}: {}'.format(keys, my_dict[keys]))
