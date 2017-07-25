def display_rotated(character, n):
    '''(str, int) -> str
    Return a string that demonstrates a rotation of the given character. The character should be rotated by n positions.
    >>> display_rotated('d', 1)
    'Rotating "d" by   1 characters yields "e"'
    >>> display_rotated('a', -3)
    'Rotating "a" by  -3 characters yields "x"'
    >>> display_rotated('z', 12)
    'Rotating "z" by  12 characters yields "l"'
    >>> display_rotated('Z', 12)
    'Rotating "Z" by  12 characters yields "L"'
    '''

    #create a variable that consists of alphabet in order a...z
    a = "abcdefghijklmnopqrstuvwxyz"
    # check if character is upper
    if character.isupper() :
        a = a.upper()

    #find index of character from the variable
    index = a.find(character)
    #add n to the index found and get the index size < len(alphabet)
    new_index = (index + n) % len(a)
  
    comment = 'Rotating "{0}" by {1:3} characters yields "{2}"'.format(character, n, a[new_index])
    return comment


def upper_every_nth(s, n):
    '''(str, int) -> (str)
    Return a string that is identical to s except that every nth character (starting at position 0) is uppercase.

    >>> upper_every_nth("cat", 2)
    'CaT'
    >>> upper_every_nth("hat", 3)
    'Hat'
    >>> upper_every_nth("abcdefg", 3)
    'AbcDefG'
    '''
    index = 0
    new_str = ""
    while index < len(s):
        if index % n ==0:
            new_str=new_str + s[index].upper()
        else:
            new_str=new_str + s[index]

        index += 1

    return new_str

import doctest
doctest.testmod()
