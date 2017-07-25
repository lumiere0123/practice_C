def median(L):
    """
    >>> median([4,3,1,5,7]) 
    4
    >>> median([4,3,1,5])
    3.5
    """
    L.sort()
    if len(L) % 2 == 0:
        first_idx = len(L)//2 - 1
        second_idx = len(L)//2
        return ( L[first_idx] + L[second_idx] ) / 2

    else:
        idx = len(L) // 2
        return L[idx]



    #if len(L) //2 == 0:
    #return (L[len(L)/2] + L[len(L)/2 + 1])/2 

    ## [4,3,1,5]
    #if len(L)%2 == 0:
    #    return (L[int(len(L)/2-1)] + L[int(len(L)/2 )])/2 
    #else:
    #    return L[int((len(L)/2-0.5))]
    #return L[(len(L)/2-0.5)]



def median2(L):
    """
    >>> median2([4,3,1,5,7]) 
    4
    >>> median2([4,3,1,5])
    3.5
    """
    L.sort()
    while len(L) > 2:
        L.remove(max(L))
        L.remove(min(L))

    if len(L) ==1:
        return L[0]

    elif len(L) ==2:
        return (L[0] + L[-1])/2

    

    



import doctest
doctest.testmod()
    
