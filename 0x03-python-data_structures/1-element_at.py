def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        if idx > len(my_list):
            return None
        if my_list[idx] == i:
            return i