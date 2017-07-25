def bubble_sort(L):
    """ (list) -> NoneType

    Sort the items of L from smallest to largest.

    >>> L = [4, 2, 5, 6, 7, 3, 1]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6, 7]
    """

    # The index of the last unsorted item.
    end = len(L) - 1

    while end != 0:

        # Bubble once through the unsorted section to move the largest item
        # to index end.
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        end = end - 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
