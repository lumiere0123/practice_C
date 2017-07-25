def greatest_difference(nums1, nums2):
    """ (list of number, list of number) -> number
    
    Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.
    
    Precondition: len(nums1) == len(nums2) and nums1 != []
    
    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    10
    """

    compare_list = []
    for i in range(0, len(nums1)): 
        compare_list.append(abs(nums1[i] - nums2[i]))
    return max(compare_list)
        
    #Typing for  i in range(nums1) 
    #would give you an error. We need to iterate of the entire length of list
    #nums1. Remember that range() expects an integer as an argument.
    
    #It's OK to skip the starting 0 and call range(len(nums1)) 
    
    # Here's an alternate solution where we don't create a new list.
    # Here we have a max_diff variable which keeps track of what is the
    # maximum absolute difference we've seen so far.
    # We update max_diff only if the absolute difference of
    # the current set of corresponding elements(e.g., nums1[i], nums2[i])
    # is greater than the previous value of max_diff.
    
    #max_diff = 0
    #for i in range(len(nums1)):
    #    max_diff = max(max_diff, abs(nums1[i] - nums2[i]))
    #return max_diff
    
    #Question: In the second solution, why do we initialize max_diff 
    #to 0?
