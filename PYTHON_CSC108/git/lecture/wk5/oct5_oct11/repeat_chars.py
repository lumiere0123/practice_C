def repeat_chars(s, num):
    '''(str, int) -> str
    Return a string consisting of each character of s 
    repeated num times.

    >>> repeat_chars('abc', 2)
    'aabbcc'
    '''

    new_s = ''
    for ch in s:
        new_s += ch * num
    return new_s

    # for every character in s
    #     add that character to the new string n times
    # return the new string