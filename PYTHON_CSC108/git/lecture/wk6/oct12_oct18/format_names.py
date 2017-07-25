def format_names(namelist):
    '''(list of str) -> (list of str)
    Return a list that is identical to namelist except that 
    each name in the list is in titlecase.

    >>> format_names(["andrew petersen", "dan discussionboardhero zingaro", "TIFFANY tong"])
    ["Andrew Petersen", "Dan Discussionboardhero Zingaro", "Tiffany Tong"]
    '''

    # Our old friend, the accumulator pattern.
    new_namelist = []
    for name in namelist:
        new_namelist.append(name.title())
    
    return new_namelist


def format_names_inplace(namelist):
    '''(list of str) -> None
    Update namelist so that each name in the list is in titlecase.

    >>> names = ["andrew petersen", "dan discussionboardhero zingaro", "TIFFANY tong"]
    >>> format_names(names)
    >>> names
    ["Andrew Petersen", "Dan Discussionboardhero Zingaro", "Tiffany Tong"]
    '''

    # A new pattern: modifying in place
    # Since we want to modify in place, we need an index so we can
    # assign back into the original list. Hence, we loop over range().
    for index in range(len(namelist)):
        namelist[index] = namelist[index].title()

    # Don't do this! This is attempting to use the accumulator pattern to
    # update the list, but all we end up updating is the local variable 
    # namelist -- not the list it refers to.
    # new_namelist = []
    # for name in namelist:
	#     new_namelist.append(name.title())
	# namelist = new_namelist 




