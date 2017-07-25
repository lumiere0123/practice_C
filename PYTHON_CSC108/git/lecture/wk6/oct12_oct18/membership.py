def no_extra_members(group_list, class_list):
    '''(list of list of int, list of int) -> bool
    Return True iff every student in group_list is a 
    member of class_list.

    >>> no_extra_members([[1, 3, 4], [2]], [1, 2, 3, 4])
    True
    >>> no_extra_members([[1, 2], [3, 4]], [1, 2, 4])
    False
    '''

    # Here is a variant of a "check property" pattern.
    # In this pattern, we check every item in the list
    # (or nested list, in this case) for a property. If
    # any item does not have that property, then we 
    # return False. If all items have the desired property,
    # then we return True *after* the loop.
    for group in group_list:
        for student in group:
            if student not in class_list:
                 return False
    return True


def count_instances(group_list, item):
    '''(list of list of int) -> int
    Return the number of instances of item in group_list.
    '''
    # Todo for Fri
    # Use an accumulator pattern to count the instance of item
    # in the nested list group_list!
    pass

def groups_okay(group_list, class_list):
    '''(list of list of int, list of int) -> bool
    Return True iff every student in class_list is in 
    exactly one group according to group_list.

    >>> groups_okay([[1, 3, 4], [2]], [1, 2, 3, 4])
    True
    >>> groups_okay([[1, 3, 4], [2, 3]], [1, 2, 3, 4])
    False
    '''

    # Here is the check property pattern again, but the 
    # property we are checking for is a complex one. We will
    # create a helper function to test it.
    for student in class_list:
        if count_instances(group_list, student) != 1:
            return False
    return True  

