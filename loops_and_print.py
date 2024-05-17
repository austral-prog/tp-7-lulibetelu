def enumerate_list(list):
    new_list = []
    index_new = 0
    for element in list:
        if element != "":
            new_element = f"{index_new}. {element}"
            new_list.append(new_element)
            index_new += 1
    return new_list

def enumerate_backwards(list):
    new_list = []
    index_new = 0
    for element in list:
        if element != "":
            new_element = f"{index_new}. {element[::-1]}"
            new_list.append(new_element)
            index_new += 1
    return new_list

    
