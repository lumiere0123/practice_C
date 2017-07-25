def dict_to_str(d):
    """
    >>> dict_to_str({3:4, 5:6})
    '3 4, 5 6'
    >>> dict_to_str({3:4})
    '3 4'
    >>> dict_to_str({})
    ''
    >>> dict_to_str({3:4, 5:6})
    '3 4,5 6'
    """
    new_str = ''
    index = 0
    is_first= True
    for key in d:
      if is_first:
        new_str = str(key) + ' ' + str(d[key])
        is_first = False
      else:
        new_str += ", " + str(key) + ' ' + str(d[key])
      
    return new_str
      



def transitive_property(d1, d2):
    """
    >>> transitive_property({'one':1, 'two':2}, {1:1.0}) 
    {'one': 1.0}
    >>> transitive_property({'one':1, 'two':2}, {3:3.0}) 
    {}
    >>> transitive_property({'one':1, 'two':2}, {2:3.0}) 
    {'two': 3.0}
    >>> transitive_property({'one':1, 'two':2}, {2:3.0, 1:1.0}) 
    {'two': 3.0, 'one': 1.0}
    >>> transitive_property({'one':1, 'two':2}, {1:1.0})
    {'one': 1.0}
    >>> transitive_property({'one':1, 'two':2}, {3:3.0})
    {}
    """
    
    new_dict = {}
    for key in d1:
        if d1[key] in d2:
          new_dict[key] = d2[d1[key]]

    return new_dict

import doctest
doctest.testmod()
