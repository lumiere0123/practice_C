def row_sum(lst):
    '''(list of list of int) -> list of int
    Return a new list that contains the sum of each sublist
    in lst.
  
    >>> row_sum([[5, 10, 15], [1, 2, 3, 4]]
    [30, 10]
    '''

    # Here is an example of the accumulator pattern used on a nested list.
    sums = []
    for sublist in lst:
        # sums.append(sum(sublist))   # This would work, but let's implement the sum function

        # The inner loop also uses an accumulator pattern!
        sum = 0
        for item in sublist:
            sum += item
        sums.append(sum)
    return sums


def column_sum(lst):
    '''(list of list of int) -> list of int
    Return a new list that contains the sum of each column
    in lst. Each sublist is the same length.
  
    >>> column_sum([[5, 10, 15], [1, 2, 3]]
    [6, 12, 18]
    '''
    if lst == []:
        return []

    # Another accumulator pattern. This time, however, we need an index, since
    # we are indexing into each sublist.  Hence, the outer loop walks over indices,
    # rather than outer lists.
    sums = []
    for col_index in range(len(lst[0])):
        sum = 0
        for row in lst:
            sum += row[col_index]
        sums.append(sum)
    return sums