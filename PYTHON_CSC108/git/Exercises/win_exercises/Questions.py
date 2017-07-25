#--------------------------- Question 1 -----------------------------------------

# for the first function in ex4, here is what I did:
    
def insert(orig_list, new_list, insert_index):
    '''(list of obj, list of obj, int) -> list of obj

    Return a copy of orig_list with the elements of new_list inserted
    starting at index insert_index

    >>> insert([1, 2, 3], ['a', 'b', 'c'], 0)
    ['a', 'b', 'c', 1, 2, 3]
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("Hello", "Bye", 3)
    'HelByelo'
    '''
    # this is my code
    result = orig_list[:insert_index] + new_list + orig_list[insert_index:]
    return result

# but in solutions:

#res = orig_list[0:insert_index]
#res += new_list[:]
#res += orig_list[insert_index:]
#return res

# I understand everything except line 25.
# What's the difference between 'new_list' in line19 and 'new_list[:] in line25?
# Are they same?


  # ANSWER: 
  #   The net effect is same in this case, but they are NOT same meaning, 
  #   new_list[:] will retrun a copy of new_list
  #   For example,
  #       
  #    >>> a=[1,2,3]
  #    >>> b=a
  #    >>> b.append(4)
  #    >>> a
  #    [1, 2, 3, 4]
  #
  #      => VS <=
  #
  #    >>> a=[1,2,3]
  #    >>> b=a[:]
  #    >>> b.append(4)
  #    >>> a
  #    [1, 2, 3]
  #    >>> b
  #    [1, 2, 3, 4]
  #   
  #     - Roy


# ------------------------------ Question 2 ------------------------------------

# If I want to use while loop for the above function, would this be a proper way?
# I checked that this code works but is there a better or more efficient way
# of finishing it using while loop?

    
def insert2(orig_list, new_list, insert_index):
    '''(list of obj, list of obj, int) -> list of obj

    Return a copy of orig_list with the elements of new_list inserted
    starting at index insert_index

    >>> insert2([1, 2, 3], ['a', 'b', 'c'], 0)
    ['a', 'b', 'c', 1, 2, 3]
    >>> insert2([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert2("Hello", "Bye", 3)
    'HelByelo'
    '''
    # count = 0
    # 
    # if type(orig_list) == str:
    #     res = ''
    #     while count < insert_index:   
    #         res += orig_list[count]
    #         count += 1
    #     res += new_list
    #     res += orig_list[insert_index:]
    # 
    # 
    # elif type(orig_list) == list:
    #     res = []
    #     while count < insert_index:
    #         res += [orig_list[count]]
    #         count += 1
    #     res += new_list
    #     res += orig_list[insert_index:]
    #     
    # return res

    # I would simplify above as follows:  - Roy
    count = 0
    
    res = []
    while count < insert_index:
        res += [orig_list[count]]
        count += 1
    res += new_list
    res += orig_list[insert_index:]
       
    if type(orig_list) == str:
      return ''.join(res)
    else:
      return res







#--------------------------- Question 3 ----------------------------------------
# same question as above but using for loop. (any better way?)
# plus, are there 2 kinds of for loop?
# first one is using range and the other one is not?
# please give examples 'cause I only know how to do with the first one(using range)
def insert3(orig_list, new_list, insert_index):
    '''(list of obj, list of obj, int) -> list of obj

    Return a copy of orig_list with the elements of new_list inserted
    starting at index insert_index

    >>> insert3([1, 2, 3], ['a', 'b', 'c'], 0)
    ['a', 'b', 'c', 1, 2, 3]
    >>> insert3([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert3("Hello", "Bye", 3)
    'HelByelo'
    '''
##if type(orig_list) == str:    
##    res = ''    
##    for number in range(0, insert_index):
##        res += orig_list[number]
##    res += new_list
##    res += orig_list[insert_index:]
##
##elif type(orig_list) == list:
##    res = []
##    for number in range(0, insert_index):
##        res += [orig_list[number]]
##    res += new_list
##    res += orig_list[insert_index:]
##
##return res

    # We could do the same without 'range', but it will add complexity and
    # is not worth
    res = []
    for number in range(0, insert_index):
        res += [orig_list[number]]
    res += new_list
    res += orig_list[insert_index:]
    
    if type(orig_list) == str:
      return ''.join(res) 
    else:
      return res




#------------------------------- Question 4 ------------------------------------
# for the second function in ex4, my code is :

def up_to_first(orig_list, search_obj):
    '''(list of obj, obj) -> list of obj
    Returns a copy of the orig_list up to the first occurrence of search_obj.
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first("Jeehun", "h")
    'Jee'
    >>> up_to_first("Jeehun", "k")
    'Jeehun'
    >>> up_to_first([10, 20, 30, 40], 30)
    [10, 20]
    '''
    #if type(orig_list) == list:
    #    res = []
    #    if search_obj in orig_list:
    #        res = orig_list[:(search_obj - 1)]
    #        
    #elif type(orig_list) == str:
    #    res = ''
    #    if search_obj in orig_list:
    #        res = orig_list[:orig_list.index(search_obj)]
    #        
    #return res

    # The above code is incorrect and it doesn't work with
    # >>> up_to_first([10, 20, 30, 40], 30)
    # [10, 20]
    # Better way would be
    res = []
    if search_obj in orig_list:
      res = orig_list[:orig_list.index(search_obj)]

      if type(orig_list) == str:
        return ''.join(res)
      else: 
        return res

    else:
      return orig_list


# I checked this works but is there a way that I can do both str and list at one time?
# if there is, please give examples doing with loop(for, while) and not using loop


if __name__ == '__main__' :
  import doctest
  doctest.testmod()
  
