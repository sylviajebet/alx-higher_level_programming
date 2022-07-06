#!/usr/bin/python3


# search_replace - Function to replace all occurences of an element with another
def search_replace(my_list, search, replace):
	rep_list = []
	for i in my_list:
		if i == search:
			rep_list.append(replace)
		else:
			rep_list.append(i)
	return rep_list
