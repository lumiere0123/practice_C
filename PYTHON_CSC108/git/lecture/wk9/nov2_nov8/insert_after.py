def insert_after(L, n1, n2):
    '''(list, object, object) -> None
    Insert n2 after every occurrence of n1 in L.
    
    >>> L = [1, 2, 3]
    >>> insert_after(L, 3, 4)
    >>> L    # Inserting at end
    [1, 2, 3, 4]
    >>> L = [1, 3, 5, 7]
    >>> insert_after(L, 3, 100)
    >>> L    # Inserting in the middle
    [1, 3, 100, 5, 7]
    >>> L = [1, 1, 2]
    >>> insert_after(L, 1, 'banana')
    >>> L    # Inserting multiple times 
    [1, 'banana', 1, 'banana', 2]
    >>> L = [1, 2, 3]
    >>> insert_after(L, 1, 1)
    >>> L    # Inserting when n1 == n2 
    [1, 1, 2, 3]
    >>> L = [0, 0, 0]
    >>> insert_after(L, 1, 2)
    >>> L    # n1 not in L
    [0, 0, 0]
    >>> L = []
    >>> insert_after(L, 1, 2)
    >>> L    # empty list
    []
    >>> L = [1, 2, 1]
    >>> insert_after(L, 1, 'banana')
    >>> L    # inserting multiple times, end of list
    [1, 'banana', 2, 1, 'banana']
    '''
    
    # Broken whenever you are inserting more than once and
    # the last item to insert is toward the end.
    # Especially broken when n1 == n2
    for index in range(len(L)):
        if L[index] == n1:
            L.insert(index + 1, n2)
            
            
            
            