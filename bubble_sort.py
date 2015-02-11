'''
Created on Oct 6, 2014

@author: M
'''

def bubble_sort(lst):
    """
    Sorts a list in increasing order. Because of lists are mutable
    this function does not have to return something.
    This algorithm uses bubble sort.
    @param lst: a list (in general unsorted)
    """
    for i in range(len(lst) - 1):
        already_sorted = True
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                already_sorted = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        # if no swaps were developed in the previous loop,
        # it means that the list is already sorted. Thus,
        # loop is exited and function terminates (returns None)
        if already_sorted:
            break
