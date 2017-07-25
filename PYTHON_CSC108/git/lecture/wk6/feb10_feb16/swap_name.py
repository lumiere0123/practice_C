def swap_name(name_list): 
    """ (list of str) -> NoneType 
 
    name_list contains a single person's name.  Modify name_list so that the
    first name and last name are swapped. 
                 
    >>> name = ['John', 'Smith'] 
    >>> swap_name(name) 
    >>> name 
    ['Smith', 'John'] 
    >>> name = ['John', 'Andrew', 'Gleeson', 'Smith'] 
    >>> swap_name(name) 
    >>> name 
    ['Smith', 'Andrew', 'Gleeson', 'John'] 
    """ 

    tmp = name_list[-1]
    name_list[-1] =  name_list[0]
    name_list[0] = tmp
    