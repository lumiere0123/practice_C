def find(search_s, sub):
    '''Return the lowest index in the str search_s 
    where the substring sub is found.

    >>> find("abcd", "ab")
    0
    >>> find("abcd", "cd")
    2
    >>> find("abcdcd", "cd")
    2
    >>> find("abcd", "efg")
    -1
    '''

     # Use a for or a while -- not find! -- and we'll compare.