#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0   # counts the real number of elements printed
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end='')
            c += 1
    except IndexError:
        pass
    print()
    return c
