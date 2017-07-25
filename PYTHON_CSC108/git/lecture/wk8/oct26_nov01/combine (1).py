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
    
    combined_dict = {}
    for key in d1:
        if key in d2:
            combined_dict[key] = sum(d1[key] + d2[key])
    return combined_dict  


def fully_combine(d1, d2):
    '''(dict {obj:list of int}, dict {obj:list of int}) ->
            dict {obj:int}
    Return the dictionary where each key is a key in either
    d1 or d2. The value associated with each key is 
    the sum of all the integers associated with that key
    in both d1 and d2.
    
    >>> fully_combine({1:[2], 2:[4, 5]}, {2:[2], 3:[5, 7]})
    {1:2, 2:11, 3:12}
    '''
    
    combined_dict = {}
    for key in d1:
        if key in d2:
            combined_dict[key] = sum(d1[key] + d2[key])
        else:  # Just in d1
            combined_dict[key] = sum(d1[key])
    for key in d2:
        if key not in d1:
            combined_dict[key] = sum(d2[key])

    return combined_dict
    

# This version is, in my opinion, the most elegant.
def fully_combine_v2(d1, d2):
    '''(dict {obj:list of int}, dict {obj:list of int}) ->
            dict {obj:int}
    Return the dictionary where each key is a key in either
    d1 or d2. The value associated with each key is 
    the sum of all the integers associated with that key
    in both d1 and d2.
    
    >>> fully_combine_v2({1:[2], 2:[4, 5]}, {2:[2], 3:[5, 7]})
    {1:2, 2:11, 3:12}
    '''    
    
    combined_dict = {}
    for key in d1:
        combined_dict[key] = sum(d1[key])
    for key in d2:
        combined_dict[key] = combined_dict.get(key, 0) + sum(d2[key])

    return combined_dict 


def fully_combine_v3(d1, d2):
    '''(dict {obj:list of int}, dict {obj:list of int}) ->
            dict {obj:int}
    Return the dictionary where each key is a key in either
    d1 or d2. The value associated with each key is 
    the sum of all the integers associated with that key
    in both d1 and d2.
    
    >>> fully_combine_v3({1:[2], 2:[4, 5]}, {2:[2], 3:[5, 7]})
    {1:2, 2:11, 3:12}
    '''

    combined_dict = d1.copy()
    for key in d2:
        combined_dict.setdefault(key, []).extend(d2[key])
    for key in combined_dict:
        combined_dict[key] = sum(combined_dict[key])
    return combined_dict
