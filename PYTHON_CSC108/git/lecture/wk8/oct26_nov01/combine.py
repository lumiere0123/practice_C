def combine(d1, d2):
    '''(dict {obj:list of int}, dict {obj:list of int}) ->
            dict {obj:int}
    Return the dictionary where each key is a key is in 
    both d1 and d2. The value associated with each key is 
    the sum of all the integers associated with that key
    in both d1 and d2.
    
    >>> combine({1:[2], 2:[4, 5]}, {2:[2], 3:[5, 7]})
    {2:11}
    '''
    
    1. How do you identify all of the keys that are in both dictionaries?
    
    for key in d1:
        if key in d2:
            ... key is guaranteed to be in d1 and d2 ...
    
    2. How do you pull the items for a key from both and combine them?
    
    key is in both dictionaries.
    sum(d1[key] + d2[key])
    
    Homework: solve this problem!