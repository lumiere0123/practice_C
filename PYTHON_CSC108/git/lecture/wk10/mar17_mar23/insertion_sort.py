def insert(L, i):
    """ (list, int) -> NoneType

    Precondition: L[:i] is sorted in non-descending order.

    Move L[i] to where it belongs in L[:i + 1].

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """

    # The value to be inserted into the sorted part of the list.
    value = L[i]

    # Find the position, i, where value should go.
    # Make room for the value by shifting.
    while i > 0 and L[i - 1] > value:
        L[i] = L[i - 1]
        i = i - 1
    
    L[i] = value


def insertion_sort(L):
    """ (list) -> NoneType

    Sort the items of L into non-descending order.

    >>> L = [4, 2, 5, 6, 7, 3, 1]
    >>> insertion_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6, 7]
    """

    for i in range(len(L)):
        insert(L, i)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
