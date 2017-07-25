def collect_underperformers(nums, threshold):
    
    """ (list of number, int) -> list of number
    
    Return a new list consisting of those numbers in nums that 
    are below threshold, in the same order as nums.
    
    >>> collect_underperformers([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_underperformers([], 7)
    []   
    """
    #We want to create a new list. 
   

























 
    underperformers = []
    for item in nums:
        if item < threshold:
            underperformers.append(item)
            #underperformers  = underperformers + [item]
    return underperformers
    
#If you want you can uncomment the following function call, add a breakpoint
#at line 15, and run this through the debugger. Step through the code
#and see how the underperformers list is gradually created.
#collect_underperformers([1, 2, 3, 4], 3)

    #Alternative implementation using range
    #notice that i is the index, so we need to append nums[i]
    #
    #underperformers = []
    #for i in range(len(nums)):
    #    if nums[i] < threshold:
    #        underperformers.append(nums[i])
    #return underperformers
            

def scale_midterm_grades(grades, multiplier, bonus):
    
    """ (list of number, number number) -> NoneType
        
    Modify each grade in grades by multiplying it by multiplier
    and then adding bonus. Cap grades at 100.
    
    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    >>> grades
        [55, 60, 65, 100]
    """
    #Be careful here we ask you to modify the grades list!
    #To do this you need to know the index, so the range function comes in 
    #handy.
    
    for i in range(len(grades)):
        grades[i] = grades[i] * multiplier + bonus
        if grades[i] > 100:
            grades[i] = 100
        #You could also substitute the previous 3 lines with this:
        #grades[i] = min(100, grades[i] * multiplier + bonus)
        
    #Could you do this without the range() function?
    #Yes, but you need to separately keep track of the index and
    #increment it in every loop iteration. You can see an example below:
    
    #index = 0
    #for mark in grades:
    #    grades[index] = mark * multiplier + bonus
    #    if grades[index] > 100:
    #        grades[index] = 100
    #    index = index + 1
