'''
Created on Oct 4, 2014

@author: M
'''

def linear_search(list_, value):
    """
    Searches for a specified value in a list.
    It performs linear search in an iterative way.
    
    @param list_: a list containing numbers
    @param element:  element to be search
    
    @return: True if value is found. Otherwise, False.    
    """
    for dummy_element in list_:
        if dummy_element == value:
            return True
    
    # if value hasn't been found
    return False

def linear_search_recursive(list_, value):
    """
    Searches for a specified value in a list.
    It performs linear search in a recursive way.
    
    @param list_: a list containing numbers
    @param element:  element to be search
    
    @return: True if value is found. Otherwise, False.    
    """
    if len(list_) == 0:
        return False
    
    if list_[0] == value:
        return True
    
    return linear_search_recursive(list_[1:], value)

def linear_search_v2(list_, value):
    """
    Searches for a specified value in a list.
    
    @param list_: a list containing numbers
    @param element:  element to be search
    
    @return: True if value is found. Otherwise, False.    
    """
    for dummy_index in range(len(list_)):
        if list_[dummy_index] == value:
            return True
    
    # if value hasn't been found
    return False

"""
list_ = list(range(20))
value = 10
print("Recursive:", linear_search_recursive(list_, value))
"""
