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

    index = 0
    while index < len(search_s):
        current_str = search_s[index: index + len(sub)]
        if current_str == sub:
            return index
        index += 1
    return -1


# Here's a variant that uses a for loop over the legal
# indices into the string. It looks just like our while loop.
def findv2(search_s, sub):
    for index in range(len(search_s)):
        current_str = search_s[index: index + len(sub)]
        if current_str == sub:
            return index        
    return -1


# What if you try to use a for loop over the string itself?
# Ugly code! You end up needing to keep an index, too.
def findv3(search_s, sub):
    substring = ''
    index = 0
    for ch in search_s:
        substring += ch
        if len(substring) > len(sub):
            substring = substring[1:]
        if substring == sub:
            return index - len(sub) + 1
        index += 1
    return -1    
    
    