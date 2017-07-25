def skip_n(s, n):
    '''(str, int) -> str
    Return a new string that is composed of every nth
    character in s. Start at index 0.
    
    >>> skip_n('0123456', 2)
    '0246'
    >>> skip_n('0123456', 3)
    '036'
    '''

    new_s = ''    
    for index in range(0, len(s), n):
        print(type(index), index)
        new_s += s[index]
    return new_s