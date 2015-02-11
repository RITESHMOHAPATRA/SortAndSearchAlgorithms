'''
Created on Oct 4, 2014

@author: M
'''

def binary_search_iterative(list_, value):
    """
    Searches for an value within a given list.
    This algorithm uses binary search in an iterative way.
    
    @param list_: a list containing numbers
    @param value: the number to be found      
    
    @return: True if the value has been found. Otherwise, False.
    """
    if len(list_) == 0:
        return False    

    # if high = len(list_) you will get an error
    # when the element is higher than the last element
    # of a sorted list, and you will have to make more
    # complicated the condition in the while loop.
    high = len(list_) - 1
    low = 0    
    
    while(high >= low):
        middle = (high + low) // 2
        if list_[middle] == value:
            return True
        elif list_[middle] >  value:
            high = middle - 1
        else:
            low = middle + 1
    
    # if value not found
    return False

def binary_search_recursive(list_, value):
    """
    Searches for an value within a given list.
    This algorithm uses binary search in a recursive way.
    
    @param list_: a list containing numbers
    @param value: the number to be found      
    
    @return: True if the value has been found. Otherwise, False.
    """
    if len(list_) == 0:
        return False    
    
    middle = len(list_) // 2
    
    if list_[middle] == value:
        return True
    elif list_[middle] > value:
        return binary_search_recursive(list_[:middle], value)
    else:
        return binary_search_recursive(list_[middle + 1:], value)

"""
list_ = list(range(10))
for i in range(-20, 21):
    print("Recursive:", i, binary_search_iterative(list_, i))
"""
