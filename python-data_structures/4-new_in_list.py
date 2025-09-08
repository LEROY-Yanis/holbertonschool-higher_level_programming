#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        list = my_list
        return (list)
    elif idx not in range(len(my_list)):
        list = my_list
        return (list)
    else:
        list = [i for i in my_list]
        list[idx] = element
        return (list)
