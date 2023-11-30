def create_an_empty_list():
    return []

def create_a_list():
    users = list(['Samuel', 'Livio ', 'Otieno', 'Kamau'])
    return users

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(element, 0)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    first_element = l[0]
    return first_element

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]