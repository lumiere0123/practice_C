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
    index = 0
    for ch in s:
        print(type(ch), ch)
        if index % n == 0:
            new_s += ch
        index += 1
    return new_s