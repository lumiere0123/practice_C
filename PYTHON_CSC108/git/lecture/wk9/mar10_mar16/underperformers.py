def collect_underperformers(nums, threshold):
    """ (list of number, int) -> list of number
    
    Return a new list consisting of those numbers in nums that are below
    threshold, in the same order as in nums.
    
    >>> collect_underperformers([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_underperformers([1, 2, 108, 3, 4], 50)
    [1, 2, 3, 4]
    >>> collect_underperformers([], 7)
    []
    """
    
    result = []
    
    for item in nums:
        if item < threshold:
            result.append(item)
    
    return result
    