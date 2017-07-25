def collect_underperformers(nums, threshold):
    """ (list of number, int) -> NoneType
    
    Modify the existing list to only contain those numbers in nums that 
    are below threshold, in the same order as in nums.
    
    """

    #We will be changing the length of a list so save it up front.
    length_list = len(nums)
    new_index = 0
    
    for i in range(length_list):
        #remove all elements above or equal to threshold
        #Update new index only if we don't remove anything.
        if nums[new_index] >= threshold:
            nums.remove(nums[new_index])
        else:
            new_index += 1


#Be careful: the following code will not work:
#
#for element in nums:
#    if element >= threshold:
#	nums.remove(element)
#
#Try it with this example and use the debugger to figure out why:
# >>> nums = [8, 10, 2, 4, 3]
# >>> collect_underperformers(nums, 6)
# >>> nums
# [10, 2, 4, 3]
